# Fruit Game - keeps asking!
while True:
    fruit = input("\nEnter fruit (or 'quit' to stop): ").strip().lower()
    
    if fruit == "quit":
        print("Bye! Game over!")
        break
    elif fruit == "apple":
        print("🍎 Apple! Red and crunchy!")
    elif fruit == "banana":
        print("🍌 Banana! Yellow and sweet!")
    elif fruit == "mango":
        print("🥭 Mango! King of fruits!")
    else:
        print(f"Wow, {fruit.title()} is new! Tell me more!")

print("Thanks for playing my game!")
