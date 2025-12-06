# Expense tracker

expensesList = []
print("\nWelcome To Expense Tracker : Please Spend Mindfully")

while True : 
    print("======== MENU ========")
    print("1. Add New Expense ")
    print("2. View All Expenses")
    print("3. View total Spent")
    print("4. Exit ")
    print("======================")

    choice = int(input("\nPlease Enter Your Choice : "))

    # add expense
    if (choice == 1) :
        date = input("Today's Date? : ")
        category = input("Category? (Food, Travel, Books....) : ")
        discription = input("A Short Discription : ")
        amount = float(input("Enter The Amount : "))

        expense = {

            "date" : date,
            "category" : category,
            "discription" : discription,
            "amount" : amount
        }
        
        expensesList.append(expense)
        print("\nExpense Added Successfully!!")

    # view all expense
    elif(choice == 2) :
        if (len(expensesList) == 0 ):
            print("No Amount Spend!!!")

        else :
            print("==== Here's Everything You spent! ====")
            count = 1
            for eachexpense in expensesList :
                print(f"\nExpense Number {count} -> Date : {eachexpense["date"]}, \n\t\t    What You Spent on : {eachexpense["category"]}, \n\t\t    Discription : {eachexpense["discription"]}, \n\t\t    How Much You Spent : {eachexpense["amount"]} ")
                count = count + 1
                


    # view total kharchaaa
    elif(choice == 3) :
        total = 0
        for eachexpense in expensesList :
            total = total + eachexpense["amount"]

        print("\n Total Spent = ", total)

    # Exit
    elif (choice == 4) :
        print("Thank You! Have a Great Day")
        break

    else :
        print("INVALID CHOICE!!")
        











