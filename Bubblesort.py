aList = [5215,743,8987,3214,742,6589,214,864,215,868,6,97987,23,532,6346426462,65687,13,64898,8,38,232222,1335]
print(len(aList))
counter = 0
iterations = 0
def Bubblesort(mylist, startpoint):
    global counter
    global iterations
    #base recursive case
    if counter == len(mylist) - 1:
        iterations += 1
        return 
    
    #iterate once, bubblesorting
    for i in range( startpoint, len(mylist) - 1):
        counter+= 1
        
        if mylist[i] > mylist[i+1]:
            temp = mylist[i]
            mylist[i] = mylist[i+1]
            mylist[i+1] = temp
        #recursive call
        Bubblesort(aList, counter )
        
        #restart
        
        if iterations < len(mylist) - 1:
            counter = 0
            Bubblesort(mylist, counter)
        return    
    
Bubblesort(aList, 0)    
print(aList)
        
        