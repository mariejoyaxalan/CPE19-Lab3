print("======================================")
print("        Gadget Purchasing System")
print("======================================")
print("Hi, good day! Welcome to our store. \nKindly fill up the form below:")
print("")

name = str(input("Name     : "))
age = int(input("Age      : "))
add = str(input("Address  : "))

print("")
print("======================================")
print("      Available Gadgets for Sale")
print("======================================")
print("1. Mobile Phone")
print("2. Laptop")
print("")
typ = int(input("Choose the number of your choice: "))

if typ == 1:
    print("")
    print("======================================")
    print("    Mobile Phone Operating System")
    print("======================================")
    print("1. Android")
    print("2. iOS")
    print("")
    os = int(input("Choose the number of your choice: "))
    
    
    if os == 1:
        ost = "Android"
        print("======================================")
        print("      Android Memory Capacity")
        print("======================================")
        print("1. 4GB RAM; 64GB ROM")
        print("2. 4GB RAM; 128GB ROM")
        print("3. 6GB RAM; 64GB ROM")
        print("4. 6GB RAM; 128GB ROM")
        print("")
        memr = int(input("Choose the number of your choice: "))
        
        if memr == 1:
            memrt = "4GB RAM; 64GB ROM"
            price = "8,489.00"
            print("======================================")
            print("                Color")
            print("======================================")
            print("1. Shadow Black")
            print("2. Frost White")
            print("3. Aqua Green")
            print("")
            colr = int(input("Choose the number of your choice: "))
            
            if colr == 1:
                colort = "Shadow Black"
            elif colr == 2:
                colort = "Frost White"
            elif colr == 3:
                colort = "Aqua Green"
            else:
                print("Invalid input, please try again.")
        
        elif memr == 2:
            memrt = "4GB RAM; 128GB ROM"
            price = "9,599.00"
            print("======================================")
            print("                Color")
            print("======================================")
            print("1. Shadow Black")
            print("2. Frost White")
            print("3. Aqua Green")
            print("")
            colr = int(input("Choose the number of your choice: "))
            
            if colr == 1:
                colort = "Shadow Black"
            elif colr == 2:
                colort = "Frost White"
            elif colr == 3:
                colort = "Aqua Green"
            else:
                print("Invalid input, please try again.")
        
        elif memr == 3:
            memrt = "6GB RAM; 64GB ROM"
            price = "10,489.00"
            print("======================================")
            print("                Color")
            print("======================================")
            print("1. Shadow Black")
            print("2. Frost White")
            print("3. Aqua Green")
            print("")
            colr = int(input("Choose the number of your choice: "))
            
            if colr == 1:
                colort = "Shadow Black"
            elif colr == 2:
                colort = "Frost White"
            elif colr == 3:
                colort = "Aqua Green"
            else:
                print("Invalid input, please try again.")
            
        elif memr == 4:
            memrt = "6GB RAM; 128GB ROM"
            price = "11,599.00"
            print("======================================")
            print("                Color")
            print("======================================")
            print("1. Shadow Black")
            print("2. Frost White")
            print("3. Aqua Green")
            print("")
            colr = int(input("Choose the number of your choice: "))
            
            if colr == 1:
                colort = "Shadow Black"
            elif colr == 2:
                colort = "Frost White"
            elif colr == 3:
                colort = "Aqua Green"
            else:
                print("Invalid input, please try again.")
            
        else:
            print("Invalid input, please try again.")

        print("")
        print("======================================")
        print("Wonderful choice! \nHere's the summary of your order:")
        print("======================================")
        print("Name: {}" .format(name))
        print("Address: {}" .format(add))
        print(" ")
        print("Mobile Phone : {}" .format(ost))
        print("Color: {}" .format(colort))
        print("Display: Super AMOLED")
        print("Memory: {}" .format(memrt))
        print("Camera: 48 MP")
        print("Battery: Li-Po 5000 mAh")
        print("======================================")
        print("Total Price: ₱{}" .format(price))
        print("======================================")
       
    elif os == 2:
        ost = "iOS"
        print("======================================")
        print("      iOS Memory Capacity")
        print("======================================")
        print("1. 6GB RAM; 128GB ROM")
        print("2. 6GB RAM; 256GB ROM")
        print("3. 6GB RAM; 512GB ROM")
        print("")
        memr = int(input("Choose the number of your choice: "))
        
        if memr == 1:
            memrt = "6GB RAM; 128GB ROM"
            price = "50,990.00"
            print("======================================")
            print("                Color")
            print("======================================")
            print("1. Graphite")
            print("2. Gold")
            print("3. Silver")
            print("")
            colr = int(input("Choose the number of your choice: "))
            
            if colr == 1:
                colort = "Graphite"
            elif colr == 2:
                colort = "Gold"
            elif colr == 3:
                colort = "Silver"
            else:
                print("Invalid input, please try again.")
            
        elif memr == 2:
            memrt = "6GB RAM; 256GB ROM"
            price = "57,990.00"
            print("======================================")
            print("                Color")
            print("======================================")
            print("1. Graphite")
            print("2. Gold")
            print("3. Silver")
            print("")
            colr = int(input("Choose the number of your choice: "))
            
            if colr == 1:
                colort = "Graphite"
            elif colr == 2:
                colort = "Gold"
            elif colr == 3:
                colort = "Silver"
            else:
                print("Invalid input, please try again.")
        
        elif memr == 3:
            memrt = "6GB RAM; 512GB ROM"
            price = "69,990.00"
            print("======================================")
            print("                Color")
            print("======================================")
            print("1. Graphite")
            print("2. Gold")
            print("3. Silver")
            print("")
            colr = int(input("Choose the number of your choice: "))
            
            if colr == 1:
                colort = "Graphite"
            elif colr == 2:
                colort = "Gold"
            elif colr == 3:
                colort = "Silver"
            else:
                print("Invalid input, please try again.")

        else:
            print("Invalid input, please try again.")

        print("")
        print("======================================")
        print("Wonderful choice! \nHere's the summary of your order:")
        print("======================================")
        print("Name: {}" .format(name))
        print("Address: {}" .format(add))
        print(" ")
        print("Mobile Phone : {}" .format(ost))
        print("Color: {}" .format(colort))
        print("Display: Super Retina XDR OLED")
        print("Memory: {}" .format(memrt))
        print("Camera: 12 MP")
        print("Battery: Li-Ion 4373 mAh")
        print("======================================")
        print("Total Price: ₱{}" .format(price))
        print("======================================")
            
    else:
        print("Invalid input, please try again.")
    
elif typ == 2:
    print("")
    print("======================================")
    print("      Laptop Operating System")
    print("======================================")
    
else:
    print("Invalid input, please try again.")

print("")
conf = str(input("Do you want to confirm? (Y/N): "))
if conf == "Y" or conf == "y":
    print("")
    print("Thank you for purchasing, {}. \nHave a nice day!" .format(name))
elif conf == "N" or conf == "n":
    print("")
    print("Ok.")