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
    bluezero = f"{WHITE}[ {BLUE}0 {WHITE}]"
    blueone = f"{WHITE}[ {BLUE}1 {WHITE}]"
    xrblue = f"\n{blueplus} Instagram Sessionid {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
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
                if x!="" and ":" in x:
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
    def save_account(self, filename, account):
        with open(f"{filename}.txt", "a") as file:
            file.write(f"\n{account}")
            file.close()
    def login(self, account):
        username, password = account.split(":")[0], account.split(":")[1]
        head = {
            "Host": "www.instagram.com",
            "user-agent": "Mozilla/5.0",
            "x-csrftoken": "r9HYY0x3vVWCUoGjMIKrYmcDUtsiZBuS",
            "x-instagram-ajax": "45f20c1511ec-hot",
            "x-ig-app-id": "1217981644879628",
            "x-asbd-id": "198387",
            "x-ig-www-claim": "0",
            "content-type": "application/x-www-form-urlencoded",
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/"
        }
        data = {
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:0:{password}",
            "username": username
        }
        req = requests.post("https://www.instagram.com/accounts/login/ajax/", headers=head, data=data)
        if "userId" in req.text:
            print(f"\n{DESIGN.blueplus} Logged In {DESIGN.BLUE}{username}")
            sessionid = req.cookies.get("sessionid")
            if mode=="0":
                self.save_account(username, sessionid)
            else:
                self.save_account("sessions", sessionid)
                self.save_account("sessions-info", f"{sessionid}:{account}")
        else:
            if mode=="0":
                print(f"\n{DESIGN.redminus} {req.text}, {req.status_code}")
            else:
                print(f'\n{DESIGN.redminus} {req.text} {DESIGN.RED}{username}')
        time.sleep(1)
x = Xnce()
print(f"\n{DESIGN.bluezero} Single Account {DESIGN.blueone} Multi Accounts: ", end="")
mode = input()
if mode=="0":
    print(f"\n{DESIGN.blueplus} username: ", end="")
    username = input()
    print(f"\n{DESIGN.blueplus} password: ", end="")
    password = input()
    x.login(f"{username}:{password}")
elif mode=="1":
    try:
        from tkinter import *
        from tkinter import filedialog
        FILES(accounts, DESIGN.blueaccounts, DESIGN.redaccounts)
    except:
        FILES2("accounts", accounts)
    print(f"\n{DESIGN.blueplus} Enter To Start: ", end="")
    input()
    for account in accounts:
        x.login(account)
else:
    print(f"{DESIGN.redminus} ['0', '1']")
x.inex()