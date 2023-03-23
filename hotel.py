import datetime
print("    WELCOME TO BANIYA HOTEL    ")
print("DO YOU WANT TO CHECK IN OR ORDER FOOD ?")
bill=0
choice=input("checkin/order food:    ")
if (choice=="checkin"):
    # NO OF PEOPLE
    print("HOW MANY PEOPLE WANT TO STAY ?")
    male=int(input("ENTER THE NO. OF ADULT MALES: "))
    female=int(input("ENTER THE NO. OF ADULT FEMALES: "))
    children=int(input("ENTER THE NO. OF CHILDREN: "))
    total=male+female+children
    # NO OF ROOMS
    ch=int(input("ENTER THE NO. OF ROOMS"))
    if (total==1) and (ch==1): 
        if ch>1:
            print("NOT AVAILABLE")
        print("""          ##OUR SERVICES##
                     ECONOMICAL     500/- per night
                     GENRAL         800/- per night
                     PREMIUM        2000/- per night
                     """)
        select=input("CHOOSE YOUR SERVICE: ")
        select.lower()
        if select=="economical":
            stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
            bill=+stay*500
            print(bill)
        elif select=="genral":
            stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
            bill=+stay*800
            print(bill)
        elif select=="premium":  
            stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
            bill=+stay*2000
            print(bill)
        else:
            pass 
    elif (total==2) and (ch==1):
        print("YOU SELECTED SINGLE ROOM")
        bed=input("YOU WANT SINGLE BED OR DOUBLE:  ")
        bed.lower()
        if (bed=="single"):
            print("""      ##OUR SERVICES##
                     ECONOMICAL     1000/- per night
                     GENRAL         2000/- per night
                     PREMIUM        5000/- per night
                     """)
            select=input("CHOOSE YOUR SERVICE: ")
            select.lower()
            if select=="economical":
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*1000
                print(bill)
            elif select=="genral":
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*2000
                print(bill)
            elif select=="premium":  
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*5000
                print(bill)
            else:
                pass
        elif (bed=="double"):
            print("""OUR SERVICES 
                     ECONOMICAL     800/- per night
                     GENRAL         1500/- per night
                     PREMIUM        3000/- per night
                     """)
            select=input("CHOOSE YOUR SERVICE: ")
            select.lower()
            if select=="economical":
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*800
                print(bill)
            elif select=="genral":
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*1500
                print(bill)
            elif select=="premium":  
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*3000
                print(bill)
            else:
                pass
        else:
            pass