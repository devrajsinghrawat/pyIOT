# initiate empty list to hold user input and sum value of zero
def user_input():
    user_list = []
    list_sum = 0

    # seek user input for ten numbers
    for _ in range(10):
        userInput = int(input("Enter any 2-digit number: "))

        try:
            number = userInput
            user_list.append(number)
            if number % 2 == 0:
                list_sum += number
        except ValueError:
            print("Incorrect value. That's not an int!")

    print("user_list: {}".format(user_list))
    print("The sum of the even numbers in user_list is: {}.".format(list_sum))


def main():
    print('testing user_input function')
    user_input()

# write all the executable statements here
if __name__ == '__main__':
    main()
    print('this is my test iug')
