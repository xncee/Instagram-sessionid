import os, time, subprocess
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    blueaccounts = f"{WHITE}[ {BLUE}ACCOUNTS {WHITE}]"
    redaccounts = f"{WHITE}[ {RED}ACCOUNTS {WHITE}]"
    xrblue = f"\n{blueplus} Instagram Sessionid Checker {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
accounts = []
class FILES():
    def __init__(self, my_list, bluefile, redfile):
        self.select_file(f"\n{bluefile} Enter To Select File: ")
        self.open_file(my_list, bluefile, redfile)
    def select_file(self, text):
        print(text, end="")
        input()
        root = Tk()
        root.title(".txt")
        self.path = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=(("txt document","*.txt"),("All Files", "*.*")))
        root.destroy()
        root.mainloop()
    def open_file(self, my_list, bluefile, redfile):
        filename = self.path.split("/")[-1]
        if self.path[-4:]!=".txt":
            print(f"\n{redfile} Please Select (.txt) File ", end="")
            input()
            exit()
        try:
            for x in open(self.path, "r").read().split("\n"):
                if x!="":
                    my_list.append(x)
            print(f"\n{bluefile} Successfully Load {DESIGN.BLUE}{filename}")
            time.sleep(2)
        except Exception as err:
            print(f"\n{redfile} {err} ", end="")
            input()
            exit()
class FILES2():
    def __init__(self, filename, my_list):
        self.open_file(filename, my_list)
    def open_file(self, filename, my_list):
        try:
            file = open(f"{filename}.txt", "r").read().split("\n")
            for x in file:
                if x!="":
                    my_list.append(x)
            print(f"\n{DESIGN.blueplus} Successfully Load {DESIGN.BLUE}{filename}.txt")
            time.sleep(2)
        except:
            print(f"\n{DESIGN.redminus} {DESIGN.RED}{filename} {DESIGN.WHITE}is missing ", end="")
            input()
            exit()
class Xnce():
    def __init__(self):
        clear()
        print(DESIGN.xrblue)
    def inex(self):
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
        input()
        exit()
    def save_session(self, filename, sessionid):
        with open(f"{filename}.txt", "a") as file:
            file.write(f"\n{sessionid}")
            file.close()
    def check(self, sessionid):
        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "cookie": f"sessionid={sessionid}"
        }
        req = requests.get("https://www.instagram.com/instagram/", headers=head)
        if "no-js logged-in" in req.text:
            print(f"\n{DESIGN.blueplus} Good {DESIGN.BLUE}{sessionid}")
            self.save_session("Good", sessionid)
        else:
            print(f"\n{DESIGN.redminus} Bad {DESIGN.RED}{sessionid}")
x = Xnce()
try:
    from tkinter import *
    from tkinter import filedialog
    FILES(accounts, DESIGN.blueaccounts, DESIGN.redaccounts)
except:
    FILES2("accounts", accounts)
print(accounts)
print(f"\n{DESIGN.blueplus} Enter To Start: ", end="")
input()
for account in accounts:
    x.check(account)
x.inex()