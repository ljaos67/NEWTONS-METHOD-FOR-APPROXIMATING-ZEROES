#!/usr/bin/env python
# coding: utf-8

# Math 435
# Leo Jaos
# 02/24/2022
# Assign 2.3

# 6). Use Newton’s method to find solutions accurate to within 10−5 for the following problems.
# <br> a. ex + 2−x + 2 cos x − 6 = 0 for 1 # x # 2

# In[7]:


import math

def func(x):
    return math.exp(x) + 2**(-x) + 2*math.cos(x) - 6
def dFunc(x):
    return math.exp(x) - ((math.log(2))/(2**x)) -2*math.sin(x)

print("function f(x): e^x + 2 - x + 2*math.cos(x)\n")
x = 1
chk = True
Tol = 10**-5
cnt = 1;
while(chk):
    x0 = x
    x = x0 - (func(x0))/(dFunc(x0))
    if(abs(x - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1


# 8). Repeat Exercise 6 using the Secant method.

# In[19]:


def func(x):
    return math.exp(x) + 2**(-x) + 2*math.cos(x) - 6
def dFunc(x):
    return math.exp(x) - ((math.log(2))/(2**x)) -2*math.sin(x)

print("function f(x): e^x + 2^-x + 2*math.cos(x) - 6\n")
x = 1
chk = True
Tol = 10**-5
cnt = 1;
x0 = 1;
x1 = 2;
xPrev = func(x0)
xCurr = func(x1)
while(chk):
    x = x1 - (xCurr * (x1 - x0))/(xCurr - xPrev)
    x0 = x1
    xPrev = func(x0)
    x1 = x
    xCurr = func(x1)
    if(abs(x1 - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1


# 15). The following describes Newton’s method graphically: Suppose that f $(x) exists on [a, b] and that
# f $(x) %= 0 on [a, b]. Further, suppose there exists one p & [a, b] such that f ( p) = 0, and let p0 & [a, b] be arbitrary. Let p1 be the point at which the tangent line to f at ( p0, f ( p0)) crosses the x-axis. For
# each n ' 1, let pn be the x-intercept of the line tangent to f at ( pn−1, f ( pn−1)). Derive the formula
# describing this method.

# Equation for line: y = mx + b
# 
# Finding the equation of the line tangent to f at (p0, f(p0))
# 
# m = f'(po)
# 
# f(p0) = (f'(p0) * p0) + b
# 
# So b = f(p0) - (f'(p0) * p0)
# 
# So equation for line becomes
# 
# y(x) = (f'(po) * x) + f(p0) - (f'(p0) * p0)
# 
# p1 is the intersection point, solve for p1:
# 
# (p1,0), y(p1) = 0
# 
# 0 = y(p1) = (f'(po) * p1) + f(p0) - (f'(p0) * p0)
# 
# p1 = p0 - (f(p0))/(f'(p0))
# 
# and for each n + 1, replace p0 with pn-1, p1 with pn
# 
# m = f'(pn-1)
# 
# f(pn-1) = (f'(pn1-1) * pn-1) + b
# 
# So b = f(pn-1) - (f'(pn-1) * pn-1)
# 
# So equation for line becomes
# 
# y(x) = (f'(pn-1) * x) + f(pn-1) - (f'(pn-1) * pn-1)
# 
# pn is the intersection point, solve for pn:
# 
# (pn,0), y(p1) = 0
# 
# 0 = y(pn) = (f'(n-1) * pn) + f(pn-1) - (f'(pn-1) * pn-1)
# 
# p1 = pn-1 - (f(pn-1))/(f'(pn-1))
# 

# 16). Use Newton’s method to solve the equation
# 0 = 1/2 + 1/4 * x^2 -xsinx -1/2cos2x
# 
# with p0 = pi/2
# 
# Iterate using Newton’s method until an accuracy of 10−5 is obtained. Explain why the result seems unusual for Newton’s method. Also, solve the equation with p0 = 5pi and p0 = 10pi.

# In[30]:


def func(x):
    return (1/2 + (1/4)*(x**2) - x*math.sin(x) - (1/2)*math.cos(2*x))
def dFunc(x):
    return math.sin(2*x) - math.sin(x) - x*math.cos(x) + x/2

print("function f(x): 1/2 + (1/4)(x**2) - x*sin(x) - (1/2)*cos(2*x)\n")
print("po = pi/2")
x = math.pi/2
chk = True
Tol = 10**-5
cnt = 1;
while(chk):
    x0 = x
    x = x0 - (func(x0))/(dFunc(x0))
    if(abs(x - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1
print("po = 5pi")
x = math.pi*5
chk = True
Tol = 10**-5
cnt = 1;
while(chk):
    x0 = x
    x = x0 - (func(x0))/(dFunc(x0))
    if(abs(x - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1
print("po = 10pi")
x = math.pi*10
chk = True
Tol = 10**-5
cnt = 1;
while(chk):
    x0 = x
    x = x0 - (func(x0))/(dFunc(x0))
    if(abs(x - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1
    if(cnt > 50):
        chk = False;
        print("\tPassed max interations")


# Newton's method typically converges very quickly, so having 10+ iterations is unusual. This is because derivative tends to zero as x approaches the root.
# 
# ![Screenshot%20%28993%29.png](attachment:Screenshot%20%28993%29.png)

# 18. The function f (x) = tan pix − 6 has a zero at (1/pi) arctan 6 ( 0.447431543. Let p0 = 0 and p1 = 0.48, and use ten iterations of each of the following methods to approximate this root. Which method is most successful and why?
# 
# a. Bisection method
# 
# c. Secant method

# In[38]:


# Function definition
def funct(x):
    return math.tan(math.pi*x) - 6
# Checks if zero exists, intermediate value THM
def IVT(b1, b2):
    if funct(b1)*funct(b2) > 0:
        return False
    else:
        return True
# This function returns the amount of bisection iterations
# it takes to find a zero with an accuracy of 1/x
def fCount(b1,b2,x):
    return (math.floor((math.log(x*(b2 - b1))/(math.log(2)))) + 1)
def bMethod(b1,b2,count):
    # If Zero exists
    if IVT(b1, b2):
        num = fCount(b1,b2,100000)
        while count < num:

            p = (b1 + b2)/(2)

            if funct(b1)*funct(p) < 0 :
                # Then there is a root in [b1,p]
                b2 = p;
                count+=1

            elif funct(b1)*funct(p) == 0 :
             # p is a root
                count += 1

            else:
                # funct("b1")*funct("p") > 0 
                # Then there is a root in [p,b]
                count +=1
                b1 = p
        print("\tZero is %1.5f after %d iterations" % (p, num))
        print("\tAnd so, the lower bound for the number of iterations is: %d" % num)
    else:
        print("No zero in interval [%d,%d]" % (b1,b2))
# a
print("Bisection for f(x) = tan(pi*x) -6 where for 0 ≤ x ≤ .48")
bMethod(0,.48,0)
#c

def func2(x):
    return math.tan(math.pi*x) -6


print("\n\nsectant method: function f(x): tan(pi*x) -6\n")
chk = True
Tol = 10**-5
cnt = 1;
x0 = 0;
x1 = .48;
xPrev = func2(x0)
xCurr = func2(x1)
while(chk):
    x = x1 - (xCurr * (x1 - x0))/(xCurr - xPrev)
    x0 = x1
    xPrev = func2(x0)
    x1 = x
    xCurr = func2(x1)
    if(abs(x1 - x0) <= Tol*(1 + abs(x0))):
        chk = False
    print("\tapproximation %d: %2.8f" % (cnt,x))
    cnt+=1
    if(cnt == 20):
        print("Failed to find root in 20 iterations, method failed")
        chk = False


# The bisection method is better because it provides a root in 16 iterations where the secant method has yet to discover a root at 20 iterations.

# 19).The iteration equation for the Secant method can be written in the simpler form
# pn = (f(pn−1)pn−2 − f(pn−2)pn−1)/(f(pn−1) − f(pn−2)).
# 
# Explain why, in general, this iteration equation is likely to be less accurate than the one given in Algorithm 2.4.

# Cancellation error - subtracting numbers that are almost equal
# 
# This can occur for when pn-1 is close in value to pn-2, which affects the calculation in the numerator and denominator. 

# In[ ]:




