def run(t):    
    n,k,s = map(int,input().split(' '))
    
    res = min(k+n, (k-1)+(k-s)+(n-s)+1)
    
    print ('Case #{}: {}'.format(t, res))

t = int(input())
for  i in range(1,t+1):
    run(i)

    

