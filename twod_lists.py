a = [[1,2,3],
     [4,5,6]]
##one way to traverse a 2d list
#b = a[0]
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        print(a[i][j],end=' ')
#    print()

##Another way is
def print_2dlist(tsil):
    for row in a:
        for element in row:
            print(element,end= ' ')
        print()
    
#add all elements

#sum = 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum += a[i][j]
#print(sum)
#sum = 0
#for row in a:
#    for element in row:
#        sum += element
#print(sum)

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] += 1

#Creating 2d list
#Doesnt WORK
#x = [[0] * 5]*8
#x[0][0] = 100
        
To Make an m * n list
x = [[0]*5 for i in range(8)]
x[0][0] = 100
print(x)


        