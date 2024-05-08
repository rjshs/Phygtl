import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import numpy as np

# Random seed for reproducibility
np.random.seed(42)

# Sample data: Immersion levels and willingness to re-engage
data = {
    'User_ID': list(range(1, 201)),  # User IDs from 1 to 200
    'Immersion_Level': [
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75,
        90, 85, 88, 91, 70, 95, 80, 84, 92, 75
    ],  # Immersion levels
    'Willingness_to_Reengage': [
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
        85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80,
         85, 90, 95, 80, 75, 70, 85, 90, 95, 80
    ]  # Willingness to re-engage
}

df = pd.DataFrame(data)

print("Descriptive Statistics:\n", df.describe())
# visualize dist for both variables separately and together
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Immersion_Level', y='Willingness_to_Reengage', data=df)
plt.title('Relationship between Immersion Level and Willingness to Re-Engage')
plt.xlabel('Immersion Level (%)')
plt.ylabel('Willingness to Re-Engage (%)')
plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['Immersion_Level'], bins=15, kde=True, color='blue')
plt.title('Distribution of Immersion Levels')

plt.subplot(1, 2, 2)
sns.histplot(df['Willingness_to_Reengage'], bins=15, kde=True, color='green')
plt.title('Distribution of Willingness to Re-Engage')
plt.show()
# The Pearson correlation coefficient indicates the strength and direction of a linear relationship between two variables. 
# A p-value below 0.05 would suggest a statistically significant relationship.
correlation, p_value = pearsonr(df['Immersion_Level'], df['Willingness_to_Reengage'])
print(f"Pearson correlation coefficient: {correlation:.2f}")
print(f"P-value: {p_value:.3f}")