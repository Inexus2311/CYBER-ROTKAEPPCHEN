######################################################################################################################
# Name: Inexus
# Programming: Python
# Project-Date: 16th Dez 2021
# Hacking-Challenge CYBER-ROTKAEPPCHEN
######################################################################################################################

#############################################
# Functions - Group
#############################################

# Controll every cyber_binary Byte for Byte
def check_Byte(txt):
    count = 0
    for _ in txt:
        count += 1
        if count == 8:
            return txt
    while count < 8:
        txt += str(0)
        count += 1
    return txt


# Function Binary to Ascii-char output
def to_ascii(char):
    return chr(int(char, 2))


# Translate one Byte-block of binaries
def translate(txt):
    result_tmp: str = ''
    letters = txt.split(' ')
    for letter in letters:
        byte_var = check_Byte(letter)
        result_tmp += to_ascii(byte_var)
    return result_tmp


##############################################
# main
##############################################

datei = open('cybertext.txt', 'r')
string = datei.read().splitlines()
NewText = list()
cyber_binary = ""
count_index = 0
num_block = 0  # 1 Byte-Block counter

# Split lines in Text
for lines in string:
    if lines.__len__() > 0:
        NewText.append(lines.split())

# Jedes Wort aus Text einzeln lesen
for line in NewText:
    for i in line:
        if count_index <= 8:
            if i.__contains__("Cyber-") or i.__contains__("cyber-"):
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
###################################################################
# Output
###################################################################

print("??bersetze cyber_binary zu einem lesbaren ASCII-Code.... \n")
result = translate(cyber_binary)
print("Das L??sungswort lautet: " + str(result))
print("done")
datei.close()  # Close Text-datafile
