#Text Compere Tool


print("Welcome to our Text Compere Tool !\n")
def compere():
    text1 = input("Enter your first text: ")
    text2 = input("Enter your Second text: ")
    
    if text1==text2:
        print(f"\nYour first and second text are same,  no defference found!")
        print(f"\nYour text:\n{text1}")
    else:
        print(f"\nYour first and second text are not same! ")
    

while True:
    compere()

    more = input("\nDo you compere more text? (yes/no): ").strip().lower()
    if more != "yes":
        print("Closing compere tool system. Goodbye!")
        break
        
