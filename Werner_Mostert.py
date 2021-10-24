import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Get the sum of all the digits of the factorial.')
parser.add_argument('n', metavar = 'Number', help='Enter a number.')
def main(n):
    #n = 10                  # input number
    a = np.math.factorial(n)  # get the factorial using numpy
    print(a)
    sum_diget = 0             # set a sum variable
    
    """
    while the factorial of the number is positive:
    divide the factorial with ten and add the remainder
    then divide the factorial with 10.
    
    example:
    use n = 10
    factorial is 3628800
    factorial divided by ten will be 362880.0, with the rest being 0.
    Then sum the rest with the initial variable.
    
    sum will look something like 0 + 0 + 8 + 8 + 2 + 6 + 3 = 27
    
    This method allows you to sum the digits of the number from the back to the front.
    """
    while(a != 0):
        sum_diget = sum_diget + (np.mod(a ,10))
        a = a // 10
        
    print(sum_diget)
    
if __name__ == '__main__':
    args = parser.parse_args()
    n  = args.n 
    if (type(n) != 'int'):
        n = int(n)
    main(n)



#############################################################
#sollution using casting between string and int
"""
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Get the sum of all the digits of the factorial.')
parser.add_argument('n', metavar = 'Number', help='Enter a number.')
def main(n):
    
    #  Calculate the factorial using np.math.
    a = np.math.factorial(5)
    ans = str(a)    # Make the answer a string
    arr = []     
    
    #  Append the answer to arr as an integer.
    
    for i in ans:
        arr.append(int(i))
        
    arr = np.array(arr)     # make the python list a numpy array
    print(sum(arr))         # use the sum function to sum together the array
    
if __name__ == '__main__':
    args = parser.parse_args()
    n  = args.n    
    main(n)
"""
