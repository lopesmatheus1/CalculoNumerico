from sympy import symbols, sin,ln,cos ,exp,sqrt
from sympy.plotting import plot


# Define a variável simbólica
x = symbols('x')

# Plota o gráfico da função

f_x = ln(2*x) - exp(-x**2)
p1 = plot(f_x, show=True)

#Define a função f(x)
def f(x): 
    y = ln(2*x) - exp(-x**2)
    return y

#Define o algoritimo da bisseção como função
def bissecao(a, b, E, max_iter):
    #Bolzano
    if f(a) * f(b) >= 0:
        print("Não há raiz neste intervalo.")
        return None
    #bisseção
    iteracao = 0
    while abs((b - a) / 2 )> E and iteracao < max_iter:
        xI = (a + b) / 2
        if f(xI) == 0:
            print("A raiz é:", xI)
            return xI
        else:
            if f(a) * f(xI) < 0:
                b = xI
            else:
                a = xI
        iteracao += 1

    if iteracao == max_iter:
        print("Número máximo de iterações atingido.")
        return None
    print("O numero de iteraçoes foi:",iteracao)
    print("A raiz é:", xI)
    return xI

print("Digite o intervalo inicial [a,b] e uma Tolerância(epsilon)")

a, b, E = float(input()), float(input()), float(input())
max_iter = 100


bissecao(a, b, E, max_iter)
