
## Proyecto de Análisis de Seguridad Urbana con K-Means y Mapa Interactivo

Este proyecto permite analizar datos de seguridad urbana, agrupar zonas según sus características usando K-Means, y visualizar los resultados en un mapa interactivo generado con Folium.

El sistema toma datos recopilados en campo (iluminación, comercios, reportes, flujo de personas, etc.) y crea un mapa con círculos de colores, donde cada color representa un clúster con un nivel similar de seguridad.

## Características principales

Carga un archivo Excel con datos reales recolectados

Limpieza y estandarización del dataset

Conversión de datos en formato numérico

Clasificación automática de zonas usando K-Means (Machine Learning no supervisado)

Generación de un mapa HTML interactivo con marcadores

Círculos coloreados y ampliados para mejor visibilidad

Código en Python, fácil de modificar o ampliar

# ¿El proyecto usa Inteligencia Artificial?

Sí, utiliza un algoritmo de Machine Learning no supervisado llamado K-Means, que permite agrupar zonas según similitudes en:

- Nivel de iluminación

- Cantidad de comercios

- Número de reportes

- Flujo de personas

- Distancia al punto policial más cercano

No predice incidentes, pero clasifica patrones y zonas según nivel de riesgo/similaridad.

##  Estructura del proyecto

Proyecto-Seguridad/
│

├── SEGURIDAD.xlsx         # Base de datos original

├── mapa_zonas.html        # Mapa generado automáticamente

├── main.py                # Código principal del análisis

└── README.md              # Documentación del proyecto

## Tecnologías utilizadas

- Python

- Pandas → manejo y limpieza de datos

- Scikit-learn → algoritmo K-Means

- Folium → creación de mapas interactivos

- MarkerCluster → agrupar marcadores en el mapa


##  Interpretación de colores


| Clúster | Color      | Significado aproximado                     |

| ------- | ---------- | ------------------------------------------ |

| 0       | 🟢 Verde   | Zonas con mejores indicadores              |

| 1       | 🟠 Naranja | Zonas intermedias o mixtas                 |

| 2       | 🔴 Rojo    | Zonas con más reportes / menos iluminación |



## Resultado final

El archivo mapa_zonas.html muestra:

- Círculos de gran tamaño para mejor visibilidad

- Agrupamiento geográfico con colores

- Información de cada punto mediante popup

- Navegación tipo Google Maps (zoom, arrastre, etc.)


