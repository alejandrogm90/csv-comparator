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
from typing import cast


def showError(num, text):
    print(text)
    exit(num)


if __name__ == '__main__':
    NEW_data = list()
    OLD_data = list()
    fil_NEW = 0
    col_NEW = 0
    leftover_lines = 0

    if len(sys.argv) != 3:
        showError(1, "ERROR:\n"+sys.argv[0]+" fichero1.csv fichero2.csv")

    try:
        with open(sys.argv[1], encoding='unicode_escape') as File:
            reader = csv.reader(File, delimiter=';',
                                quotechar=':', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                OLD_data.append(row)
    except:
        showError(2, "Error: "+sys.argv[1]+" file not found")

    try:
        with open(sys.argv[2], encoding='unicode_escape') as File:
            reader = csv.reader(File, delimiter=';',
                                quotechar=':', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                NEW_data.append(row)
    except:
        showError(3, "Error: "+sys.argv[2]+" file not found")

    if len(NEW_data) > len(OLD_data):
        fil_NEW = len(OLD_data)
        col_NEW = len(OLD_data[0])
        leftover_lines = len(NEW_data) - len(OLD_data)
    else:
        fil_NEW = len(NEW_data)
        col_NEW = len(NEW_data[0])
        leftover_lines = len(OLD_data) - len(NEW_data)

    if leftover_lines != 0:
        showError(4, "The files do not have the same number of lines")

    for fil_ACT in range(fil_NEW):
        for col_ACT in range(col_NEW):
            dato1 = str(NEW_data[fil_ACT][col_ACT])
            dato2 = str(OLD_data[fil_ACT][col_ACT])
            if dato1 != dato2:
                print("Discrepancy: "+dato1+" ||| "+dato2)
                print("ROW: "+str(fil_ACT)+" COLUMN: "+str(col_ACT))
        print("ROW ("+str(fil_ACT)+") status: OK")
