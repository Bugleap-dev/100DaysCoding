vowel = ["a","e","i","o","u"]

word = input("")

if vowel in word.lower():
    print(word.replace(vowel, ""))

for vowel in word:
    print(word.replace(vowel, ""), end ="")