import numpy as np


def curl(self, x, y, eps=1e-6):
    u_x, v_x = self.field(x + eps, y)
    u_y, v_y = self.field(x, y + eps)
    du_dx = (u_x - self.field(x, y)[0]) / eps
    dv_dx = (v_x - self.field(x, y)[1]) / eps
    du_dy = (u_y - self.field(x, y)[0]) / eps
    dv_dy = (v_y - self.field(x, y)[1]) / eps
    return dv_dx - du_dy


def divergence(self, x, y, eps=1e-6):
    u_x, v_x = self.field(x + eps, y)
    u_y, v_y = self.field(x, y + eps)
    du_dx = (u_x - self.field(x, y)[0]) / eps
    dv_dx = (v_x - self.field(x, y)[1]) / eps
    du_dy = (u_y - self.field(x, y)[0]) / eps
    dv_dy = (v_y - self.field(x, y)[1]) / eps
    return du_dx + dv_dy


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
