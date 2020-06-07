'''
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.​
The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, 
you are the last one remaining and survive.

Example:
Input:
2
3 2
5 3
Output:
3
4

Explanation:
Testcase 1: There are 3 persons so skipping 1 person i.e 1st person 2nd person will be killed. Thus the safe position is 3.
'''

def josephus(n,k):
    #Your code here
    if n==1:
        return 1
    
    return (josephus(n-1, k)+k-1)%n+1

def main():

        
	nk=[int(x) for x in input().strip().split()]
	n=nk[0]
	k=nk[1]
	
	print(josephus(n,k))


if __name__=="__main__":
    main()