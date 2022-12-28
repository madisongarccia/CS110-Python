# Your Name
# Section B
# Problem 2: Personal Library


# Update yourname_book to the name of your class file's name!!
from yourname_book import Book 

def add_book(title, author):
	# Create new Book object by calling the Book class's constructor
	# Add new Book object to user's library (list)
	# Print example: “Tales of the City by: Armistead Maupin added to your library!"

def print_library():
	# Prints each Book object in the user’s library (list) by calling the Book class’s string method.

def update_rating(title, new_rating):
	# Takes a title (string) and new_rating (integer) as parameters
	# Uses them to update a Book object’s private rating attribute using the Book class’s set_rating() mutator method.


def main():
	# Prints menu out to user
	# If the user chooses ‘a’, ask the user to enter a book title and author (strings) and calls the add_book() function to add the book to the library. 
	# If the user chooses ‘b’, print the user’s library by calling the print_library() function. 
	# If the user chooses ‘c’, ask the user to enter a book title (string) and a new rating (integer) and calls the update_rating() function to update the book’s rating. 
	# If the user enters anything else, print “Goodbye!” and exit the program.


	# print('Welcome to your library! Please select an option below:')
	# print('a. Add new book')
	# print('b. View your library')
	# print('c. Rate a newly read book')

	# input('Please enter a, b, or c: ')

	
	# input('Enter book title: ')
	# input('Enter author name: ')

	# input('Enter the title of the book you want to rate: ')
	# input('Enter rating (1-5): ')
	
	# print('Goodbye!')



main()