import random

words_pool = ["lorry", "cycle", "bike", "bus", "car"]
secret_word = random.choice(words_pool)
progress = ["_"] * len(secret_word)
lives = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")

while lives > 0 and "_" in progress:
    print("\n🔤 Word:", " ".join(progress))
    print("❤️ Lives remaining:", lives)
    print("📜 Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
    
    letter = input("👉 Guess a letter: ").lower().strip()
    
    # Validate input
    if len(letter) != 1 or not letter.isalpha():
        print("⚠️ Enter a single valid letter (a-z).")
        continue
    
    if letter in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue
    
    guessed_letters.append(letter)
    
    if letter in secret_word:
        for pos, char in enumerate(secret_word):
            if char == letter:
                progress[pos] = letter
        print("✅ Good guess!")
    else:
        lives -= 1
        print("❌ Incorrect!")

if "_" not in progress:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)