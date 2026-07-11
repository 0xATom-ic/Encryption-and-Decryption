def clean_keyword(keyword):
    cleaned = ''.join(c for c in keyword if c.isalpha()).upper()
    if not cleaned:
        raise ValueError("The keyword needs at least one letter in it.")
    return cleaned


def encrypt(text, keyword):
    keyword = clean_keyword(keyword)
    result = ""
    k_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[k_index % len(keyword)]) - ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
            k_index += 1
        else:
            result += char
    return result


def decrypt(text, keyword):
    keyword = clean_keyword(keyword)
    result = ""
    k_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[k_index % len(keyword)]) - ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
            k_index += 1
        else:
            result += char
    return result


def show_key_table(keyword):
    keyword = clean_keyword(keyword)
    width = 55
    print(f"\n  {'─' * (width - 2)}")
    print(f"  {'HOW YOUR KEYWORD BREAKS DOWN':^{width - 2}}")
    print(f"  {'─' * (width - 2)}")
    print(f"  {'Position':<12} {'Letter':<14} {'Shift'}")
    print(f"  {'─' * (width - 2)}")
    for i, letter in enumerate(keyword):
        shift = ord(letter) - ord('A')
        print(f"  {i:<12} {letter:<14} +{shift}")
    print(f"  {'─' * (width - 2)}")


def show(label, text):
    width = 55
    print(f"\n{'─' * width}")
    print(f"  {label}")
    print(f"{'─' * width}")
    print(f"  {text}")
    print(f"{'─' * width}")


def get_keyword():
    while True:
        kw = input("  Enter your keyword (letters only): ").strip()
        try:
            return clean_keyword(kw)
        except ValueError as e:
            print(f"  {e}")


def main():
    print("\n" + "=" * 55)
    print("   DECODELABS  |  Vigenere Cipher")
    print("=" * 55)
    print("   E = Encrypt    D = Decrypt")
    print("   T = Key Table  Q = Quit")
    print("=" * 55)

    while True:
        print()
        choice = input("  What do you want to do? (E / D / T / Q): ").strip().upper()

        if choice == 'Q':
            print("\n  Got it, heading back!\n")
            break

        elif choice == 'E':
            plaintext = input("  Type your message: ")
            keyword = get_keyword()
            ciphertext = encrypt(plaintext, keyword)

            show("Your original message", plaintext)
            show(f"Keyword used  [{keyword}]", "")
            show("Encrypted result", ciphertext)

            recovered = decrypt(ciphertext, keyword)
            status = "✓ Looks good" if recovered == plaintext else "✗ Something went wrong"
            print(f"\n  Quick check — decrypted back to: {recovered!r}  [{status}]")

        elif choice == 'D':
            ciphertext = input("  Paste the encrypted text: ")
            keyword = get_keyword()
            plaintext = decrypt(ciphertext, keyword)

            show(f"Encrypted text  (keyword = {keyword})", ciphertext)
            show("Decrypted message", plaintext)

        elif choice == 'T':
            keyword = get_keyword()
            show_key_table(keyword)

        else:
            print("  Not sure what you meant — use E, D, T, or Q.")


if __name__ == "__main__":
    main()
