print("This is a reverse name generator")

while True:
    name = input("Enter the name you want to reverse: ")
    reversed_name = name[::-1]
    
    print(f"Your reverse name should be: {reversed_name.title()}")
    
    again = input("Do you want to try another name? (y/n): ")
    again.lower()
    if again != "y":
        print("Thanks for using the app! ")
        break