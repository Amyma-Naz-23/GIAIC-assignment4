import math

def main():
    ab= float(input("Enter the length of side ab: "))
    ac= float(input("Enter the length of side bc: "))

    bc = math.sqrt(ab**2 + ac**2)

    print(f"The length of hypotenuse is {bc}")

if __name__ == "__main__":
    main()
