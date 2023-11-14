from dataclasses import dataclass

@dataclass
class ItemOrigin:
    country: str
    production_date: str

@dataclass
class InventoryItem:
    name: str
    quantity: int
    serial_number: str
    origin: ItemOrigin

def main():
    item_origin = ItemOrigin(country = "China", production_date = "02/12/2023")
    
    my_item1 = InventoryItem(name = "Printer", 
                             quantity = 10, 
                             serial_number = "PRNT12345",
                             origin = item_origin)
    
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1)

    my_item2 = InventoryItem(**my_serialized_object1)
    print (my_item2.__dict__)

if __name__ == "__main__":
    main() # Call main function

