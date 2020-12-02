#-------------------------------#
# Title: Assignment07_Pickling
# Desc: Using Pickling in Python
# Chang Log: (Who, When, What)
# ALi,Dec. 1, 2020,Created File
#-------------------------------#

import pickle

print("We are going to try some pickling.\n")

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
