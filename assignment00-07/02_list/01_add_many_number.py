def add_many_number(numbers):  
    total: int = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_numbers: int = add_many_number(numbers)
    print(sum_numbers)

if __name__ == "__main__":
    main()