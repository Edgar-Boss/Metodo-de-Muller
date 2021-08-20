import math

#x**4-3*x**3+x**2+x+1
expr = input("Ingrese la funcion: ")
p0 = float(input("Ingrese a: "))
p1 = float(input("Ingrese b: "))
p2 = (p1+p0)/2
x_v = 1#se asigna 1 para que pueda entrar al while

it=0
tol=1.e-4
it_max=100
error = 1

while abs(x_v-p2) > tol and it <= it_max:
#for k in range(0,5):
	it += 1


	libres=dict(x=p0)#Evalua en p0
	func=vars(math)
	fp0=eval(expr,func,libres)

	libres=dict(x=p1)#Evalua en p1
	func=vars(math)
	fp1=eval(expr,func,libres)

	libres=dict(x=p2)#Evalua en p2
	func=vars(math)
	fp2=eval(expr,func,libres)
	h0 = p1-p0
	h1 = p2-p1
	s0 = (fp1 - fp0)/h0
	s1 = (fp2-fp1)/h1
	a = (s1-s0)/(h1-h0)
	b = a*h1+s1 
	c = fp2

	raiz = math.sqrt(b**2-4*a*c)

	if b >= 0:
		raiz = abs(raiz)
	else:
		if(raiz > 0):
			raiz=(-1)*raiz


	
	p3=p2-((2*c)/(b+raiz))

	x_v=p2
	p0=p1
	p1=p2
	p2=p3

	
	
	
	print(p3)
	