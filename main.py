from operations import display,clear
from rent_land import rent 
def main():
    #Display the main data
    print("""
                 _____                 _                         ____                                         _               _   _                          _ 
                |_   _|   ___    ___  | |__    _ __     ___     |  _ \   _ __    ___    _ __     ___   _ __  | |_   _   _    | \ | |   ___   _ __     __ _  | |
                  | |    / _ \  / __| | '_ \  | '_ \   / _ \    | |_) | | '__|  / _ \  | '_ \   / _ \ | '__| | __| | | | |   |  \| |  / _ \ | '_ \   / _` | | |
                  | |   |  __/ | (__  | | | | | | | | | (_) |   |  __/  | |    | (_) | | |_) | |  __/ | |    | |_  | |_| |   | |\  | |  __/ | |_) | | (_| | | |
                  |_|    \___|  \___| |_| |_| |_| |_|  \___/    |_|     |_|     \___/  | .__/   \___| |_|     \__|  \__, |   |_| \_|  \___| | .__/   \__,_| |_|
                                                                                       |_|                          |___/                   |_|                               

                                                        𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: 𝐌𝐚𝐥𝐞𝐩𝐚𝐭𝐚𝐧, 𝐏𝐨𝐤𝐡𝐚𝐫𝐚     𝐏𝐡𝐨𝐧𝐞 𝐍𝐮𝐦𝐛𝐞𝐫: 𝟗𝟕𝟔𝟓𝟗𝟒𝟎𝟖𝟒𝟓""")

    while True:
            try:
                # Shows  the menu option
                print(""" 
                                                                ╔════╦═════════════════════════════════════╗
                                                                ║ SN ║    Menu                             ║
                                                                ╠════╬═════════════════════════════════════╣
                                                                ║  1 ║    Display                          ║
                                                                ╠════╬═════════════════════════════════════╣
                                                                ║  2 ║    Rent                             ║
                                                                ╠════╬═════════════════════════════════════╣
                                                                ║  3 ║    Return                           ║
                                                                ╠════╬═════════════════════════════════════╣   
                                                                ║  4 ║    Exit                             ║
                                                                ╚════╩═════════════════════════════════════╝
 """)
                
                user_input =int(input("Select any option from the above table: "))
                
                if user_input == 1:
                    display() #Calling the display function
                
                elif user_input == 2:
                    rent()#Calling the rent funtion from rent_land

                elif user_input == 3:
                    pass #Calling the return function from return_land
                    
                elif user_input == 4:
                    print('Exiting...') # Exit the loop and terminate the program
                    break
                else:
                    print("Choose number between 1 to 4 from the above table only.") 
                
            except:
                print("Please enter integer only.") # Displays an error message if an exception occurs when user_input enters invalid number
main() #calling the main function in order to start the program 
