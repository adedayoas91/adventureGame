import time
import random


class GameColor:
    COLORS = ["\033[91m", "\033[95m", "\033[94m", "\033[96m", "\033[92m"]

    @classmethod
    def get_color(cls):
        return random.choice(cls.COLORS)


def print_colored(message, delay=2):
    color_message = f"{GameColor.get_color()}{message}\033[0m"
    print(color_message)
    time.sleep(delay)


def get_user_choice(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print("Invalid input. Try again.")

def battle_sequence(battle_texts):
    for text in battle_texts:
        print_colored(text, 1)
    print_colored("\n", 1)


def battle_text():
    return [
        "You prepare for battle...",
        "With a determined look, you face the challenge ahead.",
        "The encounter is fierce, but you fight valiantly.",
        "Victory is yours! The enemy has been defeated.",
    ]


def fight_or_flee():
    decision = get_user_choice("Choose 1 to fight or 2 to flee: ", ["1", "2"])
    if decision == "1":
        battle_sequence(battle_text())
        return True
    elif decision == "2":
        print_colored("You decide to flee.\n")
        return False


def house_encounter(enemy, weapon):
    print_colored(f"A {enemy} emerges from the house.", 2)
    print_colored(f"The {enemy} attacks! Prepare to defend yourself.\n")

    if weapon == "badKnife":
        print_colored("You feel unprepared with just a small dagger.", 2)
        choice = fight_or_flee()
    elif weapon == "newKnife":
        choice = fight_or_flee()
    return choice


def explore_cave(weapon):
    if weapon == "badKnife":
        print_colored("You enter the cave and spot a gleam of metal.", 2)
        print_colored("You've discovered the magical new knife!", 2)
        print_colored("You discard your old dagger and take the new weapon.", 2)
        weapon = "newKnife"
    elif weapon == "newKnife":
        print_colored("You enter the cave but find it empty.", 2)
    print_colored("You leave the cave and return to the field.\n", 2)
    return weapon


def game_intro(enemy):
    print_colored("Welcome to an adventure in a mystical land!", 2)
    print_colored("You're in an open field with grass and wildflowers.", 2)
    print_colored(f"A {enemy} is rumored to be nearby, terrorizing the village.", 2)
    print_colored("To your right is a dark cave, and ahead is a mysterious house.", 2)
    print_colored("You hold a dagger, ready to face any challenges.\n", 2)


def play_adventure(creatures, weapon):
    while True:
        print_colored("Enter 1 to approach the house, or 2 to explore the cave.", 2)
        action = get_user_choice("What's your choice? (Enter 1 or 2): ", ["1", "2"])

        if action == "1":
            choice = house_encounter(creatures, weapon)
            if choice:
                break
        elif action == "2":
            weapon = explore_cave(weapon)


def main_game():
    weapon = "badKnife"
    enemies = ["medusa", "pirate", "lion", "wicked mermaid"]

    while True:
        enemy = random.choice(enemies)
        game_intro(enemy)
        play_adventure(enemy, weapon)

        replay = get_user_choice("Play again? (y/n): ", ["y", "n"])
        if replay == "n":
            print_colored("Thanks for playing! Until next time.", 2)
            break
        elif replay == "y":
            print_colored("Restarting the adventure...\n", 2)


if __name__ == "__main__":
    main_game()
