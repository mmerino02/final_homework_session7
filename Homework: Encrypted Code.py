# 1. Import the text
import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
text = r.text
print(text)

# 2. Create the variables
vowels = ["a", "e", "i", "o", "u"]
n_vol = []

# 3. Count the vowels in each line
for line in text.split("\n"):
    sum = 0
    for char in line:
        if char in vowels:
            sum += 1
    n_vol.append(sum)  # Appends the result, sum, to the n_vol list.
print(n_vol)

# 4. Associate the number of vowels with a letter
alphabet = " abcdefghijklmnopqrstuvwxyz"  # the space is needed as the enumerate function starts from 0

mapping = {}
for i, letter in enumerate(alphabet):
    mapping[i] = letter
print(mapping)

str = ""
for i in n_vol:
    temp = mapping[i]
    str += temp
print(f'The encrypted code is: {str}')
