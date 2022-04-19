first_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Casesar's Cipher Coder and Decoder


def decoder(message, offset):
    decoded_message = ''
    new_index = None
    for symbol in message:
        if symbol in alphabet:
            symbol = alphabet[(alphabet.find(symbol) + offset) % 26]
        decoded_message += symbol
    return decoded_message


first_message_decoded = decoder(first_message, 10)
print(first_message_decoded)
print('\n')


def coder(message, offset):
    coded_message = ''
    new_index = None
    for symbol in message:
        if symbol in alphabet:
            new_index = alphabet.find(symbol) - offset
        symbol = alphabet[new_index]
        coded_message += symbol
    return coded_message


second_message = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud'
third_message = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

second_message_decoded = decoder(second_message, 10)
print(second_message_decoded)
print('\n')
third_message_decoded = decoder(third_message, 14)
print(third_message_decoded)
print('\n')
fourth_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# Bruteforcing loop:
# for offset in range(1, 26):
#     print('offset: ' + str(offset))
#     print('\t' + decoder(fourth_message, offset) + '\n')


fifth_message = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'
key = 'friends'


# Vigeneres Cipher Coder and Decoder


def cipher(message, keyword):
    message_in_key = ''
    message_coded = ''
    i = 0
    for symbol in message:
        if symbol in alphabet:
            if i < len(keyword):
                symbol = keyword[i]
                i += 1
            else:
                symbol = keyword[0]
                i = 1
        message_in_key += symbol
    for x in range(len(message)):
        if message[x] in alphabet:
            message_coded += alphabet[(alphabet.find(message[x]) + alphabet.find(message_in_key[x])) % 26]
        else:
            message_coded += message[x]
    return message_coded


def decipher(message, keyword):
    message_in_key = ''
    message_decoded = ''
    i = 0
    for symbol in message:
        if symbol in alphabet:
            if i < len(keyword):
                symbol = keyword[i]
                i += 1
            else:
                symbol = keyword[0]
                i = 1
        message_in_key += symbol
    for x in range(len(message)):
        if message[x] in alphabet:
            new_index = alphabet.find(message[x]) - alphabet.find(message_in_key[x])
            message_decoded += alphabet[new_index]
        else:
            message_decoded += message[x]
    return message_decoded


fifth_message_decoded = decipher(fifth_message, key)
print(fifth_message_decoded + '\n')
fifth_message_coded = cipher(fifth_message_decoded, key)
print(fifth_message_coded + '\n')
