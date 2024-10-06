import random


def generate_progression(start, ratio, length):
    return [start * (ratio ** i) for i in range(length)]


def play_progression():
    rounds = 3
    print("What number is missing in the progression?")
    for _ in range(rounds):
        start = random.randint(1, 10)
        ratio = random.randint(2, 5)
        length = random.randint(5, 10)
        progression = generate_progression(start, ratio, length)
        missing_index = random.randint(0, length - 1)
        correct_answer = progression[missing_index]
        progression[missing_index] = '..'
        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return False
    return True
