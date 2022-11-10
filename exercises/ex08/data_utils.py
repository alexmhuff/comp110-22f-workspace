"""Dictionary related utility functions."""

__author__ = "730484416"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produe a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, list[str]] = table[0]
    for column in first_row:
        result[column] = column_values(table, column)
    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if rows == 0:
        empty_list: list[str] = []
        for i in column_table:
            result[i] = empty_list
        return result
    for i in column_table:
        if rows > len(column_table[i]):
            return column_table
        new_list: list[str] = []
        j: int = 0
        while j < rows:
            new_list.append(column_table[i][j])
            j += 1
        result[i] = new_list
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of columns."""
    result: dict[str, list[str]] = {}
    for i in column_names:
        result[i] = column_table[i]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for i in table_1:
        result[i] = table_1[i]
    for i in table_2:
        if i not in result:
            result[i] = table_2[i]
        else:
            for j in table_2[i]:
                result[i].append(j)
    return result


def count(freq: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the given list."""
    result: dict[str, int] = {}
    for i in freq:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result