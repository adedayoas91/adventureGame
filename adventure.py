import time
import random


class PrintColor:
    COLORS = ["\033[91m", "\033[95m", "\033[94m", "\033[96m", "\033[92m"]

    @classmethod
    def get_color(cls):
        """
        Choose colors randomly to be used for printing texts in the console
        """
        return random.choice(cls.COLORS)


def print_colored(text, delay=2):
    """
    Function that calls get_color() method and displays
    texts in the chosen color
    Args
    :param text: (str) message to be displayed on the console
    :param delay: (int) The number of seconds delay before
    another text is printed on the console
    """
    color_text = f"{PrintColor.get_color()}{text}\033[0m"
    print(color_text)
    time.sleep(delay)


def get_user_decision(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print("Invalid input. Try again.")


def battle_sequence(battle_texts):
    for text in battle_texts:
        print_colored(text, 2)
    print_colored("\n", 2)


def battle_text():
    return [
        "You prepare for battle...",
        "With a determined look, you face the challenge ahead.",
        "The encounter is fierce, but you fight valiantly.",
        "Victory is yours! The enemy has been defeated.",
    ]


def escape_or_fight():
    decision = get_user_decision("Choose 1 to fight or 2 "
                                 "to flee: ", ["1", "2"])
    if decision == "1":
        battle_sequence(battle_text())
        return True
    elif decision == "2":
        print_colored("You decide to flee.\n")
        return False


def house_encounter(deamon, weapon):
    print_colored(f"A {deamon} emerges from the house.", 2)
    print_colored(f"The {deamon} attacks! Prepare to defend yourself.\n")

    if weapon == "small dagger":
        print_colored("You feel unprepared with just a small dagger.", 2)
        decision = escape_or_fight()
    elif weapon == "newKnife":
        decision = escape_or_fight()
    return decision


def explore_cave(weapon):
    if weapon == "small dagger":
        print_colored("You enter the cave and spot a gleam of metal.", 2)
        print_colored("You've discovered the magical new knife!", 2)
        print_colored("You discard your old dagger and take the "
                      "new weapon.", 2)
        weapon = "newKnife"
    elif weapon == "newKnife":
        print_colored("You enter the cave but find it empty.", 2)
    print_colored("You leave the cave and return to the field.\n", 2)
    return weapon


def game_opener(deamon):
    print_colored("Welcome to an adventure in a mystical land!", 2)
    print_colored("You're in an open field with grass and "
                  "wildflowers.", 2)
    print_colored(f"A {deamon} is rumored to be nearby, "
                  f"terrorizing the village.", 2)
    print_colored("To your right is a dark cave, and ahead is "
                  "a mysterious house.", 2)
    print_colored("You hold a dagger, ready to face any challenges.\n", 2)


def play_adventure(creatures, weapon):
    while True:
        print_colored("Enter 1 to approach the house, or 2 "
                      "to explore the cave.", 2)
        action = get_user_decision("What's your decision? "
                                   "(Enter 1 or 2): ", ["1", "2"])

        if action == "1":
            decision = house_encounter(creatures, weapon)
            if decision:
                break
        elif action == "2":
            weapon = explore_cave(weapon)


def main_game():
    weapon = "small dagger"
    deamon_list = ["medusa", "pirate", "lion", "wicked mermaid"]

    while True:
        deamon = random.choice(deamon_list)
        game_opener(deamon)
        play_adventure(deamon, weapon)

        replay = get_user_decision("Would you like to play again? "
                                   "(y/n): ", ["y", "n"])
        if replay == "n":
            print_colored("🤨🤨🤨")
            print_colored("Thanks for playing! Looking forward to "
                          "your coming back for more🤗", 2)
            break
        elif replay == "y":
            print_colored("Restarting the adventure...\n", 2)


if __name__ == "__main__":
    main_game()
