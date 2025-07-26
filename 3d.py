from math import sin, cos, pi, hypot as mag

t = 0
n = 10000
for i in range(480):
    t += pi / 240
    with open("%03d.skel" % i, "w") as file:
        file.write("SKEL\n")
        file.write("%d 1\n" % n)
        for x in range(n):
            y = x / 235
            k = (4 + sin(x / 11 + t * 8)) * cos(x / 14)
            e = y / 8 - 19
            d = mag(k, e) + sin(y / 9 + t * 2)
            q = 2 * sin(k * 2) + sin(y / 17) * k * (9 + 2 * sin(y - d * 3))
            c = d * d / 49 - t
            u = 50 * cos(c) + q
            v = d * 39 + q * sin(c)
            w = 30 * sin(c / 2 + 0.1 * q)
            file.write("%.16e %.16e %.16e\n" % (u, v, w))
        file.write("%d " % n)
        for x in range(n):
            file.write(" %d" % x)
        file.write(" 0\n")
