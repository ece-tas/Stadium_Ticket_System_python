# 2210356039
# Ece Nur Taş

from sys import argv

input=argv[1]
output=[]

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp1=[x for x in alphabet]
alp2=[[x] for x in alphabet]     # [['A'], ['B'], ['C'], ...]

category_names=[]
seats=[]
range_seats=[]
category_dict=[]
rows=[]
columns=[]
student=[]
full=[]
season=[]

def create_category():
    create=line.split()
    category_names.append(create[1])

    if category_names.count(create[1])>1:
        print(f"Warning: Cannot create the category for the second time. The stadium has already '{create[1]}'.")
        output.append(f"Warning: Cannot create the category for the second time. The stadium has already '{create[1]}'.")
        create.pop()
        category_names.pop()
    else: 
        x=create[2].find("x")
        row=int(create[2][:x])      #row=int
        rows.append(row)
        column=int(create[2][x+1:]) #column=int
        columns.append(column)
        seats=row*column
        print(f"The category '{create[1]}' having {seats} seats has been created")
        output.append(f"The category '{create[1]}' having {seats} seats has been created")
        ct_dict= {"ct_name": create[1], "row": row, "column": column}             #keeps in dictionary as {"ct_name":category-1A, 'row': 25, 'column': 25}
        category_dict.append(ct_dict)
        
