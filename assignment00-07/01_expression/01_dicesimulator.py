import random

NUM_SIDES = 6  # Define the number of sides on each die

def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    total_rolls: int = die1 + die2
    print(f"You rolled a {die1} and a {die2} for a total of {total_rolls}")
     
def main():
    die1 = 10
    print(f"die1 in main() starts as {die1}")

    for _ in range(3):
        roll_dice()

    print(f"die1 in main() and still {die1}")

if __name__ == "__main__":
    main()
