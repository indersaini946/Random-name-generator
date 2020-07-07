import random
print("Welcome to the Random name generator.")
print()
print("Developed by Inder Saini")
print()
adjectives = ["soft", "hard", "fluffy", "quick"]
nouns = ["rabbit", "zebra", "unicorn", "dog"]
def main():
    answer = input("Do you want a username? y/n ")
    if(answer == "y"):
        word1 = random.choice(adjectives)
        word2 = random.choice(nouns)
        username = word1 + " " + word2
        print(username)
        repeat = input("Again? y/n ")
        if(repeat == "y"):
            main()
        else:
            print("Thank you for using the random name generator")
    else:
        print("Thank you for using the random name generator")
    
main()
