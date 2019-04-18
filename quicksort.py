
#a  = [1,5,8,3,5,2,2,1,5,17]


def quicksort(a):
    if len(a) <= 1:
       return a
    else:
        pivot = a[0]
        min = [i for i in a[1:] if i < pivot]
        max = [i for i in a[1:] if i >= pivot]
    return quicksort(min) + [pivot] + quicksort(max)
