start = input("please enter start number : ")
length = input("please enter length of array : ")
integer_list = range(int(start), int(length) + int(start),1)
for element in integer_list:
    print(element)
