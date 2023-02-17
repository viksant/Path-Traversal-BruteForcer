import requests
import argparse
import sys
from pwn import *
from args_type_request import *
from args import *
from preFile import encoded, files

def def_handler(sig, frame):
    print("[!] Aborting...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

class Interface:
    def __init__(self):
        self.red = '\033[91m'
        self.green = '\033[92m'
        self.white = '\033[37m'
        self.yellow = '\033[93m'
        self.blue = '\033[94m'

    def header(self, message):
        print(f"\n {self.green}{message}\n")

    def error(self, message):
        print(f"{self.red}{message}")

    def success(self, message):
        print(f"{self.green}{message}")

    def message(self, message):
        print(f"{self.yellow}{message}")

colorMessage = Interface()

if __name__ == "__main__":

    print("######################################")
    print("Path Traversal scanner made by VIKSANT")
    print("######################################")

    File_MakeRequest()

