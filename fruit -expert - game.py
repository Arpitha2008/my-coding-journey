basket = []
count = 0

print("Welcome to Fruit Basket Game, Arpitha! 🧺")

while True:
    fruit = input("\nEnter fruit (or 'quit' to stop): ").strip().lower()
    
    if fruit == "quit":
        break
    
    if fruit == "":
        print("Oops, you typed nothing! Try again.")
        continue

    basket.append(fruit)
    count = count + 1
    
    if fruit == "apple":
        print("🍎 Apple added to basket!")
    elif fruit == "banana":
        print("🍌 Banana added!")
    elif fruit == "mango":
        print("🥭 Mango! King added!")
    elif fruit == "litchi":
        print("Litchi! Bihar special added!")
    else:
        print(f"{fruit.title()} added to your basket!")

print("\n--- GAME OVER ---")
print(f"You collected {count} fruits!")
print(f"Your basket: {basket}")

if count >= 5:
    print("Wow Arpitha, your basket is FULL! You are FRUIT QUEEN! 👑")
else:
    print("Nice basket! Collect 5 to become Queen!")

# Bonus: Show unique fruits
unique = list(set(basket))
print(f"Unique fruits you tried: {unique}")
