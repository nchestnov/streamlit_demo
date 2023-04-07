import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

slider_result = st.slider("Choose sine parameter", 0, 100)

fig, ax = plt.subplots()
x_arr = np.linspace(-10, 10, 500)
y_arr = np.sin(slider_result * x_arr)
ax.plot(x_arr, y_arr)
st.pyplot(fig)

df = pd.DataFrame(y_arr, columns=['y'], index=x_arr)
st.line_chart(df)
