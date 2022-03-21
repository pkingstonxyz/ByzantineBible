import os

# I know that I'm violating DRY in this. It's easier for me to do manual adjustments in this specific case

# Removes unwanted characters from the line
def processLine(line):
    return line.replace("ʼ", "'").replace("\uFEFF", "").replace("\u02BA", "\u0374").replace("\u02B9", "\u0374").replace("\\", "").replace("\u2E00", "[").replace("\u2E02", "[").replace("\u2E03", "]").replace("\u2E01", "[").replace("\u2E05", "]").replace("\u27E6", "[[").replace("\u27E7", "]]").replace("\u2E04", "[").replace("\u03DB", "\u03C2")


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

    if currBook != lines[0]:
        outFile.write("\\section{" + lines[0].rstrip()[:-1] + "}\n")
        currBook = lines[0]
    lines = lines[2:]

    outFile.writelines(lines)
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

    if currBook != lines[0]:
        outFile.write("\\section{" + lines[0].rstrip()[:-1] + "}\n")
        currBook = lines[0]
    lines = lines[2:]

    outFile.writelines(lines)
    chap.close()

outFile.write(affix)
outFile.close()

# EXTRA
outFile = open("./build/Extra.tex", "w")
outFile.writelines(prefix)

Extra = [i for i in os.listdir("./texts/ex/") if ".txt" in i]
Extra.sort()

currBook = ""
for chapter in Extra:
    chap = open("./texts/ex/" + chapter, "r")
    lines = chap.readlines()
    lines = [processLine(i) for i in lines]

    if currBook != lines[0]:
        outFile.write("\\section{" + lines[0].rstrip()[:-1] + "}\n")
        currBook = lines[0]
    lines = lines[2:]

    outFile.writelines(lines)
    chap.close()

outFile.write(affix)
outFile.close()

