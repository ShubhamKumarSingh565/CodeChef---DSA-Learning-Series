"""
You're given a number N. If N is divisible by 5 or 11 but not both then print "ONE"(without quotes). 
If N is divisible by both 5 and 11 then print "BOTH"(without quotes). If N is not divisible by 5 or 11 then print "NONE"(without quotes).

Input:
First-line will contain the number N.
Output:
Print the answer in a newline.

Sample Input 1:
50
Sample Output 1:
ONE
Sample Input 2:
110
Sample Output 2:
BOTH
Sample Input 3:
16
Sample Output 3:
NONE

EXPLANATION:
In the first example, 50 is divisible by 5, but not 11.
In the second example, 110 is divisible by both 5 and 11.
In the third example, 16 is not divisible by 5 or 11.
"""


num  = int(input())
if (num%5==0 and num%11!=0) or (num%5!=0 and num%11==0):
  print("ONE")
elif num%5==0 and num%11==0:
  print("BOTH")
elif num%5!=0 or num%11!=0:
  print("NONE")
else:
  pass
