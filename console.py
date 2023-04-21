import os

class console:
    def __init__(self, db, tags=None):
        self.output = None
        self.tags = tags
        self.atb = None
        self.db = db

    def new_cmd(self):
        if self.tags != None:
            user_input = input(f"{self.tags}/> ")
        else:
            user_input = input("/> ")

        self.input_handler(user_input)

    def input_handler(self, inn):
        if inn == "cls" or inn == "clear":
            try:
                os.system("cls")
            except:
                os.system("clear")

        elif inn == "?help":
            print("newentry --> Make a new entry to database.")
            print("listentry -a<list all> -f<list fixed> --> List unfixed entries.")
            print("displayentry -- <entry id> --> Display a spesific entry.")
            print("fixentry --<entry id> --> Mark entry as 'Fixed'")

        elif inn.startswith("listentry"):
            if "-" in inn:
                atb = inn[inn.index("-")+1]

                self.db.list_entry(atb)

            else:
                self.db.list_entry()

        elif inn.startswith("displayentry --"):
            try:
                num = int(inn[15:])

            except:
                print("Invalid entry type: ", inn[13:])
                print("Must be Int32.")

                return 1
            
            self.db.display_entry(num)

        elif inn.startswith("fixentry --"):
            try:
                num = int(inn[11:])
            except:
                print("Invalid entry type: ", inn[13:])
                print("Must be Int32.")

                return 1
        
            self.db.mark_entry(num)


        elif inn == "newentry":
            title = None
            error = None
            text = None
            
            title = input("[Title]/> ")
            error = input("[Error]/> ")
            text = input("[Text]/> ")

            self.db.new_entry(title, error, text)

        else:
            print("Invalid command.")
            print("You can display valid commands with '?help'.")

if __name__ == "__main__":
    pass