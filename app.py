import streamlit as st
import matplotlib.pyplot as plt
from beam_calcs import shear_distribution, shear_midspan

st.title("Reinforced Concrete Beam Shear Solver")

st.sidebar.header("Beam Inputs")

L = st.sidebar.number_input("Beam Length (ft)", value=25.0)
D = st.sidebar.number_input("Dead Load (k/ft)", value=1.8)
L_load = st.sidebar.number_input("Live Load (k/ft)", value=1.4)

# Factored load
wu = 1.2 * D + 1.6 * L_load

st.write("### Factored Load")
st.write(f"w_u = {wu:.2f} k/ft")

# Shear calculation
x, V = shear_distribution(wu, L)

# Plot
fig, ax = plt.subplots()
ax.plot(x, V)
ax.set_xlabel("Beam Length (ft)")
ax.set_ylabel("Shear (kips)")
ax.set_title("Shear Force Diagram")

st.pyplot(fig)

# Midspan shear
V_mid = shear_midspan(wu, L)

st.write("### Shear at Midspan")
st.write(f"{V_mid:.2f} kips")
