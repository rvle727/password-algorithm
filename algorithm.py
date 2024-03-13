def remove_vowels(name):
    vowels = "aeiouAEIOU"
    return "".join([char for char in name if char not in vowels])

def generate_password(step1, step2):
    return step1 + step2 #concatenates step 1 and step 2

name_user_input = input("Enter the company/website name: ")  # Prompt the user to input the company/website name
company_name = remove_vowels(name_user_input)  

print(company_name) #result of step 1

birthYear = input("Enter the last 2 digits of your birth year: ")

passwordv1 = generate_password(company_name, birthYear)
print("Password draft:", passwordv1) #step 3 of the password generation. Concatenates step 1 and 2.

password_upper = passwordv1.upper()

digit_symbols = {'0': ')', '1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '('} #Created dictionary to map each symbol to it's digit

shifted_password_upper = ""
for char in password_upper:
    if char.isdigit():
        shifted_password_upper += digit_symbols[char]  # Replace the digit with its respective symbol
    else:
        shifted_password_upper += char
        
print("Your password is: ", passwordv1 + shifted_password_upper)