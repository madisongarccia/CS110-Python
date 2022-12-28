Madison Wozniak

SOURCES:
Lab instructions

The purpose of this program is to accept a radius value from the user and output the circle's circumference and area with that information. After calculating, it will ask for a new radius value to be given.

It first imports math so the program can use an accurate value for pi in its calculations. Then if defines two functions: circumference(r) and area(r) that calculate the circumference and area of a circle when given a value for the radius. Next, the main function calls the user to input a radius value, and checks if it is a valid length. If it equals 0, the program tells the user Goodbye and ends, if negative, it tells the user the value is invalid and asks again for a radius. Finally, if the radius is a valid amount, it calls the area() and circumference() functions with argument 'radius' to return their calculations in a sentence that tells the user: 'A circle of radius {radius} has a circumference {circumference(radius)} and area {area(radius)}'. 