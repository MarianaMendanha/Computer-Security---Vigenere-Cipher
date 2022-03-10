#!/usr/bin/python3

# python3 trab1.py -cif -msg='mateuslindo' -key='julia'
# python3 trab1.py -decif -msg='vuemubftvdx' -key='julia'
# python3 trab1.py -quebra -msg='fhvzpiehmmnpdlzvdtuoeazncdseaxmdwsoodedqaahpahaztljyhbgtyulrbuifyyigmfxfreimoiywedakqzvvqsamvnzzzeyunamnbrghgmfccweuazdfutargwaruahpvfhpoebwwbneheeawqtktxysmwqryanlvqqgbxadexwtvtwogsviaifvasefnwwehmupjcxgbxnqeubzjrvudekppzrlsztrvjbulnsedjlzedseieosqqgeziebsmzldplvwqbratmlcbsmyrrqmzxdczjezeiiewevoztymtvghrzekbpvqwodegmlbcuepewqymqfhgnbalaahcqsjicgzdkunxbsqfwhqfzzdbguuqgvvpznwodoebsmvqtqremeqgxsqsrltkglozaigznbyedlrbtvjrrpstwxjvqepwzbsiudnpfltznzrdqljmybrqcqskzfkgxrqskwrmahrmtvtzzrpibsluhpvfhxofsdzrdsanrjwmgkeseemcighdxoimxqcvuyijbsmehfarviwenbsrrvmqzbprqpvbtbvrnunamnbrghgmfccweqozcyicipwedijbtkjrrpsvbn' -lang='us'

import sys

ASC_OFFSET = 97
ALF_OFFSET = 26

DE_CIF_ARGS = ['-msg', '-key']
QUEBRA_ARGS = ['-msg', '-lang']

br_freqs = {'a':0.1463, 'b':0.0104, 'c':0.0388, 'd':0.0499, 'e':0.1257,
            'f':0.0102, 'g':0.0130, 'h':0.0128, 'i':0.0618, 'j':0.0040,
            'k':0.0002, 'l':0.0278, 'm':0.0474, 'n':0.0505, 'o':0.1073,
            'p':0.0252, 'q':0.0120, 'r':0.0653, 's':0.0781, 't':0.0434,
            'u':0.0463, 'v':0.0167, 'w':0.0001, 'x':0.0021, 'y':0.0001, 'z':0.0047}
us_freqs = {'a':0.08167, 'b':0.01492, 'c':0.02782, 'd':0.04253, 'e':0.12702,
             'f':0.02228, 'g':0.02015, 'h':0.06094, 'i':0.06966, 'j':0.00153,
             'k':0.00772, 'l':0.04025, 'm':0.02406, 'n':0.06749, 'o':0.07507,
             'p':0.01929, 'q':0.00095, 'r':0.05987, 's':0.06327, 't':0.09056,
             'u':0.02758, 'v':0.00978, 'w':0.02360, 'x':0.00150, 'y':0.01974, 'z':0.00074}

# CIFRADOR #
def Cifrador(plain_msg, key):
    enc_msg = ""
    i = 0

    print("[...] Encoding '%s' with key '%s'" % (plain_msg, key))

    for letra in plain_msg:
        p = ord(letra) - ASC_OFFSET
        k = ord(key[i]) - ASC_OFFSET
        enc_msg += chr(ASC_OFFSET + ((p + k) % ALF_OFFSET))
        
        if i >= len(key) - 1:   i = 0 
        else:   i += 1

    return enc_msg

# DECIFRADOR #
def Decifrador(enc_msg, key):
    plain_msg = ""
    i = 0

    print("[...] Decoding '%s' with key '%s'" % (enc_msg, key))

    for enc in enc_msg:
        c = ord(enc) - ASC_OFFSET
        k = ord(key[i]) - ASC_OFFSET
        plain_msg += chr(ASC_OFFSET + ((c - k + ALF_OFFSET) % ALF_OFFSET))
        
        if i >= len(key) - 1:   i = 0 
        else:   i += 1

    return plain_msg

# QUEBRA CIFRA #
def Quebra_cifra(msg, lang):

    key_len = 0
    lens_ics = {}

    for key_len in range(2, 21):
        coset_s = get_cosets(msg, key_len)
        ic = 0
        for coset in coset_s:
            coset_freqs = get_char_frequencies(coset)
            ic += get_IC(coset_freqs, len(coset))

        ic /= key_len

        lens_ics[key_len] = ic

    closest_ic_len = 0

    if lang == "br":
        closest_ic_len = find_closest_ic(lens_ics, get_IC(br_freqs, 10000))
    elif lang == "us":
        closest_ic_len = find_closest_ic(lens_ics, get_IC(us_freqs, 10000))

    print("[!] Tamanho mais provável (Chave): %d" % closest_ic_len)

    return get_key(msg, lang, closest_ic_len)

def get_char_frequencies(msg):
    frequencies = {}

    for asc_code in range(ASC_OFFSET, ASC_OFFSET + ALF_OFFSET):
        letter_count = msg.count(chr(asc_code))
        frequencies[chr(asc_code)] = letter_count / len(msg)

    return frequencies

