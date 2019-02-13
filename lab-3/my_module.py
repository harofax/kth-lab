import text_encryption_function
import random


############# UPG 1 #############
def copy_texy_file(in_file, out_file):
	file_input = open(in_file, "r")
	file_copy = open(out_file, "w")

	for line in file_input:
		file_copy.write(line)

	file_input.close()
	file_copy.close()


#copy_texy_file("namn.csv", "my_copy.csv")


########### UPG 2 #############
def encrypt_file(in_file, out_file):
	file_input = open(in_file, "r")
	file_encrypted = open(out_file, "w")

	for line in file_input:
		file_encrypted.write(text_encryption_function.encrypt(line))

	file_input.close()
	file_encrypted.close()


#encrypt_file("namn.csv", "secret_names.csv")


############ UPG 3 ############
def user_dialogue():

	while "Pigs" != "Fly":

		in_file = input("Name of file to be encrypted: ")
		out_file = input("Name of encrypted file: ")

		try:
			encrypt_file(in_file, out_file)
		except FileNotFoundError:
			print("Invalid filename, no such file exists: ", in_file)
		else:
			print("Encryption finished successfully!")
			break


#user_dialogue()


############# UPG 4 ###########
def get_int_input(prompt_string):

	while "Pigs" != "Fly":

		try:
			number = int(input(prompt_string))
		except ValueError:
			print("That is not a number! Try again.")
			continue
		else:
			break

	return number


#get_int_input("Ange ett tal: ")

############# UPG 5 ############
short_quiz_list = [[
	"Vad heter Norges huvudstad?", "Oslo", "Bergen", "Köpenhamn", "London"
], [
	"Vad står ABBA för?", "Agneta Björn Benny Annefrid",
	"Amsterdam Berlin Bergen Asperido", "Agneta Bosse Boris Ann-Marie",
	"Alfons Bill Bertil Alina"
]]


def run_quiz():
	
	quiz_questions = get_quiz_list_handle_exceptions()
	
	print("==============================")
	print("=       WELCOME TO THE       =")
	print("=            QUIZ            =")
	print("==============================")
	
	score = 0
	max_score = len(quiz_questions)

	for question in quiz_questions:

		print("-------------------------------")
		correct_answer = question[1]

		alternatives = question[1:]
		random.shuffle(alternatives)
		
		print(question[0])

		print("-------------------------------")
		for q_alt in alternatives:
			q_alternative_number = str(alternatives.index(q_alt) + 1)

			print("Alternativ", q_alternative_number + ":", q_alt)

		print()

		answer = get_int_input("Vad är ditt svar? (1, 2, 3)\n")



		print("**************")
		if answer == alternatives.index(correct_answer) + 1:
			print("* Rätt svar! *")
			score += 1
		else:
			print("* Fel svar!  *")
		print("**************")
		print()
		

	print("#########################")
	print("#     THE QUIZ IS       #")
	print("#        OVER           #")
	print("#########################")
	print()
	if score == max_score:
		print("Du fick alla", max_score, "frågor rätt! Grattis!")
	elif score == 0:
		print("Du fick 0 rätt, men det är tanken som räknas!")
	else:
		print("Du fick", score, "ut av", max_score, "rätt! Bra jobbat!")

#run_quiz(short_quiz_list)

################ UPG 6 ###############
def get_quiz_list_handle_exceptions():
	
	while "Pigs" != "Fly":
		
		quiz_file_name = input("Name of quiz-file: ")
		
		try:
			quiz_list = quiz_file_convert(quiz_file_name)
		except FileNotFoundError as fnf:
			print("File \"" + fnf.filename+"\" does not exist.")
			print("Try again.")
		except OSError as oe:
			print("This file is in an incorrect format.")
			print("Each question must be four strings")
			print("separated by ; on separate lines.")
		else:
			break
	
	return quiz_list

def quiz_file_convert(quiz_file_name):
	quiz_file = open(quiz_file_name, "r")
	quiz_list = []

	for line in quiz_file:
		line.strip()
		question = line.strip().split(";")
		if len(question) != 4:
			raise OSError
		else:
			quiz_list.append(question)
	
	return quiz_list

run_quiz()
