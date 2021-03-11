#!/din/python
#coder:https://github.com/mao2116/
#Ekramul Hassan
import os,sys,time,datetime,random
from pyfiglet import figlet_format
from termcolor import colored


mao = 'THBD'
mao = figlet_format(mao, 'slant')
Mao1 = colored(mao, 'cyan')
x1 = "2116"
gf = figlet_format("GF Need?", 'slant')
gf = colored(gf, 'red')
em = ("😑😶😑")
try1 = ("Try Again.")
wa = colored("wait,,,,,,,,", 'cyan')
try2 = colored(try1, 'cyan')
def Mao (z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.01)
    
    
while True:
  x2 = input('Pass :')
  if(x2 == x1):
    Mao(Mao1)
    Mao(gf)
    print(em)
    print(wa)
    
    os.system('xdg-open https://www.facebook.com/groups/365865727812895/?ref=share')
    break
  else:
    #os.system('xdg-open https://www.facebook.com/ekramul.hassan.79827')
      Mao(try2)
      
