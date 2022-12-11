from parser import Parser


class HackAssembler:
    def __init__(self, input_file_path, output_file_path):
        self.parser = Parser()
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

   def _read_file():
        input_file = open(self.input_file_path, "r")

