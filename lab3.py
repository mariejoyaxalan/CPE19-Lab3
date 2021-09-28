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
    print("1. Windows")
    print("2. macOS")
    print("")
    lapos = int(input("Choose the number of your choice: "))
    
    
    if lapos == 1:
        lapost = "Windows"
        print("======================================")
        print("      Windows Memory Capacity")
        print("======================================")
        print("1. 4GB RAM; 512GB Hard Disk")
        print("2. 4GB RAM; 1TB ROM")
        print("3. 8GB RAM; 512GB Hard Disk")
        print("4. 8GB RAM; 1TB ROM")
        print("")
        memr = int(input("Choose the number of your choice: "))
        
        if memr == 1:
            memrt = "4GB RAM; 512GB HArd Disk"
            price = "49,990.00"
            print("======================================")
            print("             Screen Size")
            print("======================================")
            print("1. 14 inches")
            print("2. 15 inches")
            print("3. 17 inches")
            print("")
            ss = int(input("Choose the number of your choice: "))
            
            if ss == 1:
                sst = "14 inches"
            elif ss == 2:
                sst = "15 inches"
            elif ss == 3:
                sst = "16 inches"
            else:
                print("Invalid input, please try again.")
        
        elif memr == 2:
            memrt = "4GB RAM; 1TB Hard Disk"
            price = "54,990.00"
            print("======================================")
            print("              Screen Size")
            print("======================================")
            print("1. 14 inches")
            print("2. 15 inches")
            print("3. 17 inches")
            print("")
            ss = int(input("Choose the number of your choice: "))
            
            if ss == 1:
                sst = "14 inches"
            elif ss == 2:
                sst = "15 inches"
            elif ss == 3:
                sst = "16 inches"
            else:
                print("Invalid input, please try again.")
        
        elif memr == 3:
            memrt = "8GB RAM; 512GB Hard Disk"
            price = "59,990.00"
            print("======================================")
            print("              Screen Size")
            print("======================================")
            print("1. 14 inches")
            print("2. 15 inches")
            print("3. 17 inches")
            print("")
            ss = int(input("Choose the number of your choice: "))
            
            if ss == 1:
                sst = "14 inches"
            elif ss == 2:
                sst = "15 inches"
            elif ss == 3:
                sst = "17 inches"
            else:
                print("Invalid input, please try again.")
            
        elif memr == 4:
            memrt = "8GB RAM; 1TB Hard Disk"
            price = "64,990.00"
            print("======================================")
            print("              Screen Size")
            print("======================================")
            print("1. 14 inches")
            print("2. 15 inches")
            print("3. 17 inches")
            print("")
            ss = int(input("Choose the number of your choice: "))
            
            if ss == 1:
                sst = "14 inches"
            elif ss == 2:
                sst = "15 inches"
            elif ss == 3:
                sst = "17 inches"
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
        print("Laptop OS : {}" .format(lapost))
        print("Screen Size: {}" .format(sst))
        print("Memory: {}" .format(memrt))
        print("Intel: corei7 8th Gen")
        print("SSD: 256 GB")
        print("======================================")
        print("Total Price: ₱{}" .format(price))
        print("======================================")
       
    elif lapos == 2:
        lapost = "macOS"
        print("======================================")
        print("      MacOS Memory Capacity")
        print("======================================")
        print("1. 8GB RAM; 1TB ROM")
        print("2. 16GB RAM; 1TB ROM")
        print("")
        memr = int(input("Choose the number of your choice: "))
        
        if memr == 1:
            memrt = "8GB RAM; 1TB Hard Disk"
            price = "70,990.00"
            print("======================================")
            print("             Screen Size")
            print("======================================")
            print("1. 11 inches")
            print("2. 12 inches")
            print("3. 13 inches")
            print("")
            ss = int(input("Choose the number of your choice: "))
            
            if ss == 1:
                sst = "11 inches"
            elif ss == 2:
                sst = "12 inches"
            elif ss == 3:
                sst = "13 inches"
            else:
                print("Invalid input, please try again.")
            
        elif memr == 2:
            memrt = "16GB RAM; 1TB Hard Disk"
            price = "99,990.00"
            print("======================================")
            print("               Screen Size")
            print("======================================")
            print("1. 11 inches")
            print("2. 12 inches")
            print("3. 13 inches")
            print("")
            ss = int(input("Choose the number of your choice: "))
            
            if ss == 1:
                sst = "11 inches"
            elif ss == 2:
                sst = "12 inches"
            elif ss == 3:
                sst = "13 inches"
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
        print("Laptop OS : {}" .format(lapost))
        print("Screen Size: {}" .format(sst))
        print("Memory: {}" .format(memrt))
        print("Intel: corei7 8th Gen")
        print("SSD: 256 GB")
        print("======================================")
        print("Total Price: ₱{}" .format(price))
        print("======================================")
            
    else:
        print("Invalid input, please try again.")
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