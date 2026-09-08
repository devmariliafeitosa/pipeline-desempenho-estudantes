import pandas as pd

df = pd.read_csv("data/raw/student_prediction.csv")

print("DIMENSÕES:")
print(df.shape)

print("\nCOLUNAS:")
print(df.columns.tolist())