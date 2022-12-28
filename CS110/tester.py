from MadisonWozniak_book import Book 

userLibrary = []

def add_book(title, author):
	newBook = Book(title,author)
	userLibrary.append(newBook)
	print(f'{title} by: {author} added to your library! \n')

def print_library():
	for obj in userLibrary:
		print(obj)

def update_rating(title, new_rating):
	for obj in userLibrary:
		if title in obj.get_title(title):
			obj.set_rating(new_rating)

def main():
	keepGoing = True
	while keepGoing:
		print('Welcome to your library! Please select an option below:')
		print('a.	Add new book')
		print('b.	View your library')
		print('c.	Rate a newly read book \n')
		userChoice=input('Please enter a, b, or c: ')
		if userChoice in ['a','A']:
			bookTitleA = input('Enter book title: ')
			authorA = input('Enter author name: ')
			add_book(bookTitleA,authorA)
			keepGoing = True
		elif userChoice in ['b','B']:
			print_library()
			keepGoing = True
		elif userChoice in ['c','C']:
			bookTitleC = input('Enter the title of the book you want to rate: ')
			newRatingC = int(input('Enter rating (1-5): '))
			update_rating(bookTitleC,newRatingC)
			keepGoing=True
		else:
			print('Goodbye!')
			keepGoing = False



main()