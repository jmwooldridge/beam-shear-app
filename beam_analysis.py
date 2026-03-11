import numpy as np

def reactions_uniform(w, L):
    R = w * L / 2
    return R, R

def shear_uniform(w, L, n=200):
    x = np.linspace(0, L, n)
    R, _ = reactions_uniform(w, L)
    V = R - w*x
    return x, V

def shear_partial_uniform(w, L, side="left", n=200):

    x = np.linspace(0, L, n)
    R1 = 0
    R2 = 0

    if side == "left":
        a = L/2
        W = w*a
        xbar = a/2
        R2 = W*xbar/L
        R1 = W - R2

    if side == "right":
        a = L/2
        W = w*a
        xbar = L - a/2
        R1 = W*(L-xbar)/L
        R2 = W - R1

    V = []

    for xi in x:

        if side == "left":
            if xi <= L/2:
                V.append(R1 - w*xi)
            else:
                V.append(R1 - w*(L/2))

        if side == "right":
            if xi <= L/2:
                V.append(R1)
            else:
                V.append(R1 - w*(xi-L/2))

    return x, np.array(V)
