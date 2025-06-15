import numpy as np


def trapezoid (a,b,n,f):
    h=(b-a)/n
    x=a
    
    integral = f(a)
    for i in range (1,n):
        integral += 2*f(a+i*h)
    return (integral + f(b))*h*0.5

def romberg (a,b,n,f):
    T=np.zeros((n,n))

    for i in range (n):
        T[i,0]= trapezoid(a,b,2**i,f)

    for k in range (1,n):
        for j in range (k,n):
            T[j, k] = (4**k * T[j, k-1] - T[j-1, k-1]) / (4**k - 1)

    return T

if __name__ == '__main__':
    def f(x):
        return x**2+1
    print("Input lower limit")
    a=int(input())
    print("Input upper limit")
    b=int(input())
    print("Input Table Rows")
    n=int(input())
    T=romberg(a,b,n,f)
    print(T,'\n')
    print("Result:")
    print(T[n-1,n-1])
