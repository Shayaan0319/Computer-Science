# Constants
# ----------------
ASCII_ART = '''
         { }
         {^^,
         (   `-;
    _     `;;~~
   /(______);
  (         (
   |:------( )
 _//         \\
/ /          vv
'''

# ----------------
# Subprograms
# ----------------
def game(desicion1):
  if decision1 == "shortcut":
    print(" Rudolph gets caught in a snowstorm and loses his way. Game over.")
    exit()
  elif decision1 == "valley":
    print("Rudolph reaches the valley and continues his journey…")
  else:
    print("Invalid input") 
  if decision2 == "fly":
   print("Whilst attempting to fly, the strong winds toss Rudolph around, and he crashes into a tree. Game over.")
   exit()
  elif decision2 == "cave":
   print("Rudolph waits out the storm and continues afterward.")
  else:
    print("Invalid input") 
  if decision3 == "door":
    print("By attempting to open the locked front door, he accidentally triggers an alarm, leading to his discovery. Game over.")
    exit()
  elif decision3 == "chimney":
    print("Rudolph skillfully slides down and successfully places the presents under the tree.")
  else:
      print("Invalid input") 
  if decision4 == "push":
    print("Rudolph collapses, and the remaining presents are undelivered. Game over.")
    exit()
  elif decision4 == "nap":
    print("Rudolph's nap allows him to regain energy, and he successfully completes the rest of the deliveries.")
  else:
    print("Invalid input") 
# ----------------
# Main program
# ----------------
print(ASCII_ART)
print("Welcome to Rudolph's Adventure, a choose-your-own-adventure game.")
print(" It's Christmas Eve, and Rudolph needs to deliver all of the presents on time for Christmas!")

decision1 = input("Rudolph starts at Santa's Workshop. He needs to choose between taking a shortcut through the snowy mountains or following the longer, safer path through the valley.(shortcut/valley):")
decision2 = input("A blizzard hits, and Rudolph faces a choice: should he try to fly above the storm or find shelter in a cave?(cave/fly):")
decision3 = input("Rudolph arrives at the first house to deliver presents. He faces a decision: should he use the chimney to deliver the presents or attempt to open the locked front door?(chimney/door):")
decision4 = input("Rudolph is running out of time. He faces a decision: should he push through exhaustion to complete the deliveries or take a quick nap to regain energy?(push/nap):")
print("Rudolph successfully delivers all the presents on time! Santa and the elves celebrate his heroic efforts, and Rudolph's nose shines brightly with joy.")
