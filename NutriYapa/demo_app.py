"""
NutriYapa - Demo Interactiva
Sistema inteligente de recomendaciones nutricionales
"""
import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Configurar path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.recommender import NutriRecommender
from src.decision_tree_model import DecisionTreeHeuristic

# Configuración de la página
st.set_page_config(
    page_title="NutriYapa - Recomendador Nutricional",
    page_icon="🥗",
    layout="wide"
)

# Título principal
st.title("🥗 NutriYapa - Tu Asistente Nutricional Inteligente")
st.markdown("### Sistema de recomendaciones personalizado para tus objetivos de salud")

# Cargar datos
@st.cache_data
def load_data():
    try:
        recipes = pd.read_csv(PROJECT_ROOT / "data" / "processed" / "recipes.csv")
        # Limpiar datos
        recipes = recipes.dropna(subset=['name', 'calories'])
        # Convertir columnas numéricas
        for col in ['calories', 'protein', 'fat', 'carbs']:
            if col in recipes.columns:
                recipes[col] = pd.to_numeric(recipes[col], errors='coerce')
        recipes = recipes.dropna(subset=['calories', 'protein'])
        return recipes
    except Exception as e:
        st.error(f"Error cargando datos: {e}")
        return pd.DataFrame()

recipes_df = load_data()

if recipes_df.empty:
    st.error("⚠️ No se pudieron cargar los datos. Asegúrate de ejecutar primero prepare_data.py")
    st.stop()

# Sidebar - Configuración del usuario
st.sidebar.header("👤 Tu Perfil")

# Información del usuario
user_id = st.sidebar.text_input("ID de Usuario", "usuario_demo")

# Objetivo principal
goal = st.sidebar.selectbox(
    "🎯 ¿Cuál es tu objetivo?",
    ["lose_weight", "gain_muscle", "wellness"],
    format_func=lambda x: {
        "lose_weight": "🔥 Bajar de peso",
        "gain_muscle": "💪 Ganar músculo",
        "wellness": "🌟 Bienestar general"
    }[x]
)

# Alergias
st.sidebar.subheader("⚠️ Alergias")
allergies = st.sidebar.multiselect(
    "Selecciona tus alergias:",
    ["peanut", "dairy", "egg", "soy", "wheat", "shellfish", "fish", "tree nuts"],
    default=[]
)

# Ingredientes no deseados
st.sidebar.subheader("❌ No me gusta")
dislikes = st.sidebar.multiselect(
    "Ingredientes que prefieres evitar:",
    ["garlic", "onion", "cilantro", "mushroom", "olive", "pickle", "mayo"],
    default=[]
)

# Número de recomendaciones
top_k = st.sidebar.slider("📊 Número de recomendaciones", 5, 20, 10)

# Crear perfil de usuario
user_profile = {
    'user_id': user_id,
    'goal': goal,
    'allergies': allergies,
    'dislikes': dislikes,
    'lat': 0.0,  # Placeholder
    'lon': 0.0   # Placeholder
}

# Sección principal
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Recetas disponibles", f"{len(recipes_df):,}")

with col2:
    goal_emoji = {"lose_weight": "🔥", "gain_muscle": "💪", "wellness": "🌟"}
    st.metric("🎯 Tu objetivo", goal_emoji[goal])

with col3:
    st.metric("🚫 Filtros activos", len(allergies) + len(dislikes))

# Botón para generar recomendaciones
st.markdown("---")
if st.button("✨ Generar Recomendaciones Personalizadas", type="primary", use_container_width=True):
    with st.spinner("🔍 Analizando recetas perfectas para ti..."):
        try:
            # Inicializar recomendador
            recommender = NutriRecommender()
            
            # Obtener recomendaciones
            recommendations = recommender.recommend_for_user(
                user_profile, 
                recipes_df, 
                top_k=top_k
            )
            
            if len(recommendations) == 0:
                st.warning("⚠️ No se encontraron recetas que cumplan con tus criterios. Intenta reducir los filtros.")
            else:
                st.success(f"✅ ¡Encontramos {len(recommendations)} recetas perfectas para ti!")
                
                # Mostrar estadísticas de recomendaciones
                st.markdown("### 📊 Resumen de Recomendaciones")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    avg_calories = recommendations['calories'].mean()
                    st.metric("🔥 Calorías promedio", f"{avg_calories:.0f}")
                with col2:
                    avg_protein = recommendations['protein_per_serving'].mean()
                    st.metric("🥩 Proteína promedio", f"{avg_protein:.1f}g")
                with col3:
                    avg_score = recommendations['score'].mean()
                    st.metric("⭐ Score promedio", f"{avg_score:.1f}")
                with col4:
                    top_category = recommendations['score_tag'].mode()[0] if len(recommendations) > 0 else "N/A"
                    st.metric("🏷️ Categoría principal", top_category)
                
                # Mostrar recomendaciones
                st.markdown("### 🍽️ Tus Recetas Recomendadas")
                
                for idx, row in recommendations.iterrows():
                    with st.expander(f"**{row['name']}** - Score: {row['score']:.1f} ⭐"):
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.markdown(f"**Categoría:** `{row['score_tag']}`")
                            
                            if pd.notna(row.get('description')):
                                st.markdown(f"**Descripción:** {row['description'][:200]}...")
                            
                            if pd.notna(row.get('ingredients')):
                                with st.expander("📝 Ver ingredientes"):
                                    ingredients = str(row['ingredients'])
                                    st.text(ingredients[:500])
                        
                        with col2:
                            st.markdown("#### 📊 Información Nutricional")
                            st.markdown(f"- **Calorías:** {row['calories']:.0f} kcal")
                            st.markdown(f"- **Proteínas:** {row['protein_per_serving']:.1f}g")
                            st.markdown(f"- **Grasas:** {row.get('fat', 0):.1f}g")
                            st.markdown(f"- **Carbohidratos:** {row.get('carbs', 0):.1f}g")
                            st.markdown(f"- **Ratio Proteína:** {row['protein_ratio']:.3f}")
                
                # Gráfico de distribución de categorías
                st.markdown("### 📈 Distribución de Categorías")
                category_counts = recommendations['score_tag'].value_counts()
                st.bar_chart(category_counts)
                
                # Opción de descargar resultados
                csv = recommendations[['name', 'calories', 'protein_per_serving', 'score_tag', 'score']].to_csv(index=False)
                st.download_button(
                    label="📥 Descargar recomendaciones (CSV)",
                    data=csv,
                    file_name=f"nutriyapa_recomendaciones_{user_id}.csv",
                    mime="text/csv"
                )
                
        except Exception as e:
            st.error(f"❌ Error generando recomendaciones: {str(e)}")
            st.exception(e)

# Información adicional en el sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Sobre NutriYapa")
st.sidebar.info(
    """
    **NutriYapa** es un sistema inteligente que te ayuda a:
    
    - 🎯 Alcanzar tus objetivos de salud
    - 🥗 Descubrir recetas saludables
    - 🚫 Evitar alergias e ingredientes no deseados
    - 📊 Tomar decisiones nutricionales informadas
    
    **Objetivos disponibles:**
    - **Bajar de peso:** Recetas bajas en calorías y altas en proteína
    - **Ganar músculo:** Recetas altas en proteína y energía
    - **Bienestar:** Recetas balanceadas y saludables
    """
)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Desarrollado con ❤️ usando Python, FastAPI y Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
