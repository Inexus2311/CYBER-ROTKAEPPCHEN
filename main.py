import re

datei = open('cybertext.txt', 'r')
string = datei.read().splitlines()
NewText = list()
cyber_binary = ""
count_index = 0
num_block = 0 # 1 Byte-Block counter


# Kontrolliere cyber_binary Byte für Byte

def check_Byte(txt):
    count = 0
    for i in txt:
        count+=1
        if count ==8:
            return txt
    while count <8:
        txt += str(0)
        count += 1
    return txt

# Function Binary to Ascii-char output
def to_ascii(char):
    return chr(int(char, 2))

# Translate one Byte-block of binaries
def translate(txt):
    result = ''
    letters = txt.split(' ')
    for letter in letters:
        byte_var = check_Byte(letter)
        result += to_ascii(byte_var)
    return result

# Split lines in Text
for lines in string:
    if lines.__len__() > 0:
        NewText.append(lines.split())


# Jedes Wort aus Text einzeln lesen
for line in NewText:
    for i in line:
        if count_index <= 8:
            if  i.__contains__("Cyber-") or i.__contains__("cyber-"):
                cyber_binary += str(1)
                count_index = count_index + 1
            elif i.__contains__("Cyber") or i.__contains__("cyber"):
                cyber_binary += str(0)
                count_index = count_index + 1

            if cyber_binary.__len__() > 0 and count_index == 8:
                num_block += 1
                if num_block < 23:
                    cyber_binary += str(' ')
                count_index = 0

print("Übersetze cyber_binary zu einem lesbaren ASCII-Code.... \n")
result = translate(cyber_binary)
print("Das Lösungswort lautet: " + str(result))
print("done")


datei.close()