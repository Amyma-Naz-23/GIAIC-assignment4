def double_number(numbers):
    doubled = []
    for number in numbers:
        doubled.append(number * 2)
    return doubled

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    doubled_numbers: list[int] = double_number(numbers)
    print(doubled_numbers)

if __name__ == "__main__":
    main()
