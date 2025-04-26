import pandas as pd

#Load the dataset
df=pd.read_csv('BlinkIT-Grocery-Data.csv')


# 1. Quick look
print(df.info())
print(df.head())
print(df.describe())

# 2. Removing duplicate value if any exits
df=df.drop_duplicates()
print(f"\nData after removing duplicates: {df.shape}")

# 3. Handling missing value
print(df.isnull().sum()) #checking missing value
df=df.dropna()  # dropping missing value in item weight


# 4. Replacing Values
df['Item Fat Content']=df['Item Fat Content'].replace({
    "LF" : "Low Fat",
    'lf':'Low Fat',
    'low fat':'Low Fat',
    'reg':'Regular',
    'regular':'Regular'
})


# 5.Clean Column Name
df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")


# 6. Confirm the cleaning
print("\n✅ Final Cleaned Data Info:")
print(df.info())
print(df.head())
print(df.describe())

# 7. Save Cleaned File
df.to_csv('BlinkIT-Grocery-Data-Cleaned.csv',index=False)



