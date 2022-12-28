from movie import Movie

def read_movie_data(file):
	movieList=[]
	for line in file.readlines():
		thing=line.split(',')
		title=thing[0]
		release_year=thing[1]
		director=thing[2]
		for i in range(3,len(thing)):
			director+=', '
			director+=thing[i]
		movieThing=Movie(title,release_year,director)
		movieList.append(movieThing)
	return movieList



def main():
	file=open('movie_data.txt','r')
	reading=read_movie_data(file)
	file.close()
	running=True
	while running:
		userText=input('Input text to search movie titles: ')
		continuing=False
		for movie in reading:
			if userText ==movie.get_title():
				print(movie.__str__)
				continuing=True
		if not continuing:
			print('Movie not found')
		userResponse=input('Would you like to search another movie? ')
		if userResponse=='Y' or userResponse=='y':
			running=True
		else:
			print("Goodbye!")
			running=False
