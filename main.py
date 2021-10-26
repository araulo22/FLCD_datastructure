import re

from domain.symboltable import SymbolTable
from domain.pif import PIF
from domain.scanner import Scanner
from domain.languagesetup import *

class Main:
    def __init__(self):
        self.st = SymbolTable(16)
        self.pif = PIF()
        self.scanner = Scanner()

    def run(self):
        read_file()
        file_name = "p1err.txt"
        error = ""

        with open(file_name, 'r') as file:
            lines = 0
            extra = ''
            for line in file:
                lines+=1
                tokens = self.scanner.tokenize(line.strip())
                for i in range(len(tokens)):
                    if tokens[i] in reservedWords+operators+separators:
                        if tokens[i] == ' ':
                            continue
                        self.pif.add(tokens[i], (-1, -1))
                    elif tokens[i] in self.scanner.accepted and i < len(tokens) - 1:
                        if re.match("[1-9]", tokens[i+1]):
                            self.pif.add(tokens[i][:-1], (-1, -1))
                            extra = tokens[i][-1]
                            continue
                        else:
                            error += "Error at token " + tokens[i] + " at line " + str(lines) + "\n"
                    elif self.scanner.isIdentifier(tokens[i]):
                        id = self.st.add(tokens[i])
                        self.pif.add("id " + tokens[i], id)
                    elif self.scanner.isConstant(tokens[i]):
                        const = self.st.add(extra + tokens[i])
                        extra = ''
                        self.pif.add("const", const)
                    else:
                        error += "Error at token " + tokens[i] + " at line " + str(lines) + "\n"

        with open(file_name[:-4] + '_st.out', 'w') as writer:
                writer.write(str(self.st))

        with open(file_name[:-4] + '_pif.out', 'w') as writer:
                writer.write(str(self.pif))

        if error != "":
            print(error)
        else:
            print("no errors found")

main = Main()
main.run()