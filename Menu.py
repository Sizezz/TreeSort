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