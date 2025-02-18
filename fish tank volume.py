# Fish tank volume problem

# -------------------------
# Subprograms
# -------------------------
def volume(length, width, height):
   return (length*width*height)/1000
   
def litres_to_gallons(litres):
  return litres / 4.546
# -------------------------
# Main program
# -------------------------
length = int(input("Enter the length"))
width = int(input("Enter the width"))
height = int(input("Enter the height"))
litres = volume(length,width,height)
gallons = litres_to_gallons(litres)
print("A", length, "x", width, "x", height, "cm tank is", litres, "litres and", gallons, "imperial gallons.")
