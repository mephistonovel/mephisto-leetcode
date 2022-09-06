#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        #head가 원소가 여러개 일때, insertion sort에서 각 단계마다
        #생성되는 list에 대해 새 원소를 추가할 때 필요한 함수 define
def insert(ssl,val):
    if ssl.val < val:
        if ssl.next is None:
            ssl.next = ListNode(val=val,next=None)
        else:
            org_val = ssl.val
            output = insert(ssl.next,val)
            ssl = ListNode(val = org_val,next = output)
    else:
        ssl = ListNode(val=val, next = ssl)

    return ssl

def is_sort(head):
    """
    :param head:Listnode
    :return: Listnode
    """
    if head.next is None:
        return head

    output = ListNode(head.val,next=None)
    init = head

    while init.next is not None:
        output = insert(output,init.next.val)
        init = init.next

    return output



if __name__ == '__main__':
    test = ListNode(val=4,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=1,next=None))))
    output = is_sort(test)
    for i in range(4):
        print(output.val)
        output=output.next