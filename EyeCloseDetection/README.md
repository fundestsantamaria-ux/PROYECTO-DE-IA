# EyeClose Detection  
Sistema de Detección de Somnolencia

## 1. Descripción General
EyeClose Detection es un sistema desarrollado en Python que permite identificar señales de somnolencia mediante la detección del cierre prolongado de los ojos en tiempo real.  
Para ello, emplea técnicas de visión por computadora e inteligencia artificial basadas en el cálculo del Eye Aspect Ratio (EAR), utilizando la malla facial provista por MediaPipe Face Mesh.

El sistema genera alertas visuales y sonoras cuando detecta que el usuario mantiene los ojos cerrados durante un periodo determinado, lo cual permite prevenir accidentes o pérdida de atención en actividades críticas.

## 2. Objetivo
El propósito del sistema es detectar somnolencia en tiempo real a través de:

- Medición de la apertura ocular mediante el cálculo del EAR.  
- Detección del cierre prolongado de párpados con MediaPipe Face Mesh.  
- Generación de alertas visuales y auditivas ante señales de sueño.  
- Implementación de una solución accesible sin necesidad de hardware especializado.  
- Visualización en pantalla del proceso de detección y del valor del EAR.  

## 3. Entradas del Sistema
El programa requiere los siguientes elementos:

- Cámara web funcional.  
- Buenas condiciones de iluminación para una correcta detección facial.  

Las bibliotecas necesarias deben estar instaladas en el entorno Python, incluyendo:

- OpenCV  
- MediaPipe  
- SciPy  
- Winsound (para alertas en Windows)

## 4. Procesamiento y Funcionamiento

### 4.1 Captura y detección facial
El sistema accede a la cámara web y utiliza MediaPipe Face Mesh para identificar una malla de 468 puntos en el rostro del usuario.  
A partir de puntos específicos de ambos ojos, se extraen las coordenadas necesarias para calcular el EAR.

### 4.2 Cálculo del EAR (Eye Aspect Ratio)
El EAR se determina usando distancias verticales y horizontales entre puntos clave del ojo.  
Un valor alto indica un ojo abierto y un valor bajo indica un ojo cerrado.

### 4.3 Detección de cierre prolongado
El sistema compara continuamente el valor del EAR con un umbral definido.  
Si el EAR se mantiene por debajo de este umbral durante un periodo determinado, se interpreta como una señal de somnolencia.

### 4.4 Alertas
Ante la detección de cierre prolongado, el sistema emite:

- Alerta visual en pantalla.  
- Alerta sonora a través del módulo winsound.  

## 5. Salidas del Sistema
El programa proporciona:

- Visualización en tiempo real de la cámara con puntos faciales y estado del ojo.  
- Valor del EAR actualizado constantemente.  
- Activación automática de alarmas visuales y sonoras cuando se detecta somnolencia.

## 6. Resultados Obtenidos
El sistema detecta de forma efectiva el cierre prolongado de los ojos, mostrando que las técnicas de visión por computadora e inteligencia artificial son útiles para prevenir somnolencia en actividades como conducción, estudio o trabajo operativo.

## 7. Equipo de Desarrollo
Proyecto desarrollado como parte del Proyecto Final del Módulo de Inteligencia Artificial  
Samsung Innovation Campus – SIC 2025
