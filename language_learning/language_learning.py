#!/usr/bin/env python3


import random


words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of/from"},
    {"spanish": "que", "english": "that/which"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to/at"},
    {"spanish": "en", "english": "in/on"},
    {"spanish": "un", "english": "a/an"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself/itself"},
    {"spanish": "no", "english": "no/not"},
    {"spanish": "haber", "english": "to have"},
    {"spanish": "por", "english": "for/by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/your/their"},
    {"spanish": "para", "english": "for/to"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "him/her/you"},
    {"spanish": "lo", "english": "it/him/you"},
]


def quiz_user(words):
    random.shuffle(words)
    score = 0
    for word in words:
        print(f"What is the English translation of {word['spanish']}?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"Incorrect! The correct answer is {word['english']}.")

    print(f"Quiz complete! Your Score: {score}/{len(words)}")


def main():
    print("Welcome to the language learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)


if __name__ == "__main__":
    main()
