import random

word_bank = {
    "technology": [
        ("python", "A popular programming language"),
        ("database", "Stores organized information"),
        ("algorithm", "Step-by-step method to solve a problem"),
        ("keyboard", "Used to type on a computer")
    ],
    "animals": [
        ("elephant", "The largest land animal"),
        ("penguin", "A bird that cannot fly"),
        ("giraffe", "Animal with a very long neck"),
        ("dolphin", "An intelligent sea animal")
    ],
    "space": [
        ("planet", "Earth is one of these"),
        ("galaxy", "A huge collection of stars"),
        ("asteroid", "A rocky object in space"),
        ("rocket", "Used to travel into space")
    ]
}

print("=" * 45)
print("        🧠 WORD HUNTER - HANGMAN")
print("=" * 45)

print("\nChoose your category:")
print("1. Technology")
print("2. Animals")
print("3. Space")

choice = input("Enter choice: ")

categories = {
    "1": "technology",
    "2": "animals",
    "3": "space"
}

category = categories.get(choice, "technology")

word, hint = random.choice(word_bank[category])

guessed = set()
wrong = 0
max_wrong = 6

while wrong < max_wrong:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong attempts:", wrong, "/", max_wrong)
    print("Guessed letters:", ", ".join(sorted(guessed)) if guessed else "None")

    if all(letter in guessed for letter in word):
        print("\n🎉 YOU FOUND THE WORD!")
        print("The word was:", word)
        print("Score:", (max_wrong - wrong) * 10)
        break

    guess = input("Enter a letter or type 'hint': ").lower()

    if guess == "hint":
        print("💡 Hint:", hint)
        continue

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only one alphabet letter.")
        continue

    if guess in guessed:
        print("🔁 You already tried that letter.")
        continue

    guessed.add(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        wrong += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 GAME OVER!")
    print("The correct word was:", word)
