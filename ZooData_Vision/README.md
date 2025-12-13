# Proyecto de Clasificación y Procesamiento de Imágenes de Fauna

Este proyecto implementa un pipeline completo para el procesamiento, detección y clasificación de imágenes de fauna silvestre usando técnicas de visión computacional y aprendizaje profundo.

## Estructura del Proyecto

- `prediction_pipeline.py`: Ejecuta el pipeline principal de procesamiento de imágenes (detección, recorte, mejora y organización).
- `Inferencia.py`: Realiza la inferencia final sobre las imágenes procesadas.
- `run_pipeline.sh`: Script bash para ejecutar ambos pasos en un solo comando.
- `processing/`: Módulos de procesamiento (CLAHE, recortes, detección, etc).
- `models/`: Modelos pre-entrenados utilizados en el pipeline.
- `resultados_megadetector.json`: Salida de detección de MegaDetector.
- `crops_clahe_processed/`: Carpeta de recortes procesados con CLAHE.
- Otros directorios y archivos auxiliares.

## Requisitos

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

## Ejecución del Pipeline Completo

Para ejecutar todo el pipeline (procesamiento + inferencia) en un solo paso:

```bash
./run_pipeline.sh
```

Esto ejecutará primero el procesamiento (`prediction_pipeline.py`) y luego la inferencia (`Inferencia.py`).

## Descripción del Pipeline

1. **Detección con MegaDetector**: Detecta animales en las imágenes.
2. **División de Imágenes**: Separa imágenes con animales y vacías.
3. **Recortes (Crops)**: Genera recortes de las regiones detectadas.
4. **Mejora con CLAHE**: Aplica mejora de contraste a los recortes.
5. **Inferencia**: Clasifica los recortes procesados usando modelos pre-entrenados.

## Notas

- Asegúrate de colocar tus imágenes originales en la carpeta `DATASET_PRUEBA`.
- El pipeline elimina carpetas intermedias automáticamente para ahorrar espacio.
- Modifica los parámetros en los scripts según tus necesidades.
