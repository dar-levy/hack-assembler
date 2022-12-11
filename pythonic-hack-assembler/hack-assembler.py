import os.path

from parser import Parser


class HackAssembler:
    def __init__(self, input_file_path):
        self.parser = Parser()
        self.binary_file_content = []
        self.file_content = _read_file(input_file_path)
        self.output_file_path = os.path.dirname(input_file_path)


    def assemble(self):
        pass

   def _read_file(self, file_path):
        input_file = open(file_path, "r")
        lines = input_file.readlines()
        input_file.close()

        return lines

