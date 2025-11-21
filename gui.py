import tkinter
from app import Inventory, Item
inventory = Inventory("greger", 999)
main = tkinter.Tk()
#main.geometry("500x400")

def log(event = None):
    print(inventory.get_contents())
    new_list = inventory.get_contents()
    for i in range(len(new_list)):
        textlabel.insert(tkinter.END, new_list[i] + "\n")

def createAdd(event = None):
    itemName = textbox.get()
    inventory.add_item(Item(itemName, "yo", 0, "yo2"))

label = tkinter.Label(main, text="Hello World")
label.pack()

textbox = tkinter.Entry(main)
textbox.pack(pady = 20)

button = tkinter.Button(main, text="Create and Add Item", command = createAdd)
button.pack(pady = 20)

log_button = tkinter.Button(main, text="Show Items", command = log)
log_button.pack(pady = 20)

textlabel = tkinter.Text(main, height = 10, width = 50)
textlabel.pack(pady = 20)

main.mainloop()