def get_key(msg, lang, key_len):

    coset_s = get_cosets(msg, key_len)

    probable_key = ""

    for coset in coset_s:
        coset_X_s = get_coset_X_s(coset, lang)
        min_x = min(coset_X_s, key = coset_X_s.get)
        # print("> Min X² value for '%s': %f" % (chr(ASC_OFFSET + min_x), coset_X_s[min_x]))
        probable_key += chr(ASC_OFFSET + min_x)

    return probable_key

def get_coset_X_s(coset, lang):
    
    X_s = {}
    size = len(coset)

    for shift in range(ALF_OFFSET):
        X_2 = 0
        for asc_code in range(ASC_OFFSET, ASC_OFFSET + ALF_OFFSET):
            count_char = coset.count(chr(asc_code))
            if lang == "br":
                X_2 += ((count_char - (br_freqs[chr(asc_code)]*size))**2) / (br_freqs[chr(asc_code)]*size)
            elif lang == "us":
                X_2 += ((count_char - (us_freqs[chr(asc_code)]*size))**2) / (us_freqs[chr(asc_code)]*size)

        X_s[shift] = X_2

        shifted_coset = ""

        for i in range(len(coset)):
            asc = ord(coset[i]) - ASC_OFFSET
            shifted_coset += chr(ASC_OFFSET + ((asc - 1 + ALF_OFFSET) % ALF_OFFSET))

        coset = shifted_coset

    return X_s

def get_IC(data, n):
    ic = 0

    for freq in data:
        ic += (data[freq]*n) * ((data[freq]*n) - 1)

    ic /= (n * (n - 1))

    return ic

def get_cosets(msg, n):
    coset_s = []
    count = 0

    # Separa a mensagem criptografada em 'n' pedaços para achar a chave usando a decodificação de cesar
    for i in range(n):
        cesar = ""
        
        while i + (count * n) < len(msg):
            cesar += msg[i + (count * n)]
            count += 1
        
        count = 0
        coset_s.append(cesar)

    return coset_s

def find_closest_ic(len_ics, target):
    closest = 0
    closest_dist = None

    for _len in len_ics:
        if closest_dist is None:
            closest = _len
            closest_dist = abs(len_ics[_len] - target)
        else:
            if abs(len_ics[_len] - target) < closest_dist:
                closest = _len
                closest_dist = abs(len_ics[_len] - target)
    
    return closest

def main():

    args = []
    args_vals = []

    # Monta estrutura para verificar os argumentos passados
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            index = sys.argv[i].find('=')
            if index is -1:
                args.append(sys.argv[i])
                args_vals.append('')
            else:
                args.append(sys.argv[i][:index])
                args_vals.append(sys.argv[i][index+1:])      

    print("\n########################################")
    print("# Seguração Computacional - Trabalho 1 #")
    print("########################################\n")

    if len(sys.argv) is 1:
        print(" > Informações sobre os parâmetros (-help)\n")
    elif str(sys.argv[1]) == '-help':
        print(" [*] Cifra -> -cif [mensagem em claro] -key [chave]\n"
              " [*] Decifra -> -decif [mensagem cifrada] -key [chave]\n"
              " [*] Quebra de senha -> -break [mensagem cifrada] -lang [br|us]\n")
    elif str(sys.argv[1]) == '-cif':
        # CODIFICADOR #
        for arg in DE_CIF_ARGS:
            if arg not in args:
                print(" [X] Argumento '%s' não fornecido\n" % arg)
                return

        print(" (*) CODIFICADOR (*)\n")
        print("> Plain text: %s" % sys.argv[2])
        enc_msg = Cifrador(args_vals[1], args_vals[2])
        print("\n> Encrypted text: %s\n" % enc_msg)
    elif str(sys.argv[1]) == '-decif':
        # DECODIFICADOR # 
        for arg in DE_CIF_ARGS:
            if arg not in args:
                print(" [X] Argumento '%s' não fornecido\n" % arg)
                return

        print(" (*) DECODIFICADOR (*)\n")
        print("> Encrypted text: %s" % sys.argv[2])
        plain_msg = Decifrador(args_vals[1], args_vals[2])
        print("\n> Decrypted text: %s\n" % plain_msg)
    elif str(sys.argv[1]) == '-quebra':
        # QUEBRA DE CIFRA (ANÁLISE DE FREQUÊNCIA) # 
        for arg in QUEBRA_ARGS:
            if arg not in args:
                print(" [X] Argumento '%s' não fornecido\n" % arg)
                return

        print(" (*) QUEBRA DE CIFRA (*)\n")
        print("> Encrypted text: %s\n" % args_vals[1])
        print("> Language: %s\n" % args_vals[2])
        key = Quebra_cifra(args_vals[1], args_vals[2])
        print("[!] Found possible key: %s" % key)
        plain_msg = Decifrador(args_vals[1], key)
        print("\n> Decrypted text: %s\n" % plain_msg)
    else:
        print(" [X] Parâmetro '%s' não reconhecido\n" % sys.argv[1])

if __name__=='__main__':
    main()