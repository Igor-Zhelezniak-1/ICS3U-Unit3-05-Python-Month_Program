#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is month program


def main():
    # This is month program

    # input
    number_month = int(input("Enter number of month(1-12): "))

    # process
    if number_month == 1:
        print("January")
    elif number_month == 2:
        print("February")
    elif number_month == 3:
        print("March")
    elif number_month == 4:
        print("April")
    elif number_month == 5:
        print("May")
    elif number_month == 6:
        print("June")
    elif number_month == 7:
        print("July")
    elif number_month == 8:
        print("August")
    elif number_month == 9:
        print("September")
    elif number_month == 10:
        print("October")
    elif number_month == 11:
        print("November")
    elif number_month == 12:
        print("December")
    else:
        print("This is not number 1-12")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
