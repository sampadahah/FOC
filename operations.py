from read import read
import os

def display():
    # it reads data from  the text file
    file_data = read()
    print("-----------------------------------------------------------------------------------------------")
    for row in file_data: # using for loop so it iterates over each row in the file_data
        print(row[0].ljust(9) + '|', end='') #prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
        for each in row[1:]:
            print(each.ljust(16) + '|', end='') #prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
        print() #Print a new line after printing each row
        print("-----------------------------------------------------------------------------------------------")


def calculate(price,duration):
    total_amount = price * duration
    vat_amount = 0.15 * total_amount
    final_amount = total_amount + vat_amount
    return total_amount, final_amount

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Remove the content from the console screen

