# 🌱 AGRO SENSE AI — El agrónomo en el bolsillo

## Descripción general
**AGROSENSE AI** es un prototipo de sistema de diagnóstico agrícola basado en Inteligencia Artificial y Visión por Computadora.  
Está diseñado para pequeños y medianos agricultores del Ecuador y permite identificar **enfermedades y deficiencias en cultivos a partir de una fotografía tomada con el celular**.

El proyecto sigue tres principios fundamentales:

- **Offline-first:** funciona sin conexión a internet.
- **Edge AI:** el modelo corre directamente en el dispositivo.
- **Human-in-the-loop:** validación humana para casos críticos.

No es solo una app: es una herramienta de apoyo a la toma de decisiones en el campo.

## 🚀 Características principales
- Diagnóstico automático de enfermedades y deficiencias de plantas.
- Modelos ligeros optimizados para Android de gama baja.
- Inferencia local sin necesidad de internet.
- Flujo de validación por agrónomos.
- Diseñado para condiciones reales del campo (mala iluminación, ruido, fotos movidas).
- Base para recolección de datos agrícolas locales.

## 📂 Estructura del proyecto
```text
.
├── train_plantai.py
├── PlantVillage/          # Dataset (no incluido)
├── README.md
├── requirements.txt       # Opcional
└── modelo_plantas_samsung.keras
```

## 🧰 Requisitos
- Python 3.9+
- TensorFlow 2.10+
- numpy
- matplotlib
- pillow
- (Opcional) kaggle CLI

Instalación recomendada:
```bash
pip install tensorflow numpy matplotlib pillow kaggle
```

## 🌾 Dataset
El prototipo utiliza el dataset público **PlantVillage**.

Estructura esperada:
```text
PlantVillage/
 ├── clase_1/
 │   ├── img1.jpg
 │   └── img2.jpg
 ├── clase_2/
 └── clase_n/

⚠️ **Nota:** PlantVillage se usa solo para prototipos.  
Para producción se requieren datos locales ecuatorianos, etiquetados por agrónomos.


## ▶️ Ejecución en VS Code
1. Clona o copia el proyecto.
2. Coloca la carpeta `PlantVillage` en la raíz.
3. (Opcional) Activa un entorno virtual.
4. Ejecuta:

```bash
python train_plantai.py
```

El script:
- Carga el dataset.
- Entrena un modelo CNN ligero.
- Guarda el modelo.
- Ejecuta una prueba de diagnóstico.

## 🧠 Configuración de memoria
Para equipos con recursos limitados:
- Reducir `batch_size`
- Reducir tamaño de imagen (`img_height`, `img_width`)
- Reducir `epochs`

Estas variables están al inicio de `train_plantai.py`.


## 💾 Salida del modelo
El modelo entrenado se guarda como:
```text
modelo_plantas_samsung.keras
```

Este archivo puede:
- Usarse para inferencia local.
- Convertirse a TensorFlow Lite (`.tflite`).
- Integrarse en una app Android.


## 📱 Despliegue en Android (resumen)
- Convertir el modelo a `.tflite`.
- Usar TensorFlow Lite Interpreter.
- Preprocesar imágenes al mismo tamaño del entrenamiento.
- Ejecutar inferencia local (Edge AI).


## 📊 Métricas objetivo
- Accuracy ≥ 85%
- Recall en enfermedades críticas ≥ 95%
- Tiempo de inferencia < 1.5 s
- Reducción de pérdidas agrícolas ≥ 10%


## ⚖️ Ética y seguridad
- La IA **no reemplaza** al agrónomo.
- Las recomendaciones químicas incluyen advertencias.
- Datos anonimizados.
- Consentimiento explícito para compartir imágenes.

## 🗺️ Roadmap
### Fase 1 — MVP
- Cacao
- 4 clases principales
- Pilotos con cooperativas

### Fase 2 — Beta
- Banano y café
- Modelo offline
- Recolección masiva de datos

### Fase 3 — Escala
- Papa y maíz
- Integración con Ministerio
- Alertas tempranas regionales


## 📜 Licencia
MIT License  
(Sujeta a cambios según acuerdos de datos y alianzas institucionales)


## 🤝 Contacto y próximos pasos
El proyecto busca alianzas con:
- Universidades
- Cooperativas agrícolas
- Instituciones públicas
- Agrónomos validadores

**AGRO SENSE AI**  
Tecnología para el campo. Conocimiento en el bolsillo.
