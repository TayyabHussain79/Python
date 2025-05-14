import copy

# Creating Class to manage the Inventory
class InventoryManager:

    # Attribute
    def __init__(self):
        self.inventory = {
            "laptop": {"price": 1000, "stock": 5, "category": "electronics"},
            "banana": {"price": 100, "stock": 100, "category": "groceries"},
            "apple": {"price": 200, "stock": 50, "category": "groceries"},
            "tv": {"price": 1, "stock": 2, "category": "electronics"},
            "computer": {"price": 800, "stock": 5, "category": "electronics"},
            "fans": {"price": 300, "stock": 6, "category": "electronics"}
        } 

    # Method To Add product
    def add_product(self):

        product_name = input("Enter The Product Name: ")
        price = int(input("Enter the Price: "))
        stock = int(input("Enter the Stock of product: "))
        category= input("Enter the Category of the Product: ")

        cis_product_name = product_name.lower()
        cis_category = category.lower()
        if cis_product_name in self.inventory:
            print(f"{product_name} Already Exist in the Inventory You just need to update the stock")
        else:
            self.inventory[cis_product_name] = {"price": price, "stock": stock, "category": cis_category }
            print("Done! The Data is added Successfully")
        
        print(self.inventory)

    # Method to Update the Stock
    def update_stock(self):
        product_name = input("Enter The Product Name: ")
        stock = int(input("Enter the Stock of product: "))
        cis_product_name = product_name.lower()
        if cis_product_name in self.inventory:
            self.inventory[cis_product_name]['stock'] = stock
        else:
            print("Item not Found in the Inventory")

    # Method To Check the Stock
    def check_stock(self):
        product_name = input("Enter The Product Name: ")
        cis_product_name = product_name.lower()
        if cis_product_name in self.inventory:
            print(f"{product_name} has the stock of {self.inventory[cis_product_name]['stock']}")
        else:
            print("Item not Found in the Inventory")

    # Method To Find Low Stock Report
    def low_stock_report(self):
        threshold = int(input("Enter The Threshold Value: "))
        report={}
        for item, values in self.inventory.items():
            if values['stock'] < threshold:
                print(f"{item} has stock of {values['stock']}")
                report[item] = [values["stock"]]
        if len(report) == 0:
            print(f"All the items have more stock then {threshold}")
        else:
            print(report)
    
    # Method To Find Product By Category
    def find_product_by_category(self):
        category= input("Enter the Category: ")
        cis_category = category.lower()
        listOfProduct=[]
        for item, values in self.inventory.items():
            if values["category"] == cis_category:
                print(f"{item}")
                listOfProduct.append(item)
        if len(listOfProduct) == 0:
            print(f"No Item Match to {category}")
        else:
            print(listOfProduct)
            return(listOfProduct)
    
    # Method to Apply Discount6
    def apply_discount(self):
        # category= input("Enter the Category: ")
        listOfProduct = self.find_product_by_category()
        discount_percentage = int(input("Enter the Discount Percentage: "))
        # Getting the deep copy of the inventory dictionary because it is an multidimensional dictionary
        afterDiscount = copy.deepcopy(self.inventory)

        for item in listOfProduct:
            afterDiscount[item]['price'] -= (afterDiscount[item]['price'] * discount_percentage) / 100
            print(afterDiscount[item]['price'])
            # Checking for price if it less than 1 or not
            if afterDiscount[item]['price'] <= 1:
                afterDiscount[item]['price'] = self.inventory[item]['price']
                print(f"We Cannot allow {discount_percentage} percent discount on the {item}")
        # Print to check whether the changing is just in the copy of the original inventory  
        print(afterDiscount)
        print(self.inventory)

        


# Object of the Class
inventory_c = InventoryManager()
while(1):
    action = input(''' :Choose The Option:
                    1: add_product
                    2: update_stock
                    3: check_stock
                    4: low_stock_report
                    5: find_product_by_category
                    6: apply_discount 
                      ''')
    print(action)

    match action:
        case '1':
            inventory_c.add_product()

        case '2':
            inventory_c.update_stock()

        case '3':
            inventory_c.check_stock()

        case '4':
            inventory_c.low_stock_report()

        case '5':
            inventory_c.find_product_by_category()

        case '6':
            inventory_c.apply_discount()

        case _:
            print("The Option doesn't match, Kindly provide the Correct One")

# # Applying Mehtods of the Class
# inventory_c.add_product()
# inventory_c.update_stock()
# inventory_c.check_stock()
# inventory_c.low_stock_report()
# inventory_c.find_product_by_category()
# inventory_c.apply_discount()

    
