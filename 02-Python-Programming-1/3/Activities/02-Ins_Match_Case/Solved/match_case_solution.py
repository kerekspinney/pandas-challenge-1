# Boolean to place the order
place_order = True

# List to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pie List
pie_list = ["Pecan", 
            "Apple", 
            "Lemon Meringue", 
            "Banoffee", 
            "Black Bun",
            "Bean", 
            "Buko", 
            "Burek", 
            "Tamale", 
            "Steak"]

# Display initial message


# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while True:

    # Show pie selection prompt
    print("-" * 50)
    for pie_number, pie in enumerate(pie_list, start=1):
        print(f"({pie_number}) {pie}")

    pie_choice = input("Which would you like? ")

    # Validate input
    if pie_choice.isdigit():
        choice_index = int(pie_choice) - 1

        # Validate index
        if 0 <= choice_index < len(pie_list):
            # Add pie to the pie list by finding the matching index and adding one to its value
            pie_purchases[choice_index] += 1

            print("-" * 50)

            # Inform the customer of the pie purchase
            print("Great! We'll have that " + pie_list[choice_index] 
                  + " Pie right out for you.")

            # Provide exit option
            while True:
                # Ask the customer if they would like to order anything else
                keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

                # Check the customer's input
                if keep_ordering == 'y':
                    # Keep ordering
                    break
                elif keep_ordering == 'n':
                    # Complete the order
                    print("Thank you for your order.")
                    break
                else:
                    # Tell the customer to try again
                    print("I didn't understand your response. Please try again.")
        else:
            print("Invalid pie number. Please try again.")
    else:
        print("Invalid input. Please enter a number.")

    if keep_ordering == 'n':
        break

# Once the pie list is complete
print("-" * 50)
print("You purchased: ")

# Loop through the full pie list
for pie_index, pie_name in enumerate(pie_list):
    pie_count = pie_purchases[pie_index]

    # If the pie count is greater than or equal to 1:
    if pie_count >= 1:
        # Gather the count of each pie in the pie list and print them alongside the pies
        print(f"{pie_count} {pie_name} Pie")



        ## Adding something else 
