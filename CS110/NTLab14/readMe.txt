Madison Wozniak

Sources:
Instructions page

This program tests the efficiency of three different sorting methods by creating three random lists, and recording the time it takes for selection sort, insertion sort, and bubble sort to put them all in order.

The functions for sorting the data were predefined, so I worked on the main() function. To created each random list, the length had to be the same length as maxvalue so it had to be in range 0-maxvalue, and for each value, I would generate a random integer using the random module's function random.randrange() between 1 and maxvalue. Then I recorded each start and stop time by assigning the time module function call to startTime and endTime. To calculate the total elapsed time I subtracted start time from end time and printed that time. 