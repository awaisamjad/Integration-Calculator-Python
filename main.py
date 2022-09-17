import math

N = int(input("Enter number of rectangles (5000 recommended): "))
a = float(input("lower integral bound: "))
b = float(input("higher integral bound: "))
def Integrate (N, a, b):
    #FUNCTION
    def f(x):
        f= math.sin(x)
        return f
    
    value=0  
    TotalArea=0 
    for n in range(1, N+1): 
        x_bar = a+(2*n-1)*(b-a)/(2*N)
        value = value + f(x_bar) 
    TotalArea= round(((b-a)/N)*value, 4)
    return TotalArea  
print(Integrate(N,a,b))