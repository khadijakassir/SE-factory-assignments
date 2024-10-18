import math
N_values = []
input = input("Give me your integers (separate them by space): ")
N_values = [int(x) for x in input.split()]  #took help from google 

def big_o(expression, N): # expression is the mathmatical expression 
    return expression(N)
def a(N):
    return (1/6) * N + 8000 * N**3 + 24
def b(N):
    return (1/6) * N**3
def c(N):
    return (1/6) * math.factorial(N) + 200 * N**4
def d(N):
    return N * math.log(N) + 1000
def e(N):
    return math.log(N) + N
def f(N):
    return (1/2) * N * (N - 1)
def g(N):
    return N**2 + 220 * N * math.log(N**2) + 3 * N + 9000
def h (N):
    return math.factorial(N) + 3 * N + 2 * N + N**3 + N**2

expressions =[a,b,c,d,e,f,g,h]
for   element in expressions: 
    print(f"Growth for {element}:")
    for N in N_values:
        print(f"  N={N}: {big_o(element, N)}")
    print()