def sell():
    sell = line.split()

    ticket = {"name": sell[1], "t_type": sell[2], "ct_name": sell[3], "seats": sell[4:]}
    for seat in ticket["seats"]:
        if "-" not in seat:
            for key in category_dict:
                if key["ct_name"]==ticket["ct_name"]:                              
                    q = seat         # q = ["C2", "4"]   
                    if int(seat[1:]) > key["column"] and alp1.index(q[0][0])+1 > key["row"]:        #seat[0]=="letter"
                        print("Error: The category {c} has less row and column than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                        output.append("Error: The category {c} has less row and column than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                    elif int(seat[1:]) > key["column"]:
                        print("Error: The category {c} has less column than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                        output.append("Error: The category {c} has less column than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                    elif alp1.index(q[0][0]) +1 > key["row"]:
                        print("Error: The category {c} has less row than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                        output.append("Error: The category {c} has less row than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                    elif int(seat[1:]) <= key["column"] and alp1.index(seat[0]) +1 <= key["row"]:           
                        if seat not in seats:
                            seats.append(seat)
                            range_seats.append(seat)
                            print("Success: {} has bought {} at {}".format(ticket["name"], seat, ticket["ct_name"]))
                            output.append("Success: {} has bought {} at {}".format(ticket["name"], seat, ticket["ct_name"]))
                            break
                        elif seat in seats:
                            print("Error: The seat {s} cannot be sold to {n} due some of them have already been sold!".format(s=seat, n=ticket["name"]))
                            output.append("Error: The seat {s} cannot be sold to {n} due some of them have already been sold!".format(s=seat, n=ticket["name"]))
                            break 
        if "-" in seat:
            for key in category_dict:
                if key["ct_name"]==ticket["ct_name"]:
                    q = seat.split("-")         # q = ["C2", "4"]         
                    if int(q[1]) > key["column"] and alp1.index(q[0][0]) +1 > key["row"]:
                        print("Error: The category {c} has less row and column than the specified index {s}!".format(c=key["ct_name"], s=seat))
                        output.append("Error: The category {c} has less row and column than the specified index {s}!".format(c=key["ct_name"], s=seat))
                    elif int(q[1]) > key["column"]:
                        print("Error: The category {c} has less column than the specified index {s}!".format(c=key["ct_name"], s=seat))
                        output.append("Error: The category {c} has less column than the specified index {s}!".format(c=key["ct_name"], s=seat))
                    elif alp1.index(q[0][0]) +1 > key["row"]:
                        print("Error: The category {c} has less row than the specified index {s}!".format(c=key["ct_name"], s=seat))
                        output.append("Error: The category {c} has less row than the specified index {s}!".format(c=key["ct_name"], s=seat))
                    elif int(q[1]) <= key["column"] and alp1.index(q[0][0]) +1 <= key["row"]:
                        bottom=int(q[0][1:])
                        top=int(q[1]) + 1             
                        for k in range(bottom, top):             
                            k = q[0][0] + str(k)  # k = C2 C3 C4
                            range_seats.append(k)
                            
                        if seat not in seats: 
                            seats.append(seat)
                            print("Success: {n} has bought {s} at {c}".format(n=ticket["name"], s=seat, c=ticket["ct_name"]))
                            output.append("Success: {n} has bought {s} at {c}".format(n=ticket["name"], s=seat, c=ticket["ct_name"]))
                            break
                            
                        elif seat in range_seats:
                            print("Error: The seats {s} cannot be sold to {n} due some of them have already been sold!".format(s=seat, n=ticket["name"]))
                            output.append("Error: The seats {s} cannot be sold to {n} due some of them have already been sold!".format(s=seat, n=ticket["name"]))
                            break
    if ticket["t_type"]=="student":
        student.append(ticket["name"])
    if ticket["t_type"]=="full":
        full.append(ticket["name"])
    if ticket["t_type"]=="seasons":
        season.append(ticket["name"])

def cancel():
    cancel=line.split()
    ticket={"ct_name":cancel[1],"seats":cancel[2:]}
    for seat in ticket["seats"]:
       
        for key in category_dict:
                if key["ct_name"]==ticket["ct_name"]:
                    if int(seat[1]) > key["column"] and alp1.index(seat[0][0]) +1 > key["row"]:
                        print("Error: The category '{c}' has less row and column than the specified index {s}!".format(c=key["ct_name"], s=seat))
                        output.append("Error: The category '{c}' has less row and column than the specified index {s}!".format(c=key["ct_name"], s=seat))
                    elif int(seat[1:]) > key["column"]:
                        print("Error: The category '{c}' has less column than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                        output.append("Error: The category '{c}' has less column than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                    elif alp1.index(seat[0][0]) +1 > key["row"]:
                        print("Error: The category '{c}' has less row than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                        output.append("Error: The category '{c}' has less row than the specified index {s}!".format(c=ticket["ct_name"], s=seat))
                    elif int(seat[1:]) <= key["column"] and alp1.index(seat[0]) +1 <= key["row"]:
                        for x in range_seats:
                            if seat in range_seats:   
                                print(f"Success: The seat {x} at ’{ticket['ct_name']}’ has been canceled and now ready to sell again")
                                output.append(f"Success: The seat {x} at ’{ticket['ct_name']}’ has been canceled and now ready to sell again")
                                range_seats.remove(x)
                                break
                            if seat not in range_seats:
                                print(f"Error: The seat {seat} at ’{ticket['ct_name']}’ has already been free! Nothing to cancel")
                                output.append(f"Error: The seat {seat} at ’{ticket['ct_name']}’ has already been free! Nothing to cancel")
                                break

def show():
    show=line.split()
    ticket={"ct_name":show[1]}
    print(f"Printing category layout of {ticket['ct_name']}")
    output.append(f"Printing category layout of {ticket['ct_name']}")
    

def balance():
    balance=line.split()
    ticket={"ct_name":balance[1]}
    print("Category report of '{c}'".format(c=ticket['ct_name']))
    print("--------------------------------")
    output.append("Category report of '{c}'".format(c=ticket['ct_name']))
    output.append("--------------------------------")
    Revenue=len(student)*10+len(full)*20+len(season)*250
    print(f"Sum of students = {len(student)}, Sum of full pay = {len(full)}, Sum of season ticket = {len(season)},  and Revenues = {Revenue} Dollars")
    output.append(f"Sum of students = {len(student)}, Sum of full pay = {len(full)}, Sum of season ticket = {len(season)},  and Revenues = {Revenue} Dollars")
# python assignment3.py input.txt
with open (input,"r") as f:
    global line
    for line in f:
        if line[0:14] == "CREATECATEGORY":
            create_category()
        elif line[0:10]== "SELLTICKET":
            sell()
        elif line[:12]== "CANCELTICKET":
            cancel()
        elif line[:12]=="SHOWCATEGORY":
            show()
        elif line[:7]=="BALANCE":
            balance()

def outputs():
    with open("output.txt", "w") as file:
        for lines in output:
            file.write(lines + "\n")
outputs()





