from numpy import matrix, linalg

def gcd(a,b):
    a,b = (a,b) if a>b else (b,a)
    rem = a%b
    return gcd(b, rem) if rem != 0 else b

def pulverizer(a,b):
    x,y = (a,b) if a>b else (b,a)
    q = x//y
    rem = x%y
    print (rem,q)
    return pulverizer(y, rem) if rem != 0 else y

def bezout(a,b):
    """Finding Bezout's Identity by Extended Euclid's method"""
    px,py = (a,b)
    a,b = (a,b) if a>b else (b,a)
    x,y = a,b
    q = a//b
    rem = a%b
    s = t = 0
    s_2, s_1 = [1, 0]
    t_2, t_1 = [0, 1]
    
    while rem != 0:
        #print (rem,q)
        q, rem = a//b, a%b
        a,b = (b,rem)
        s = s_2 - q*s_1
        t = t_2 - q*t_1
        s_2, s_1 = s_1, s
        t_2, t_1 = t_1, t
    assert abs(a*s) == abs(y)
    assert abs(a*t) == abs(x)
    s_2, t_2 = (s_2, t_2) if px>py else (t_2, s_2)
    assert (s_2*px + t_2*py) == a
    #print a, b
    #print s, t
    #print (a*s), (a*t)
    #print x,y
    #print px,py
    return a, s_2, t_2

def multiplicative_inverse(a,n):
    t = 0
    newt = 1
    r = n
    newr = a    
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)
    if r > 1: return "a is not invertible"
    if t < 0: t = t + n
    return t


#REWORK - FIX CONCEPT!
def pulverizer_bezout_matrix(a,b):
    """Pulverizing to find Bezout's Identity by Matrix Method"""
    mat_list = []
    a,b = (a,b) if a>b else (b,a)
    x,y = a,b
    q = a//b
    rem = a%b
    
    while rem != 0:
        #return pulverizer(y, rem) if rem != 0 else y
        #print (rem,q)
        mat_list.append(matrix([[q, 1], [1,0]]))
        a,b = (b,rem) if b>rem else (rem,b)
        q, rem = a//b, a%b
    
    #print a, b, rem  #b - previous remainder - r[N-1] or r0 when rem == 0
    mat_list.append(matrix([[q, 1], [1,0]]))
    rem_mat = matrix([[b],[rem]])
    m = reduce(lambda m1,m2: (m1*m2), mat_list)
    #print mat_list
    #print rem_mat
    #print m * rem_mat
    mInv = linalg.inv(m)
    #print mInv
    #print  mInv * matrix([[x],[y]])
    assert all([i for i in (mInv * matrix([[x],[y]]) == rem_mat)])
    #print mInv[0,0], mInv[0,1]
    assert long(mInv[0,0]*x + mInv[0,1]*y) == b
    return (mInv[0,0], mInv[0,1], mInv[0,0]*x + mInv[0,1]*y, b)

def euler_tot(n):
    """Euler's Totient Function"""
    return len([i for i in range(1, n) if gcd(n, i)==1])