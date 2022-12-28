MADISON WOZNIAK

SOURCES
Instructions page

This program contains five recursive functions that find factorials, sums a number, sums a list, multiplies two numbers, and reverses a list all using recursion. 

the factorial function takes a value n and returns zero if n=1,0 and returns n*n-1 until n reaches 0. sum_recursively returns 0 if n=0 but similarly to the factorial function, adds n to the function of n-1 until it reaches n=0. sumlist_recursively takes a list as a parameter and if the length of the list is 1, the function returns the values at index zero. If greater, the function is called and adds index value 0 to each element from index 1 to the end of the list. multiply_recursively takes two values are parameters, and multiplies x y times using addition, by estalishing a base case when y=1 that returns the value of x, then counts down the amount of times y occurs and adds x to itself that many times. Finally reverse_recursively reverses the positions of each item in a list. I assumed the list wouldn't be sorted, so the base case finds the length of the list when it is 0 and returns an empty list, then adds to that list in the next position, the last position l[-1] into that place. 