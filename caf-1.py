import os, time, string
import requests as req
from colorama import Fore as F
from cfonts import render

class App:
    def text(self, msg):
        for Str in msg:
            print(Str, end="", flush=True)
            time.sleep(8 / 1000)

    def welcomeFunction(self):
        msgWelcome = f""" {F.RESET} Welcome In {F.GREEN}Cobra Admin Finder{F.RESET} - {F.GREEN}1{F.RESET}. """
        l = render(
            text="CAF-1",
            colors=["white", "green"],
            align="center"
        )
        print(l)
        self.text(" " * 60 + msgWelcome + '\n')
        self.text(" "*65 + f"{F.GREEN}Thx{F.RESET} For Use This Tool." + '\n')
        self.text(" "*65 + F.GREEN + "-"*22 + "\n")        

    def script(self):
        try:
            target = (input(f"{F.GREEN}[ {F.RESET}?{F.GREEN} ]{F.RESET} Enter The Target Url: {F.GREEN}")).strip("/")
            
            if not target.startswith('https') or not target.startswith("http"):
                target = "https://"+target

            with open("./paths.txt", "r") as file:
                paths = file.read().splitlines()
                print(f"{F.RESET}[{F.GREEN} = {F.RESET}] Start Search On {F.GREEN}Pages Admin{F.RESET}.")
                okPaths_list = []

                for path in paths:
                    url_path = f"{target}/{path}"
                    try:
                        res = req.get(url_path, timeout=5)
                        if res.status_code == 200:
                            print(f"[{F.GREEN} OK {F.RESET}] Url: {F.GREEN}{url_path}{F.RESET}")
                            okPaths_list.append(url_path)
                        else:
                            print(f"[ {F.RED} NOT {F.RESET}] Url: {F.RED}{url_path}{F.RESET}")
                    except:
                        print(f"{F.RED}Error :(")

        except KeyboardInterrupt:
            print(f"\n{F.RED}[!] Tool Stopped By User.{F.RESET}")
            if okPaths_list:
                print(f"{F.GREEN}[+] Successful Admin Pages Found:{F.RESET}")
                for path in okPaths_list:
                    print(f"{F.GREEN}- {path}")
            else:
                print(f"{F.RED}[-] No Admin Pages Found.{F.RESET}")
        except Exception as e:
            print(f"{F.RED}[!] Error: {e}{F.RESET}")

if __name__ == "__main__":
    a = App()
    a.welcomeFunction()
    a.script()
