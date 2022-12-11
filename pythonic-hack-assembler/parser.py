from code import Code
from symbol_table import SymbolTable


class Parser:
    def __init__(self):
        self.code = Code()
        self.symbol_table = SymbolTable()

    def parse(self, expression):
        if self._instruction_type(expression) == 'a':
            return self._symbol(expression[1:])
        else:
            subexpressions = self._get_subexpressions(expression)
            return self._convert_subs_to_binary_expression(subexpressions)

    def _convert_subs_to_binary_expression(self, subexpressions):
        binary_comp = self.code.comp(subexpressions[0])
        binary_dest = self.code.dest(subexpressions[1])
        binary_jump = self.code.jump(subexpressions[2])

        return binary_comp + binary_dest + binary_jump

    def _get_subexpressions(self, expression):
        expression.replace(" ", "")
        subexpressions = expression.split('=|;', expression)
        if len(subexpressions) < 3:
            subexpressions.append('null')

        return subexpressions

    def _instruction_type(self, instruction):
        return 'a' if instruction[0] == '@' else 'c'

    def _symbol(self, symbol, address):
        if self.symbol_table.contains(symbol):
            return '{0:016b}'.format(self.symbol_table[str(symbol)])
        else:
            self.symbol_table.add_entry(symbol, address)
            return '{0:016b}'.format(address)

    def _dest(self, sub_expression):
        return self.code.dest(sub_expression)

    def _comp(self, sub_expression):
        return self.code.comp(sub_expression)

    def _jump(self, sub_expression):
        return self.code.jump(sub_expression)
