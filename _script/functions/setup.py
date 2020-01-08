import sys
import os

import response

def main():
    if (len(sys.argv) <= 1):
        return response.create(101, "File not provided with Interpreter")
    else:
        return response.create(200)