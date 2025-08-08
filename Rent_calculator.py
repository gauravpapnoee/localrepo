n = int(input("enter the number of roommates"))
total_rent = 0
value = True
while value:
    bill_amt = int(input("enter the amount of bill"))
    total_rent += bill_amt
    check = input('any other rent you pay? (yes or no)')
    if check == "yes":
        value = True
    else :
        value = False
print(f"the total rent of your team is {total_rent}")
print(f"the amount pay by one person is {total_rent/n}" )
print("Thank you for using this program !")