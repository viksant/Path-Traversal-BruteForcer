import argparse

from args_type_request import *

# Arguments

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--URL", help="Target's URL")
parser.add_argument("-f", "--file", help="Desired File to read")
# parser.add_argument("-sl", "--standard_linux", action="store_true", help="Look for standard linux files")
# parser.add_argument("-sw", "--standard-windows", action="store_true", help="Look for standard windows files")

args = parser.parse_args()
URL = args.URL
file = args.file
# standard_linux = args.standard_linux
# windows_standard = args.standart_windows