import pandas as pd
import re

# Read the TSV file exported from AlphaLasso
df = pd.read_csv("/Users/thuytrangskalska/Documents/Python /AlphaLasso_20251107_002816.tsv", sep="\t")

# Names of the columns
print(df.columns.tolist())

# Create a new column for simple Lasso type: L4, L5, etc.
df['Lasso_type_simple'] = df['#Lasso_type'].apply(
    lambda x: re.findall(r'L[+\-*]?([4-8])', str(x).strip())[0] if (pd.notna(x) and re.findall(r'L[+\-*]?([4-8])', str(x).strip())) else None
)
df['Lasso_type_simple'] = df['Lasso_type_simple'].apply(lambda n: f"L{n}" if n else None)

# Calculate overall averages
overall_avg_loop_area = df['Loop_area'].mean()
overall_avg_loop_length = df['Loop_length'].mean()
overall_avg_plddt_chain = df['pLDDT_chain'].mean()

# Print overall averages
print("Overall Averages:")
print(f"Loop_area: {overall_avg_loop_area:.2f}")
print(f"Loop_length: {overall_avg_loop_length:.2f}")
print(f"pLDDT_chain: {overall_avg_plddt_chain:.2f}")

#Overall Averages:
#Loop_area: 3810.33
#Loop_length: 161.53
#pLDDT_chain: 86.86

# Group by Lasso_type_simple and compute averages
grouped = df.groupby('Lasso_type_simple').agg({
    'Loop_area': 'mean',
    'Loop_length': 'mean',
    'pLDDT_chain': 'mean'
}).reset_index()

# Print group averages
print("\nAverages by Lasso type:")
print(grouped)

#Averages by Lasso type:
  #Lasso_type_simple    Loop_area  Loop_length  pLDDT_chain
#0                L4  4473.634237   192.751295    87.210411
#1                L5  5338.300199   214.553191    86.497149
#2                L6  1836.486904    78.300317    85.855635
#3                L7  3163.900135   140.624719    89.831191
#4                L8  2920.174963   102.083951    88.502222

grouped.to_csv("lasso_proteins_stats.csv", index=False)


