
def main():
    lst = []

    val = input("Enter the value: ")
    while val:
        lst.append(val)
        val = input("Enter the value: ")

    print(lst)

if __name__ == "__main__":
    main()
