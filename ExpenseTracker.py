import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# csv file
filename = "expenses.csv"

# create csv with headers if it doesn't exist
if not os.path.exists(filename):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(filename, index=False)

# load existing expenses
df = pd.read_csv(filename)

# user's inputs
# Date (default: today)
date_input = input("Date (YYYY-MM-DD): ").strip()
if date_input == "":
    date = str(datetime.today().date())
else:
    date = date_input

# category (default: 'Other')
category = input("Category: ").strip()
if category == "":
    category = "Other"

# amount (default: 0.0)
amount_input = input("Amount: ").strip()
try:
    amount = float(amount_input) if amount_input != "" else 0.0
except ValueError:
    print("Invalid amount, setting to 0.0")
    amount = 0.0

# description
description = input("Description: ").strip()
if description == "":
    description = ""

# create a dictionary with user's inputs
new_expense = {
    "Date": date,
    "Category": category,
    "Amount": amount,
    "Description": description
}

# Old
# add new row to df
# df = df.append(new_expense, ignore_index=True)

# New (pandas 2.x)
#creates a df with one row and the columns from the dictionary keys
df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)

# save back to csv
df.to_csv(filename, index=False)

print("Expense added successfully!")

# optional graph
plot_choice = input("Do you want to see a graph of expenses by category? (y/n): ").strip().lower()
if plot_choice == "y":
    category_sum = df.groupby("Category")["Amount"].sum()
    category_sum.plot(kind="bar", color="skyblue")
    plt.ylabel("Amount")
    plt.title("Total Expenses by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()