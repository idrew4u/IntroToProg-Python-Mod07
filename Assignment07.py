#-------------------------------#
# Title: Assignment07
# Desc: Using Pickling and Exception Handling in Python
# Chang Log: (Who, When, What)
# ALi,Dec. 1, 2020,Created File
#-------------------------------#

import pickle

try:
    task = str(input("Enter a Task: "))
    priority = int(input("Enter a Priority: "))
    task_list = [task, priority]
    print(task_list)

    # Pickle the data
    pickle_file = open("AppData.dat", "ab")
    pickle.dump(task_list, pickle_file)
    pickle_file.close()

    # Read pickled data
    pickle_file = open("AppData.dat", "rb")
    pickle_data = pickle.load(pickle_file)
    pickle_file.close()
    print(pickle_data)

except ValueError as e:  # error message when a word or fraction is entered
    print()
    print("Error found.")
    print("Please enter an integer from 1-5 for priority.")

except Exception as e: # error message when error does not meet previous error
    print()
    print("Error found.")
    print("Please try again.")
