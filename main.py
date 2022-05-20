from pystyle import Colorate, Colors, Write
import random
from time import sleep

chars = '1Aa2Bb3Cc4Dd5Ee6Ff7Gg8Hh9IiLlMmNnOoPpQqRrSsTtUuVvWwKkZz'
numbers = '123456789'
numbers2 = '12345'

fakenumber = int(''.join((random.choice(numbers)for i in range(3))))

print(Colorate.Vertical(Colors.red_to_yellow, f'''
  ▄▄█▀▀▀▀▀█▄▄
▄█▀░░▄░▄░░░░▀█▄
█░░░▀█▀▀▀▀▄░░░█ ┌┐┌┬┐┌─┐  ┌┬┐┬┌┐┌┌─┐┬─┐
█░░░░█▄▄▄▄▀░░░█ ├┴┐│ │    │││││││├┤ ├┬┘  
█░░░░█░░░░█░░░█ └─┘┴ └─┘  ┴ ┴┴┘└┘└─┘┴└─
▀█▄░▀▀█▀█▀░░▄█▀
  ▀▀█▄▄▄▄▄█▀▀ 

https://github.com/palblo/FakeBTCminer

'''))
wallet = Write.Input('Wallet address -> ', Colors.red_to_yellow, interval=0.00005)
print(Colorate.Horizontal(Colors.green_to_white, f'\nwallet set up successfully! : {wallet}', 1))
Write.Input('\nPress enter to start mining!\n', Colors.red_to_yellow, interval=0.00005)

for i in range(fakenumber):
    fakewallet= ''.join((random.choice(chars)for i in range(24)))
    randomnumber = ''.join((random.choice(numbers2)for i in range(2)))
    fakepassword= ''.join((random.choice(chars)for i in range(10)))
    print(Colorate.Horizontal(Colors.red_to_white, 'WALLET : ' + fakewallet + ' | PASS : ' + fakepassword + ' | INVALID | 0.00', 1))
    sleep(0.09)
print(Colorate.Horizontal(Colors.green_to_white, '\nWALLET : ' + fakewallet + ' | PASS : ' + fakepassword + ' | VALID | 0.' + randomnumber, 1))
print(Colorate.Horizontal(Colors.green_to_white, '\nThe bitcoins will be transferred to your bitcoin address...', 1))
Write.Input('\nPRESS ENTER TO EXIT', Colors.red_to_yellow, interval=0.00005)
