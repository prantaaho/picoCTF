#!/usr/bin/env python3


def main():
    with open("enc") as fh:
        data = fh.read()
    flag = "".join((chr(ord(x) >> 8) + chr(ord(x) & 0xFF) for x in data))
    print(flag)


if __name__ == "__main__":
    main()
