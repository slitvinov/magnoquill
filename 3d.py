from math import sin, cos, pi, hypot as mag

for x in range(10000):
    y = x / 235
    k = (4 + sin(x / 11)) * cos(x / 14)
    e = y / 8 - 19
    d = mag(k, e) + sin(y / 9)
    q = 2 * sin(k * 2) + sin(y / 17) * k * (9 + 2 * sin(y - d * 3))
    c = d * d / 49
    u = q + 50 * cos(c)
    v = q * sin(c) + d * 39
    print(u, v)
