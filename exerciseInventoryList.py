def addToInventory(inventory, addItems):
    for i in range(len(addItems)):
        if addItems[i] in inventory.keys():
            inventory[addItems[i]] += 1
        else:
            inventory.setdefault(addItems[i], 1)
    return inventory


inv = {'gold coin': 42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)


def displayInventory(inventory):
    print ('Inventory:\n')
    item_total = 0
    for k,v in inventory.items():
        print (str(v) + ' ' + k)
        item_total += v
    print ('Total number of items: ' + str(item_total))

displayInventory(inv)