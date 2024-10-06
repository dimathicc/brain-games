import random
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def get_lcm(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result


def play_lcm():
    rounds = 3
    print("Find the smallest common multiple of given numbers.")
    for _ in range(rounds):
        numbers = random.sample(range(1, 50), 3)
        correct_answer = get_lcm(numbers)
        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return False
    return True
