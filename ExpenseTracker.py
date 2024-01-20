#EXPENSE TRACKER
Expense_tracker={"categories":[],"expenses":[]}

def addcategory():
    name=input("Enter the category u want to add:").lower()
    if name not in Expense_tracker["categories"]:
        Expense_tracker["categories"].append(name)
        print("Category is added successfully to the tracker")
    else:
        print("This category already exits..")

def addexpense():
    #enter in which category u want to add expenses
    name=input("Enter the category name to add expense.:").lower()
    if name in Expense_tracker["categories"]:
        amount=float(input("Enter expenses for this category:"))
        date_of_expense=input("Enter expense date(YYYY-MM-DD):")
        Expense_tracker["expenses"].append({"category":name,"amount":amount,"date":date_of_expense})
        print("Expenses added successfully to the respective category")
    else:
        print("Category is not found..Please add category first.")
        
def viewspendingpattern():
    if not Expense_tracker["expenses"]:
        print("No expenses recorded.")
        return

    Total_expense={}#total expense spend in each category
    for expense in Expense_tracker["expenses"]:
        category=expense["category"]
        amount=expense["amount"]
        Total_expense[category]=Total_expense.get(category,0)+amount#gets the current total of the category if not 0 will be added

        print("SPENDING PATTERN...")
        for category,total in Total_expense.items():
            print(f"{category}:{total}")


def viewexpense():
    if not Expense_tracker["expenses"]:
        print("No expenses recorded.")
        return
    print("Your Expenses:")
    for i,expense in enumerate(Expense_tracker["expenses"],start=1):
        category=expense["category"]
        amount=expense["amount"]
        date=expense["date"]
        print(f"{i}.Category:{category},Amount:{amount},Date:{date}")

def main():
    while True:
        print("\n1.ADD CATEGORY\n2.ADD EXPENSES\n3.VIEW SPENDING PATTERN\n4.VIEW EXPENSE\n5.QUIT")
        choice=input("Enter your choice:")

        if choice=="1":
            addcategory()
        elif choice=="2":
            addexpense()
        elif choice=="3":
            viewspendingpattern()
        elif choice=="4":
            viewexpense()
        elif choice=="5":
            print("Bye..Existing expense tracker")
            return
        else:
            print("Please choose valid choice..")

if __name__=="__main__":
    main()
