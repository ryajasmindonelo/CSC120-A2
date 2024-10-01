from typing import Dict, Optional, List
from computer import *

class ResaleShop:

    itemID = [0]
    inventory_list: List[Dict[int, 'Computer']] = []
    inventory: Dict[int, 'Computer'] = {}
    inventory_list.append(inventory)
    itemID.append(1)

    def __init__(self, inventory):
        self.inventory = inventory

    itemID = 0

    def buy(self,computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID

    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id]  # locate the computer
            if computer.year_made < 2000:
                computer.price = 0  # too old to sell, donation only
            elif computer.year_made < 2012:
                computer.price = 250  # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550  # discounted price on machines 4-to-10 years old
            else:
                computer.price = 1000  # recent stuff

            if new_os is not None:
                computer.operating_system = new_os  # update details after installing new OS
        else:
            print(f"Computer {item_id} refurbished. New price: {computer.price}, OS: {computer.operating_system}")
        
def main():
    inventory : Dict[int, Computer] = {}
    Rya = ResaleShop({})
    Rya.buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})
    Rya.update_price(1,35)
    Rya.print_inventory()

main()