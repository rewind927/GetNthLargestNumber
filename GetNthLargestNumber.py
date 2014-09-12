import sys

def printNum():
#    print ("---------- find number in the list ----------")
    for num in array:
        print num

def swap(array,x,y):
    tmp = array[x]
    array[x] = array[y]
    array[y] = tmp

number = raw_input("Input number: ")
if number.isdigit():
    number = int(number)
else:
    print("not digital number, break this loop!")
    quit()

array = [0]*(number+1)
#print "========== input data =========="
f = open(sys.argv[1], 'r')
for data in f:
    data = int(data.strip())
#    print data
    if data > array[number]:
        array[number] = data
        i = number
        while i > 0:
            if array[i] > array[i-1]:
               swap(array,i,i-1)
            else:
                break
            i-=1
f.close()

array.pop()

printNum()



