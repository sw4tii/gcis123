##Mohammed abujbara did the clean and prepare data function https://github.com/MohamadAbujbara/mhmd-s-repo
##Maryam Sabt did the Visualize data function https://github.com/maryamsabt/Maryam.git 
##Samira al saqqa did the analyze an insertion sort function https://github.com/SamiraAlsaqqa/gcis123
##Swati Pojary did the data function https://github.com/sw4tii/gcis123.git
import csv
import re


def load_data():
    print("---------------------------------")
    print("Welcome to Data Analysis CLI")
    print("---------------------------------")
    print("Program stages:")
    print("1. Load Data")
    print("2. Clean and prepare data")
    print("3. Analyse Data")
    print("4. Visualize Data")
    print()

    print("Stage 1: Load Data")
    while True:
        try:
            path = input("Please enter path to the csv file: ")
            with open(path, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
                headers = data[0]
                print("\nFile exists.")
                print("Loading file...")
                print("File successfully loaded!\n")
                print("Loaded data:")
                for row in data:
                    print(row)
                print()
                return headers, data[1:]
        except FileNotFoundError:
            print("Wrong input. Please enter a valid path.\n")

def clear_and_prepare(data):
    try:
        print("Stage 2: Clear and prepare data")
        print("Choose column from selection below to clear and prepare data:")
        print("Branch / Product / Price / Units sold")
        while True:
            column = input("Please choose column: ")
            c = []
            a = []

            if column.lower() in ["branch", "product", "price", "units sold"]:
                col_index = ["branch", "product", "price", "units sold"].index(column.lower())
                for i in data:
                    a.append(i[col_index])
            else:
                raise ValueError

            print("\nAll empty values replaced with average values!")
            print("###NOTE: Print the updated column here###\n")
            for i in a:
                if re.findall("[0-9]", i):
                    b = int(i)
                elif i.strip() == "":
                    # Replace empty cells with average value
                    b = sum([int(row[col_index]) for row in data if row[col_index].strip() != ""]) / len([int(row[col_index]) for row in data if row[col_index].strip() != ""])
                else:
                    raise TypeError
                c.append(b)

            break

    except ValueError:
        print("Wrong input, please try again.\n")
        clear_and_prepare(data)

    except TypeError:
        print("Non-numerical column, please try again.\n")
        clear_and_prepare(data)

    return c

def analyze_data(data):
    print("Stage 3: Analyse data")
    print("Please choose if you want to sort column in:")
    print("1. Ascending order")
    print("2. Descending order")
    while True:
        try:
            choice = int(input("Please enter your choice: "))
            if choice not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    if choice == 1:
        sorted_data = insertion_sort(data, ascending=True)
        print("\nColumn values are sorted in ascending order!")
    else:
        sorted_data = insertion_sort(data, ascending=False)
        print("\nColumn values are sorted in descending order!")
    print("###NOTE: Print the updated column here###\n")
    return sorted_data

def insertion_sort(data, ascending=True):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and (data[j] > key if ascending else data[j] < key):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def visualize_data(headers, sorted_data):
    print("Stage 4: Visualise Data")
    print("Column:", headers[-1])
    print("Legend: each '*' represents 5 units\n")
    for value in sorted_data:
        print("*" * (int(value) // 5))
    print("\nVisualisation completed!\nThank you and goodbye!")

def main():
    headers, data = load_data()
    cleaned_data = clear_and_prepare(data)
    sorted_data = analyze_data(cleaned_data)
    visualize_data(headers, sorted_data)

if __name__ == "__main__":
    main()

