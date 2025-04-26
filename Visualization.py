# 📦 Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#  Settings
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 100
colors = sns.color_palette("pastel")

#  Create folder for saving plots
if not os.path.exists('plots'):
    os.makedirs('plots')

#  Helper Function
def save_plot(name):
    plt.tight_layout()
    plt.savefig(f"plots/{name}.png")
    plt.show()

#  Load Data
df = pd.read_csv('BlinkIT-Grocery-Data-Cleaned.csv')

# ----------------------------------------------------------------------
#  1. Sales Distribution (Histogram)
plt.figure(figsize=(10,6))
sns.histplot(df['sales'], bins=30, kde=True, color=colors[1])
plt.title('Sales Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Sales ₹', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
save_plot("sales_distribution")

# ----------------------------------------------------------------------
#  2. Sales Distribution (Boxplot)
plt.figure(figsize=(10,6))
sns.boxplot(x=df['sales'], color=colors[0])
plt.title('Boxplot of Sales ₹', fontsize=16, fontweight='bold')
save_plot("sales_boxplot")

# ----------------------------------------------------------------------
#  3. Sales by Item Type (Boxplot)
plt.figure(figsize=(14,7))
sns.boxplot(x='item_type', y='sales', data=df, palette='pastel')
plt.xticks(rotation=90)
plt.title('Sales ₹ by Item Type', fontsize=16, fontweight='bold')
save_plot("sales_by_item_type")

# ----------------------------------------------------------------------
#  4. Sales by Outlet Type (Boxplot)
plt.figure(figsize=(10,6))
sns.boxplot(x='outlet_type', y='sales', data=df, palette='pastel')
plt.title('Sales ₹ by Outlet Type', fontsize=16, fontweight='bold')
save_plot("sales_by_outlet_type")

# ----------------------------------------------------------------------
#  5. Correlation Heatmap
df_numeric = df.select_dtypes(include=['number'])
correlation_matrix = df_numeric.corr()

plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title('Heatmap of Numerical Features', fontsize=16, fontweight='bold')
save_plot("correlation_heatmap")

# ----------------------------------------------------------------------
#  6. Top Selling and Lowest Selling Item
item_sale = df.groupby('item_identifier')['sales'].sum()

top_selling_item = item_sale.idxmax()
lowest_selling_item = item_sale.idxmin()

top_sale = item_sale.max()
lowest_sale = item_sale.min()

plt.figure(figsize=(8,5))
bars = plt.bar([top_selling_item, lowest_selling_item], [top_sale, lowest_sale], color=['green', 'red'])

# Add Labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 500, f'{int(yval)}', ha='center', va='bottom', fontsize=10)

plt.xlabel('Item Identifiers', fontsize=14)
plt.ylabel('Total Sales ₹', fontsize=14)
plt.title('Top Selling vs Lowest Selling Item', fontsize=16, fontweight='bold')
save_plot("top_vs_lowest_selling_item")

print(f"Top selling item: {top_selling_item} - Sales: ₹{top_sale}")
print(f"Lowest selling item: {lowest_selling_item} - Sales: ₹{lowest_sale}")

# ----------------------------------------------------------------------
#  7. Rating Analysis (Average Rating by Item Type)
item_type_avg_rating = df.groupby('item_type')['rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(14,7))
sns.barplot(x=item_type_avg_rating.index, y=item_type_avg_rating.values, palette="viridis")
plt.xticks(rotation=90)
plt.xlabel('Item Type', fontsize=14)
plt.ylabel('Average Rating', fontsize=14)
plt.title('Average Rating by Item Type', fontsize=16, fontweight='bold')
save_plot("rating_analysis")

# ----------------------------------------------------------------------
#  8. Boxplot of Rating by Item Type
plt.figure(figsize=(14,7))
sns.boxplot(x='item_type', y='rating', data=df, palette='coolwarm')
plt.xticks(rotation=90)
plt.title('Distribution of Ratings by Item Type', fontsize=16, fontweight='bold')
save_plot("rating_boxplot")

# Highest and Lowest Rated
highest_rated_item = item_type_avg_rating.idxmax()
lowest_rated_item = item_type_avg_rating.idxmin()

print(f"Highest Rated Item Type: {highest_rated_item}")
print(f"Lowest Rated Item Type: {lowest_rated_item}")

# ----------------------------------------------------------------------
#  9. Highest Selling Product by Item Type
itemtype_highest_sale = df.groupby('item_type')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(14,7))
sns.barplot(x=itemtype_highest_sale.index, y=itemtype_highest_sale.values, palette='viridis')
plt.xticks(rotation=90)
plt.xlabel('Item Type', fontsize=14)
plt.ylabel('Total Sales ₹', fontsize=14)
plt.title('Total Sales by Item Type', fontsize=16, fontweight='bold')
save_plot("highest_selling_product")

highest_sold_product = itemtype_highest_sale.idxmax()
lowest_sold_product = itemtype_highest_sale.idxmin()

print(f"Highest selling product: {highest_sold_product} - Sales: ₹{itemtype_highest_sale.max()}")
print(f"Lowest selling product: {lowest_sold_product} - Sales: ₹{itemtype_highest_sale.min()}")

# ----------------------------------------------------------------------
# 📊 10. Top 10 Highest Selling Items
top_10_items = df.groupby('item_identifier')['sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(14,7))
sns.barplot(x=top_10_items.index, y=top_10_items.values, palette="mako")
plt.xticks(rotation=90)
plt.xlabel('Item Identifier', fontsize=14)
plt.ylabel('Total Sales ₹', fontsize=14)
plt.title('Top 10 Highest Selling Items', fontsize=16, fontweight='bold')
save_plot("top_10_highest_selling_items")

# ----------------------------------------------------------------------

print("\n🎯 All plots saved in 'plots/' folder successfully!")