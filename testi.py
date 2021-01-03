
rock = '''
  _______
---' ____)
   (_____)
   (_____)
   (____)
---.__(___)
'''
paper = '''
_______
---' ____)____
______)
_______)
_______)
---.__________)
'''
scissors = '''
_______
---' ____)____
______)
__________)
(____)
---.__(___)
'''
import random

käsieleet = [rock, scissors, paper]
#################
print("Tervetuloa pelaamaan kivi-sakset paperia.")
pelaajan_valinta = int(input( "Minkä valitset : kivi = 0, sakset = 1 ja paperi =2\n"))
if (pelaajan_valinta > 2) or (pelaajan_valinta < 0):
  print("Virheellinen valinta. Hävisti!")
else:
  print (käsieleet[pelaajan_valinta])
  print("\n"
  "XxXxXxXxXxXxXxXxXx")
  koneen_valinta = random.randint(0,2)
  print(käsieleet[koneen_valinta])
  if pelaajan_valinta == koneen_valinta:
    print ("Tasapeli")
  elif (pelaajan_valinta == (koneen_valinta - 1)) or (pelaajan_valinta == (koneen_valinta + 2)):
    print("olet voittaja")
  else:
    print("Hävisit")
