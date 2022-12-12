class SymbolTable:
    def __init__(self):
        self.current_available_address = 16
        self.data = {
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            '11': 11,
            '12': 12,
            '13': 13,
            '14': 14,
            '15': 15,
            'SCREEN': 16384,
            'KBD': 24576,
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4
        }

    def add_entry(self, symbol, address):
        if (not self.contains(symbol)) and '@' in symbol:
            self.data[symbol.replace('@', '')] = self.current_available_address
            self.current_available_address += 1
        elif '(' in symbol:
            self.data[symbol[1:-1]] = address
        else:
            self.data[symbol] = address

    def contains(self, symbol):
        return True if symbol in self.data else False

    def get_address(self, symbol):
        return self.data[str(symbol)]
