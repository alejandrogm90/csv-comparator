#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import csv
import sys

APP_NAME = 'CSV CMPARTOR'
DELIMITER = ','

def show_error(num, text):
    """ Shows a menssage output and exit
    :param num:
    :param text:
    :return:
    """
    print(text)
    sys.exit(num)


def load_file_in_lines(file_location):
    """ Load all data in a matrix
    :param file_location: the string location of selected file
    :return: matrix_of_elements: matrix with elements
    """
    matrix_of_elements = []
    try:
        with open(file_location, 'r', encoding="utf-8") as current_file:
            reader = csv.reader(current_file, delimiter=DELIMITER, quoting=csv.QUOTE_NONE)
            for line in reader:
                matrix_of_elements.append(line)

    except current_file:
        show_error(2, "Error: " + file_location + " file not found")
    return matrix_of_elements


def get_maximun_lines(first_file, second_file):
    """ Get maximun number of rows and columns
    :param first_file:
    :param second_file:
    :return: max_row, max_column
    """
    if len(first_file) > len(second_file):
        return len(second_file), len(second_file[0])
    return len(first_file), len(first_file[0])


def show_discrepances(file1, file2, max_row, max_column):
    """ Show discrepances betewn 2 csv files
    :param file1:
    :param file2:
    :param max_row:
    :param max_column:
    :return:
    """
    output_string = ""
    num_discrepances = 0
    for current_row in range(max_row):
        for current_column in range(max_column):
            dato1 = str(file1[current_row][current_column])
            dato2 = str(file2[current_row][current_column])
            if dato1 != dato2:
                output_string = output_string + "Discrepancy: " + dato1 + " ||| " + dato2 + " ==> "
                output_string = output_string + "ROW: " + str(current_row) + \
                                " COLUMN: " + str(current_column) + "\n"
                num_discrepances = num_discrepances + 1
        #output_string = output_string + "ROW (" + str(current_row) + ") status: OK" + "\n"
    return num_discrepances, output_string




def frame(root, side):
    """ Show discrepances betewn 2 csv files
    :param root:
    :param side:
    :return w:
    """
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class Calculator(Frame):
    """ Show discrepances betewn 2 csv files
    :param Frame:
    :return :
    """
    
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculadora')
        #self.master.iconname("cal1")
        first_frame = frame(self, TOP)
        self.selected = IntVar()
        rad1 = Radiobutton(first_frame, text='Union', value=1, variable=self.selected)
        rad2 = Radiobutton(first_frame, text='Intersection', value=2, variable=self.selected)
        rad1.grid(column=0, row=0)
        rad2.grid(column=1, row=0)
        button1 = Button(first_frame, text="Click Me", command=self.clicked)
        button1.grid(column=0, row=1)
        self.path_file1 = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/",
            title="Open CSV file 1",
            filetypes=(("CSV Files", "*.csv"),)
        )
        self.path_file2 = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/",
            title="Open CSV file 2",
            filetypes=(("CSV Files", "*.csv"),)
        )

    def clicked(self):
        if self.selected.get() == -1:
            messagebox.showerror('ERROR', 'Empty element: '+str(self.selected.get()))
        else:
            if self.selected.get() == 1:
                first_file = load_file_in_lines(self.path_file1)
                second_file = load_file_in_lines(self.path_file2)
                max_row, max_column = get_maximun_lines(first_file, second_file)
                num_d, output_s = show_discrepances(first_file, second_file, max_row, max_column)
                print(output_s)
            else:
                messagebox.showerror('ERROR', 'Empty element: ' + str(self.selected.get()))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        Calculator().mainloop()
    else:
        if len(sys.argv) != 3:
            show_error(1, "ERROR:\n" + sys.argv[0] + " fichero1.csv fichero2.csv")

        first_file = load_file_in_lines(sys.argv[1])
        second_file = load_file_in_lines(sys.argv[2])
        size_first_file = len(first_file)
        size_second_file = len(second_file)

        if (size_first_file - size_second_file) != 0:
            print(sys.argv[1] + " have " + str(size_first_file) + " lines.")
            print(sys.argv[2] + " have " + str(size_second_file) + " lines.")
            show_error(3, "The files do not have the same number of lines")

        max_row, max_column = get_maximun_lines(first_file, second_file)

        show_discrepances(first_file, second_file, max_row, max_column)
