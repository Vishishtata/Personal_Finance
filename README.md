# Personal_Finance
This is a personal finance app

Expense Tracker

A simple, interactive command-line tool to help you track your daily expenses and understand where your money disappears every day (because it does disappear).

I Overview

    This Expense Tracker is a beginner-friendly Python program that allows you to:

    Add new expenses (with date, category, description, amount)

    View all recorded expenses

    View your total expenditure

    Exit anytime

    Keep all data stored in a list during runtime


II Features

    1. Add New Expense

        Input:

        Date

        Category (Food, Travel, Books, etc.)

        Short description

        Amount spent

        The expense is stored in a list as a dictionary.

    2. View All Expenses

        Displays:

        Entry number

        Date

        Category

        Description

        Amount spent

        If no expenses exist, it informs the user.

    3. View Total Spent

        Calculates and displays the sum of all expenses recorded so far.

    4. Exit

        Exits the program gracefully with a goodbye message.


III How It Works (Internals)

    All expenses are stored temporarily in a Python list called expensesList.

    Each expense is a dictionary with keys:

        {
            "date": ...,
            "category": ...,
            "discription": ...,
            "amount": ...
        }


    The while-loop keeps the program running until the user chooses option 4.


IV Example Flow
    Welcome To Expense Tracker : Please Spend Mindfully

    {
        "date": ...,
        "category": ...,
        "discription": ...,
        "amount": ...
    }


    Please Enter Your Choice : 1
    Today's Date? : 06-12-2025
    Category? (Food, Travel, Books....) : Food
    A Short Discription : Pizza lunch
    Enter The Amount : 250

    Expense Added Successfully!!


V Future Improvements


    Edit or delete previous entries

    Add monthly summaries

    Add category-wise spending charts

    Add validations (e.g., wrong input handling)