size = input("Choose coffee size (Small, Medium, Large): ")

if size not in ["Small", "Medium", "Large"]:
    print("Invalid size.")
else:
    extra_shot = input("Do you want an extra shot of espresso? (yes/no): ")

    print("\nYour order:")
    print(f"Size: {size}")
    if extra_shot.lower() == "yes":
        print("Extra shot: Yes")
    else:
        print("Extra shot: No")
