def add(menu, item):
    if item not in menu:
        menu.append(item)
    return menu

def remove(menu, item):
    if item in menu:
        menu.remove(item)
    return menu

def check(menu, item):
    if item in menu:
        return f'{item} is available'
    else:
        return f'{item} is not available'

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

menu = add(initial_menu, add_item)
menu = remove(menu, remove_item)
availability = check(menu, check_item)

print("Updated menu:", menu)
print("Availability:", availability)
