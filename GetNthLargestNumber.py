import sys

def printNum():
#    print ("---------- find number in the list ----------")
    for num in array:
        print num

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
               array[i], array[i-1] = array[i-1], array[i]
            else:
                break
            i-=1
f.close()

array.pop()

printNum()



