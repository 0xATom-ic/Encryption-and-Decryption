def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, 26 - shift % 26)


def show(label, text):
    width = 55
    print(f"\n{'─' * width}")
    print(f"  {label}")
    print(f"{'─' * width}")
    print(f"  {text}")
    print(f"{'─' * width}")


def get_shift():
    while True:
        try:
            shift = int(input("  Pick a shift number (1 to 25): "))
            if 1 <= shift <= 25:
                return shift
            print("  That number is out of range, try something between 1 and 25.")
        except ValueError:
            print("  Please type a whole number.")


def main():
    print("\n" + "=" * 55)
    print("   DECODELABS  |  Caesar Cipher")
    print("=" * 55)
    print("   E = Encrypt    D = Decrypt    Q = Quit")
    print("=" * 55)

    while True:
        print()
        choice = input("  What do you want to do? (E / D / Q): ").strip().upper()

        if choice == 'Q':
            print("\n  Got it, heading back!\n")
            break

        elif choice == 'E':
            plaintext = input("  Type your message: ")
            shift = get_shift()
            ciphertext = encrypt(plaintext, shift)

            show("Your original message", plaintext)
            show(f"Encrypted  (shift = {shift})", ciphertext)

            verified = decrypt(ciphertext, shift)
            status = "✓ Looks good" if verified == plaintext else "✗ Something went wrong"
            print(f"\n  Quick check — decrypted back to: {verified!r}  [{status}]")

        elif choice == 'D':
            ciphertext = input("  Paste the encrypted text: ")
            shift = get_shift()
            plaintext = decrypt(ciphertext, shift)

            show(f"Encrypted text  (shift = {shift})", ciphertext)
            show("Decrypted message", plaintext)

        else:
            print("  Not sure what you meant — use E, D, or Q.")


if __name__ == "__main__":
    main()
