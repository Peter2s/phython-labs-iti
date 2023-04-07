array =[]
for i in range(5):
    array_element = input(f"enter your element number {i} : ")
    array.append(int(array_element))
array.sort()
print("array ascending")
print(array)
print("array descending")
array.sort(reverse=True)
print(array)
    