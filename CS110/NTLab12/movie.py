class Movie:

    def __init__(self,title,release_year,director,ratings=[],average_rating=0):
        self.__title=str(title)
        self.__release_year=int(release_year)
        self.__director=str(director)
        self.__ratings=ratings
        self.__average_rating=float(average_rating)

    #create and initialize movie objects (private)

    def __str__(self):
        return (f'Title: {self.__title} Year: {self.__release_year} Director: {self.__release_year}')

    def add_rating(self,new_rating):
        self.__ratings.append(new_rating)
    # public method to append a rating to a list of ratings, doesn't return anything

    def calc_average_rating(self):
        for element in self.__ratings:
            element=int(element)
        self.__average_rating=(sum(self.__ratings))/len(self.__ratings)

        #calc avg rating and store it in 'average_rating attribute'
        #doesn't return anything

    def getRatings(self):
        return self.__ratings

    def getAverageRating(self):
        return self.__average_rating
        #returns average rating 

    def get_title(self):
        return self.__title
