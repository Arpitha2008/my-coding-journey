# Fruit Expert Game - by Arpitha
# Level 3 - Score Counter

count = 0

while True:
    fruit = input("\nEnter fruit (or 'quit' to stop): ").strip().lower()
    
    if fruit == "quit":
        print(f"\nBye! Game over! You tasted {count} fruits!")
        if count >= 5:
            print("Wow Arpitha, you are a FRUIT EXPERT! 🍎👑")
        else:
            print(f"Good job! Try to taste 5 fruits next time!")
        break
    
    count = count + 1
    
    if fruit == "apple":
        print("🍎 Apple! Red and crunchy!")
    elif fruit == "banana":
        print("🍌 Banana! Yellow and sweet!")
    elif fruit == "mango":
        print("🥭 Mango! King of fruits!")
    elif fruit == "litchi":
        print("Litchi! Juicy and from Bihar!")
    elif fruit == "orange" or fruit == "ornage":
        print("🍊 Orange! Vitamin C power!")
    elif fruit == "grapes":
        print("🍇 Grapes! Small but mighty!")
    else:
        print(f"Wow, {fruit.title()} is new! Added to your list!")

print(f"Thanks for playing, Arpitha! Total score: {count}")
