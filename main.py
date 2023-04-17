from database import database
from console import console

def main():
    db = database("mongo_client")
    c = console(db)

    while True:
        c.new_cmd()

main()