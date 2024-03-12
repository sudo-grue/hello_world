#!/usr/bin/env python3

import pytesseract

def main():
    print(pytesseract.image_to_string('hello.png'))

if __name__ == '__main__':
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        from traceback import print_exc
        print_exc()


