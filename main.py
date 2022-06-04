import random, os, requests
from time import sleep
from colorama import Fore

os.system('cls')

licensekey = '2407503423363549'
chars = '1a2b3c4d5e6f7g8h9ilmnopqrstuvwkz'
numbers = '123456789'
numbers2 = '12345'

def main():
  os.system('cls')
  fakenumber = int(''.join((random.choice(numbers)for i in range(4))))
  print(Fore.MAGENTA + f'''
┌┐┌┬┐┌─┐  ┌┬┐┬┌┐┌┌─┐┬─┐
├┴┐│ │    │││││││├┤ ├┬┘  
└─┘┴ └─┘  ┴ ┴┴┘└┘└─┘┴└─ 

Pąblo#4316 | github.com/palblo/FakeBTCminer
  ''')
  wallet = input(Fore.RED + 'Wallet: ')
  check = requests.get('https://blockchain.info/q/addressbalance/' + wallet)
  print(Fore.CYAN + 'Checking wallet...')
  if check.status_code == 200:
     print(Fore.CYAN + 'Wallet found')
  else:
     print(Fore.BLUE + 'Invalid Wallet')
     sleep(1)
     main()
  print(Fore.BLUE + f'Wallet set up successfully! : {wallet}')
  input(Fore.CYAN + '\nPress enter to start mining!\n')

  for i in range(fakenumber):
      fakewallet= ''.join((random.choice(chars)for i in range(40)))
      randomnumber = ''.join((random.choice(numbers2)for i in range(2)))
      fakepassword= ''.join((random.choice(chars)for i in range(10)))

      #print the resoults
      print(Fore.CYAN + '[-] ' + Fore.RED + 'WALLET : bc1' + fakewallet + Fore.CYAN + ' | INVALID | 0.00')
      sleep(0.09)
  print(Fore.CYAN + '[+] ' + Fore.GREEN + 'WALLET : bc1' + fakewallet + Fore.CYAN + ' | VALID | 0.' + randomnumber)
  print(Fore.CYAN + 'The bitcoins will be transferred to your bitcoin address...')
  input(Fore.CYAN + 'Press enter to exit')
  main()

def defkey():
  keyin = input(Fore.RED + 'License key: ')
  if keyin == licensekey:
    print(Fore.GREEN + 'Key is valid!')
    sleep(1)
    os.system('cls')
    main()
  else:
    print(Fore.RED + 'Invalid Key!')
    sleep(1)
    os.system('cls')
    defkey()

defkey()
