import pandas as pd
from pathlib import Path

# Get the project root directory (parent of script directory)
PROJECT_ROOT = Path(__file__).parent.parent
RAW = PROJECT_ROOT / "data" / "raw"
PROC = PROJECT_ROOT / "data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

def clean_recipes():
    try:
        df = pd.read_csv(RAW / "recipes.csv")
        print(f"Recipes loaded: {len(df)} rows")
        # Map actual column names to desired names
        column_mapping = {
            'Name': 'name',
            'RecipeIngredientParts': 'ingredients',
            'Calories': 'calories',
            'ProteinContent': 'protein',
            'FatContent': 'fat',
            'CarbohydrateContent': 'carbs',
            'Description': 'description',
            'RecipeInstructions': 'instructions'
        }
        # Select and rename columns that exist
        cols_to_keep = [col for col in column_mapping.keys() if col in df.columns]
        df = df[cols_to_keep]
        df = df.rename(columns=column_mapping)
        # Drop rows with missing critical data
        df = df.dropna(subset=['name', 'calories'], how='any')
        df.to_csv(PROC / "recipes.csv", index=False)
        print(f"Recipes processed: {len(df)} rows with columns {df.columns.tolist()}")
    except Exception as e:
        print(f"Error processing recipes: {e}")

def clean_products():
    try:
        # Read with error handling for malformed lines
        df = pd.read_csv(RAW / "en.openfoodfacts.org.products.csv", 
                        sep='\t', 
                        low_memory=False, 
                        on_bad_lines='skip',  # Skip malformed lines
                        encoding='utf-8',
                        nrows=100000)  # Limit to first 100k rows for performance
        # Select columns that exist
        cols_to_keep = []
        for col in ['product_name', 'ingredients_text', 'nutriscore_grade', 
                    'energy-kcal_100g', 'proteins_100g', 'carbohydrates_100g', 'fat_100g']:
            if col in df.columns:
                cols_to_keep.append(col)
        if cols_to_keep:
            df = df[cols_to_keep]
        df.to_csv(PROC / "products.csv", index=False)
        print(f"Products processed: {len(df)} rows")
    except Exception as e:
        print(f"Error processing products: {e}")
        print("Creating empty products.csv as fallback")

if __name__ == "__main__":
    clean_recipes()
    clean_products()
    print("Datasets preparados en data/processed/")
