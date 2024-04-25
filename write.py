import datetime
from operations import calculate

def modify_data(data):
    rent_bill = open("land.txt", "w") #Opening the 'land.txt' rent_bill in write mode.
    for i in range(1, len(data)):
        each = data[i]
        rent_bill.write(f"{each[1]},{each[2]},{each[3]},{each[4]},{each[5]},{each[6]}\n") # writing the updated data to the rent_bill.
    rent_bill.close() #Closing the rent_bill after writing

def rent_invoice(customer_name,phone_no,address,invoice,total_amount,vat_amount,final_amount,land_faced,duration):


     with open(f"Rented By {customer_name}.txt", "w") as rent_bill:

        bill_top=f"""
                                                         Techno Property Nepal
                                                     Hospital Chowk,Pokhara, Nepal
                    VAT : 13579                                                                         Ph. No:9765940845

                    Name:{customer_name}
                    Address:{address}
                    Phone:{phone_no}

                    -----------------------------------------------------------------------------------------------------
                    |Sn | Items                                                      | Rate      | Qty       | Total    |
                    -----------------------------------------------------------------------------------------------------"""


        rent_bill.write("Customer Name: " + customer_name + "\n")
        rent_bill.write("Phone Number:"+ phone_no +"\n")
        rent_bill.write("Address:"+address+"\n")
        rent_bill.write(f"Date & Time of Rent: {datetime.datetime.now()}\n") #Writing the current data and time to the invoice.
        rent_bill.write("------------------------------------------------------\n")                
        for i in invoice:
            rent_bill.write(f'Kitta No: {i[0]}\n') #Writing the kitta no of land in the invoice.
            rent_bill.write(f'City/District: {i[1]}\n') #Writing the location of land in the invoice.
            rent_bill.write(f'Land Faced: {i[2]}\n') #Writing the direction of land faced in the invoice.
            rent_bill.write(f'Net Amount: {i[3]}\n') #Writing the net amount of each land in the invoice.
            rent_bill.write("------------------------------------------------------\n")
        rent_bill.write(f"Total net amount : Rs.{total_amount}\n") #Keeping record about the total net amount in the invoice.
        rent_bill.write(f"VAT amount (15%): Rs.{vat_amount}\n") # Recording the VAT amount in the invoice.
        rent_bill.write(f"Amount including VAT: Rs.{final_amount}") #Recording the final amount including VAT in the invoice.

   


def return_invoice(invoice,duration,customer_name,phone_no,address):

    total_amount = 0
    for x in invoice:
        total_amount += int(x[2])                      #Calculating the total amount by summing the net amounts of each item in the invoice.
    vat_amount = total_amount * 0.15                   #Calculating the VAT amount as 15% of the total amount.
    final_amount = total_amount + vat_amount 

    rent_bill = open( "Returned By "+ customer_name+".txt","w") #Opening the sell invoice rent_bill for the specific customer in write mode.


    rent_bill.write("------------------------------------------------------\n") 
    rent_bill.write("                   TECHNO PROPERTY NEPAL\n") 
    rent_bill.write("------------------------------------------------------\n") 
    rent_bill.write("Customer name: " + customer_name + "\n")
    rent_bill.write("Phone Number:"+ phone_no +"\n")
    rent_bill.write("Address:"+address+"\n")
    rent_bill.write(f"Date & Time of Return: {datetime.datetime.now()}\n") #Recording the current date and time to the invoice .
    rent_bill.write("------------------------------------------------------\n")                
    for i in invoice:
        rent_bill.write(f'Kitta No: {i[0]}\n') #Writing the kitta no of land in the invoice.
        rent_bill.write(f'City/District: {i[1]}\n') #Writing the location of land in the invoice.
        rent_bill.write(f'Land Faced: {i[2]}\n') #Writing the direction of land faced in the invoice.
        rent_bill.write(f'Duration: {i[3]}\n') #Writing the duration of land rental in invoice
        rent_bill.write(f'Net Amount: {i[3]}\n') #Writing the net amount of each land in the invoice.
        rent_bill.write("------------------------------------------------------\n")
    rent_bill.write(f"Total net amount : Rs.{total_amount}\n") #Keeping record about the total net amount in the invoice.
    rent_bill.write(f"VAT amount (15%): Rs.{vat_amount}\n") # Recording the VAT amount in the invoice.
    rent_bill.write(f"Amount including VAT: Rs.{final_amount}") #Recording the final amount including VAT in the invoice.

                
    rent_bill.close() #Closing the sell invoice rent_bill after writing.
