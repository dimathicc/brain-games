from src.engine import run_game
from src.games.lcm import play_lcm
from src.games.progression import play_progression


def main():
    print("Choose a game: 1 - LCM, 2 - Progression")
    choice = input()
    if choice == '1':
        run_game(play_lcm)
    elif choice == '2':
        run_game(play_progression)
    else:
        print("Invalid choice.")


if __name__ == '__main__':
    main()
