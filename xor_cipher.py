def xor_encrypt(text, key):
    return [ord(char) ^ key for char in text]


def xor_decrypt(byte_values, key):
    return ''.join(chr(byte ^ key) for byte in byte_values)


def to_hex(byte_values):
    return ' '.join(f'{b:02X}' for b in byte_values)


def to_binary(byte_values):
    return ' '.join(f'{b:08b}' for b in byte_values)


def show_bit_table(text, key):
    width = 63
    print(f"\n  {'─' * width}")
    print(f"  {'BIT-LEVEL BREAKDOWN  (key = ' + str(key) + ')':^{width}}")
    print(f"  {'─' * width}")
    print(f"  {'Char':<6} {'ASCII':>6}  {'Binary':^10}  XOR {key:08b}  {'Result':^10}  {'Hex':>4}")
    print(f"  {'─' * width}")
    for char in text[:10]:
        ascii_val = ord(char)
        xored = ascii_val ^ key
        print(f"  {char!r:<6} {ascii_val:>6}  {ascii_val:08b}  XOR {key:08b}  {xored:08b}  {xored:>4X}")
    if len(text) > 10:
        print(f"  ... ({len(text) - 10} more characters)")
    print(f"  {'─' * width}")


def get_key():
    while True:
        try:
            key = int(input("  Enter a key number (1 to 255): "))
            if 1 <= key <= 255:
                return key
            print("  That's out of range — pick something between 1 and 255.")
        except ValueError:
            print("  Please type a whole number.")


def show(label, value):
    width = 55
    print(f"\n{'─' * width}")
    print(f"  {label}")
    print(f"{'─' * width}")
    print(f"  {value}")
    print(f"{'─' * width}")


def main():
    print("\n" + "=" * 55)
    print("   DECODELABS  |  XOR Cipher")
    print("=" * 55)
    print("   E = Encrypt    D = Decrypt")
    print("   B = Bit Table  Q = Quit")
    print("=" * 55)
    print("\n  heads up: XOR uses the exact same step to")
    print("  encrypt and decrypt — same key, same function.")

    stored_bytes = []

    while True:
        print()
        choice = input("  What do you want to do? (E / D / B / Q): ").strip().upper()

        if choice == 'Q':
            print("\n  Got it, heading back!\n")
            break

        elif choice == 'E':
            plaintext = input("  Type your message: ")
            key = get_key()
            byte_values = xor_encrypt(plaintext, key)
            stored_bytes = byte_values

            show("Your original message", plaintext)
            show(f"Encrypted result  (key = {key})", to_hex(byte_values))

            recovered = xor_decrypt(byte_values, key)
            status = "✓ Looks good" if recovered == plaintext else "✗ Something went wrong"
            print(f"\n  Quick check — decrypted back to: {recovered!r}  [{status}]")
            print(f"\n  Binary view: {to_binary(byte_values[:4])} ...")

        elif choice == 'D':
            if stored_bytes:
                print(f"  I still have your last encrypted output ({len(stored_bytes)} bytes).")
                use_stored = input("  Want to decrypt that? (Y / N): ").strip().upper()
                if use_stored == 'Y':
                    key = get_key()
                    plaintext = xor_decrypt(stored_bytes, key)
                    show(f"Encrypted bytes  (key = {key})", to_hex(stored_bytes))
                    show("Decrypted message", plaintext)
                    continue

            raw = input("  Paste hex bytes separated by spaces (e.g. 4A 1F 3C): ")
            try:
                byte_values = [int(b, 16) for b in raw.split()]
                key = get_key()
                plaintext = xor_decrypt(byte_values, key)
                show("Decrypted message", plaintext)
            except ValueError:
                print("  Something looks off with those hex values — try something like: 4A 1F 3C")

        elif choice == 'B':
            text = input("  Type the text you want to inspect: ")
            key = get_key()
            show_bit_table(text, key)

        else:
            print("  Not sure what you meant — use E, D, B, or Q.")


if __name__ == "__main__":
    main()
