import importlib
import sys
import os

CIPHERS = {
    '1': ('caesar_cipher',   'Caesar Cipher    — shift by a number'),
    '2': ('vigenere_cipher', 'Vigenere Cipher  — shift by a keyword'),
    '3': ('xor_cipher',      'XOR Cipher       — binary level encryption'),
}

SEPARATOR = "=" * 55

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"\n{SEPARATOR}")
    print("   DECODELABS  |  Cybersecurity Project 2")
    print("   Basic Encryption & Decryption Suite")
    print(SEPARATOR)
    print("   Pick a cipher to work with:\n")
    for key, (_, desc) in CIPHERS.items():
        print(f"   [{key}]  {desc}")
    print(f"\n   [Q]  Quit")
    print(SEPARATOR)

def main():
    clear()
    while True:
        print_header()
        choice = input("\n  Your choice: ").strip().upper()

        if choice == 'Q':
            print("\n  Alright, see you next time. Stay secure!\n")
            sys.exit(0)

        if choice in CIPHERS:
            module_name, _ = CIPHERS[choice]
            try:
                module = importlib.import_module(module_name)
                clear()
                module.main()
                input("\n  Done! Press Enter to go back to the main menu...")
                clear()
            except ModuleNotFoundError:
                print(f"\n  Hmm, can't find '{module_name}.py'.")
                print("  Make sure all four files are sitting in the same folder.")
                input("  Press Enter to continue...")
        else:
            print("  That's not a valid option — try 1, 2, 3, or Q.")


if __name__ == "__main__":
    main()
