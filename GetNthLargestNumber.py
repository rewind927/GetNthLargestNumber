import sys

def printNum(array):
#    print ("---------- find number in the list ----------")
    for num in array:
        print num

def getNthLargestNumber(getNthNumber,file):
    array = [None]*(getNthNumber+1)
#    print "========== input data =========="
    for data in file:
        data = int(data.strip())
#        print data
        if data > array[getNthNumber]:
            array[getNthNumber] = data
            i = getNthNumber
            while i > 0:
                if array[i] > array[i-1]:
                    array[i], array[i-1] = array[i-1], array[i]
                else:
                    break
                i-=1
    array.pop()
    return array   


if __name__ == "__main__":
    number = raw_input("Input number: ")
    if number.isdigit():
        number = int(number)
    else:
        print("not digital number, break this loop!")
        quit()
    f = open(sys.argv[1], 'r')

    printNum(getNthLargestNumber(number,f))
    f.close()


