import cv2
import mediapipe as mp
import time
import numpy as np
import winsound
from scipy.spatial import distance as dist
from sklearn.svm import OneClassSVM

#CONFIGURACIÓN
TIEMPO_LIMITE = 3.0       # Segundos antes de sonar
TIEMPO_CALIBRACION = 8.0  # Tiempo para aprender los ojos
# Ángulos para la cabeza
ANGULO_CABEZA_ADELANTE = -10  # Si baja de -10 
ANGULO_CABEZA_ATRAS = 20      # Si sube de 20

# Índices de MediaPipe
OJO_IZQ_IDX = [362, 385, 387, 263, 373, 380]
OJO_DER_IDX = [33, 160, 158, 133, 153, 144]

#FUNCIONES

def calcular_ear(landmarks, indices_ojo, w, h):
    coords = []
    for idx in indices_ojo:
        lm = landmarks[idx]
        coords.append((int(lm.x * w), int(lm.y * h)))
    A = dist.euclidean(coords[1], coords[5])
    B = dist.euclidean(coords[2], coords[4])
    C = dist.euclidean(coords[0], coords[3])
    return (A + B) / (2.0 * C), coords

def obtener_rotacion_cabeza(img, landmarks):
    h, w, _ = img.shape
    face_3d = []
    face_2d = []
    indices_clave = [1, 152, 33, 263, 61, 291]

    for idx in indices_clave:
        lm = landmarks[idx]
        x, y = int(lm.x * w), int(lm.y * h)
        face_2d.append([x, y])
        face_3d.append([x, y, lm.z])
    
    face_2d = np.array(face_2d, dtype=np.float64)
    face_3d = np.array(face_3d, dtype=np.float64)

    focal_length = 1 * w
    cam_matrix = np.array([[focal_length, 0, w/2],
                           [0, focal_length, h/2],
                           [0, 0, 1]])
    dist_matrix = np.zeros((4, 1), dtype=np.float64)

    success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)
    rmat, jac = cv2.Rodrigues(rot_vec)
    angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)
    
    return angles[0] * 360 # Pitch

#INICIO DEL PROGRAMA

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

cap = cv2.VideoCapture(0)

# Variables de estado
datos_calibracion = []
modelo_ia = None
calibrado = False
inicio_calibracion = None
tiempo_inicio_sueno = None

print("[INFO] Iniciando sistema...")

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    texto_estado = "Esperando..."
    color_texto = (255, 255, 255)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            lm_list = face_landmarks.landmark

            # 1. Calcular EAR
            leftEAR, l_coords = calcular_ear(lm_list, OJO_IZQ_IDX, w, h)
            rightEAR, r_coords = calcular_ear(lm_list, OJO_DER_IDX, w, h)
            avgEAR = (leftEAR + rightEAR) / 2.0

            # 2. Calcular Cabeceo
            pitch = obtener_rotacion_cabeza(frame, lm_list)

            #FASE 1: CALIBRACIÓN (5 SEGUNDOS)
            if not calibrado:
                if inicio_calibracion is None:
                    inicio_calibracion = time.time()
                
                tiempo_transcurrido = time.time() - inicio_calibracion
                datos_calibracion.append([avgEAR])
                
                cv2.putText(frame, f"CALIBRANDO IA... {int(5 - tiempo_transcurrido)}s", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                cv2.putText(frame, "MIRA AL FRENTE NORMALMENTE", (30, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)

                if tiempo_transcurrido >= TIEMPO_CALIBRACION:
                    print("[INFO] Entrenando IA con tus ojos...")
                    X = np.array(datos_calibracion)
                    modelo_ia = OneClassSVM(kernel='rbf', gamma='auto', nu=0.05)
                    modelo_ia.fit(X)
                    calibrado = True
                    winsound.Beep(1000, 200)

            #FASE 2: MONITOREO
            else:
                # A. Predicción Ojos (IA)
                prediccion = modelo_ia.predict([[avgEAR]])[0]
                ojo_cerrado = True if prediccion == -1 else False
                
                # B. Detección Cabeza (Adelante y Atrás)
                cabeza_mal = False
                tipo_cabeza = ""

                if pitch < ANGULO_CABEZA_ADELANTE: # Hacia el pecho (negativo)
                    cabeza_mal = True
                    tipo_cabeza = "ADELANTE"
                elif pitch > ANGULO_CABEZA_ATRAS:  # Hacia atrás (positivo)
                    cabeza_mal = True
                    tipo_cabeza = "ATRAS"

                # Lógica Final
                detectado_sueno = False
                
                if cabeza_mal:
                    texto_estado = f"CABEZA {tipo_cabeza}! ({int(pitch)})"
                    detectado_sueno = True
                    color_texto = (0, 0, 255)
                elif ojo_cerrado:
                    texto_estado = f"OJOS CERRADOS ({avgEAR:.2f})"
                    detectado_sueno = True
                    color_texto = (0, 0, 255)
                else:
                    texto_estado = "DESPIERTO"
                    color_texto = (0, 255, 0)

                # Dibujar ojos
                for p in l_coords: cv2.circle(frame, p, 1, (0, 255, 0), -1)
                for p in r_coords: cv2.circle(frame, p, 1, (0, 255, 0), -1)

                # ALARMA
                if detectado_sueno:
                    if tiempo_inicio_sueno is None:
                        tiempo_inicio_sueno = time.time()
                    
                    duracion = time.time() - tiempo_inicio_sueno
                    cv2.putText(frame, f"ALERTA: {duracion:.1f}s", (10, 150),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                    if duracion >= TIEMPO_LIMITE:
                        cv2.putText(frame, "DESPIERTA", (200, 300),
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                        winsound.Beep(2500, 100)
                else:
                    tiempo_inicio_sueno = None

    cv2.putText(frame, texto_estado, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_texto, 2)
    cv2.imshow("Sistema Completo IA", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()