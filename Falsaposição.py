from sympy import symbols, cos
from sympy.plotting import plot

x = symbols('x')

# Plota o gráfico da função
f_x = 4 * cos(3 * x)
p1 = plot(f_x, show=True)

# Define a função f(x)
def f(x):
    return 4 * cos(3 * x)

# Implementação do Método da Falsa Posição
def falsaPosicao(f, a, b, iter_max, tol):
    if f(a) * f(b) >= 0:
        return "O método da falsa posição falhou: f(a) e f(b) devem ter sinais opostos."
    
    for i in range(iter_max):
        # Calcula a posição da falsa posição
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < tol:
            print("O número de iterações foi:", i+1)
            return c
        
        # Atualiza os valores de a e b
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return "O método falhou após", iter_max, "iterações"

# Chamar a função da Falsa Posição
resultado = falsaPosicao(f, 0, 1, 100, 1e-8)
print(resultado)
