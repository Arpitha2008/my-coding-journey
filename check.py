# Smart fruit checker - works with any case!
fruit = input("Enter a fruit name: ").strip().lower()

if fruit == "apple":
    print("It's Apple! Red and juicy!")
elif fruit == "banana":
    print("It's Banana! Yellow!")
else:
    print(f"Oh, {fruit.title()} is different! Nice!")

print("Thanks for playing!")

