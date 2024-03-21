def main():
    total = 0
    while True:
        try:
            num = float(input("Enter a number (enter -1 to stop): "))
            if num == -1:
                break
            total += num
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"The sum of all numbers entered is: {total:.2f}")

if __name__ == "__main__":
    main()