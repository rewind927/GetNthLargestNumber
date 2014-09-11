import sys

def printNum():
    print ("---------- find number in the list ----------")
    for num in array:
        print num

number = raw_input("Input number: ")
if number.isdigit():
    number = int(number)
else:
    print("not digital number, break this loop!")
    quit()

array = [0]
print "========== input data =========="
f = open(sys.argv[1], 'r')
for data in f:
    print data
    i = 0
    while i < len(array):
        if i < number and int(data) > int(array[i]):
            array.insert(i,data)
            if len(array) > number:
                array.pop()
            break
        i+=1
f.close()

printNum()



