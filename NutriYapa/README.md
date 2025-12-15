# 🥗 NutriYapa - Sistema Inteligente de Recomendaciones Nutricionales

Sistema inteligente de recomendaciones para guiar al usuario hacia su meta física mediante productos y comidas saludables adaptadas a sus gustos, necesidades y objetivos personales.

## 🎯 Características

- **Recomendaciones Personalizadas**: Basadas en objetivos (bajar de peso, ganar músculo, bienestar)
- **Filtros Inteligentes**: Respeta alergias e ingredientes no deseados
- **Scoring Avanzado**: Algoritmo que considera múltiples factores nutricionales
- **Demo Interactiva**: Interfaz web amigable con Streamlit
- **API REST**: Endpoint para integración con otras aplicaciones

## 🚀 Objetivos Soportados

### 🔥 Bajar de Peso (lose_weight)
- Recetas bajas en calorías (< 400 kcal)
- Alto contenido de proteína para saciedad
- Prioriza opciones nutritivas y ligeras

### 💪 Ganar Músculo (gain_muscle)
- Alto contenido proteico (≥ 20-25g)
- Calorías suficientes para crecimiento muscular
- Balance adecuado de macronutrientes

### 🌟 Bienestar General (wellness)
- Balance nutricional óptimo
- Opciones saludables y variadas
- Enfoque en nutrición completa

## 📦 Instalación

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# En Windows:
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 🗄️ Preparar Datos

```bash
# Procesar datasets
python script/prepare_data.py

# Entrenar modelo (opcional)
python script/train_model.py
```

## 🖥️ Ejecutar Demo Interactiva

```bash
streamlit run demo_app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

## 🌐 Ejecutar API REST

```bash
python -m uvicorn src.api:app --reload --port 8000
```

La API estará disponible en `http://localhost:8000`
- Documentación: `http://localhost:8000/docs`

### Ejemplo de uso de la API:

```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "lat": 0.0,
    "lon": 0.0,
    "goal": "lose_weight",
    "allergies": ["peanut", "dairy"],
    "dislikes": ["mushroom"]
  }'
```

## 📊 Estructura del Proyecto

```
NutriYapa/
├── data/
│   ├── raw/              # Datos sin procesar
│   └── processed/        # Datos procesados
├── models/               # Modelos entrenados
├── src/
│   ├── api.py           # API FastAPI
│   ├── recommender.py   # Sistema de recomendaciones
│   ├── decision_tree_model.py  # Modelo de decisión
│   ├── feature_engineering.py  # Procesamiento de features
│   ├── data_loader.py   # Cargador de datos
│   └── config.py        # Configuración
├── script/
│   ├── prepare_data.py  # Preparación de datos
│   └── train_model.py   # Entrenamiento de modelo
├── demo_app.py          # Demo interactiva Streamlit
└── requirements.txt     # Dependencias
```

## 🧪 Cómo Funciona

1. **Carga de Datos**: Se cargan recetas con información nutricional
2. **Filtrado**: Se eliminan recetas con alérgenos o ingredientes no deseados
3. **Feature Engineering**: Se calculan métricas nutricionales derivadas
4. **Clasificación**: El modelo asigna categorías según el objetivo del usuario
5. **Scoring**: Sistema de puntuación que considera:
   - Categoría de recomendación
   - Ratio proteína/calorías
   - Ajustes por objetivo específico
   - Distancia y precio (cuando disponible)
6. **Rankings**: Se retornan las mejores opciones ordenadas por score

## 🎨 Características de la Demo

- **Perfil de Usuario**: Configura objetivo, alergias y preferencias
- **Recomendaciones en Tiempo Real**: Genera sugerencias personalizadas
- **Visualizaciones**: Gráficos de distribución de categorías
- **Información Nutricional Detallada**: Calorías, proteínas, grasas, carbohidratos
- **Exportación**: Descarga recomendaciones en CSV

## 🛠️ Tecnologías

- **Python 3.8+**
- **Pandas**: Manipulación de datos
- **Scikit-learn**: Machine Learning
- **FastAPI**: API REST
- **Streamlit**: Interfaz web interactiva
- **Joblib**: Persistencia de modelos

## 📈 Categorías de Recomendación

- `optimal_weightloss`: Óptimo para pérdida de peso
- `high_protein_bulk`: Alto en proteína para volumen
- `balanced_healthy`: Balance saludable
- `high_protein`: Alto contenido proteico
- `lowcal_highprot`: Bajo en calorías, alto en proteína
- `low_fat_healthy`: Bajo en grasas, saludable
- `lowcal`: Bajo en calorías
- `energy_dense`: Denso en energía
- `balanced`: Balanceado
- `moderate`: Moderado

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto.

## 👥 Autores

Desarrollado con ❤️ para ayudar a las personas a alcanzar sus objetivos de salud.
