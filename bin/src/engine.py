from bin.src.cli import welcome


def run_game(game_function):
    name = welcome()
    if game_function():
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
