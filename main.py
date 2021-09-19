import os
import sys


def decrypt(path, filename, key):
    file_data = open(path + filename, "rb").read()
    key_data = open(key, "rb").read()

    decrypted_data = bytes(a ^ b for (a, b) in zip(file_data, key_data))

    with open(path + filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)


def encrypt(src, key_dst, filename):
    to_encrypt = open(src + filename, "rb").read()
    size = len(to_encrypt)
    
    key = os.urandom(size)
    
    if not os.path.exists(os.path.dirname(key_dst)):
        os.makedirs(os.path.dirname(key_dst))
    with open(key_dst + filename + ".key", "wb") as key_file:
        key_file.write(key)
    
    encrypted_data = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    
    with open(src + filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)


def encrypt_medium(src, dst):
    for path, dirs, files in os.walk(src):
        if len(files) > 0:
            for file in files:
                key_dst = (path + "\\").replace(src, dst)
                encrypt(path + "\\", key_dst, file)


def decrypt_medium(src, key):
    for path, dirs, files in os.walk(src):
        if len(files) > 0:
            for file in files:
                key_src = (path + "\\").replace(src, key)
                decrypt(path + "\\", file, key_src + file + ".key")


if __name__ == "__main__":
    print("\nWhat action do you want to execute?")
    action = input("Encrypt [e] | Decrypt [d]: ")

    print()

    if action == "e":
        src = input("Folder to be encrypted (recursively): ")
        dst = input("Path where the keys will be stored:   ")

        print("\n!!! Attention: All files inside the folder {src} \nwill be encrypted and can only be accessed by decrypting them again with the keys stored in \n{dst} !!!\n")

        confirm = input("Confirm [y/n]: ")
        if confirm != "y":
            sys.exit(0)

        encrypt_medium(src, dst)
    
    elif action == "d":
        src = input("Folder to be decrypted (recursively): ")
        key = input("Path where the keys are stored:       ")

        print("\n!!! Attention: All files inside the folder {src} \nwill be decrypted with the keys stored in {key} \nand can therefore be accessed again !!!\n")

        confirm = input("Confirm [y/n]: ")
        if confirm != "y":
            sys.exit(0)

        decrypt_medium(src, key)
    
    else:
        print("Aborted, nothing encrypted or decrypted!")
        sys.exit(0)
