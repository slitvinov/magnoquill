from math import sin, cos, pi, hypot as mag

nu = 206
nv = 309
t = 0
for i in range(480):
    canvas = nv * nu * [0]
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
        u -= 96
        v -= 55
        canvas[u + v * nu] += 96

    with open(f"{i:08}.pgm", "w") as pgm:
        pgm.write(f'''P2
{nu} {nv}
255
''')
        for u in canvas:
            pgm.write(f"{u}\n")
