species = input("Enter your pet's species (Dog/Cat): ").lower()
age = float(input("Enter your pet's age in years: "))

if species == "dog":
    if age < 2:
        print("Recommendation: Puppy food")
    elif age <= 7:
        print("Recommendation: Adult dog food")
    else:
        print("Recommendation: Senior dog food")

elif species == "cat":
    if age < 2:
        print("Recommendation: Kitten food")
    elif age <= 5:
        print("Recommendation: Adult cat food")
    else:
        print("Recommendation: Senior cat food")

else:
    print("Sorry, recommendations available only for dogs and cats.")
