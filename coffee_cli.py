import coffee_db as cdb

def init_menu():

   full_name = cdb.get_full_name_of_current_user()
   print(f"\nThanks for logging in, {full_name}\n")
   
   while True:
        print("Welcome to the menu! \n")
        menu_input = int(input(("Type your choice: \n"
                                    "1. Add new tasting \n"
                                    "2. See users with most unique tastings \n"
                                    "3. See the coffees with best value \n"
                                    "4. Search for coffees with a search word \n"
                                    "5. See unwashed coffees from Colombia and Rwanda \n"
                                    "6. Log ut \n\n"
                                    "Valg: "
                                )))
        if menu_input == 1:
            us1()
        elif menu_input == 2:
            us2()
        elif menu_input == 3:
            us3()
        elif menu_input == 4:
            us4()
        elif menu_input == 5:
            us5()
        elif menu_input == 6:
            break
        else:
            print("Invalid choice")

def us1():
    print("Enter the following for a new tasting - ")
    roastery = input("Roastery Name: ")
    coffee_name = input("Coffee Name: ")
    score = int(input("Points: "))
    note = input("Note: ")

    coffe_id = cdb.get_coffee_id(coffee_name, roastery)[0]
    user_id = cdb.get_user_id()
    
    cdb.new_tasting(note, score, coffe_id, user_id)

def us2():
    users_unique_tasting = cdb.get_unique_tasting()

    if users_unique_tasting is None:
        print("Error with getting unique tastings")
    elif len(users_unique_tasting) == 0:
        print("The list is empty")
    else:
        print("Users with most unique coffee tasting -")
        print(users_unique_tasting)

def us3():
    list_of_data = cdb.get_unique_tasting()

    if list_of_data is None:
        print("Error with getting most valuable coffe per kg")
    elif len(list_of_data) == 0:
        print("The list of most valuable coffe per kg is empty")
    else:
        print("Most valuable coffe per kg -")
        print(list_of_data)

def us4():
    print("Enter search word - ")
    search_word = input("search word: ")

    list_of_data = cdb.get_coffee_by_description(search_word)

    if list_of_data is None:
        print("Error with getting results based on search word")
    elif len(list_of_data) == 0:
        print("No result found")
    else:
        print("Results -")
        print(list_of_data)

def us5():
    data = cdb.get_coffee_by_country_and_processing()

    if data is None:
        print("Error with getting results based on search word")
    elif len(data) == 0:
        print("No result found")
    else:
        print("Unwashed coffees from Rwanda and Colobmia -")
        print(data)

init_menu()