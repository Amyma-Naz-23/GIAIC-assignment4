def main():

    ferhneit = float(input("\033[1;3m Enter the temperature in ferhneit: \033[0m"))

    celcius = (ferhneit - 32.00) * (5.00/9.00)

    print(f"Temperature : {ferhneit}F = {celcius}C")


if __name__ == "__main__":
    main()

