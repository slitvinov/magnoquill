t=0
draw=$ => {
    w = 400
    t || createCanvas(w, w);
    background(9).stroke(w, 96);
    for(t += PI/240, i = 1e4; i--;) {
	x = i
	y = i / 235
	k = (4+sin(x/11+t*8))*cos(x/14)
	e = y/8-19
	d = mag(k, e) + sin(y/9 + t*2)
	point((q=2*sin(k*2)+sin(y/17)*k*(9+2*sin(y-d*3)))+50*cos(c=d*d/49-t)+200,
	      q*sin(c)+d*39-440)
    }
}
