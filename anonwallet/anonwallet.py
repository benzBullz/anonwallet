from bitcoinlib.wallets import HDWallet
import bitcoinlib
import random

name = random.randint(10000,1000000000000000000000000000000000000000)
letter = "ABCD"
name2 = random.choice(letter)
name = f"wallet_{name2}{name}"
wallet = HDWallet.create(name)
key1 = wallet.new_key()
print("""
                         __          __   _ _      _   
     /\                  \ \        / /  | | |    | |  
    /  \   _ __   ___  _ _\ \  /\  / /_ _| | | ___| |_ 
   / /\ \ | '_ \ / _ \| '_ \ \/  \/ / _` | | |/ _ \ __|
  / ____ \| | | | (_) | | | \  /\  / (_| | | |  __/ |_ 
 /_/    \_\_| |_|\___/|_| |_|\/  \/ \__,_|_|_|\___|\__|                                                                                                          
""")
print("                    (Bitcoin)                         ")
print("======================================================")
print("Simply restart the program to aquire a new wallet.")
wallet_name = name
address = key1.address
print(f"name: {wallet_name}")
print(f"address: {address}")
print("======================================================")
print("0. OPTIONS")
print("1. SEND")
print("2. WALLET INFO")
print("<<<<<<<<<<<<<<")
while True:
    inp = input("AnonWallet >>> ")

    if inp == "0":
        print("0. OPTIONS")
        print("1. SEND")
        print("2. WALLET INFO")
        print("<<<<<<<<<<<<<<")
    elif inp == "1":
        try:
            receiver = input("AnonWallet >>> Address >>> ")
            amount = float(input("AnonWallet >>> Amount >>> "))
            confirmation = input("AnonWallet >>> Confirm(Y,n) >>> ")
            if confirmation == "Y":
                wallet.send_to(receiver, amount)
                print("Payment is on it's way!")
            elif confirmation == "n":
                print("Payment cancelled.")
            else:
                print("Error: Invalid confirmation")
        except bitcoinlib.wallets.WalletError:
            print("Error: Insufficient funds.")
        except bitcoinlib.encoding.EncodingError:
            print("Error: Invalid address.")
    elif inp == "2":
        print("======================================================")
        wallet.info()
        print("======================================================")
        
    else:
        print("Error: Invalid choice.")
