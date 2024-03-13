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
print("Generated password:", passwordv1) #step 3 of the password generation. Concatenates step 1 and 2.

password_upper = passwordv1.upper()
print(passwordv1 + password_upper)