class CodeGenerator:
    def __init__(self):
        self.comp = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101',
            'M': '110000',
            '!M': '110001',
            '-M': '110011',
            'M+1': '110111',
            'M-1': '110010',
            'D+M': '000010',
            'D-M': '010011',
            'M-D': '000111',
            'D&M': '000000',
            'D|M': '010101',
        }

        self.dest = {
            'M': '001',
            'D': '010',
            'DM': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'ADM': '111',
        }

        self.jump = {
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
        }

    def get_comp(self, expression):
        return self.comp[expression]

    def get_dest(self, expression):
        return self.dest[expression] if expression in self.dest else '000'

    def get_jump(self, expression):
        return self.jump[expression] if expression in self.jump else '000'
