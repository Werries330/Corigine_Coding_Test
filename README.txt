Two solutions to the problem were found. The first solution involved casting the factorial from an integer to a string and summing the value each string index together. 
The second solution used division and the modular operation to achieve the correct answer. The latter solution is explained in a bit more detail in the rest of the text.

while the factorial of the number is positive:
	devide the factorial with 10 and add the remainder to the sum.
	then devide the factorial with 10 and round down.
    
example:
use n = 10
factorial is 3628800
factorial devided by 10 will be 362880.0 with the rest being 0.
Then sum the rest with the initial variable.
    
sum will look something like 0 + 0 + 8 + 8 + 2 + 6 + 3 = 27
  
This method allows you to sum the digets of the number from the back to the front.

#################################################################################

https://github.com/Werries330/Corigine_Coding_Test