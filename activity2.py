##Mohammed Abujbara: https://github.com/MohamadAbujbara/mhmd-s-repo main function
##Samira al saqqa: https://github.com/SamiraAlsaqqa/gcis123 main function
##Swati poojary:https://github.com/sw4tii/gcis123.git the rest of the functions plus the docstrings and some editing in the main function
##Maryam Sabt:https://github.com/maryamsabt/GCIS123.git the rest of the functions plus the docstrings and some editing in the main function



# Conversion rates
AED_to_EUR_rate = 0.25 #AED to Euro
AED_to_GBP_rate = 0.21 #AED to British Pound
AED_to_USD_rate = 0.27 #AED to US Dollar

# Functions to convert from AED to other currencies
def aed_to_eur(money):
    return money * AED_to_EUR_rate #Converts from AED to Euro

def aed_to_britishPound(money):
    return money * AED_to_GBP_rate #Converts from AED to British Pound

def aed_to_dollar(money):
    return money * AED_to_USD_rate #Converts from AED to US Dollar

# Functions to convert from other currencies to AED
def dollar_to_aed(amount):
    return amount / AED_to_USD_rate #Converts from AED to US Dollar

def britishPound_to_aed(amount):
    return amount / AED_to_GBP_rate #Converts from AED to British Pound

def eur_to_aed(amount):
    return amount / AED_to_EUR_rate #Converts from AED to Euro 

# Main function for the conversions
def main():
    print('"    Main Menu"')
    print("Welcome to Currency Converter")
    print("--------------------------")
    print("Select the conversion direction:")
    print("1. AED to other currencies (EUR, GBP, USD)")
    print("2. Other currencies (EUR, GBP, USD) to AED")
    print("3. Exit")

    choice = int(input("Enter your choice of coversion (1/2/3): "))

    if choice == 1:
        money = float(input("Enter your amount in AED: ")) #Here float is used because the amount entered can also be in decimals
        print("Select the currency you want to convert to:") #Conversion of AED to the other currencies
        print("1. AED to Euro(EUR) ")
        print("2. AED to British Pound(GBP) ")
        print("3. AED to US Dollar(USD) ")
        print('4. Exit')

        conv_choice = int(input("Enter your choice (1/2/3): "))

        if conv_choice == 1:
            result = aed_to_eur(money) #Converts AED to Euro
            print(f"{money} AED is equal to {result} Euro")
        elif conv_choice == 2:
            result = aed_to_britishPound(money) #Converts AED to British Pound
            print(f"{money} AED is equal to {result} British Pound")
        elif conv_choice == 3:
            result = aed_to_dollar(money) #Converts AED to US Dollar
            print(f"{money} AED is equal to {result} US Dollar")
        else:
            print("Invalid choice")

    elif choice == 2:
        amount = float(input("Enter your amount in the foreign currency: "))
        print("Select the currency to convert to AED:")
        print("1. Euro(EUR) to AED")
        print("2. British Pound(GBP) to AED")
        print("3. US Dollar(USD) to AED")
        print("4. Exit")

        conv_choice = int(input("Enter your choice (1/2/3/4): "))

        if conv_choice == 1:
            result = eur_to_aed(amount) #Converts Euro to AED
            print(f"{amount} Euro is equal to {result} AED")
        elif conv_choice == 2:
            result = britishPound_to_aed(amount) #Converts British Pound to AED
            print(f"{amount} British Pound is equal to {result} AED")
        elif conv_choice == 3:
            result = dollar_to_aed(amount) #Converts US Dollar to AED
            print(f"{amount} US Dollar is equal to {result} AED")
        else:
            print("Invalid choice.")

    elif choice == 3:
        exit

    else:
        print("Invalid choice! Please enter 1 or 2")

    otherwise_reposnse = input("do you wish to continue(yes/no): ")
    if otherwise_reposnse == "yes":
        main() ## go back to the main menu
    elif otherwise_reposnse == "no":
        print("program is exit")
    else:
        print("please enter a valid option yes/no ")
        
    
if __name__ == "__main__":
    main()