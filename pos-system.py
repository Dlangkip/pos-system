import tkinter as tk
import tkinter.simpledialog as tk_simpledialog
import tkinter.messagebox as tk_messagebox

class POS_System:
    def __init__(self):  #constructor (self) used to initialize object in this class
        self.total = 0
        self.receive = 0
        self.order_items = []

        self.root = tk.Tk()
        self.root.title("Simple POS System") #title 
        self.root.geometry("500x450")  #size of the window
        self.root.configure(bg="#26bf98")  # Set the background color of the root window


        self.menu_frame = tk.Frame(self.root,bg= "#26bf98", width=600, height=250)
        self.menu_frame.pack()

        self.total_label = tk.Label(self.menu_frame, text="Total: 0")
        self.total_label.pack(pady=10)

        self.menu_label = tk.Label(self.menu_frame, text="DLANG'S RESTAURANT MENU")
        self.menu_label.pack(pady=10)

        self.option_label = tk.Label(self.menu_frame, text="Choose a category:")
        self.option_label.pack(pady=10)

        self.food_categories = [
            "Breakfast",
            "Salads",
            "Sandwiches",
            "Pasta dishes",
            "Seafood dishes",
            "International cuisine",
            "Desserts"
            
        ]

        self.selected_category = tk.StringVar()
        self.selected_category.set(self.food_categories[0])  # Set the default category

        self.category_dropdown = tk.OptionMenu(self.menu_frame, self.selected_category, *self.food_categories, command=self.update_options)
        self.category_dropdown.pack(pady=10)

        self.menu_options = tk.StringVar()
        self.menu_options.set("")  # Set the initial menu options to empty

        self.menu_option_label = tk.Label(self.menu_frame, text="Choose an option:")
        self.menu_option_label.pack(pady=10)

        self.menu_option_dropdown = tk.OptionMenu(self.menu_frame, self.menu_options, "")
        self.menu_option_dropdown.pack(pady=10)

        self.add_to_total_button = tk.Button(self.menu_frame, text="Add to Total", command=self.add_to_total)
        self.add_to_total_button.pack(pady=10)

        self.cashout_button = tk.Button(self.menu_frame, text="Cash Out", command=self.cash_out)
        self.cashout_button.pack(pady=10)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=10)

    def update_options(self, selected_category):
        # Update the menu options based on the selected category
        menu_options = self.get_menu_options(selected_category)
        self.menu_options.set("")  # Clear the previous selection
        menu = self.menu_option_dropdown["menu"]
        menu.delete(0, "end")
        for option in menu_options:
            menu.add_command(label=option, command=lambda value=option: self.menu_options.set(value))

    def get_menu_options(self, category):
        # Return the menu options based on the selected category
        if category == "Breakfast":
            return [
                "Scrambled eggs - Ksh 100",
                "Bacon - Ksh 100",
                "Sausages - Ksh 100",
                "Pancakes - Ksh 100",
                "Fresh fruits - Ksh 100",
                "Cereal - Ksh 100",
                "Pastries - Ksh 100"
            ]
        elif category == "Salads":
            return [
                "Caesar salad - Ksh 100",
                "Greek salad - Ksh 100",
                "Caprese salad - Ksh 100",
                "Cobb salad - Ksh 100",
                "Waldorf salad - Ksh 100",
                "Spinach salad - Ksh 100",
                "Quinoa salad - Ksh 100"
            ]
        elif category == "Sandwiches":
            return [
                "Club sandwich - Ksh 100",
                "Turkey and Swiss sandwich - Ksh 100",
                "Chicken Caesar wrap - Ksh 100",
                "BLT sandwich - Ksh 100",
                "Veggie panini - Ksh 100",
                "Tuna salad sandwich - Ksh 100",
                "Reuben sandwich - Ksh 100"
            ]
        elif category == "Pasta dishes":
            return [
                "Spaghetti Bolognese - Ksh 100",
                "Fettuccine Alfredo - Ksh 100",
                "Penne Arrabiata - Ksh 100",
                "Lasagna - Ksh 100",
                "Pesto pasta - Ksh 100",
                "Carbonara - Ksh 100",
                "Macaroni and cheese - Ksh 100"
            ]
        elif category == "Seafood dishes":
            return [
                "Grilled salmon - Ksh 100",
                "Shrimp scampi - Ksh 100",
                "Fish and chips - Ksh 100",
                "Lobster bisque - Ksh 100",
                "Seared tuna steak - Ksh 100",
                "Crab cakes - Ksh 100",
                "Clam chowder - Ksh 100"
            ]
        elif category == "International cuisine":
            return [
                "Chicken tikka masala (Indian) - Ksh 100",
                "Pad Thai (Thai) - Ksh 100",
                "Beef stir-fry (Chinese) - Ksh 100",
                "Tacos al pastor (Mexican) - Ksh 100",
                "Margherita pizza (Italian) - Ksh 100",
                "Sushi rolls (Japanese) - Ksh 100",
                "Moussaka (Greek) - Ksh 100"
            ]
        elif category == "Desserts":
            return [
                "Chocolate cake - Ksh 100",
                "Crème brûlée - Ksh 100",
                "Apple pie - Ksh 100",
                "Cheesecake - Ksh 100",
                "Tiramisu - Ksh 100",
                "Ice cream sundaes - Ksh 100",
                "Freshly baked cookies - Ksh 100"
            ]
        else:
            return []

    def add_to_total(self):
        selected_option = self.menu_options.get()
        if selected_option:
            # Extract the price from the option string (assuming it follows the format "<option> - Ksh <price>")
            price = int(selected_option.split(" - Ksh ")[1])
            self.total += price
            self.total_label.config(text="Total: " + str(self.total))
            self.order_items.append(selected_option.split(" - Ksh ")[0])  # Add the item to the order list

    def cash_out(self):
        self.receive = int(tk_simpledialog.askstring("Input Money Received", "Enter the amount received:"))
        change = self.receive - self.total
        self.generate_receipt()  # Generate receipt
        tk_messagebox.showinfo("Change", "Change: " + str(change))
        self.total = 0
        self.total_label.config(text="Total: 0")
        self.order_items = []  

    def generate_receipt(self):
        receipt = "----- RECEIPT -----\n"
        receipt += "Items:\n"
        for item in self.order_items:
            receipt += "- " + item + "\n"
        receipt += "\nTotal: Ksh " + str(self.total)
        
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")
        receipt_label = tk.Label(receipt_window, text=receipt, justify=tk.LEFT)
        receipt_label.pack()

    def start(self):
        self.root.mainloop()


def main():
    pos = POS_System()
    pos.start()


if __name__ == "__main__":
    main()
