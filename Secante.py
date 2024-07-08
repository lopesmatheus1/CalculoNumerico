from sympy import symbols, cos
from sympy.plotting import plot

x = symbols('x')

# Plota o gráfico da função
f_x = 4 * cos(3 * x)
p1 = plot(f_x, show=True)

# Define a função f(x)
def f(x):
    return 4 * cos(3 * x)

# Implementação do Método da Secante
def secante(f, x0, x1, iter_max, tol):
    for i in range(iter_max):
        # Calcula o próximo ponto usando a fórmula da secante
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 == f_x0:
            return "Divisão por zero detectada, o método falhou."
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Verifica a tolerância
        if abs(f(x2)) < tol:
            print("O número de iterações foi:", i+1)
            return x2
        
        # Atualiza os pontos para a próxima iteração
        x0 = x1
        x1 = x2
    
    return "O método falhou após", iter_max, "iterações"

# Chamar a função da Secante
resultado = secante(f, 0, 1, 100, 1e-8)
print(resultado)
