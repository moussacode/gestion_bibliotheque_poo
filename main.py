from Menu import Menu
from Database import Database
#Main Application

db = Database()
db.connecter()

menu = Menu(db)
menu.menu()
