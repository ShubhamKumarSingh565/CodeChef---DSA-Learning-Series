# Problem Code: BUYPLSE

"""
Chef went to a shop and buys a pens and b pencils. Each pen costs x units and each pencil costs y units. 
Now find what is the total amount Chef will spend to buy a pens and b pencils.

Input:
First-line will contain 4 space separated integers a, b, x and y respectively.
Output:
Print the answer in a new line.

Sample Input 1:
2 4 4 5
Sample Output 1:
28
Sample Input 2:
1 1 4 8
Sample Output 2:
12

EXPLANATION:
In the first example, total cost is (2 * 4 + 4 * 5) = 28.
In the second example, total cost is (1 * 4 + 1 * 8) = 12.

"""

a, b, x, y = input().split()
result = int(a)*int(x) + int(b)*int(y)
print(result)