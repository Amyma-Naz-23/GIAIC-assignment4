import random

NUM_SIDES:int = 6
def main():

    die1:int = random.randint(1, NUM_SIDES)
    die2:int = random.randint(1, NUM_SIDES)

    total_rolls:int = die1 + die2

    print(f"You rolled a {die1} and a {die2} for a total of {total_rolls}") 

if __name__ == "__main__":
    main()


