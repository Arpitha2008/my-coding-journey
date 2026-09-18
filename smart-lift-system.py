# Smart College Lift - Problem Solver
capacity = 8
current = 0
queue = []

print("College Smart Lift System 🏫🛗")

while True:
    action = input("\nEnter: join / exit / status / quit: ").lower()
    
    if action == "quit":
        break
    elif action == "join":
        if current >= capacity:
            print(f"Lift FULL! {current}/{capacity}. Please wait in queue.")
            queue.append("1 person")
            print(f"Queue waiting: {len(queue)}")
        else:
            current += 1
            print(f"Person entered. Inside: {current}/{capacity}")
    elif action == "exit":
        if current > 0:
            current -= 1
            print(f"Person exited. Inside: {current}")
            if queue:
                print("Calling next person from queue!")
                queue.pop(0)
                current += 1
        else:
            print("Lift empty!")
    elif action == "status":
        print(f"Inside: {current}/{capacity} | Waiting: {len(queue)}")


