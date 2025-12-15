import numpy as np


def compute_nutrient_features(df):
    # normalize to per-100g or per-serving
    df['protein_per_serving'] = df['protein'].fillna(0)
    # Fill calories with 0 if missing (or use estimated_calories if available)
    if 'estimated_calories' in df.columns:
        df['calories'] = df['calories'].fillna(df['estimated_calories'])
    else:
        df['calories'] = df['calories'].fillna(0)
    # simple derived features
    df['protein_ratio'] = df['protein_per_serving'] / (df['calories'] + 1)
    return df