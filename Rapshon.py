from sympy import symbols, ln, exp, cos,sin
from sympy.plotting import plot

x = symbols('x')

# Plota o gráfico da função
f_x =  4*cos(3*x)
p1 = plot(f_x, show=True)

# Define a função f(x)
def f(x): 
    fx =  4*cos(3*x)
    return fx

# Define a função para calcular a derivada numericamente
def fLx(x):
    h = 0.000001
    derivada = ((f(x + h) - f(x)) / h)
    return derivada

# Implementação do Método de Newton-Raphson
def newtonRaphson(fx, fLx, x, iter_max, tol):
    i = 0
    while i <= iter_max:
        x = x - fx(x) / fLx(x)
        i += 1
        
        if abs(fx(x)) < tol:
            print("O numero de iteraçoes foi:",i)
            return x
    return 'O método falhou após', i, 'iterações'

# Chamar a função Newton-Raphson
resultado = newtonRaphson(f, fLx, 1.5 , 100, 1e-8)
print(resultado)
