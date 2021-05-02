import sympy as sym
from main import equi_moist_cont, c , k
c()
k()
a  = equi_moist_cont(c,k)
x = 2
x_next = []
# ni is number of iterations
n = 10

for i in range(3):
    for j in range(3):
        print("Iteration ",(j+1))
        x = (0.743 / 1.463) + (1/(11 * x))
        x_next.append(x)
        print("x",j+1," = ", x)
        j = j + 1
    numerator = x_next[1] - x_next[0]
    denumminator = x_next[0] - (2 * x_next[1]) + x_next[2]
    D = x_next[0] - ((numerator * numerator)/(denumminator))
    x = D
    print("The Accelerated root is ",D)
    print("")
    print("")
    
    
