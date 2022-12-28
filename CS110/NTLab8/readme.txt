Madison Wozniak

SOURCES:
instructions page

This program creates a madlibs game that uses different lists for different categories, and chooses random elements from each of those categories to be inserted into the sentence provided.

I first import the random module so I can usea random function in my main() function when selecting a random element from each of my lists to be put into the madlib. I then created my print_story() function that took each of the categories as parameters. The function of print_story() is to include where each argument would go in the sentences and print the strings. Next, I created a main function that first defined each unique category into lists containing at least 10 string elements. Then, the function calls the print_story() function that randomizes each individual argument. Next the program asks the user if they would like to see another randomized version of the madlib by entering letters than indicate either yes or no. Based on two lists created that separate the yes from no answers, the program will determine whether to show another version of the madlib or exit the program with an if/elif/else statement. 