import random
import array

MAX_LEN = 8

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOWER_CASE_CHARACTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

UPPER_CASE_CHARACTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

SYMBOLS = ['@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<']

COMBINED_LIST = DIGITS + UPPER_CASE_CHARACTERS + LOWER_CASE_CHARACTERS + SYMBOLS

A_digit = random.choice(DIGITS)
B_upper = random.choice(UPPER_CASE_CHARACTERS)
C_lower = random.choice(LOWER_CASE_CHARACTERS)
D_symbol = random.choice(SYMBOLS)

temp_password = A_digit + B_upper + C_lower + D_symbol

for x in range(MAX_LEN - 2):
	temp_pass = temp_password + random.choice(COMBINED_LIST)

	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
		password = password + x

print(password)
