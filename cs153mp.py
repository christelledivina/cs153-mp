def add_subt(m, a, b):
	c = []
	print "\n******************************"
	print "Galois field addition/subtraction is bitwise XOR.\n"
	for x in a:
		print x,
	print "\n"
	for x in b:
		print x,
	print "\n---------------------------\n"

	for i in range(m):
		a = bin(Ax[i])
		b = bin(Bx[i])
		c.append(int(a,2) ^ int(b,2))
	for x in c:
		print x,
	print "\n"
	return c

def mult(m, a, b, px):
	print "\n******************************"
	print "Galois field multiplication.\n"

	for x in a:
		print x,
	print "\n"
	for x in b:
		print x,
	print "\n---------------------------\n"

	p = ''.join(str(e) for e in px)
	p = '0b' + p
	temp = [0]
	for i in range(m-1, -1, -1):
		finalout = []
		m2 = bin(b[i])
		out = [0] * ((m-1) - i)
		for j in range(m-1, -1, -1):
			m1 = bin(a[j])
			coeff = galois_mult_bin(m1, m2, p)
			out = [coeff] + out
		temp = [0]*(len(out) - len(temp)) + temp
		if i != (m-1):
			for x in temp:
				print x,
			print "\n"
		for k in range(len(out)):
			finalout = finalout + [temp[k] ^ out[k]]
		temp = finalout
	return finalout

def galois_mult_bin(m1, m2, p):
	if int(m1, 2) == 0 or int(m2, 2) == 0:
		return 0
	if int(m1, 2) == 1:
		return int(m2, 2)
	if int(m2, 2) == 1:
		return int(m1, 2)
	temp = '0b0'
	for i in range(len(m1)-1, 1, -1):
		out = '0' * ((len(m1) - 1) - i)
		for j in range(len(m2)-1, 1, -1):
			if m1[i] == '1' and m2[j] == '1':
				out = '1' + out
			else:
				out = '0' + out
		out = '0b' + out
		out = int(out, 2) ^ int(temp, 2)
		temp = bin(out)
	if len(temp) > len(p):
		p = p + ('0' * (len(temp) - len(p)))
	return int(temp, 2) ^ int(p, 2)

def output(a, b, c):
	ax = ''
	for i in range(len(a)):
		if a[i] != 0 and ((len(a)-1) - i) != 0:
			ax = ax + str(a[i]) + 'x^' + str((len(a)-1) - i) + " + "
		if ((len(a)-1) - i) == 0:
			ax = ax + str(a[i])
	print "A(x): ", ax

	bx = ''
	for i in range(len(b)):
		if b[i] != 0 and ((len(b)-1) - i) != 0:
			bx = bx + str(b[i]) + 'x^' + str((len(b)-1) - i) + " + "
		if ((len(b)-1) - i) == 0:
			bx = bx + str(b[i])
	print "B(x): ", bx

	cx = ''
	for i in range(len(c)):
		if c[i] != 0 and ((len(c)-1) - i) != 0:
			cx = cx + str(c[i]) + 'x^' + str((len(c)-1) - i) + " + "
		if ((len(c)-1) - i) == 0:
			cx = cx + str(c[i])
	print "C(x): ", cx

def check_input(a, b, p):
	aa = True
	for i in a:
		if not i.isdigit():
			aa = False
	if not aa:
		print "Invalid A(x) input!"	
	bb = True
	for i in b:
		if not i.isdigit():
			bb = False
	if not bb:
		print "Invalid B(x) input!"
	pp = True
	for i in p:
		if not i.isdigit():
			pp = False
	if not pp:
		print "Invalid P(x) input!"
	if not (aa and bb and pp):
		return False
	else:
		return True

####################### Start of program #######################
while (True):
	Ax = raw_input("Enter A(x): ").split()
	Bx = raw_input("Enter B(x): ").split()
	Px = raw_input("Enter P(x): ").split()
	if check_input(Ax, Bx, Px):
		break
Ax = map(int, Ax)
Bx = map(int, Bx)
Px = map(int, Px)
m = len(Ax)

while (True):
	op = input("Pick an operation:\n[1] +\n[2] -\n[3] x\n[4] /\nChoice: ")

	if op == 1 or op == 2:
		c = add_subt(m, Ax, Bx)
		output(Ax, Bx, c)
		break
	elif op == 3:
		c = mult(m, Ax, Bx, Px)
		output(Ax, Bx, c)
		break
	elif op == 4:

		break