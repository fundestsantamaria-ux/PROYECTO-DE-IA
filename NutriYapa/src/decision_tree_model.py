import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text


class DecisionTreeWrapper:
    def __init__(self, model=None):
        self.model = model

    def train(self, X, y, max_depth=5):
        self.model = DecisionTreeClassifier(max_depth=max_depth)
        self.model.fit(X, y)
        return self.model

    def predict(self, X):
        return self.model.predict(X)

    def export_rules(self, X):
        return export_text(self.model, feature_names=list(X.columns))


# Heuristic tree for production
class DecisionTreeHeuristic:
    def __init__(self):
        pass

    def recommend(self, row):
        # Recomendaciones basadas en objetivos
        goal = row.get('goal', 'wellness')
        calories = row.get('calories', 0)
        protein = row.get('protein_per_serving', 0)
        fat = row.get('fat', 0)
        carbs = row.get('carbs', 0)
        
        if goal == 'gain_muscle':
            # Ganar músculo: alto en proteína y calorías moderadas-altas
            if protein >= 25 and calories >= 400:
                return 'high_protein_bulk'
            elif protein >= 20:
                return 'high_protein'
            elif calories > 500:
                return 'energy_dense'
            else:
                return 'balanced'
                
        elif goal == 'lose_weight':
            # Bajar de peso: bajo en calorías, alto en proteína
            if calories < 300 and protein >= 20:
                return 'optimal_weightloss'
            elif calories < 400 and protein >= 15:
                return 'lowcal_highprot'
            elif calories < 400:
                return 'lowcal'
            else:
                return 'moderate'
                
        else:  # wellness - bienestar general
            # Balance nutricional
            protein_ratio = protein / (calories + 1)
            if protein_ratio > 0.15 and calories < 500:
                return 'balanced_healthy'
            elif fat < 15 and calories < 450:
                return 'low_fat_healthy'
            else:
                return 'balanced'