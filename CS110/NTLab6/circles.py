import math

def circumference(r):
    C=2*math.pi*r
    return C

def area(r):
    A=math.pi*(r**2)
    return A

def main():
    radius=float(input ("Input the radius of the circle : "))
    if radius==0:
        print("Goodbye!")
    elif radius<0:
        print('Invalid radius!')
        radius=float(input ("Input the radius of the circle : "))
    else:
        circumference(radius)
        area(radius)
        print(f'A circle of radius {radius} has a circumference {circumference(radius)} and area {area(radius)}')
        radius=float(input ("Input the radius of the circle : "))
main()
