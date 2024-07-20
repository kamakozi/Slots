import random


def deposit(user):
    user_dep = int(input(
        f"Your current balance: {user["balance"]}€\nHow much would you like to deposit:\nType here: "))
    if user_dep >= 10:
        user["balance"] = user["balance"] + user_dep
        print(f"Your new balance: {user["balance"]}")
        gameplay(user)
    else:
        print("Minimum deposit amount is 10€!")
        main()


def slot(user):
    if user["balance"] == 0:
        deposit(user)
    player_bet = int(input(f"How much would you like to bet?\nBalance: {user["balance"]}Amount: "))
    if player_bet > user["balance"]:
        print("You don't have enough balance!")
    else:
        gameplay(user)


def spinit(user):
    player = int(input(f"1.Spin\n2.Back\n"))
    if player == 1:
        maingame(user)
    elif player == 2:
        gameplay(user)


def maingame(user):
    slot_words = ["Tree", "Frog", "House", "Gold", "Diamond"]
    total_1 = random.sample(slot_words, 1)
    total_2 = random.sample(slot_words, 1)
    total_3 = random.sample(slot_words, 1)
    total = total_1 + total_2 + total_3
    player_bet = int(input("How much would you like to bet?\nAmount: "))
    if player_bet < user["balance"]:
        user["balance"] = user["balance"] - player_bet
        if total == ["Tree", "Tree", "Tree"]:
            winnings = player_bet * 1.3
            user["balance"] = user["balance"] * 1.3
            print(f"Slot rolled: {total}")
            print(f"Congrats! You won: {winnings}. New balance {user["balance"]}€")
            spinit(user)
        elif total == ["Frog", "Frog", "Frog"]:
            winnings = player_bet * 1.5
            user["balance"] = user["balance"] * 1.5
            print(f"Slot rolled: {total}")
            print(f"Congrats! You won: {winnings}. New balance {user["balance"]}€")
            spinit(user)
        elif total == ["House", "House", "House"]:
            winnings = player_bet * 2
            user["balance"] = user["balance"] * 2
            print(f"Slot rolled: {total}")
            print(f"Congrats! You won: {winnings}. New balance {user["balance"]}€")
            spinit(user)
        elif total == ["Gold", "Gold", "Gold"]:
            winnings = player_bet * 5
            user["balance"] = user["balance"] * 5
            print(f"Slot rolled: {total}")
            print(f"Congrats! You won: {winnings}. New balance {user["balance"]}€")
            spinit(user)
        elif total == ["Diamond", "Diamond", "Diamond"]:
            winnings = player_bet * 10
            user["balance"] = user["balance"] * 10
            print(f"Slot rolled: {total}")
            print(f"Congrats! You won: {winnings}. New balance {user["balance"]}€")
            spinit(user)
        else:
            print(f"Rolled: {total}. You lost: {player_bet}\nNew balance: {user["balance"]}€")
            spinit(user)


def gameplay(user):
    user_input = int(input("Select:\n1.Play!\n2.Balance\n3.Deposit\n4.Exit\n"))
    if user_input == 1:
        spinit(user)
    elif user_input == 2:
        print(f"Your balance is: {user["balance"]}€")
        gameplay(user)
    elif user_input == 3:
        deposit(user)
    elif user_input == 4:
        print("Exiting!")
        main()


def game_selector(user):
    user_input = int(input("Please select:\n1.Play\n2.Rules\n3.Exit\nSelect here: "))
    if user_input == 1:
        gameplay(user)
    elif user_input == 2:
        rules(user)
    elif user_input == 3:
        exit(2)
    else:
        print("Unknown selector!")


def rules(user):
    print(
        "These are the rules:\n"
        "1. You must add your nickname.\n"
        "2. You need at least 1€ to use the slot machine.\n"
        "3. You need to spin 3 of the same words in a row to win.\n"
        "4. If you don't get 3 of the same words in a row, you lose automatically."
    )
    print("______________________\n"
          "Winning Table:\n"
          "Tree = 1.3X\n"
          "Frog = 1.5X\n"
          "House = 2X\n"
          "Gold = 5X\n"
          "Diamond = 10X - Jackpot\n"
          "______________________")
    game_selector(user)


def main():
    print("Welcome to the slots. Good luck!")
    user_name = input("What is your name?: ")
    user = {"name": user_name, "balance": 0}
    game_selector(user)


main()
