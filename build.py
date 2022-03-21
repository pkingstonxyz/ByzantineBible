import os

# Removes unwanted characters from the line
def processLine(line):
    return line.replace("ʼ", "'").replace("\uFEFF", "").replace("\u02BA", "\u0374").replace("\u02B9", "\u0374")


# Gets document prefix and Affix
base = open("./build/Base.tex", "r")
prefix = base.readlines()
base.close()

affix = "\end{document}"


# OLD TESTAMENT
outFile = open("./build/OldTestament.tex", "w")
outFile.writelines(prefix)

OldTestament = [i for i in os.listdir("./texts/ot/") if ".txt" in i]
OldTestament.sort()

currBook = ""
for chapter in OldTestament:
    chap = open("./texts/ot/" + chapter, "r")
    lines = chap.readlines()
    lines = [processLine(i) for i in lines]
    outFile.writelines(lines)
    outFile.write("\n")
    chap.close()

outFile.write(affix)
outFile.close()

# NEW TESTAMENT
outFile = open("./build/NewTestament.tex", "w")
outFile.writelines(prefix)

NewTestament = [i for i in os.listdir("./texts/nt/") if ".txt" in i]
NewTestament.sort()

currBook = ""
for chapter in NewTestament:
    chap = open("./texts/nt/" + chapter, "r")
    lines = chap.readlines()
    lines = [processLine(i) for i in lines]
    outFile.writelines(lines)
    outFile.write("\n")
    chap.close()

outFile.write(affix)
outFile.close()

# NEW TESTAMENT
outFile = open("./build/Extra.tex", "w")
outFile.writelines(prefix)

Extra = [i for i in os.listdir("./texts/ex/") if ".txt" in i]
Extra.sort()

currBook = ""
for chapter in Extra:
    chap = open("./texts/ex/" + chapter, "r")
    lines = chap.readlines()
    lines = [processLine(i) for i in lines]
    outFile.writelines(lines)
    outFile.write("\n")
    chap.close()

outFile.write(affix)
outFile.close()

