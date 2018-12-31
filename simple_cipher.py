#!/usr/bin/env python3

# ==> STL Imports
from importlib import import_module
from typing import Tuple

# ==> Core/Local Imports
from args.args import parse
from utils.file_io import read_txt_file


def should_do_pip_install() -> Tuple[bool, bool]:
    print("It appears you do not have 'some_crypt' installed.")
    yesses = ['y', 'yes', 'yessir', 'yep']

    response = input("Would you like to `pip install` it? (Y/n)").lower()
    if response in yesses:
        return True, False

    response = input("Would you like to `pip install --user` it? (Y/n)").lower()
    if response in yesses:
        return True, True

    return False, False


def do_pip_install(user_flag=False) -> None:
    import sys
    import subprocess
    if user_flag:
        subprocess.call([sys.executable, "-m", "pip", "install", "--user", "some-crypt"])
    else:
        subprocess.call([sys.executable, "-m", "pip", "install", "some-crypt"])


def encrypt(cipher_module, target: str,
            key: int or str, target_type: str,
            strip_frmt=False) -> str:
    assert target_type in ['string', 'file']

    if target_type is 'file':
        plaintext = read_txt_file(target)
    else:
        plaintext = target

    return cipher_module.encrypt(plaintext, key, strip_frmt=strip_frmt)


def decrypt(cipher_module, target: str,
            key: int or str, target_type: str,
            strip_frmt=True) -> str:
    assert target_type in ['string', 'file']

    if target_type is 'file':
        ciphertext = read_txt_file(target)
    else:
        ciphertext = target

    return cipher_module.decrypt(ciphertext, key, strip_frmt=strip_frmt)


def main():
    argv = parse()
    assert argv.mode in ['encrypt', 'decrypt']

    try:
        cipher_module = import_module(f".{argv.cipher}", "some_crypt.ciphers")
    except ModuleNotFoundError:
        _do_pip, _user = should_do_pip_install()
        if _do_pip:
            do_pip_install(_user)
            cipher_module = import_module(f".{argv.cipher}", "some_crypt.ciphers")
        else:
            print("Aborting.")
            quit()

    res = globals()[argv.mode](cipher_module, argv.target, argv.key, argv.target_type, argv.strip_frmt)

    if argv.output is None:
        print(res)
    else:
        # TODO: write to argv.output location
        pass


if __name__ == "__main__":
    main()
