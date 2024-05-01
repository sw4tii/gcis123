##Mohammed Abujbara: https://github.com/MohamadAbujbara/mhmd-s-repo  read data function
##Samira Al Saqqa: https://github.com/SamiraAlsaqqa/gcis123  class article
##Swati Poojary:https://github.com/sw4tii/gcis123.git  main function
##Maryam Sabt:https://github.com/maryamsabt/GCIS123.git  class cart

import csv

INVENTORY = {}


def read_data(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) == 3:
                name, inventory, price = row
                INVENTORY[name] = (int(inventory), float(price))


class Article:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return "Article: " + self.name + ", Quantity: " + str(self.quantity) + ", Price: $" + str(self.price)


class Cart:
    def __init__(self):
        self.list_of_purchased = []

    def addProduct(self, name, quantity):
        if name in INVENTORY:
            available_quantity = INVENTORY[name][0]
            if quantity > available_quantity:
                quantity = available_quantity
            for item in self.list_of_purchased:
                if item.name == name:
                    item.quantity += quantity
                    break
            else:
                self.list_of_purchased.append(Article(name, INVENTORY[name][1], quantity))
            INVENTORY[name] = (INVENTORY[name][0] - quantity, INVENTORY[name][1])

    def removeProduct(self, name, quantity):
        for item in self.list_of_purchased:
            if item.name == name:
                if quantity > item.quantity:
                    quantity = item.quantity
                    self.list_of_purchased.remove(item)
                else:
                    item.quantity -= quantity
                if name in INVENTORY:
                    INVENTORY[name] = (INVENTORY[name][0] + quantity, INVENTORY[name][1])
                break

    def displayCart(self):
        if not self.list_of_purchased:
            print("Sorry, the shopping cart is empty")
        else:
            for item in self.list_of_purchased:
                print(item)

    def checkout(self):
        total_bill = 0
        for item in self.list_of_purchased:
            price = item.price
            if item.quantity > 3:
                price *= 0.9  # 10% discount if quantity > 3
            total_bill += price * item.quantity
        total_bill *= 1.07  # 7% VAT
        return total_bill


def main():
    read_data("products.csv")
    cart = Cart()
    while True:
        print("1. List all items, inventory, and price")
        print("2. List cart shopping items")
        print("3. Add an item to the shopping cart")
        print("4. Remove an item from the shopping cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Inventory:")
            print(INVENTORY)
        elif choice == '2':
            cart.displayCart()
        elif choice == '3':
            name = input("Enter the name of the article: ")
            quantity = int(input("Enter the quantity: "))
            cart.addProduct(name, quantity)
        elif choice == '4':
            name = input("Enter the name of the article: ")
            quantity = int(input("Enter the quantity: "))
            cart.removeProduct(name, quantity)
        elif choice == '5':
            total_bill = cart.checkout()
            print("Total bill: $" + format(total_bill, ".2f"))
        elif choice == '6':
            break
        else:
            print("Invalid choice")
            
        while True:
            user_input = input("Do you want to continue (y/n): ")
            if user_input == 'y' or user_input == 'Y':
                break
            elif user_input == 'n' or user_input == 'N':
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")




if __name__ == "__main__":
    main()
