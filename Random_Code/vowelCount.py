str = input("Enter String: ")
vowels = "aeiou"
vowelCount = 0

for char in str:

    if char in vowels:
        vowelCount += 1

print(f"Total Vowel in the string: {vowelCount}")