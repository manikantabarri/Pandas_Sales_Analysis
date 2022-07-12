#!/usr/bin/env python
# coding: utf-8
# # PANDAS SALES ANALYSIS

# ## Objective

# Upon initial inspection of data, we can start thinking of some questions about it that it would be answer.
# - what is the over all sales trend?
# - what are the top 10 products by sales?
# - what are the most selling products?
# - which is the most preffered ship mode?
# - which are the most profitable category and sub category?

# <h4> importing required libraries

# Data Manipulation

import pandas as pd

# Data Visualization

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns

# <h4> IMPORTING THE DATASET

df = pd.read_excel("C:\\Users\\naren\\Desktop\\superstore_sales.xlsx")

# <h4> DATA AUDIT

# First five rows of the Dataset

df.head()

# Last five rows of the Dataset

df.tail()

# Shape of dataset
df.shape

# Columns present in the dataset
df.columns

# A Consice Summary of the Dataset
df.info()

# Checking Missing Vlues
df.isnull().sum()

# Getting descriptive statistics summary
df.describe()


# <h4> Exploratory Data Analysis

# <h2> what is the overall sales trend?

df["order_date"].min()

df["order_date"].max()

# Getting month year from the dataset
df['month_year'] = df['order_date'].apply(lambda x: x.strftime('%Y-%m'))

# Grouping month year 
df_trend = df.groupby("month_year").sum()["sales"].reset_index()

# Setting the figure size
plt.figure(figsize = (15,6))
plt.plot(df_trend['month_year'],df_trend['sales'], color = 'purple')
plt.xticks(rotation = 'vertical', size =8)
plt.show()


# <h2> what are the top 10 products by sales?

# Grouping prosct name column
prod_sales = pd.DataFrame(df.groupby('product_name').sum()["sales"])

# Sorting prod_sales column
prod_sales = prod_sales.sort_values("sales",ascending = False)

# Top 10 products by sales
prod_sales[:10]


# <h4> which are the most selling products?

# Grouping the product name
most_sell_prod = pd.DataFrame(df.groupby("product_name").sum()["quantity"])

# Sorting the most_sell_prod
most_selling_prod = most_sell_prod.sort_values("quantity",ascending = False)

# Most selling products
most_selling_prod[:10]


# <h4>  what is the most preffered ship mode?

# Setting figure size
plt.figure(figsize = (10,8.5))
import seaborn as sns
sns.countplot(df["ship_mode"])
plt.show()


# <h4>which are the most profitable category and sub category?

# Grouping category and sub_category
cat_subcat_profit = pd.DataFrame(df.groupby(["category","sub_category"]).sum()["profit"])

# Sorting cat_subcat_profit
cat_subcat_profit.sort_values(["category","profit"], ascending =  False)


