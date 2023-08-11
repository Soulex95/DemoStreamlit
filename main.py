import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hello streamlit")
st.header("Deployer son model")
st.subheader("ML")
genre = st.text_area('donne 1 si femme et 0 si homme')
if st.button("appuyer"):
    st.write(genre)
st.caption("c'est un caption")
st.code("2x + 5 = 0")
st.latex(''' x + 2x^2 + 4x^3''')
st.image("Bureau.jpg")
st.checkbox('oui')
st.radio('choisi ton genre', ['M','F'])
st.number_input('choisi un nombre', 0,20)
st.text_input('ecris le texte')
st.date_input("la date")
st.time_input('time')

data = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(data, bins=15)
st.pyplot(fig)

#st.
dt = pd.DataFrame(np.random.randn(10,2), columns=["x", "y"])

st.area_chart(dt)

