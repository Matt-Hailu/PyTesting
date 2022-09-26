import time
pin = 1234
entry = 0
attempt = 0

while entry != pin and attempt < 3:
    try:
        entry = int(input("Enter your pin >>> "))
        if entry == pin:
            print("Thank you. \nBalance is 16.32850030 BTC.\nConsider changing your pin.")
            break
        else: 
            attempt += 1
            print(f"Invalid pin. Attempt {attempt}/3")
        if attempt == 3:
            print("Maximum attempts used. Come back tomorrow or go to jail.")
    except ValueError:
        print(f"Caught a ValueError. Attempt {attempt}/3")
    except:
        print("Hacker detected. Defence systems engaged.")
        count = 3
        print("Program will terminate in..")
        while count > 0:
            print(count)
            count -= 1
            time.sleep(1)
            exit()    
