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

array = [0]
#print "========== input data =========="
f = open(sys.argv[1], 'r')
for data in f:
    data = data.strip()
#    print data
    i = 0
    while i < len(array):
        if int(data) > int(array[i]):
            if i == 0:
                array = [data] + array[:number-1]
            elif i == number-1:
                array = array[:number-1]+[data]
            else :
                array = array[:i] + [data] + array[i:number-1]
            break
        i+=1
f.close()

printNum()



