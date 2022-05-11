#!/usr/bin/env python3
import hashlib
from importlib import import_module

keygenme_trial = import_module("keygenme-trial")


def main():
    index_list = [4, 5, 3, 6, 2, 7, 1, 8]
    hexhash = hashlib.sha256(keygenme_trial.username_trial.encode()).hexdigest()
    license_key = "".join((hexhash[ii] for ii in index_list))
    print(
        keygenme_trial.key_part_static1_trial
        + license_key
        + keygenme_trial.key_part_static2_trial
    )


if __name__ == "__main__":
    main()
