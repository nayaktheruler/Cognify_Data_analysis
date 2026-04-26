import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os

# Set working directory to the notebook's location to use relative paths correctly
os.chdir(r"d:\cognify_data_analysis123\level 2")

try:
    # Load dataset
    df = pd.read_csv("../Dataset.csv")

    # Clean & prep
    df = df.dropna(subset=['Cuisines', 'Aggregate rating'])
    df['Cuisines'] = df['Cuisines'].str.strip()
    df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

    # Count frequent cuisine combinations
    combo_counts = df['Cuisines'].value_counts().reset_index()
    combo_counts.columns = ['Cuisine Combination', 'Count']

    # Top 10 combinations
    top_combos = combo_counts.head(10)
    print("Top 10 Cuisine Combos:\n", top_combos)

    # Ratings for top 10 combos
    top_combo_ratings = df[df['Cuisines'].isin(top_combos['Cuisine Combination'])]
    avg_rating_per_combo = top_combo_ratings.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
    avg_rating_per_combo.columns = ['Cuisine Combination', 'Average Rating']

    # Merge for final output
    combo_summary = pd.merge(top_combos, avg_rating_per_combo, on='Cuisine Combination')

    # Plot (clean)
    # plt.show() would block, so we'll just check if it runs
    plt.figure(figsize=(10,6))
    sns.barplot(data=combo_summary, x='Cuisine Combination', y='Count', hue='Cuisine Combination', palette='crest', legend=False)
    plt.title("Top 10 Cuisine Combinations by Frequency")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    # plt.show()

    plt.figure(figsize=(10,6))
    sns.barplot(data=combo_summary, x='Cuisine Combination', y='Average Rating', hue='Cuisine Combination', palette='flare', legend=False)
    plt.title("Top 10 Cuisine Combinations by Average Rating")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    # plt.show()
    print("Execution successful!")

except Exception as e:
    print(f"Error occurred: {e}")
