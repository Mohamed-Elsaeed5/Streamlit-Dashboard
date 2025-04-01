# !pip install plotly
#import libraries
import pandas as pd
import numpy as np
import plotly.express as px 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
#Read data
df = pd.read_csv('sleep.csv')
df.head()
#cleaning
df['Sleep Disorder']= df['Sleep Disorder'].replace(np.nan,'Normal')
#sidebar
st.sidebar.header("Sleep dashboard")
st.sidebar.image('download.jpg')
st.sidebar.write('The purpose of dashboard is to show the reasons of sleep disorder')
#sidebar filters
cat_filter = st.sidebar.selectbox('Filters',['Gender','Occupation','BMI Category',None,'Sleep Disorder'])
#Kpis
a1, a2, a3, a4 = st.columns(4)
a1.metric("Avg age", round(df['Age'].mean(), 2))
a2.metric("Count of ID", round(df['Person ID'].count(), 0))
a3.metric("Max daily steps", round(df['Daily Steps'].max(), 0))
a4.metric("Avg sleep duration", round(df['Sleep Duration'].mean(), 0))
st.subheader('Sleep quality vs stress level',)
fig = px.scatter(data_frame=df,x='Stress Level',y='Quality of Sleep',color=cat_filter,size='Quality of Sleep')
st.plotly_chart(fig,use_container_width=True)
#bottom charts
c1,c2 = st.columns([4,3])
with c1:
    st.text('Occupation VS Avg Sleep Duration (Sorted)')
    # حساب المتوسط وترتيب البيانات
    avg_sleep_by_occ = df.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False).reset_index()
    fig1 = px.bar(data_frame=avg_sleep_by_occ, x='Occupation', y='Sleep Duration')
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.text('Gender VS Quality of Sleep')
    gender_sleep = df.groupby('Gender')['Quality of Sleep'].mean().reset_index()
    fig2 = px.pie(gender_sleep, names='Gender', values='Quality of Sleep')
    st.plotly_chart(fig2, use_container_width=True)
st.subheader("Pair Plot & Heatmap for Numerical Features")

# اختيار الأعمدة الرقمية
num_cols = ['Physical Activity Level', 'Stress Level', 'Daily Steps', 'Quality of Sleep']
df_num = df[num_cols]

# Pair Plot
st.text("Pair Plot")
fig_pair = sns.pairplot(df_num)
st.pyplot(fig_pair)

st.text("Correlation Heatmap (Selected Numerical Features)")

# Choose columns
selected_cols = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
                 'Stress Level', 'Heart Rate', 'Daily Steps']
df_selected = df[selected_cols]

# heatmap
fig_heat, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_selected.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig_heat)

