x1 = 0
x2 = 1

#xr is approx root
xr = (x1 + x2)/2

# ni is number of iterations
n = 10

for i in range(n):

    # A1 is f(x1)
    A1 = 0.133 + (0.743 * x1) - (1.4629 * x1 * x1)
    # A2 is f(x2)
    A2 = 0.133 + (0.743 * x2) - (1.4629 * x2 * x2)
    # Ar is f(xr)
    Ar = 0.133 + (0.743 * xr) - (1.4629 * xr * xr)

    print("Iteration ",(i+1))
    i = i + 1

    print("x1 = ", x1, ",     x2 = ", x2, "xr = ", xr, "     f(xr) = ",Ar)
    
    if(Ar < 0):
        x2 = xr
        xr = (x1 + x2)/2
        

    elif(Ar > 0):
        x1 = xr
        xr = (x1 + x2)/2
