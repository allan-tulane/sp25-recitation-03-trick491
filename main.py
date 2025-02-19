"""
CMPS 2200  Recitation 3.
See recitation-03.md  for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    ### TODO
    x_vector, y_vector = x.binary_vec, y.binary_vec
    x_vector, y_vector = pad(x.binary_vec, y.binary_vec)

    if x.decimal_val <=1 or y.decimal_val <=1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    x_left, x_right = split_number(x_vector)
    y_left, y_right = split_number(y_vector)

    a= _quadratic_multiply(x_left, y_left)
    b= _quadratic_multiply(x_right, y_right)
    c= _quadratic_multiply(BinaryNumber(x_left.decimal_val + x_right.decimal_val), BinaryNumber(y_left.decimal_val + y_right.decimal_val))

    n= len(x_vector)
    partial_result_a= bit_shift(a, n).decimal_val
    partial_result_b= bit_shift(BinaryNumber(c.decimal_val - a.decimal_val - b.decimal_val), n//2).decimal_val
    partial_result_c= b.decimal_val
    result = BinaryNumber(partial_result_a + partial_result_b + partial_result_c)
    return result
    pass
    ###


    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000
