
#the following sorting method is an implementation of quick sort
def mySort(list):
    return mySorthelper(list, 0, len(list)-1)



def mySorthelper(list, start, end):
    if(start < end):
        pivot = partition(list, start, end)
        mySorthelper(list, start, pivot-1)
        mySorthelper(list, pivot+1, end)

    return list

def partition(list, start, end):
    pivot = list[end]
    i = (start-1)
   

    for j in range(start, end):
        if(list[j]<pivot):
            i = i+1
            list[i], list[j] = list[j], list[i]


    list[i+1], list[end] = list[end], list[i+1]

    return (i+1)   






print(mySort([3,1,2]))
    