from math import sin, cos, pi, hypot as mag

t = 0
n = 10000
for i in range(960):
    t += pi / 240
    with open("%03d.skel" % i, "w") as file:
        file.write("SKEL\n")
        file.write("%d 1\n" % n)
        for x in range(n):
            y = x / 235
            k = (4 + cos(x / 9 - t)) * cos(x / 30)
            e = y / 7 - 13
            d = mag(k, e) + sin(y / 99 + t / 2) - 4
            q = 3 * sin(k * 2) + sin(
                y / 29) * k * (9 + 2 * sin(cos(e) * 9 - d * 4 + t))
            c = d - t
            u = q + 40 * cos(c) + 200
            v = q * sin(c) + d * 35
            w = 0
            file.write("%.16e %.16e %.16e\n" % (u, -v, w))
        file.write("%d " % n)
        for x in range(n):
            file.write(" %d" % x)
        file.write(" 0\n")
