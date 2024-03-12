#!/usr/bin/env python3

from sys import argv
import pytesseract


def main():
    if 1 == len(argv):
        print("Requires .png file")
        return 1

    if not argv[1].endswith(".png"):
        print("Must be .png file")
        return 2

    print(pytesseract.image_to_string(argv[1]))

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()


