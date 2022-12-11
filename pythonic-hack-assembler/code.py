
class Code:
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
            'D|A': '010101'
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

    def comp(self, expression):
        return self.comp[str(expression)] if expression in self.comp else '1000000'

    def dest(self, expression):
        return self.dest[str(expression)] if expression in self.dest else '000'

    def jump(self, expression):
        return self.jump[str(expression)] if expression in self.jump else '000'
