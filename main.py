import csv
from datetime import datetime


# Class for methods used to create output inventory files from provided input
class OutputInventory:

    def __init__(self, item_list):
        self.item_list = item_list

    def full(self):
        # Open FullInventory.csv for writing and sort all the keys
        with open('FullInventory.csv', 'w') as the_file:
            all_items = self.item_list
            all_keys = sorted(all_items.keys())

            # for loop will iterate through each key which is an item's attribute
            for single_item in all_keys:
                iden = single_item
                name_man = all_items[single_item]['manufacturer']
                type_item = all_items[single_item]['item_type']
                the_price = all_items[single_item]['price']
                date_service = all_items[single_item]['service_date']
                damage = all_items[single_item]['damaged']

                # Write all the traits of an item to FullInventory.csv
                the_file.write(f'{iden}, {name_man}, {type_item}, {the_price}, {date_service}, {damage}\n')

    def by_type(self):

        # A csv file will have item ID, manufacturer name, price, service date, damaged written to it
        all_items = self.item_list
        all_types = []
        all_keys = sorted(all_items.keys())

        # For loop will check the item types and append them IF they are not already in the keys
        for single_item in all_items:
            type_item = all_items[single_item]['item_type']
            if type_item not in all_types:
                all_types.append(type_item)
        for single_type in all_types:

            with open('LaptopInventory.csv', 'w') as the_file:
                for single_item in all_keys:
                    iden = single_item
                    name_man = all_items[single_item]['manufacturer']
                    the_price = all_items[single_item]['price']
                    date_service = all_items[single_item]['service_date']
                    damage = all_items[single_item]['damaged']
                    type_item = all_items[single_item]['item_type']

                    # Write to file if one item's type is already inside the list
                    if single_type == type_item:
                        the_file.write(f'{iden}, {name_man}, {the_price}, {date_service}, {damage}\n')

    def past_service(self):

        # A csv output file made for items past the service date and sorted from old to new
        all_items = self.item_list

        # Get all the keys and sort them
        all_keys = sorted(all_items.keys(), reverse=True)

        with open('PastServiceDateInventory.csv', 'w') as the_file:
            for single_item in all_keys:
                iden = single_item
                name_man = all_items[single_item]['manufacturer']
                type_item = all_items[single_item]['item_type']
                the_price = all_items[single_item]['price']
                date_service = all_items[single_item]['service_date']
                damage = all_items[single_item]['damaged']
                present = datetime.now().date()
                service_exp = datetime.strptime(date_service, "%m/%d/%Y").date()

                # Write to PastServiceDateInventory.csv IF past service date
                if service_exp < present:
                    the_file.write(f'{iden},{name_man},{type_item},{the_price},{date_service},{damage}\n')

    def damaged(self):

        # A csv output file made for all items that are damaged, and sorted from highest to lowest price
        all_items = self.item_list

        # Get order of keys to write to file based on price (reverse will print the items' prices in DESCENDING order)
        all_keys = sorted(all_items.keys(), reverse=True)
        with open('DamagedInventory.csv', 'w') as the_file:
            for single_item in all_keys:
                iden = single_item
                name_man = all_items[single_item]['manufacturer']
                type_item = all_items[single_item]['item_type']
                the_price = all_items[single_item]['price']
                date_service = all_items[single_item]['service_date']
                damage = all_items[single_item]['damaged']

                # Write the id, manufacturer, type, price, and service to DamagedInventory.csv
                if damage:
                    the_file.write(f'{iden}, {name_man}, {type_item}, {the_price}, {date_service}')


if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']

    # For loop will read through each file and lines in the files with a delimiter of ','
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    # Create an object of the OutputInventory class and call the class methods to output all the files
    inventory = OutputInventory(items)
    inventory.full()
    inventory.by_type()
    inventory.past_service()
    inventory.damaged()

    # Get the different manufacturers and types in a list
    types = []
    manufacturers = []
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)
