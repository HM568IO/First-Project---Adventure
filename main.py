print("Hello Adventurer, Welcome to the land of Aclos ")
Name = input("What is your name adventurer? ")
print("Hello, " + Name)
print("Welcome to the Adventure of Aclos")
print("You are a traveler walking through the town of Graystall")
Item_1 = {'Item': ' Travellers Sword', 'Desc': ' A used but trusty sword', 'Dmg': ' Damage 5'}
Item_2 = {'Item':' Travellers Shield', 'Desc': ' A used but trusty shield' , 'Dmg': ' Damage 1'}
Item_3 ={'Item':' Torch' , 'Desc': ' A torch fashioned with a stick and fabric' , 'Dmg': ' Damage 2'}
Item_4 ={'Item':' Rations' , 'Desc': ' A hearty and tasty meal'}
Backpack = '' , '' , '' , ''
print("What would you like to do? ")
print("1. Backpack" 
      " 2. Market"
      " 3. Story")
Option1 = input(": ")
if Option1 == 1 or "Backpack".lower:
      print("The first item is" + Item_1['Item'] + Item_1['Desc'] + Item_1['Dmg'])
      print("The second item is" + Item_2['Item'] + Item_2['Desc'] + Item_2['Dmg'])
      print("The third item is" + Item_3['Item'] + Item_3['Desc'] + Item_3['Dmg'])
elif Option1 == 2 or "Market".lower:
      print("hello")
else:
      print("world")
