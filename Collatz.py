counter = 0

def collatz(num):
    global counter

   
    if num < 1:
        return "Enter valid number"
    if num == 1:
        
        return 1
    
    if num%2 == 0:
        counter+= 1
        return collatz(num/2)
    else:
        counter+=1
        return collatz((num*3) + 1)
    
collatz(0)
print(counter)