#!/usr/bin/env python3
import io
from PIL import Image


def main():
    with open("tunn3l_v1s10n", "rb") as fh:
        data = list(fh.read())

    # Fix header
    data[10:12] = [0, 0]
    data[14:16] = [40, 0]

    # Increase height
    data[22:24] = [82, 3]
    Image.open(io.BytesIO(bytes(data))).show()


if __name__ == "__main__":
    main()
