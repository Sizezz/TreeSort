import os
import random

from Sort import tree_sort

unsortedList = []
sorted_list = []
while True:
    print("1. Add a numbers")
    print("2. Generate a random array")
    print("3. Sort the numbers")
    print("4. Save numbers to a file")
    print("5. Load numbers from a file")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_choice = input("Add numbers to: \n1. New array\n2. Existing array\nEnter your choice: ")

        if add_choice == "1":
            unsortedList = []
        elif add_choice == "2":
            if not unsortedList:
                print("No existing array found. Starting with a new array.")
                unsortedList = []
            else:
                print("Adding numbers to the existing array.")
        else:
            print("Invalid choice! Please enter a valid option.")

        while True:
            num = input("Enter a number (or 'q' to exit): ")
            if num.lower() == 'q':
                break
            try:
                num = float(num)
                unsortedList.append(num)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    elif choice == "2":
        while True:
            try:
                length = int(input("Enter the length of the array: "))
                if length <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid length! Please enter a positive integer.")

        minimum = float(input("Enter the minimum value: "))
        maximum = float(input("Enter the maximum value: "))
        while maximum <= minimum:
            print("Error: Maximum value should be greater than the minimum value.")
            maximum = float(input("Enter the maximum value: "))

        unsortedList.extend(round(random.uniform(minimum, maximum), 1) for _ in range(length))
        print("Random array generated: ", unsortedList)

    elif choice == "3":
        sorted_list = tree_sort(unsortedList)
        print("Sorted numbers:", sorted_list)