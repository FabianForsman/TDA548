# package samples.filehandling;

# import java.io.*;
# import java.nio.file.Files;
# import java.nio.file.Path;
# import java.nio.file.Paths;

# *   Working with files (i.e. persistent data, data surviving the execution)
# *
# *   This also show usage of static, we don't need an object, it's
# *   pure functionality
# *
# *   *** This will NOT show up on exam (it's general knowledge) ***
from typing import List
import pickle   # for object serialization


class FileService:
    # ---------- Text files -----------------
    @staticmethod
    def read_file_as_lines(path: str):
        # Use with resource to ensure stream is closed
        with open(path, mode='rt', encoding='utf-8') as file_reader:
            lines = []
            while (line := file_reader.readline()) != '':
                actual_line = line.strip('\n')  # readline() includes \n at the end, unless last line
                lines.append(actual_line)
            return lines

    @staticmethod
    def write_file_from_lines(path: str, lines: List[str]):
        with open(path, mode='wt', encoding='utf-8') as file_writer:
            for line in lines:
                file_writer.write(line)
                file_writer.write('\n')

    # ---------- Binary files -----------------
    @staticmethod
    def write_object_file(path: str, obj):
        # Use with resource to ensure stream is closed
        with open(path, mode="wb") as object_writer:
            pickle.dump(obj, object_writer)
            # object_writer.write(obj)

    @staticmethod
    def read_object_file(path):
        with open(path, mode="rb") as object_reader:
            return pickle.load(object_reader)
            # return object_reader.read()

    # We don't ever want objects of type FileService, it's purely static.
    def __init__(self):
        raise NotImplementedError()
