import random

def print_story(personName,place,adj,plNoun,plNoun2,place2,actionVerb,food,actionVerb2,noun,adj2):
	print(f'Last year, we went for a vacation with {personName} on a trip to {place}. The weather there is very {adj}! Western {place} has many {plNoun}, and they make {plNoun2} there.')
	print(f'Many people there also go to the {place2} to {actionVerb}. The people who live there like to eat {food}. They also like to {actionVerb} in the desert and swim in the {noun}.')
	print(f'It was a really {adj2} vacation!')

def main():
	personName=['Madison','Skyler','Jake','Stephanie','Lia','Bob','Hana','Katie','Julia','Mark','Sara']
	place=['home','school','Russia','Uzbekistan','Kurdistan',"Istanbul",'ice cream shop','Barnes&Noble','Disneyland','Dollywood']
	adjective=['Charming','Cruel','Fantastic','Gentle','Huge','Perfect','Rough','Sharp','Tasty','Zealous']
	pluralNoun=['plants', 'cats', 'beaches', 'fungi', 'feet','women','men','children','teeth','books']
	morePlaces=['Machu Picchu','The Maldives','Africa','Taj Mahal','Paris','Amazon Rainforest',' Santorini','Bali','French Polynesia','The Pyramids of Giza','Home Depot']
	actionVerb=['Play','Jump','Eat','Work','Study','Drive','Walk','Write','Read','Talk']
	food=['burger','ice cream','hot sauce','philly cheesesteak','fries','bacon','corndog','NY steak','caviar','tacos','tamale']
	noun=['people','history','art','helicopter','juice','kangaroo','kitchen','hydrogen','island','jelly','motorcycle']
	print_story(random.choice(personName),random.choice(place),random.choice(adjective),random.choice(pluralNoun),random.choice(pluralNoun),random.choice(morePlaces),random.choice(actionVerb),random.choice(food),random.choice(actionVerb),random.choice(noun),random.choice(adjective))
	userResponse=input("Please answer 'y','Y','yes','Yes','YES' or 'n','N','no','No','NO'." )
	responsesPositive=['y','Y','yes','Yes',"YES"]
	responsesNeg=['n','N','no','No','NO']
	if userResponse in responsesPositive:
		print_story(random.choice(personName),random.choice(place),random.choice(adjective),random.choice(pluralNoun),random.choice(pluralNoun),random.choice(morePlaces),random.choice(actionVerb),random.choice(food),random.choice(actionVerb),random.choice(noun),random.choice(adjective))
	elif userResponse in responsesNeg:
		exit()
	else:
		print('invalid try again')


main()