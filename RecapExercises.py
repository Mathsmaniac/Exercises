import webbrowser


def biggest_number():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print("Those are not numbers, try again ")
            continue
        if num1 == 0 or num2 == 0:
            break
        if num1 == num2:
            print("The numbers are equal")
        else:
            print("The larger number is {}".format(max(num1, num2)))


def sum_number():
    summ = 0
    for i in range(20, 26):
        summ += i
        print(i)
    print(f"sum is {summ}")


choice = input("Choose either 'biggest' for biggest number or 'sum' for sum number: ")
if choice.lower() == "sum":
    sum_number()
elif choice.lower() == "biggest":
    biggest_number()
else:
    print("That was not a valid input, I am extremely disappointed in you")
    print("Now you are going to have to run me again as punishment")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
