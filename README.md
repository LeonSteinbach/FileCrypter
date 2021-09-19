# FileCrypter

A tool to encrypt and decrypt single files or folders (recursively).

## Example usage

### Encryption

```
> python .\main.py

What action do you want to execute?
Encrypt [e] | Decrypt [d]: e

Folder to be encrypted (recursively): C:\Users\<user>\<folder_to_encrypt>
Path where the keys will be stored:   C:\Users\<user>\<folder_to_keys>

!!! Attention: All files inside the folder C:\Users\<user>\<folder_to_encrypt>
will be encrypted and can only be accessed by decrypting them again with the keys stored in
C:\Users\<user>\<folder_to_keys> !!!

Confirm [y/n]: y
```

### Decryption

```
> python .\main.py

What action do you want to execute?
Encrypt [e] | Decrypt [d]: d

Folder to be decrypted (recursively): C:\Users\<user>\<folder_to_decrypt>
Path where the keys are stored:       C:\Users\<user>\<folder_to_keys>

!!! Attention: All files inside the folder C:\Users\<user>\<folder_to_decrypt>
will be decrypted with the keys stored in C:\Users\<user>\<folder_to_keys>
and can therefore be accessed again !!!

Confirm [y/n]: y
```

## Disclaimer
I am not responsible for any damage, deleted files or unintended changes to your file system that could potentially happen.

**Use at your own risk!**
