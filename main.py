#create a function that takes in default argurements of the values

import math
import numpy as np



def c(c_0 = 0.001645, h_1 = 24831, r = 8.314 , t = 325.75):
    c = c_0 * math.exp(h_1/(r*t))
    print(c)
    return c
    
    
    
def k(k_0 = 5.710, h_2 = -5118 , r = 8.314 , t = 325.75):
    k = k_0 * math.exp(h_2/(r*t))
    print(k)
    return k 

def equi_moist_cont(k , c , a_w = 'a_w', m_o = 0.06156):
    p1 = np.ploy1d([])

c()
k()
equi_moist_cont(k,c)