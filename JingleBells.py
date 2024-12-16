BELL_ASCII_ART = """			   			  		
				   _,--._
                                 ,'  _.._`.
                            ,^.,' ,-" _," ;
                   _,----.._\\|( _/,--"  ,<
                 ,'     ____(_))< ___..".  `.
                :  _,-"__,-" (_)-.      ,\\.  \
                :,'..-"  _,-")|(\\ `._.-"_,\\  \
                 `.__ ,-"    '-`'   \\.-"   Y  :
                 /  /:-...______...-:      |  |
                (  ( |-...______...-'      ;  ;_
                 \\ ,\\|              |     /,^/  ;._
                  `  .              .        _,'   ;
                     :              :    _,-'    ,"
                     '              ` ,-'     _,"
                    '                '    _,-"`.
                   ;`--...______,,,--":.-"     ;
                  :                    :  `..."
                  '---....______,,,,---'
                           :     ;
                            `.,."          
"""

# ----------------
# Subprograms
# ----------------
def generate_lyrics(noun,animal,place_plural,verb):
   
  carol = "Jingle bells, jingle bells, jingle all the way! \nDashing through the " + noun + "\n On a one "  +  animal + " open-sleigh \n O'er the " + place_plural + " we go\n "+ verb + " all the way"
  return carol  

# ----------------
# Main program
# ----------------
print(BELL_ASCII_ART)
print("Welcome to the Jingle Bell project! This program will generate your very own version of 'Jingle Bells' for you!")
noun = input("Enter a noun")
animal = input("Enter an animal")
place_plural = input("Enter a place")
verb = input ("Enter a verb")
print(generate_lyrics(noun,animal,place_plural,verb))
