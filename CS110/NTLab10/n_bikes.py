def main():
	with open("n_bikes-1.txt","r") as myFile:
		families=len(myFile.readlines())
		individual_ints = [ int(num) for num in myFile.split() ]
		totalBikes=sum(individual_ints)
		avgBikes=totalBikes/families
		minNum=min(individual_ints)
		maxNum=max(individual_ints)
		print('Number of families:', families)
		print('Total number of bikes:', totalBikes)
		print('Average number of bikes per family:', avgBikes)
		print('Maximum number of bikes in a family:', maxNum)
		print('Minimum number of bikes in a family:', minNum)
		
main()