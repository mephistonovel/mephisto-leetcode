import numpy as np
def merge(A,p,mid,r):
    t=0
    i=p
    j=mid+1
    tmp = list(np.zeros(p+r+1))
    while (i<=mid and j <= r):
        if (A[i]<A[j]):
            tmp[t] = A[i]
            t+=1
            i+=1
        else:
            tmp[t] = A[j]
            t+=1
            j+=1

    while (i<=mid):
        tmp[t]=A[i]
        t+=1
        i+=1

    while (j<=r):
        tmp[t] = A[j]
        t+=1
        j+=1

    t=0
    for x in range(p,r+1):
        A[x] = tmp[t]
        t+=1




def ms(A,p,r):

    if (p<r):
        mid = (p+r)//2
        ms(A,p,mid) #A[p]~A[mid]
        ms(A,mid+1,r) #A[mid+1]~A[r] 즉, p=0 to r = lne(A)-1 이면 A전체
        merge(A,p,mid,r)

if __name__ == '__main__':
    A = [4, 2, 3, 5]
    ms(A,0,3)
    print(A)