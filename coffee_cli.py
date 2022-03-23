import coffee_db as cdb

def init_menu():
   while True:
        print("Velkommen til dmenyen! \n")
        menu_input = int(input(("Skriv inn ønsket valg: \n"
                                "'1' for å legge til ny smaking \n"
                                "'2' for å se brukere med flest unike kaffesmakinger \n"
                                "'3' for å se kaffene som gir mest for pengene \n"
                                "'4' for å se kaffene beskrevet med et søkeord \n"
                                "'5' for å se uvaskede kaffer fra Colombia og Rwanda \n"
                                "'6' for å logge ut ")))
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
    notes = str(input("Skriv inn et kaffenotat"))

def us2():
    

def us3():
    

def us4():
    

def us5():
    