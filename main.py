#create a function that takes in default argurements of the values

import math
import numpy as np



def c(c_0 = 0.001645, h_1 = 24831, r = 8.314 , t = 325.75):
    c_value = c_0 * math.exp(h_1/(r*t))
    print(c_value)
    return c_value
    
    
    
def k(k_0 = 5.710, h_2 = -5118 , r = 8.314 , t = 325.75):
    k_value = k_0 * math.exp(h_2/(r*t))
    print(k_value)
    return k_value 

def equi_moist_cont(k_value , c_value , a_w = 'a_w', m_o = 0.06156, x_e =0.133):
    p1 = np.poly1d([0, -0.8628, 1])
    p2 = np.poly1d([0, -12.749, 1])
    p = p1*p2* x_e
    p3 = np.poly1d([0,0.8376,0])
    quadratic_equation = p - p3
    print(quadratic_equation)
    return quadratic_equation

if __name__ == '__main__':
    c()
    k()
    equi_moist_cont(c,k)