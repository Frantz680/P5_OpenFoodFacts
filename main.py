from database import Database

class Main:

  def connecting(self):

    print("Welcome to OpenFoodFact")
    authentication = 1

    while authentication:
      choice = int(input(
        "Press 1 for creating new profile.\n"
        "Press 2 for connecting.\n"
        "Press 3 for exit.\n"
      ))

      if choice == 1:
        
        Login = input("Enter your login:")
        Password = input("Enter your password : ")
        print("creation of the database")
        Database.create_database()
        print("database create")
        choice_menu = 1

      if choice == 2:
        Login = input("Enter your login:")
        while Login !=("Login"):

          Login = input("Incorrect username. Try Again")
          if Login == ("Login"):

            Password = input("Enter your password : ")

            while Password != ("Password"):

              Password = input("Incorrect password. Try Again")

              if Password == ("Password"):

                Database.connecting()
                print("successful connection")
                choice_menu = 1

      if choice == 3:

        print("Bye, Bye")
        authentication = 0

      while choice_menu:

        choice = int(input(
          "Press 1 for research substituted.\n"
          "Press 2 for my substituted foods.\n"
          "Press 3 for exit.\n"
        ))

        if choice == 1:
          print("")



        if choice == 2:
          print("")


        if choice == 3:
          authentication = 0
          choice_menu = 0



def main():
  reception = Main()
  reception.connecting()


if __name__ == '__main__':
    main()