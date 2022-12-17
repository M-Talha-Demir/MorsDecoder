mors_dic = {
"A":".-",
"B":"-...",
"C":"-.-.",
"D":"-..",
"E":".",
"F":"..-.",
"G":"--.",
"H":"....",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--..",
"Ç":"-.-..",
"Ğ":"--.-.",
"İ":".-..-",
"Ö":"---.",
"Ş":".--..",
"Ü":"..--",
"0":"-----",
"1":".----",
"2":"..---",
"3":"...--",
"4":"....-",
"5":".....",
"6":"-....",
"7":"--...",
"8":"---..",
"9":"----.",
".":".-.-.-",
",":"--..--",
"?":"..--..",
"'":".----.",
"!":"-.-.--",
"/":"-..-.",
"(":"-.--.",
")":"-.--.-",
"&":".-...",
":":"---...",
";":"-.-.-.",
"=":"-...-",
"+":".-.-.",
"-":"-....-",
"_":"..--.-",
"\"":".-..-.",
"$":"...-..-",
"@":".--.-.",
"¿":"..-.-",
"¡":"--...-"}


def mors_converter(sentence):
    convert_sentence = ""
    for word in sentence.split(" "):
        for letter in word:
            convert_sentence += mors_dic[letter.upper()]
            convert_sentence += " "
        convert_sentence += "/"

    return convert_sentence


def mors_translater(sentence):
    convert_sentence = ""
    for word in sentence.split(" / "):
        for letter in word.split(" "):
            value = [i for i in mors_dic if mors_dic[i] == letter]
            # print(value)
            convert_sentence += str(value[0]).upper()
        convert_sentence += " "

    return convert_sentence


print(mors_converter(input("Enter the sentence you want to convert to morse code: ")))

print(mors_translater(input("Enter the morse code you want to translate into a sentence.")))

