word = input("Enter word to search for Vowels:")
set1 = set(word)
print(set1) #
vowels={'a','e','i','o','u'}
result = set1.intersection(vowels)
print("Vowels Present in give Word is:", result)

#Enter word to search for Vowels:prostack
#{'o', 'c', 'r', 'k', 't', 's', 'p', 'a'}
#Vowels Present in give Word is: {'a', 'o'}