# Madison Wozniak
# Section B
# Problem 2: Binary Game
import random

def generate_binary():
	binary_number=""
	while len(binary_number)<6:
		for char in binary_number:
			char=str(random.randint(0,1))
			binary_number=binary_number+char
	return binary_number

def check_answer(binary_number, decimal_number):
	value=0

	if binary_number[0]=='1':
		value=16
	else:
		value=value
	if binary_number[1]=='1':
		value=value+8
	else:
		value=value
	if binary_number[2]=='1':
		value=value+4
	else:
		value=value
	if binary_number[3]=='1':
		value=value+2
	else:
		value=value
	if binary_number[4]=='1':
		value=value+1
	else:
		value=value
	

	if value == decimal_number
		answer=True
	else:
		answer=False
	return answer


def main():
	total_correct_answers= 0
	total_questions_asked=0

	generate_binary()
	response=int(input(f"What is the decimal value of the binary number {binary_number}? "))
	check_answer(binary_number, response)
		if check_answer(binary_number, response) == False:
			print("Incorrect!")
			total_questions_asked=total_questions_asked+1
			total_correct_answers=total_correct_answers
		else:
			print("Correct!")
			total_correct_answers= total_correct_answers+1
			total_questions_asked=total_questions_asked+1
	askUser=input("\nEnter 'exit' to quit. Enter anything else to play again: ")
	while askUser != 'exit':
		main()

	print(f"You got {total_correct_answers} out of {total_questions_asked} questions correct. Thanks for playing! "))


main()



