print ("This app is to change the format of a sentence")

sentence = input("Enter the sentence you want to change the format: ")
print ("1. UPPERCASE")
print ("2. lowercase")
print ("3. Title Case")
print ("4. Sentence case")

option_selected = input("Choose an option from 1 to 4: ")

if option_selected == "1":
    print(sentence.upper())
elif option_selected == "2":
    print(sentence.lower())
elif option_selected == "3":
    print(sentence.title())
elif option_selected == "4":
    print(sentence.capitalize())
    
    