from math import sin, cos, pi, hypot as mag

w = 400
t = 0
for i in range(480):
    canvas = w * w * [0]
    t += pi / 240
    for x in range(10000):
        y = x / 235
        k = (4 + sin(x / 11 + t * 8)) * cos(x / 14)
        e = y / 8 - 19
        d = mag(k, e) + sin(y / 9 + t * 2)
        q = 2 * sin(k * 2) + sin(y / 17) * k * (9 + 2 * sin(y - d * 3))
        c = d * d / 49 - t
        u = q + 50 * cos(c) + 200
        v = q * sin(c) + d * 39 - 440
        u = int(u)
        v = int(v)
        canvas[u + v * w] += 96
