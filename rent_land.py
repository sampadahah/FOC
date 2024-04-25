from operations import display
from read import read
invoice = [] #Creating an empty list to store invoice data.

def rent():
    while True:
        customer_name = input("Enter your name: ")
        phone_no = input("Enter your phone number: ")
        address = input("Enter your address: ")

        if not customer_name.strip() or not phone_no.strip() or not address.strip():
            print("Please provide valid customer name, phone number, and address.")  # Print an error message if any field is empty
        else:
            break

    data=read()  
    rent=True  

    while rent:
        display()
        kitta_no = input("Enter the kitta no. of the land you would like to rent: ")
        if any(row[0] == kitta_no for row in data[1:]):  # Check if kitta_no exists in data
            land = next(row for row in data if row[0] == kitta_no)
            if land[-1].strip() == "Not Available":
                print("This land is not available. Please choose another one.")
            else:
                # return kitta_no, land
                print(f"You have selected venue {land[0]} in {land[1]}, {land[2]} facing, Price: Rs.{land[4]}")

                duration = int(input("Enter the rental period in months: "))

                total_amount, final_amount = calculate_total_amount(int(venue[4]), duration)
                vat_amount = final_amount - total_amount 

                rent_invoice(customer_name,phone_no,address,invoice,total_amount,vat_amount,final_amount,land_faced,duration)
                print(f"Rental bill saved in 'rental_bill.txt'.")

                choice = input("Do you want to select another venue? (Y/N): ").upper()
                if choice != "Y":
                    break
                print(f"Rental bill has been saved in {customer_name}.txt")
        else:
            print("Invalid kitta no. Please enter a valid kitta number.")

        
       
    
 