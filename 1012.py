i=input().split()
a=float(i[0])
b=float(i[1])
c=float(i[2])
pi=3.14159

print("TRIANGULO: {0:.3f}".format((a*c)/2))
print("CIRCULO: {0:.3f}".format((pi*(c**2))))
print("TRAPEZIO: {0:.3f}".format(((a+b)*c)/2))
print("QUADRADO: {0:.3f}".format(b**2))
print("RETANGULO: {0:.3f}".format(a*b))
