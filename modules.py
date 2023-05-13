import random
import matematik as mt
from day3 import Human as hm
from seleniumExample import webdriver 


#from matematik import topla as tp, bol as bl

print(mt.bol(10,2))

print(random.randint(0,100))

Human1 = hm("Mirza")
Human1.talk("Merhaba")

chromeDriver = webdriver.Chrome()