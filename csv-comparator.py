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

def showError(num, text):
    print(text)
    exit(num)
    
def loadFileInLines(fileLocation):
    matrixOfElements = list()
    try:
        with open(fileLocation) as currentFile:
            reader = csv.reader(currentFile, delimiter=DELIMITER, quoting=csv.QUOTE_NONE)
            for line in reader:
                matrixOfElements.append(line)
    except:
        showError(2, "Error: " + fileLocation + " file not found")
    return matrixOfElements

def getMaximunLines(firstFile, secondFile, sizeFirstFile, sizeSecondFile):
    if sizeFirstFile > sizeSecondFile:
        mr = sizeSecondFile
        mc = len(secondFile[0])
    else:
        mr = sizeFirstFile
        mc = len(firstFile[0])

    return mr, mc

def showdiscrepances(file1, file2, mr, mc):
    for currentRow in range(mr):
        for currentColumn in range(mc):
            dato1 = str(file1[currentRow][currentColumn])
            dato2 = str(file2[currentRow][currentColumn])
            if dato1 != dato2:
                print("Discrepancy: "+dato1+" ||| "+dato2)
                print("ROW: "+str(currentRow)+" COLUMN: "+str(currentColumn))
        print("ROW ("+str(currentRow)+") status: OK")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        showError(1, "ERROR:\n"+sys.argv[0]+" fichero1.csv fichero2.csv")

    FIRST_FILE = loadFileInLines(sys.argv[1])
    SECOND_FILE = loadFileInLines(sys.argv[2])
    SIZE_FIRST_FILE = len(FIRST_FILE)
    SIZE_SECOND_FILE = len(SECOND_FILE)

    if ( SIZE_FIRST_FILE - SIZE_SECOND_FILE) != 0:
        print(sys.argv[1] + " have " + str(SIZE_FIRST_FILE) + " lines.")
        print(sys.argv[2] + " have " + str(SIZE_SECOND_FILE) + " lines.")
        showError(3, "The files do not have the same number of lines")

    MAX_ROW, MAX_COLUMN = getMaximunLines(FIRST_FILE, SECOND_FILE, SIZE_FIRST_FILE, SIZE_SECOND_FILE)

    showdiscrepances(FIRST_FILE, SECOND_FILE, MAX_ROW, MAX_COLUMN)