import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Date": ["2023-01-31", "2023-02-28", "2023-03-31", "2023-04-30", "2023-05-31"],
    "Department": ["Sales", "Marketing", "HR", "Finance", "IT"],
    "Revenue": [38714, 15229, 38391, 36943, 44360],
    "Expenses": [9234, 21055, 22385, 8104, 29802],
    "Customer Satisfaction": [1, 4, 1, 5, 7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate KPIs
total_revenue = df["Revenue"].sum()
total_expenses = df["Expenses"].sum()
average_satisfaction = df["Customer Satisfaction"].mean()
df["Profit"] = df["Revenue"] - df["Expenses"]

# Summary table
summary_table = df.groupby("Department").agg({
    "Revenue": "sum",
    "Expenses": "sum",
    "Customer Satisfaction": "mean",
    "Profit": "sum"
}).reset_index()

# Print KPI Report
print("KPI Report")
print("==========")
print(f"Total Revenue: {total_revenue}")
print(f"Total Expenses: {total_expenses}")
print(f"Average Customer Satisfaction: {average_satisfaction:.2f}")
print("\nProfit per Department:")
print(summary_table)

# --- Visualizations ---

# Bar chart: Profit per Department
plt.figure(figsize=(10, 6))
plt.bar(summary_table["Department"], summary_table["Profit"], color='skyblue')
plt.xlabel('Department')
plt.ylabel('Profit')
plt.title('Profit per Department')
plt.tight_layout()
plt.savefig('profit_per_department.png')
plt.show()

# Pie chart: Revenue Distribution
plt.figure(figsize=(8, 8))
plt.pie(summary_table["Revenue"], labels=summary_table["Department"], autopct='%1.1f%%', startangle=140)
plt.title('Revenue Distribution by Department')
plt.tight_layout()
plt.savefig('revenue_distribution.png')
plt.show()

# Line chart: Customer Satisfaction Over Time
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Customer Satisfaction"], marker='o', linestyle='-', color='green')
plt.xlabel('Date')
plt.ylabel('Customer Satisfaction')
plt.title('Customer Satisfaction Over Time')
plt.tight_layout()
plt.savefig('customer_satisfaction_over_time.png')
plt.show()
