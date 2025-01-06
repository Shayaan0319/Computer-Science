names = ["Kevin", "Ceejay", "Luqman", "ledis", "khaled"]
names_to_find = input("Name to find: ")

found = False
index = 0

while found == False and index < len(names):
  if names[index] == names_to_find:
    found = True
  else:
    index = index + 1
if found == True:
  print("Name found")
else:
  print("Name not found")
