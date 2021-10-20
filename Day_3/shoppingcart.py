from IPython.display import clear_output
# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def cart():
    state = True
    emptycart = {}
    while state:
        cart_action = input("Do you want to: 'Show', 'Add', 'Delete' or Quit?' ")
        if cart_action.lower() == "show":
            if emptycart:
                for k,v in emptycart.items():
                    print(f"You have {v} {k}(s)")
            else:
                print("Your cart is empty")
            continue
        if cart_action.lower() == "add":
            item = input("What would you like to add? ")
            quantity = input("Enter quantity: ")
            emptycart[item] = quantity
            continue
        if cart_action.lower() == "delete":
            del_item = input("What would you like to remove? ")
            if del_item in emptycart:
                quantity_delete = input("How many would you like to remove? ")
                emptycart[del_item] = int(quantity) - int(quantity_delete)
                if emptycart[item] <= 0:
                    del emptycart[del_item]
            else:
                print("lol sry u don't have this")
            continue
        if cart_action.lower() == "quit":
            state = False
            clear_output()
            break
    print("Here is what you have in your cart:")
    for k,v in emptycart.items():
        print(f"{v} {k}(s)")

cart()
 