import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text , shift_amount,encode_or_decode) :
    empty_string = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for item in original_text:
        if item in alphabet :
            index = alphabet.index(item)
            index = shift_amount + index
            index = index % len(alphabet)
            empty_string += alphabet[index]
        else :
            empty_string += item

    print(f"Here is the {encode_or_decode}d result : {empty_string} ")


while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if choice == "yes" :
        continue
    elif choice == "no" :
        print("Good bye")
        break


