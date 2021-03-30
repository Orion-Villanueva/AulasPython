import numpy as np

#constantes
h = 1/1000
a = -0.5
e = np.exp(1)

#primeiros elememtos
x0 = 1
x1 = np.exp(h*a)
x2 = np.exp(2*h*a)
L = [x0, x1, x2]

#expressão
U = L[2] + h*a*(23/12*L[2] - 4/3*L[1] + 5/12*L[0])
print(U)

#loop
n=0    
while n < 3:
    u = L[n+2] + h*a*(23/12*L[n+2] - 4/3*L[n+1] + 5/12*L[n])
    L.append(u)
    print(u)
    n=n+1 
print(L)
        
#função
def u(x):    
    n=0    
    while n < x:
        u = L[n+2] + h*a*(23/12*L[n+2] - 4/3*L[n+1] + 5/12*L[n])
        L.append(u)
        n=n+1
        return print(L)
        
u(7)