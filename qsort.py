def qsort(A,p,r):
    """
    :param A: array, list
    :param p: 시작점의 index
    :param r: 끝점의 index
    :return: None, just in the function, already sorted
    """
    if p<r:
        q = partition(A,p,r)
        qsort(A,p,q-1)
        qsort(A,q+1,r)

def partition(A,p,r):
    """
    :param A: array,list
    :param p: 시작점의 index
    :param r: 끝점의 index
    :return: 마지막 index의 실제 위치
    """
    q_val = A[r]
    i = p-1 # 이전구역의 끝지점
    for j in range(p,r-1):
        if A[j]<q_val: # q_val이 위치할 자리를 체크해서 놔둔 후,
            i+=1
            tmp_val = A[i]
            A[i] = A[j]
            A[j] =tmp_val

    #그 체크한 자리에 q_val을 넣고 대신 넣어둔 건 맨뒤로 보냄...
    _val = A[i+1]
    A[i+1] = A[r]
    A[r] = _val

    return i+1

if __name__ == '__main__':
    A = [31,8,48,73,11]
    qsort(A,0,4)
    print(A)


