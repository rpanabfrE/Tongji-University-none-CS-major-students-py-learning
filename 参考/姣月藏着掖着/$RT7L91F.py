import math
a=99
x0=2
x1=2/3*x0+a/(3*x0**2)
while math.fabs(x1-x0)>1E-5 :
    x0=x1
    x1=2/3*x0+a/(3*x0**2)
print(x1)
