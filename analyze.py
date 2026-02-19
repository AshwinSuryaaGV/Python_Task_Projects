import pandas as pd

# Step 1: Load CSV
df = pd.read_csv("students.csv")

# Step 2: Basic Info
print("First 5 rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

# Step 3: Add Total & Average Columns
df["Total"] = df["Maths"] + df["Physics"] + df["Chemistry"]
df["Average"] = df["Total"] / 3

# Step 4: Find Top Performer
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performer:")
print(top_student)

# Step 5: Save Updated CSV
df.to_csv("students_updated.csv", index=False)

print("\nUpdated file saved successfully!")
