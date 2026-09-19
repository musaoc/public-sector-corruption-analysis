"""
Public Sector Corruption Analytics — Bribe Reporting Study
An investigative data analytics project analyzing citizen-reported corruption records to uncover systemic patterns, most affected public departments, and geographic bribe concentrations.

Original Kaggle Notebook: https://www.kaggle.com/code/lazer999/exposing-the-most-corrupt-departments
Author: Muhammad Musa Khan (Kaggle Master: https://kaggle.com/lazer999)
"""

import os
import sys
import warnings
warnings.filterwarnings("ignore")

# --- Smart Dataset Path Resolution ---
def _resolve_data_path(file_path):
    """Checks local and data/ directories if dataset path is missing."""
    if os.path.exists(file_path):
        return file_path
    base = os.path.basename(file_path)
    candidates = [
        base,
        os.path.join("data", base),
        os.path.join("..", "data", base),
        file_path.replace("/kaggle/input/", "data/"),
        file_path.replace("../input/", "data/"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return file_path

# --- Pipeline Execution ---

# --- Cell 1 ---
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

import warnings
warnings.filterwarnings('ignore')

# --- Cell 2 ---
df=pd.read_csv('../input/corruption/data.csv',parse_dates=["Date"])

# --- Cell 3 ---
df.head()

# --- Cell 4 ---
df.info()

# --- Cell 5 ---
r,c=df.shape
print('The dataset has ',r,' rows and ',c,' columns.' )

# --- Cell 6 ---
df.describe()

# --- Cell 7 ---
df.describe(include=object)

# --- Cell 8 ---
df.isnull().sum()

# --- Cell 9 ---
df[df['Department'].isnull()].head()

# --- Cell 10 ---
df['Department'].fillna('Others',inplace=True)

# --- Cell 11 ---
sns.histplot(df['Amount(INR)'],kde=True,bins=1000);
#data is highly skewed.

# --- Cell 12 ---
df['Amount(INR)'].quantile(0.90)

# --- Cell 13 ---
# Switching to only relevant data
df=df[df['Amount(INR)']<df['Amount(INR)'].quantile(0.90)]
#df

# --- Cell 14 ---
sns.histplot(df['Amount(INR)'],kde=True);

# --- Cell 15 ---
df.isnull().sum()

# --- Cell 16 ---
df.sample(5)

# --- Cell 17 ---
### Exploring
df.Department.unique()

# --- Cell 18 ---
df[['City','Province']]=df['Location'].str.split(',',expand=True)

# --- Cell 19 ---
df.head()

# --- Cell 20 ---
sns.heatmap(df.corr(), annot=True);

# --- Cell 21 ---
most_bribe_area=df.groupby(['City'])['Amount(INR)'].agg(['count','sum']).sort_values(by='count',ascending=False).head(10)

# --- Cell 22 ---
most_bribe_area

# --- Cell 23 ---
sns.barplot(y=most_bribe_area.index,x=most_bribe_area['count'])
plt.xlabel('Count')
plt.ylabel("Cities")
plt.title('Most Bribes taken by City?');
# Bangalore,Karnataka has the highest number of reported cases against bribery

# --- Cell 24 ---
most_bribe_province=df.groupby(['Province'])['Amount(INR)'].agg(['count','sum']).sort_values(by='count',ascending=False).head(10)
sns.barplot(y=most_bribe_province.index,x=most_bribe_province['count']);

# --- Cell 25 ---
depart_freq=df.groupby('Department')['Amount(INR)'].agg(['count','sum']).sort_values(by='count',ascending=False).head(10)
#Traffic taking the top of lists

# --- Cell 26 ---
sns.barplot(y=depart_freq.index,x=depart_freq['count']);

# --- Cell 27 ---
depart_sum=df.groupby('Department')['Amount(INR)'].agg(['mean','sum']).sort_values(by='sum',ascending=False).head(10)
depart_sum

# --- Cell 28 ---
sns.barplot(y=depart_sum.index,x=depart_sum['sum']);

# --- Cell 29 ---
df_day=df[["Amount(INR)",'Date']].copy()
df_day.head()

# --- Cell 30 ---
df_day["Day_of_month"]=df["Date"].dt.day
df_day["Week_of_year"]=df["Date"].dt.week
df_day["Year"]=df["Date"].dt.year
df_day["Month"]=df["Date"].dt.month
df_day['Day_of_week']=df['Date'].dt.dayofweek

# --- Cell 31 ---
df_day

# --- Cell 32 ---
sns.histplot(data=df_day["Day_of_month"],bins=31)
plt.ylabel("Number of bribes taken")
plt.title("Days of the Month");

# --- Cell 33 ---
sns.histplot(data=df_day["Year"])
plt.ylabel("Number of bribes taken")
plt.title("Years");

# --- Cell 34 ---
sns.histplot(data=df_day["Month"],bins=12)
plt.ylabel("Number of bribes taken")
plt.title("Bribes paid per month");

# --- Cell 35 ---
sns.histplot(data=df_day["Day_of_week"],bins=7)
plt.ylabel("Number of bribes taken")
plt.title("Days of the WEEK")
plt.xticks([0, 1, 2,3,4,5,6], ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],rotation=90);

# --- Cell 36 ---
sns.heatmap(df_day.corr(),annot=True)



if __name__ == "__main__":
    print("Pipeline execution complete.")
