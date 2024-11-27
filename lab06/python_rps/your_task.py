def hello_world():
    return "Hello world!"


def rps(hand1, hand2):
    valid_hands = ["rock", "paper", "scissors"]

    if hand1 not in valid_hands or hand2 not in valid_hands:
        return "Invalid"

    if hand1 == hand2:
        return "Tie!"
    elif (
        (hand1 == "rock" and hand2 == "scissors")
        or (hand1 == "scissors" and hand2 == "paper")
        or (hand1 == "paper" and hand2 == "rock")
    ):
        return f"{hand1.capitalize()} wins!"
    else:
        return f"{hand2.capitalize()} wins!"
