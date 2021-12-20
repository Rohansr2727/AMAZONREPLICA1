dress = [{"id": 1001,"Name": "Tops",  "Manefactuarers_Name":"adid","Available": 101, "Price": 250, "Discount": 20},
         {"id": 1002,"Name": "Pants", "Manefactuarers_Name":"puma","Available": 121, "Price": 500, "Discount": 45},
         {"id": 1003,"Name": "Sarees","Manefactuarers_Name":"jioo","Available": 100, "Price": 750, "Discount": 70},
         {"id": 1004,"Name": "Shorts","Manefactuarers_Name":"bata","Available": 201, "Price": 350, "Discount": 30},
         {"id": 1005,"Name": "Kurtas","Manefactuarers_Name":"siya","Available": 151, "Price": 400, "Discount": 30}]
dress1 = dress
temp = []
order = ""


def adminLogin():
    print("*********************")
    print("1.view order details")
    print("2.create a product")
    print("3.delete product")
    print("4.update product")
    print("5.view order list")
    print("6.Logout")
    print("*********************")


def adminDisplayMenu():
    print("Id\tName\tManefactuarers_Name\tAvailable\tPrice\tDiscount")
    print("***************************************************")
    for d in dress:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Manefactuarers_Name"]}\t{d["Available"]}\t{d["Price"]}\t{d["Discount"]}')


def addItem():
    n = int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_Name = input("Enter Name: ")
        new_Manefactuarers_Name=input("Enter Manefactuarers Name")
        new_Available = int(input("Enter Available : "))
        new_Price = int(input("Enter Price : "))
        new_original = int(input("Enter the Discount : "))
        d = [{"id": new_id, "Name": new_Name,"Manefactuarers_Name":new_Manefactuarers_Name, "Available": new_Available, "Price": new_Price,
              "Discount": new_original}]
        dress.extend(d)
        adminDisplayMenu()


def removeItem():
    dressId = int(input("Enter the id need to be deleted : "))
    found = False
    for d in dress1:
        found = d["id"] == dressId
        if found != True:
            temp.append(d)
            continue
        if found == True:
            d["Available"] -= 1
    print("Deleting item....")
    if len(temp) == d:
        print(f"{dressId} not found")
    else:
        print(f"{dressId}'s one available is removed from the list")
    adminDisplayMenu()


def Total_product():
    Total = 0
    print("\n")
    for d in dress:
        print(f'{d["Name"]} = {d["Available"]}')
    Total += (d["Available"])
    print("\nTotal available product is : ", Total)

def update_product(self,id,Name,Manefactuarers_Name,Availabel,price,Discount):
    self.id=id
    self.Name=Name
    self.Manefactuarers_name=Manefactuarers_Name
    self.Availabel=Availabel
    self.price=price
    self.Discount=Discount






def logout():
    login()


def adminChoice():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        adminDisplayMenu()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice == 2:
        adminDisplayMenu()
        print("\n***************************************************\n")
        addItem()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice == 3:
        adminDisplayMenu()
        print("\n***************************************************\n")
        removeItem()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()
    elif choice == 4:
        update_product()
    elif choice==5:
        adminDisplayMenu()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()

    elif choice == 6:
        logout()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminChoice()


def MemberLogin():
    print("*********************\n")
    print("1.view order history")
    print("2.create new order")
    print("3.Cancel order")
    print("4.Logout")
    print("\n*********************")


def MemberDisplayMenu():
    print("Id\tName\tAvailable\tPrice")
    print("***************************************************")
    for d in dress:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')


def Member_id():
    MemberDisplayMenu()
    p_id = int(input("\nEnter the id : "))


def placeOrder():
    order_number = 10
    MemberDisplayMenu()
    p_id = int(input("\nEnter the id : "))

    for d in dress:
        if d["id"] == p_id:
            print("\nId\tName\tManefactuarers_Name\tAvailable\tPrice")
            print("***************************************************")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            order = '{d["id"]}\t{d["Manefactuarers_Name"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                order_number += 1
                print("Your order number is : ", order_number)
                d["Available"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        Member_id()
    print("\nAvailable products : \n")
    MemberDisplayMenu()


def cancelOrder():
    found = False
    temp = []
    order_id = input("Enter the order id : ")
    for d in dress:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')


def MemberChoice():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        login()
    elif choice == 2:
        placeOrder()
        print("\n***************************************************\n")
        MemberLogin()
        print("\n***************************************************\n")
        MemberChoice()
    elif choice == 3:
        cancelOrder()
        print("\n***************************************************\n")
        MemberLogin()
        print("\n***************************************************\n")
        MemberChoice()
    elif choice == 4:
        logout()
    else:
        print("Invalid Choice. Please enter valid choice")


def login():
    tp = input("Admin/Member [A/M] : ")
    if tp == 'A' or tp == 'a':
        username= input("Enter the username")
        password = input("Enter the password : ")
        if password == "admin" and username== "admin":
            adminLogin()
            adminChoice()
        else:
            print("Invalid password. Please enter valid password")

    elif tp == 'M' or tp == 'm':
        Name= input("Enter the NAme")
        Email=input("Enter the Email")
        Adress =input("Enter the Adress")
        print(Name,Adress,Email,)
        password = input("Enter the password : ")
        if (password == password):
            MemberLogin()
            MemberChoice()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")


login()






