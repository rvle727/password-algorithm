def remove_vowels(name):
    vowels = "aeiouAEIOU"
    return "".join([char for char in name if char not in vowels])

spotify = "Spotify"
company_name = remove_vowels(spotify)

print(company_name)