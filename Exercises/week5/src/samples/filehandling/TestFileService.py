# package samples.filehandling

import os.path as p
import os
from FileService import FileService


# Testing FileService, a class to test file IO
#
# Run this and inspect junk.txt and Niklas.ser (.ser are binary files)
def test():
    print(os.getcwd())
    # Possible IO exception
    try:
        data = ["a", "b", "c", "d", "e"]
        test_text_read_write_identity(data)
    except IOError as e:
        print(e)

    # Object to store
    obj = MyClass("Pelle")
    obj.set_name("Niklas");
    try:
        test_object_read_write_identity(obj)
    except IOError as e:
        print(e)


def test_object_read_write_identity(obj):
    path = make_os_indep_object_path(obj)
    FileService.write_object_file(path, obj)  # Write full object to file
    obj1 = FileService.read_object_file(path)  # Read object back
    print(f"Objects have same name: {obj.get_name() == obj1.get_name()}")   # Same content ...
    print(f"Objects have different identities: {obj is not obj1}")          # ...but different object!


def make_os_indep_object_path(obj):
    path = p.join("files", f"{obj.get_name()}.ser")  # Get an os-independent path
    return path


# ------- Class to use for binary file handling ------------------
class MyClass:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


def test_text_read_write_identity(data):
    path = make_os_indep_text_path()
    FileService.write_file_from_lines(path, data)
    copy = FileService.read_file_as_lines(path)
    print(f"All lines are equal: {check_all_lines_equal(copy, data)}")


def check_all_lines_equal(copy, data):
    b = True
    # Check that what read is same as what we wrote
    for i in range(len(data)):
        b = b and data[i] == copy[i]
    return b


def make_os_indep_text_path():
    path = p.join("files", "junk.txt")  # Get an os-independent path
    return path


if __name__ == "__main__":
    test()
