a=input().split()
b=input().split()

n1=int(a[1])
n2=int(b[1])
v1=float(a[2])
v2=float(b[2])
valor=((n1*v1)+(n2*v2))

print("VALOR A PAGAR: R$ {0:.2f}".format(valor))