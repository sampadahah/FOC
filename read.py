def read():
    try:
        data = []
        column = ['Kitta No.', ' City/District ', ' Land Faced ', ' Anna ', ' Price ', ' Availability ']  
        data.append(column)  # Adding the column headers to the data list.

        file = open('land.txt', 'r')  # Opening the file 'land.txt' in read mode.
        for line in file.readlines():
             data.append(line.rstrip().split(','))  # Parsing each line from the file and appending it to the data list.
        file.close()  # Closing the file after reading.

    
    except FileNotFoundError:
        print(f"Error: File not found!")
        
    return data

def print_rent_bill(customer_name): 
    file = open("Rented By "+ customer_name+".txt","r")
    bill = file.read()
    print(bill)
    file.close()


def print_return_bill(customer_name):   
    file = open("Returned By "+ customer_name+".txt","r") #Opening the sell bill file associated with the customer name in read mode.
    bill = file.read() #Reading the contents of the sell bill file.
    print(bill) # Orinting the contents of the sell bill.
    file.close() #Cloasing the sell bill file.
