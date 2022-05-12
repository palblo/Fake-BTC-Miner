from pystyle import Colorate, Colors, Write
import random
from time import sleep

chars = '1Aa2Bb3Cc4Dd5Ee6Ff7Gg8Hh9IiLlMmNnOoPpQqRrSsTtUuVvWwKkZz'
numbers = '123456789'

#generate the fake number
fakenumber = int(''.join((random.choice(numbers)for i in range(3))))

print(Colorate.Vertical(Colors.red_to_yellow, f'''

  ▄▄█▀▀▀▀▀█▄▄
▄█▀░░▄░▄░░░░▀█▄
█░░░▀█▀▀▀▀▄░░░█
█░░░░█▄▄▄▄▀░░░█ BTC Miner
█░░░░█░░░░█░░░█ 
▀█▄░▀▀█▀█▀░░▄█▀
  ▀▀█▄▄▄▄▄█▀▀

Pąblo#4316 |https://github.com/palblo/FakeBTCminer
'''))
wallet = Write.Input('Wallet address» ', Colors.red_to_yellow, interval=0.00005)
print(Colorate.Horizontal(Colors.green_to_white, f'wallet set up successfully! : {wallet}', 1))
Write.Input('Press enter to start mining!', Colors.red_to_yellow, interval=0.00005)

for i in range(fakenumber):
    #generate the fake wallet address
    fakewallet= ''.join((random.choice(chars)for i in range(24)))

    #generate the fake wallet password
    fakepassword= ''.join((random.choice(chars)for i in range(10)))

    #print the resoults
    print(Colorate.Vertical(Colors.red_to_white, 'WALLET: ' + fakewallet + ' | PASS:' + fakepassword + ' | INVALID', 1))
    sleep(0.09)
print(Colorate.Vertical(Colors.green_to_white, 'WALLET: ' + fakewallet + ' | PASS:' + fakepassword + ' | VALID', 1))
print(Colorate.Vertical(Colors.green_to_white, 'The bitcoins will be transferred to your bitcoin address...', 1))
Write.Input('PRESS ENTER TO EXIT', Colors.red_to_yellow, interval=0.00005)
