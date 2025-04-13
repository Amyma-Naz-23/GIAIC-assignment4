
INCHES_IN_FOOT:int 12

def main():
    feet:int = int(input("Enter a number of feet: "))
    inches:int = feet * INCHES_IN_FOOT

    print(f"{feet} feet is {inches} inches")

if __name__ == "__main__":
    main()
