from math import sin, cos, pi, hypot as mag

w = 400
t = 0
h = set()
for i in range(960):
    canvas = w * w * [0]
    t += pi / 240
    for x in range(10000):
        y = x / 235
        k = (4 + cos(x / 9 - t)) * cos(x / 30)
        e = y / 7 - 13
        d = mag(k, e) + sin(y / 99 + t / 2) - 4
        q = 3 * sin(k * 2) + sin(
            y / 29) * k * (9 + 2 * sin(cos(e) * 9 - d * 4 + t))
        c = d - t
        u = q + 40 * cos(c) + 200
        v = q * sin(c) + d * 35
        u = int(u)
        v = int(v)
        canvas[u + v * w] += 96
    with open(f"{i:08}.pgm", "w") as pgm:
        pgm.write(f'''P2
{w} {w}
255
''')
        for u in canvas:
            pgm.write(f"{u}\n")
