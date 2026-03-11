import numpy as np

def reactions_uniform_load(w, L):
    R = w * L / 2
    return R, R

def shear_distribution(w, L, points=100):
    x = np.linspace(0, L, points)
    R, _ = reactions_uniform_load(w, L)
    V = R - w * x
    return x, V

def shear_midspan(w, L):
    R = w * L / 2
    V = R - w * (L/2)
    return V
