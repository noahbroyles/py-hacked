import random, time

try:
    from termcolor import colored
    color = True
except: 
    color = False

hacks = [":(){ :|: & };:", "Hacking in Progress...", "ALERT! YOUR SYSTEM HAS BEEN COMPROMISED", "REPAIRS FAILED!!!" "root hack", "root", "!BASH SHELL ERROR!", 'bash', 'ERROR!', "Failure" "Root Security flaw detected: Error code: " + str(random.randint(0, 999)), "You have been ******* by a hacker", "HACKED", "HACKED!", "sudo error", "Attempting repairs on triggers for man-db..."]
zao = [0, 1, " "]
colors = ['red', 'green', 'blue', 'none']

while True:
    message = ""
    for i in range(random.randint(10, 200)):
        message += str(random.choice(zao))
    message2 = random.choice(hacks)

    if color: 
        c = random.choice(colors)
        if c == 'none':
            print(message + message2, end="", flush=True)
        else:
            print(colored(message, c), end="", flush=True)
            print(colored(message2, c), end="", flush=True)
    else:
        print(message + message2, end="", flush=True)

    time.sleep(float(str("0.0" + str(random.randint(1, 9)))))
