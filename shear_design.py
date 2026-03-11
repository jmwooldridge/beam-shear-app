import math

def concrete_shear(fc, bw, d):

    Vc = 2 * math.sqrt(fc) * bw * d / 1000
    return Vc


def stirrup_spacing(Av, fy, d, Vs):

    s = (Av * fy * d) / (Vs * 1000)
    return s
