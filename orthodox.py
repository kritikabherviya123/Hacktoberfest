#leetcode solution ---link: https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/167530/python-O(30N)
def subarry(list1):
    res_a = set()
    pre_a = set()
    for n in list1:
        cur_a = set([n])
        for p in pre_a:
            cur_a.add(p|n)
        pre_a = cur_a
        for p in pre_a:
            res_a.add(p)
    return len(res_a)
    
test=int(input())
for _ in range(test):
    n=int(input())
    list1=list(map(int,input().split()))
    final=(n*(n+1))/2
    if final!=subarry(list1):
        print("NO")
    else:
        print("YES")
