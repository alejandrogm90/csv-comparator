#!/usr/bin/env python3

#
#
#       Copyright 2021 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Save as UTF-8 encoded CSV (comma delimited)

import sys
import csv

DELIMITER=';'
QUOTECHAR=':'

def showError(num, text):
    print(text)
    exit(num)
    
def loadFileInLines(fileLocation):
    currentFile = list()
    try:
        with open(fileLocation) as File:
            reader = csv.reader(File, delimiter=DELIMITER, quotechar=QUOTECHAR, quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                currentFile.append(row)
    except:
        showError(2, "Error: " + fileLocation + " file not found")
    return currentFile

if __name__ == '__main__':
    if len(sys.argv) != 3:
        showError(1, "ERROR:\n"+sys.argv[0]+" fichero1.csv fichero2.csv")

    file1_lines = loadFileInLines(sys.argv[1])
    file2_lines = loadFileInLines(sys.argv[2])
    fil_NEW = 0
    col_NEW = 0
    leftover_lines = 0

    if len(file1_lines) > len(file2_lines):
        fil_NEW = len(file2_lines)
        col_NEW = len(file2_lines[0])
        leftover_lines = len(file1_lines) - len(file2_lines)
    else:
        fil_NEW = len(file1_lines)
        col_NEW = len(file1_lines[0])
        leftover_lines = len(file2_lines) - len(file1_lines)

    for fil_ACT in range(fil_NEW):
        for col_ACT in range(col_NEW):
            dato1 = str(file1_lines[fil_ACT][col_ACT])
            dato2 = str(file2_lines[fil_ACT][col_ACT])
            if dato1 != dato2:
                print("Discrepancy: "+dato1+" ||| "+dato2)
                print("ROW: "+str(fil_ACT)+" COLUMN: "+str(col_ACT))
        print("ROW ("+str(fil_ACT)+") status: OK")

    if leftover_lines != 0:
        print(sys.argv[1] + " have " + str(len(file1_lines)) + " lines.")
        print(sys.argv[2] + " have " + str(len(file2_lines)) + " lines.")
        showError(3, "The files do not have the same number of lines")