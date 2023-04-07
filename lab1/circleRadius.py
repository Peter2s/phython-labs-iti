radius = float(input("please enter circle radius : "))
if radius > 0 :
    PI = 3.14159
    circumference = 2 * PI * radius
    area = PI * radius * radius

    print(f"Circumference Of a Circle =  {circumference}")
    print(f" Area Of a Circle =  {area}")
else:
    print("invalid input")