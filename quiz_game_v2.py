# Lavet af GPT

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("Okay, bye then.")
    quit()
else:
    print("\nLet's play!")

score = 0

questions = [
    ("What does IDK stand for? ", ["i don't know", "i dont know"]), # 'or' virker ikke.
    ("What does MB stand for? ", "macbook")
]

max_tries = 3

for question, correct_answer in questions:
    tries = 0
    while tries < max_tries:
        answer = input(question).lower()
        if answer == correct_answer:
            print("Correct!")
            score += 1
            break  # Break out of the loop if the answer is correct
        else:
            tries += 1
            print(f"Too bad. You have {max_tries - tries} tries left. Try again.")

print("Your final score is: ", score, "=", int(score / len(questions) * 100), "%")
