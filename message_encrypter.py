from art import logo

alphabet = [

    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',

    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

]

print(logo)

def caesar(plain_text, shift_ammount, action_decl):

    modi_txt = ""

    for letter in plain_text:

      if letter not in alphabet:

        modi_txt += letter

      else:

       new_postn = alphabet.index(letter) + shift_ammount

       if action_decl == "encode":

            while new_postn > 25:

                new_postn = new_postn - 26

            if new_postn <= 25:

                modi_txt += alphabet[new_postn]

            else:

                modi_txt += alphabet[alphabet.index(letter) + shift_ammount]

       elif action_decl == "decode":

         if letter not in alphabet:

           modi_txt += letter

         new_postn = alphabet.index(letter) - shift_ammount

         while new_postn < 0:

                new_postn = 26 + new_postn

         if new_postn >= 0:

                modi_txt += alphabet[new_postn]

         else:

                modi_txt += alphabet[alphabet.index(letter) + shift_ammount]

    print(f"The {action_decl}d message is {modi_txt}.")

should_continue = True

while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  text = input("Type your message:\n").lower()

  shift = int(input("Type the shift number:\n"))

  caesar(plain_text=text, 

 shift_ammount=shift, action_decl=direction)

  result = input("You want to continue? 'Yes' or 'No'.").lower()

  if result == "no":

   should_continue = False

   print("Goodbye.")

