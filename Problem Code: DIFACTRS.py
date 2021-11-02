# Problem Code: DIFACTRS

"""
You are given a number N and find all the distinct factors of N.

Input:
First-line will contain the number N.
Output:
In the first line print number of distinct factors of N.
In the second line print all distinct factors in ascending order separated by space.

Constraints
1≤N≤106

Sample Input 1:
4
Sample Output 1:
3
1 2 4
Sample Input 2:
6
Sample Output 2:
4
1 2 3 6

EXPLANATION:
In the first example, all factors of 4 are 1, 2, 4.
In the second example, all factors of 6 are 1, 2, 3, 6.
"""

num=int(input())
list1=[]
for i in range(1,num+1):
    if num%i==0:
        list1.append(i)
print(len(list1))
print(*list1)
