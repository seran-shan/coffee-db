import coffee_db as cdb

def init_menu():
   while True:
        print("\nTakk for at du logget inn\n")
        print("Velkommen til menyen! \n")
        menu_input = int(input(("Skriv inn ønsket valg: \n"
                                    "1. Legge til ny smaking \n"
                                    "2. Se brukere med flest unike kaffesmakinger \n"
                                    "3. Se kaffene som gir mest for pengene \n"
                                    "4. Se kaffene beskrevet med et søkeord \n"
                                    "5. Se ikke vaskede kaffer fra Colombia og Rwanda \n"
                                    "6. Logge ut \n\n"
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
            print("Du har tastet inn et ugyldig valg")

def us1():
    print("Tast inn følgende for å legge inn ny smaking - ")
    roastery = input("Brennerinavn: ")
    coffee_name = input("Kaffenavn: ")
    score = input("Points: ")
    note = input("Smaksnotat: ")

    coffe_id = cdb.get_coffee_id(coffee_name, roastery)
    user_id = cdb.get_user_id()
    
    cdb.new_tasting(note, score, coffe_id, user_id)

def us2():
    list_of_user = cdb.get_unique_tasting()

    if list_of_user is None:
        print("Error with getting unique tastings")
    elif len(list_of_user) == 0:
        print("The list is empty")
    else:
        print("Users with most unique coffee tasting -")
        for key, value in list_of_user:
            print(key, ' : ', value)

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
    print("Tast inn søkeord - ")
    search_word = input("Søkeord: ")

    list_of_data = cdb.get_coffee_by_description(search_word)

    if list_of_data is None:
        print("Error with getting results based on search word")
    elif len(list_of_data) == 0:
        print("No result found")
    else:
        print("Søketreff -")
        print(list_of_data)

def us5():
    list_of_data = cdb.get_coffee_by_country_and_processing()

    if list_of_data is None:
        print("Error with getting results based on search word")
    elif len(list_of_data) == 0:
        print("No result found")
    else:
        print("Ikke vaskede kaffer fra Colombia og Rwanda -")
        print(list_of_data)

init_menu()