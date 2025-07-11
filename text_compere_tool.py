#Text Compere Tool 

print("Welcome to our Text Compare Tool!\n")

def compere():
    text1 = input("Enter your first text: ")
    text2 = input("Enter your second text: ")

    if text1 == text2:
        print("\n✅ Your first and second text are same! No difference found.")
        print(f"\nYour text:\n{text1}")
    else:
        print("\n❌ Your first and second text are NOT same!\n")
        print("🔍 Your difference is:\n")

        words1 = text1.split()
        words2 = text2.split()

        only_in_text1 = []
        only_in_text2 = []

        for word in words1:
            if word not in words2:
                only_in_text1.append(word)

        for word in words2:
            if word not in words1:
                only_in_text2.append(word)

        print(f"Text 1 ➜ {', '.join(only_in_text1) if only_in_text1 else 'No unique words'}")
        print(f"Text 2 ➜ {', '.join(only_in_text2) if only_in_text2 else 'No unique words'}")

while True:
    compere()

    more = input("\nDo you want to compare more text? (yes/no): ").strip().lower()
    if more != "yes":
        print("\nClosing compare tool system. Goodbye!")
        break
