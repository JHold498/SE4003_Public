# User input program to calculate the area of a right triangle
print('Welcome to the Right Triangle Area calculator!\n')
#Enter Base
B = float(input('Enter the base of the triangle: '))
#Enter Height
H = float(input('Enter the height of the triangle: '))
#Calculate Area
area = float(B*H*(0.5))
#Return Result
print('The area of the triangle is: %0.2f' %area)