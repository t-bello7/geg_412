x = 0.5
# ni is number of iterations
n = 10

for i in range(n):
    print("Iteration ",(i+1))
    print("x",i+1," = ", x)
    i = i + 1
    x = x - ((0.133 + (0.743 * x) - (1.4629 * x * x)) / (0.743 -(2.9258 * x)))
