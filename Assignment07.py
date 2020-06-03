# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# CMcNiff, 5.30.2020, Updated code to complete Assignment07
# CMcniff, 5.30.2020, Updated Error Handling for proper data output
# CMcNiff, 6.1.2020, Updated virtual environment in PyCharm
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
# Declare Variables
strFileName = "C:\_PythonClass\Assignment07\AppData.dat"
lstCustomer = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """ save data to file
    :param file_name: AddData.dat
    :param list_of_data: data added to list
    :return:
    """
    with open(file_name, "wb") as file:
        pickle.dump(list_of_data, file) #This writes list of data to the file
        file.close()

def read_data_from_file(file_name):
    """ read data from file
    :param file_name: AddData.dat
    :return: list_of_data
    """
    with open(file_name, "rb") as file:
        list_of_data = pickle.load(file)
        file.close()
        return list_of_data

# Presentation ----------------------------------------#
def new_user_input():
    intID = int(input("Enter your ID: "))
    strName = str(input("Enter your Name: "))
    lstCustomer = [intID, strName]
    return lstCustomer

# Error Handling -------------------------------------- #
try:
    fileData = read_data_from_file(strFileName)
except FileNotFoundError as e:
    print("File not found, please try again")
    fileData = lstCustomer
except pickle.UnpicklingError as e:
    print("The file you selected is corrupt")
    sys.exit(1)
try:
    fileData.append(new_user_input())
    save_data_to_file(strFileName, fileData)
except ValueError as e:
    print(e)

print(read_data_from_file(strFileName))
input("Press Enter to Exit")


