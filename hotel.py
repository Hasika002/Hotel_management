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
    # NO OF ROOM
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
            #bed requirements added
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
                #bill added
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
                #hasika contribution
	elif (total>2) and (ch>=1): 
        bed=input("YOU WANT SINGLE BED OR DOUBLE:  ")
        if (bed=="single"):
            print("""      ##OUR SERVICES##
                     ECONOMICAL     1000/- per night,per person
                     GENRAL         2000/- per night,per person
                     PREMIUM        5000/- per night,per person
                     """)
            select=input("CHOOSE YOUR SERVICE: ")
            select.lower()
            if select=="economical":
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*male*1000+stay*female*1000+stay*children*1000
                print(bill)
            elif select=="genral":
                #general added
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*male*2000+stay*female*2000+stay*children*2000
                print(bill)
            elif select=="premium":  
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*male*5000+stay*female*5000+stay*children*5000
                print(bill)
            else:
                pass
        elif (bed=="double"):
            print("""OUR SERVICES 
                     ECONOMICAL     800/- per night,per person
                     GENRAL         1500/- per night,per person
                     PREMIUM        3000/- per night,per person
                     """)
            select=input("CHOOSE YOUR SERVICE: ")
            select.lower()
            if select=="economical":
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*male*800+stay*female*800+stay*children*800
                print(bill)
            elif select=="genral":
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*male*1500+stay*female*1500+stay*children*1500
                print(bill)
            elif select=="premium":  
                stay=int(input("ENTER THE NO. OF DAYS OF STAY: "))
                bill=+stay*male*3000+stay*female*3000+stay*children*3000
                print(bill)
            else:
                pass
                else:
                sum_total=0
                print("                 M_E_N_U_E                       ")
                print("""           ### CHINESE ###

    Hakka Noodles          हक्का नूडल्स       120/-          1

    Veg Choumin            वेज चाउमिन        110/-          2

    Veg Noodles            वेज नूडल्स          110/-          3

    Veg Chopsuey           वेज चोपसी         140/-           4   

    Veg Fried Rice         वेज फ्राइड राइस     105/-           5

    Veg Kofte              वेज कोथे           125/-           6

    Veg Manchurian Dry     वेज मंचूरियन ड्राय     140/-           7

    Veg Manchurian GREAVY  वेज मंचूरियन ग्रेवी     120/-            8

    Chilli Paneer Dry      चिल्ली पनीर ड्राय      140/-           9

    Chilli Paneer GREAVY   चिल्ली पनीर ग्रेवी      140/-            10

    Paneer Manchurian      पनीर मंचूरियन       135/-             11

    Chinese Bhel          चायनीस गेल         135/-              12

    Gobhi Chili            गोभी चिल्ली         140/-              13

    Gobhi Manchurian       गोभी मंचूरियन       125/-              14

    Paneer Tikka Dry       पनीर टिक्का ड्राय     125/-              15

    Manchurian Noodles     मंचूरियन नूडल्स      175/-              16

    Veg Sizler             वेज सिज़्लर         175/-               17

    Chana chili Dry        चना चिल्ली ड्राय      125/-               18

    Hani Batato            हनी बाते           240/-               19

    Veg MOMOSs             वेज मोमोस         130/-               20

    *** TO EXIT PRESS 900 ***
    """)
    #cahar commited
            n_a=[1,3,7,8,19]
            chinease={1:120, 2:110, 3:110, 4:140, 5:105, 6:125, 7:140, 8:120, 9:140, 10:140, 11:135, 12:135, 13:140, 14:125, 15:125, 16:175, 17:175, 18:125, 19:240, 20:130}
            while (choice!=0):
                order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
                if order in n_a:
                    print("SORRY THE ITEM IS UNAVALIBLE")
                elif order==900:
                     break
                elif (order>len(chinease)):
                    print("PLEASE ENTER FROM THE MENUE")    
                else:
                    qat=int(input("ENTER THE NO. OF ORDERS: "))
                    sum_total=sum_total+(chinease[order]*qat)
                    print("YOUR BILL IS:",sum_total)