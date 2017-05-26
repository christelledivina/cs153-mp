def add_subt(m, a, b):
	for i in range(m):
		a = bin(Ax[i])
		b = bin(Bx[i])
		c.append(int(a,2) ^ int(b,2))
	return c

def mult(m, a, b, px):
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

# Ax = map(int, raw_input("Enter A(x): ").split())
# Bx = map(int, raw_input("Enter B(x): ").split())
# Px = map(int, raw_input("Enter P(x): ").split())
Ax = [1,0,7,6]
Bx = [0,1,6,3]
Px = [1,0,1,1]
m = len(Ax)

while (True):
	# op = input("Pick an operation:\n[1] +\n[2] -\n[3] x\n[4] /\nChoice: ")
	op = 3

	if op == 1 or op == 2:
		c = add_subt(m, Ax, Bx)
		break
	elif op == 3:
		c = mult(m, Ax, Bx, Px)
		break
	elif op == 4:

		break