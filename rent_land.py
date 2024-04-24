from read import read ,print_rent_bill
from operations import display
from write import modify_data,rent_invoice
invoice = [] #Creating an empty list to store invoice data.

def rent():
    while True:    
        customer_name = input("Enter your name: ") # Promption the user to enter their name.
        phone_no=input("Enter your phone number:")
        address=input("Enter your address:")
        if customer_name == "" and phone_no =="" and address=="":
            print("Please provide valid customer name, phone number, and address.") #Printing an error message if the field is empty
        else:
            break 

    data = read() # Calling the 'read' function to retrieve data.
    rent = True #Initializing the 'rent' variable as true.
 
    while rent: 
              
        
        display() #Calling the 'display' function to show a table.
        kitta_no= int(input('Enter the kitta no. of the land you would like to rent ->'))

        if kitta_no== "":
            print("Kitta  number is required!")
            
        elif  kitta_no > 110 or kitta_no <101:
            print("Please! Select valid kitta number from 101 to 110")

        else:
            if data[kitta_no][6]=="Not Available":
                print("Land is not available for rent!")


            else:
                duration=int(input("Enter the rental period in months ->"))
                print("Selected land is rented succesfully.")
                            
                price = int(data[kitta_no][3].strip().strip("Rs.")) #Extracting the price of the selected land from the data.
                city = data[kitta_no][2] # Extracting the city of the selected land from the data.
                direction = data[kitta_no][3]  #Extracting the direction faced of the selected land from the data.
                area=data[kitta_no][4] #Extracting area of the selected land from the data
                total_rate = (price)  #Calculating the total rate 

                                        
                invoice.append([price, city, direction, area,  total_rate]) #Adding the purchased item details to the invoice list.

                modify_data(data) # Calling the 'modify_data' function to update the data.

                while True:
                    user_input = input("Would you like to Purchase anything else? (Y/N): ").upper() # Ask user to enter 'Y' or 'N' to continue or exit the loop.

                    if user_input == "Y":
                        break #Exiting the inner loop and continuing with the purchase.

                    elif user_input == "N":
                            
                        rent = False #Setting 'Rent' to false to exit the outer loop.
                        rent_invoice(customer_name, invoice) #Calling the 'purchase_invoice' function to generate purchase invoice.
                        print("\n\n\n\n")
                        print_rent_bill(customer_name) #Calling the 'print_purchase_bill' function to print the purchase bill.                     
                        break #Exiting the inner loop.

                    else:
                        print("Please enter Y or N only.")

 