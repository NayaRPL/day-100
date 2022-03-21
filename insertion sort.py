from turtle import position


def insertionsort (alist):
    for i in range (1,len(alist)):
        currentvalue = alist[i]
        position=i
        while position > 0 and alist [position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -=1
        alist[position]=currentvalue
data=[1,2,3,4,8,9,5,6,7]
print(data)