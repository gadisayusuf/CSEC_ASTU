n=int(input())
nums=list(map(int,input().split()))
ans=[0]*n
ans[0]=nums[0]
max_ans=ans[0]
for i in range(1,n):
    ans[i]=nums[i]+max_ans
    max_ans=max(max_ans,ans[i])
print(*ans)