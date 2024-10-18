# Temperature converter program

# -------------------------
# Subprograms
# -------------------------
def c_to_f(centigrade):
  return (centigrade * 1.8) + 32


# -------------------------
# Main program
# -------------------------
centigrade = int(input("what is the temperature in centigrade"))
fahrenheit = c_to_f(centigrade)
print(centigrade, "degrees Centigrade is", fahrenheit, "degrees Fahrenheit.")
