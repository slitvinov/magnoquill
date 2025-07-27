function setup() {
    w = 400
    t = 0
    createCanvas(w, w)
    stroke(w, 96)
}

function draw() {
    background(9)
    t += PI / 120
    for (x = 0; x < 10000; x++) {
        y = x / 235
        k = (4 + cos(x / 9 - t)) * cos(x / 30)
        e = y / 7 - 13
        d = mag(k, e) + sin(y / 99 + t / 2) - 4
        q = 3 * sin(k * 2) + sin(y / 29) * k * (9 + 2 * sin(cos(e) * 9 - d * 4 + t))
        c = d - t
        u = q + 40 * cos(c) + 200
        v = q * sin(c) + d * 35
        point(u, v)
    }
}
