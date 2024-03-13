def remove_vowels(name):
    vowels = "aeiouAEIOU"
    return "".join([char for char in name if char not in vowels])

name_user_input = input("Enter the company/website name: ")  # Prompt the user to input the company/website name
company_name = remove_vowels(name_user_input)  

print(company_name)
