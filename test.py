
from csv_comparator import *
import os

FILE_1=os.path.abspath("documentos/file_1.csv")
FILE_2=os.path.abspath("documentos/file_2.csv")


def test_load_file_in_lines():
    assert len(load_file_in_lines(FILE_1)) != 0

def test_get_maximun_lines():
    max_row, max_column = get_maximun_lines(FILE_1, FILE_2)
    assert max_row != 0
    assert max_column != 0

def test_show_discrepances():
    max_row, max_column = get_maximun_lines(FILE_1, FILE_2)
    assert show_discrepances(FILE_1, FILE_2, max_row, max_column) != 0


