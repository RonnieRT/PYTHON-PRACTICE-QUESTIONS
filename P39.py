# cook your dish here
t= int(input())
def max_sum_plus_count(arr):
     freq = {}
     for x in arr:
         freq[x] = freq.get(x, 0) + 1
     max_sum = float('-inf')
     for x in freq:
         curr_sum = x + freq[x]
         if curr_sum > max_sum:
             max_sum = curr_sum
     return max_sum
while(t!=0):
     n=int(input())
     arr= list(map(int ,input().split()))
     print(max_sum_plus_count(arr)-1)
     t=t-1
