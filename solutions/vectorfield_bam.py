import numpy as np


def bam(x, y):
    u = np.cos(x)
    v = np.sin(y)
    return u, v


def circular(x, y):
    u = -y
    v = x
    return (u, v)


def vf1(x, y):
    u = -x + y
    v = x - y
    return u, v


def vf2(x, y):
    u = x
    v = y
    return u, v


def vf3(x, y):
    u = y
    v = x
    return u, v


def vf4(x, y):
    u = x + y
    v = x + y
    return u, v


def vf5(x, y):
    u = x
    v = np.sin(y)
    return u, v


def vf6(x, y):
    u = x
    v = np.sin(x)
    return u, v


def vf7(x, y):
    u = -x
    v = -y
    return u, v
