import os
from parser import Parser


class HackAssembler:
    def __init__(self, input_file_path):
        self.parser = Parser()
        self.binary_file_content = []
        self.file_content = self._read_file(input_file_path)
        self.output_file_path = os.path.dirname(input_file_path) + '\\output_file.hack'

    def assemble(self):
        current_index = 0
        for line in self.file_content:
            if not line.strip() or '//' not in line:
                binary_line = self.parser.parse(line, current_index)
                if binary_line != -1:
                    self.binary_file_content.append(binary_line)
                    current_index += 1

    def _write_to_file(self):
        with open(self.output_file_path, 'w') as output_file:
            output_file.write('\n'.join(self.binary_file_content))

        output_file.close()

    def _read_file(self, file_path):
        with open(file_path, "r") as input_file:
            lines = input_file.readlines()

        input_file.close()
        return lines
