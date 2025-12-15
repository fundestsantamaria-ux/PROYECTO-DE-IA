from src.decision_tree_model import DecisionTreeWrapper, DecisionTreeHeuristic
from src.feature_engineering import compute_nutrient_features
import pandas as pd


class NutriRecommender:
    def __init__(self, model=None):
        self.model = model or DecisionTreeHeuristic()

    def recommend_for_user(self, user_profile, items_df, top_k=10):
        items = compute_nutrient_features(items_df.copy())
        
        # Filtrar por alergias
        items = self._filter_allergies(items, user_profile.get('allergies', []))
        
        # Filtrar por gustos (dislikes)
        items = self._filter_dislikes(items, user_profile.get('dislikes', []))
        
        if len(items) == 0:
            return items  # No hay items disponibles después de filtrar
        
        # Aplicar modelo de recomendación
        items['score_tag'] = items.apply(lambda r: self.model.recommend({**user_profile, **r.to_dict()}), axis=1)
        
        # Calcular score numérico personalizado
        items['score'] = items.apply(lambda r: self._score_row(r, user_profile), axis=1)
        
        # Ordenar y retornar top K
        return items.sort_values('score', ascending=False).head(top_k)

    def _filter_allergies(self, items, allergies):
        """Filtrar items que contengan alérgenos"""
        if not allergies or 'ingredients' not in items.columns:
            return items
        
        def has_allergen(ingredients):
            if pd.isna(ingredients):
                return False
            ingredients_str = str(ingredients).lower()
            return any(allergen.lower() in ingredients_str for allergen in allergies)
        
        return items[~items['ingredients'].apply(has_allergen)]
    
    def _filter_dislikes(self, items, dislikes):
        """Filtrar items que contengan ingredientes no deseados"""
        if not dislikes or 'ingredients' not in items.columns:
            return items
        
        def has_dislike(ingredients):
            if pd.isna(ingredients):
                return False
            ingredients_str = str(ingredients).lower()
            return any(dislike.lower() in ingredients_str for dislike in dislikes)
        
        return items[~items['ingredients'].apply(has_dislike)]

    def _score_row(self, row, user_profile):
        """Sistema de scoring mejorado basado en múltiples factores"""
        score = 100.0  # Score base
        goal = user_profile.get('goal', 'wellness')
        
        # Bonus por categoría de recomendación
        category_scores = {
            'optimal_weightloss': 50,
            'high_protein_bulk': 50,
            'balanced_healthy': 45,
            'high_protein': 40,
            'lowcal_highprot': 40,
            'low_fat_healthy': 35,
            'lowcal': 30,
            'energy_dense': 25,
            'balanced': 20,
            'moderate': 15
        }
        score += category_scores.get(row.get('score_tag', 'balanced'), 10)
        
        # Penalización por distancia (si está disponible)
        distance = row.get('distance_km', 0)
        if distance > 0:
            score -= distance * 2  # -2 puntos por km
        
        # Penalización por precio (si está disponible)
        price = row.get('price', 0)
        if price > 0:
            score -= price * 0.5  # -0.5 puntos por unidad monetaria
        
        # Bonus por ratio de proteína (importante para todos los objetivos)
        protein_ratio = row.get('protein_ratio', 0)
        score += protein_ratio * 50
        
        # Ajustes específicos por objetivo
        if goal == 'lose_weight':
            # Preferir bajas calorías
            if row.get('calories', 0) < 300:
                score += 20
            elif row.get('calories', 0) < 400:
                score += 10
        elif goal == 'gain_muscle':
            # Preferir alta proteína
            if row.get('protein_per_serving', 0) >= 25:
                score += 25
            elif row.get('protein_per_serving', 0) >= 20:
                score += 15
        
        return score