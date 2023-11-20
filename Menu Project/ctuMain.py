from ctuClass import ctuStock

# Create four objects representing the four shops
shop1 = ctuStock()
shop2 = ctuStock()
shop3 = ctuStock()
shop4 = ctuStock()

# Define some stock and price for each shop
shop1_stock = {"item1": 10, "item2": 20, "item3": 30, "item1_price": 40, "item2_price": 89, "item3_price": 90}
shop2_stock = {"item1": 5, "item2": 10, "item3": 15, "item1_price": 45, "item2_price": 79, "item3_price": 99}
shop3_stock = {"item1": 2, "item2": 4, "item3": 6, "item1_price": 35, "item2_price": 88, "item3_price": 70}
shop4_stock = {"item1": 8, "item2": 16, "item3": 24, "item1_price": 87, "item2_price": 9, "item3_price": 20}

# Set the initial stock for each shop
shop1.stock = shop1_stock
shop2.stock = shop2_stock
shop3.stock = shop3_stock
shop4.stock = shop4_stock

# Main menu
while True:
    print("\nWelcome to CTU Technologies\n")
    print("\nMain Menu\n")
    print("1. Shop Management")
    print("2. Sales")
    print("3. Returns")
    print("4. Stock")
    print("99. Exit")
    option = input("\nEnter option or 99 to exit: ")

    if option == "1":
        # Shop management submenu
        print("\nShop Management")
        print("1. Change shop Name")
        print("2. Change shop location")
        print("3. Display current shops")
        print("4. Display all shops information")
        print("0. Back")
        sub_option = input("\nEnter option or 0 to go back: ")

        if sub_option == "1":
            # Change shop name
            print("\nCurrent shop names:")
            print("1. " + shop1.shopName + ", " + shop1.shopLocation)
            print("2. " + shop2.shopName + ", " + shop2.shopLocation)
            print("3. " + shop3.shopName + ", " + shop3.shopLocation)
            print("4. " + shop4.shopName + ", " + shop4.shopLocation)
            
            shop_num = int(input("\nEnter shop number to change name: "))
            new_name = input("\nEnter new shop name: ")

            if (shop_num == 1) and (len(new_name)>0):
                shop1.shopName = new_name
                print("\nShop Name successfully changed to: " + new_name)
            elif (shop_num == 2) and (len(new_name)>0):
                shop2.shopName = new_name
                print("\nShop Name successfully changed to: " + new_name)
            elif (shop_num == 3) and (len(new_name)>0):
                shop3.shopName = new_name
                print("\nShop Name successfully changed to: " + new_name)
            elif (shop_num == 4) and (len(new_name)>0):
                shop4.shopName = new_name
                print("\nShop Name successfully changed to: " + new_name)
            else:
                print("\nInvalid shop number or name")

        elif sub_option == "2":
            # Change shop location
            print("\nCurrent shop locations:")
            print("1. " + shop1.shopName + ", " + shop1.shopLocation)
            print("2. " + shop2.shopName + ", " + shop2.shopLocation)
            print("3. " + shop3.shopName + ", " + shop3.shopLocation)
            print("4. " + shop4.shopName + ", " + shop4.shopLocation)
            
            shop_num = int(input("\nEnter shop number to change location: "))
            valid_local = ["Free State", "Gauteng", "KZN", "Limpopo", "Default"]
            new_location = input("\nEnter new shop location [Free State, Gauteng, KZN, Limpopo, Default]: ")
            isvalidlocal = False
            for x in valid_local:
                if x == new_location:
                    isvalidlocal = True
            
            if (shop_num == 1) and (isvalidlocal == True):
                shop1.shopLocation = new_location
                print("\nShop Location changed to: " + new_location)
            elif  (shop_num == 2) and (isvalidlocal == True):
                shop2.shopLocation = new_location
                print("\nShop Location changed to: " + new_location)
            elif  (shop_num == 3) and (isvalidlocal == True):
                shop3.shopLocation = new_location
                print("\nShop Location changed to: " + new_location)
            elif (shop_num == 4) and (isvalidlocal == True):
                shop4.shopLocation = new_location
                print("\nShop Location changed to: " + new_location)
            else:
                print("\nInvalid shop Location")

        elif sub_option == "3":
            # Display current shops
            print("\nCurrent shops:")
            print("1. " + shop1.shopName + ", " + shop1.shopLocation)
            print("2. " + shop2.shopName + ", " + shop2.shopLocation)
            print("3. " + shop3.shopName + ", " + shop3.shopLocation)
            print("4. " + shop4.shopName + ", " + shop4.shopLocation)
        
        elif sub_option == "4":
            #Display all shops information
            print("\n---------------------\n")

            print("Shop Name: " + shop1.shopName)
            print("Shop Location: " + shop1.shopLocation)
            print("Number of Customers: ", + shop1.customers)
            print("Current Sales: ", + shop1.sales)
            print("Returns: ", + shop1.returns)

            print("\n---------------------\n")
            print("\n---------------------\n")

            print("Shop Name: " + shop2.shopName)
            print("Shop Location: " + shop2.shopLocation)
            print("Number of Customers: ", + shop2.customers)
            print("Current Sales: ", + shop2.sales)
            print("Returns: ", + shop2.returns)

            print("\n---------------------\n")
            print("\n---------------------\n")

            print("Shop Name: " + shop3.shopName)
            print("Shop Location: " + shop3.shopLocation)
            print("Number of Customers: ", + shop3.customers)
            print("Current Sales: ", + shop3.sales)
            print("Returns: ", + shop3.returns)

            print("\n---------------------\n")
            print("\n---------------------\n")

            print("Shop Name: " + shop4.shopName)
            print("Shop Location: " + shop4.shopLocation)
            print("Number of Customers: ", + shop4.customers)
            print("Current Sales: ", + shop4.sales)
            print("Returns: ", + shop4.returns)

            print("\n---------------------\n")
            print("\n---------------------\n")
        #return to main menu
        elif sub_option == "0":
            print("Returning to Main menu\n")



    elif option == "2":
        # Display items available to sell
        print("\nItems Available to Sell")
        print("1. item1")
        print("2. item2")
        print("3. item3")
        item_num = int(input("\nEnter item number to sell: "))

        # Prompt user for number of items bought and shop selection
        num_items = int(input("Enter number of items bought: "))
        print("\nAvailable shops:")
        print("1. " + shop1.shopName + " - " + shop1.shopLocation)
        print("2. " + shop2.shopName + " - " + shop2.shopLocation)
        print("3. " + shop3.shopName + " - " + shop3.shopLocation)
        print("4. " + shop4.shopName + " - " + shop4.shopLocation)
        shop_num = int(input("\nEnter shop number to buy from: "))

        # Update shop information based on sale
        if item_num == 1:
            if shop_num == 1:
                shop1.customers += 1
                shop1.sales += num_items
                shop1.stock["item1"] -= num_items
            elif shop_num == 2:
                shop2.customers += 1
                shop2.sales += num_items
                shop2.stock["item1"] -= num_items
            elif shop_num == 3:
                shop3.customers += 1
                shop3.sales += num_items
                shop3.stock["item1"] -= num_items
            elif shop_num == 4:
                shop4.customers += 1
                shop4.sales += num_items
                shop4.stock["item1"] -= num_items
            else:
                print("\nInvalid shop number")
        elif item_num == 2:
            if shop_num == 1:
                shop1.customers += 1
                shop1.sales += num_items
                shop1.stock["item2"] -= num_items
            elif shop_num == 2:
                shop2.customers += 1
                shop2.sales += num_items
                shop2.stock["item2"] -= num_items
            elif shop_num == 3:
                shop3.customers += 1
                shop3.sales += num_items
                shop3.stock["item2"] -= num_items
            elif shop_num == 4:
                shop4.customers += 1
                shop4.sales += num_items
                shop4.stock["item2"] -= num_items
            else:
                print("\nInvalid shop number")
        elif item_num == 3:
            if shop_num == 1:
                shop1.customers += 1
                shop1.sales += num_items
                shop1.stock["item3"] -= num_items
            elif shop_num == 2:
                shop2.customers += 1
                shop2.sales += num_items
                shop2.stock["item3"] -= num_items
            elif shop_num == 3:
                shop3.customers += 1
                shop3.sales += num_items
                shop3.stock["item3"] -= num_items
            elif shop_num == 4:
                shop4.customers += 1
                shop4.sales += num_items
                shop4.stock["item3"] -= num_items
            else:
                print("\nInvalid shop number")
        else:
            print("\nInvalid item number")

    elif option == "3":
        # Display items available to return
        print("\nItems Available to Return")
        print("1. item1")
        print("2. item2")
        print("3. item3")
        item_num = int(input("\nEnter item number to Return: "))

        # Prompt user for number of items returned and shop selection
        num_items = int(input("\nEnter number of items returned: "))
        print("\nAvailable shops:")
        print("1. " + shop1.shopName + " - " + shop1.shopLocation)
        print("2. " + shop2.shopName + " - " + shop2.shopLocation)
        print("3. " + shop3.shopName + " - " + shop3.shopLocation)
        print("4. " + shop4.shopName + " - " + shop4.shopLocation)
        shop_num = int(input("\nEnter shop number to make return to: "))

        # Update shop information based on returns
        if item_num == 1:
            if shop_num == 1:
                shop1.returns += num_items
                shop1.sales -= num_items
                shop1.stock["item1"] += num_items
            elif shop_num == 2:
                shop2.returns += num_items
                shop2.sales -= num_items
                shop2.stock["item1"] += num_items
            elif shop_num == 3:
                shop3.returns += num_items
                shop3.sales -= num_items
                shop3.stock["item1"] += num_items
            elif shop_num == 4:
                shop4.returns += num_items
                shop4.sales -= num_items
                shop4.stock["item1"] += num_items
            else:
                print("\nInvalid shop number")
        elif item_num == 2:
            if shop_num == 1:
                shop1.returns += num_items
                shop1.sales -= num_items
                shop1.stock["item2"] += num_items
            elif shop_num == 2:
                shop2.returns += num_items
                shop2.sales -= num_items
                shop2.stock["item2"] += num_items
            elif shop_num == 3:
                shop3.returns += num_items
                shop3.sales -= num_items
                shop3.stock["item2"] += num_items
            elif shop_num == 4:
                shop4.returns += num_items
                shop4.sales -= num_items
                shop4.stock["item2"] += num_items
            else:
                print("\nInvalid shop number")
        elif item_num == 3:
            if shop_num == 1:
                shop1.returns += num_items
                shop1.sales -= num_items
                shop1.stock["item3"] += num_items
            elif shop_num == 2:
                shop2.returns += num_items
                shop2.sales -= num_items
                shop2.stock["item3"] += num_items
            elif shop_num == 3:
                shop3.returns += num_items
                shop3.sales -= num_items
                shop3.stock["item3"] += num_items
            elif shop_num == 4:
                shop4.returns += num_items
                shop4.sales -= num_items
                shop4.stock["item3"] += num_items
            else:
                print("\nInvalid shop number")
        else:
            print("\nInvalid item number")

    elif option == "4" :
        # Display stock option and add stock option
        print("1. Display stock")
        print("2. Add Stock")
        print("0. Back")
        sub_option = input("\nEnter an option:")
        # Display items available to upate price and stock
        if sub_option == ("1"):
            print(shop1.shopName, "item1:", shop1_stock["item1"], "price:", shop1_stock["item1_price"], "item2:", shop1_stock["item2"], "price:", shop1_stock["item2_price"],  "item3:", shop1_stock["item3"], "price:", shop1_stock["item3_price"])
            print(shop2.shopName, "item1:", shop2_stock["item1"], "price:", shop2_stock["item1_price"], "item2:", shop2_stock["item2"], "price:", shop2_stock["item2_price"],  "item3:", shop2_stock["item3"], "price:", shop2_stock["item3_price"])
            print(shop3.shopName, "item1:", shop3_stock["item1"], "price:", shop3_stock["item1_price"], "item2:", shop3_stock["item2"], "price:", shop3_stock["item2_price"],  "item3:", shop3_stock["item3"], "price:", shop3_stock["item3_price"])
            print(shop4.shopName, "item1:", shop4_stock["item1"], "price:", shop4_stock["item1_price"], "item2:", shop4_stock["item2"], "price:", shop4_stock["item2_price"],  "item3:", shop4_stock["item3"], "price:", shop4_stock["item3_price"])
        elif sub_option == ("2"):
            # Display shops available to update price and stock
            print("\nAvailable shops:")
            print("1. " + shop1.shopName + " - " + shop1.shopLocation)
            print("2. " + shop2.shopName + " - " + shop2.shopLocation)
            print("3. " + shop3.shopName + " - " + shop3.shopLocation)
            print("4. " + shop4.shopName + " - " + shop4.shopLocation)
        
        

            shop_num = int(input("\nSelect shop to add stock to: "))

            print("\nItems Available to add stock and/or update price")
            print("1. item1")
            print("2. item2")
            print("3. item3")

            item_num = int(input("\nSelect item number to add stock to: \n"))            
            num_items = int(input("\nAmount of stock to add: \n"))

            item_price = int(input("\nItem Price: "))
             # Update shop stock and price
            if item_num == 1:
                if shop_num == 1:
                    shop1.stock["item1"] += num_items
                    shop1.stock["item1_price"] = item_price
                elif shop_num == 2:
                    shop2.stock["item1"] += num_items
                    shop2.stock["item1_price"] = item_price
                elif shop_num == 3:
                    shop3.stock["item1"] += num_items
                    shop3.stock["item1_price"] = item_price
                elif shop_num == 4:
                    shop4.stock["item1"] += num_items
                    shop4.stock["item1_price"] = item_price
                else:
                    print("\nInvalid shop number")
            elif item_num == 2:
                if shop_num == 1:
                    shop1.stock["item2"] += num_items
                    shop1.stock["item2_price"] = item_price
                elif shop_num == 2:
                    shop2.stock["item2"] += num_items
                    shop2.stock["item2_price"] = item_price
                elif shop_num == 3:
                    shop3.stock["item2"] += num_items
                    shop3.stock["item2_price"] = item_price
                elif shop_num == 4:
                    shop4.stock["item2"] += num_items
                    shop4.stock["item2_price"] = item_price
                else:
                    print("\nInvalid shop number")
            elif item_num == 3:
                if shop_num == 1:
                    shop1.stock["item3"] += num_items
                    shop1.stock["item3_price"] = item_price
                elif shop_num == 2:
                    shop2.stock["item3"] += num_items
                    shop2.stock["item3_price"] = item_price
                elif shop_num == 3:
                    shop3.stock["item3"] += num_items
                    shop3.stock["item3_price"] = item_price
                elif shop_num == 4:
                    shop4.stock["item3"] += num_items
                    shop4.stock["item3_price"] = item_price
                else:
                    print("\nInvalid shop number")
            else:
                print("\nInvalid item number")
    #closing the application
    elif option == "99":
        print("\nApplication Closed.\n")
        exit()
    #Stops invalid selections from closing program
    else:
        print("\nInvalid selection\n")