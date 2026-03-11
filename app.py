import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from beam_analysis import *
from shear_design import *

st.title("ACI Beam Shear Solver")

st.sidebar.header("Beam Inputs")

L = st.sidebar.number_input("Span (ft)", value=25.0)
D = st.sidebar.number_input("Dead Load k/ft", value=1.8)
L_load = st.sidebar.number_input("Live Load k/ft", value=1.4)

fc = st.sidebar.number_input("f'c (psi)", value=4500)
fy = st.sidebar.number_input("fy (psi)", value=40000)

bw = st.sidebar.number_input("Web width (in)", value=12)
d = st.sidebar.number_input("Effective depth (in)", value=14)

# load combinations

w1 = 1.2*D + 1.6*L_load
wD = 1.2*D
wL = 1.6*L_load

st.write("### Factored Loads")

st.write("Case 1:", w1)
st.write("Case 2: 1.2D + 1.6L on left half")
st.write("Case 3: 1.2D + 1.6L on right half")

# shear diagrams

x1,V1 = shear_uniform(w1,L)
x2,V2 = shear_partial_uniform(wL,L,"left")
x3,V3 = shear_partial_uniform(wL,L,"right")

# envelope

Venv = np.maximum.reduce([np.abs(V1),np.abs(V2),np.abs(V3)])

# plot

fig,ax = plt.subplots()

ax.plot(x1,V1,label="Case 1")
ax.plot(x2,V2,label="Left Half Live")
ax.plot(x3,V3,label="Right Half Live")

ax.set_xlabel("Length (ft)")
ax.set_ylabel("Shear (kips)")
ax.legend()

st.pyplot(fig)

# envelope plot

fig2,ax2 = plt.subplots()
ax2.plot(x1,Venv)

ax2.set_title("Shear Envelope")
ax2.set_xlabel("Length (ft)")
ax2.set_ylabel("Shear (kips)")

st.pyplot(fig2)

# design

Vu = max(Venv)

Vc = concrete_shear(fc,bw,d)

phi = 0.75

Vs_req = Vu/phi - Vc

Av = 2*0.11

s = stirrup_spacing(Av,fy,d,Vs_req)

st.write("### Shear Design")

st.write("Vu =",Vu,"kips")

st.write("Vc =",Vc,"kips")

st.write("Required Vs =",Vs_req,"kips")

st.write("Stirrup spacing =",s,"in")
