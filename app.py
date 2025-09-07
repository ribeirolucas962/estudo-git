import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df_reviews = pd.read_csv('datasets\customer reviews.csv')
df_top100_books = pd.read_csv('datasets\Top-100 Trending Books.csv')

dfTopbooks = df_top100_books[df_top100_books['book price'] < 50]

priceMax = dfTopbooks['book price'].max()
priceMin = dfTopbooks['book price'].min()

price_slider = st.slider(
    "Selecionar o preço máximo do livro",
    min_value=int(priceMin),
    max_value=int(priceMax),
    value=int(priceMax)
)
df_top100_books["year of publication"].value_counts()

fig = px.bar(df_top100_books['year of publication'].value_counts())

st.plotly_chart(fig)

fig2 = px.histogram(df_top100_books, x='book price')
st.plotly_chart(fig2)

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)


            