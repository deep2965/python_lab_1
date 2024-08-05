def selection_sort(array):

    for i in range(0,len(array)-1):
        minindex=i
        for j in range(i+1,len(array)):
            if array[j]<array[minindex]:
                minindex=j
        array[i],array[minindex] = array[minindex],array[i]

array=[22,13,4,8,17,26,53,4]
print("before sorting:",array)
selection_sort(array)
print("after selection sort:",array) 