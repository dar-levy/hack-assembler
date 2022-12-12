from code_generator import CodeGenerator
from symbol_table import SymbolTable
import re


class Parser:
    def __init__(self):
        self.code = CodeGenerator()
        self.symbol_table = SymbolTable()

    def parse(self, expression, address):
        if '(' in expression:
            self.symbol_table.add_entry(expression, address)
            return -1
        elif self._instruction_type(expression) == 'a':
            return self._symbol(expression, address)
        else:
            subexpressions = self._get_subexpressions(expression)
            return self._convert_c_instruction_to_binary(subexpressions)

    def _convert_c_instruction_to_binary(self, subexpressions):
        binary_dest = self._dest(subexpressions[0])
        binary_comp = self._comp(subexpressions[1])
        binary_jump = self._jump(subexpressions[2])
        a = '1' if 'M' in subexpressions[1] else '0'

        return '111' + a + binary_comp + binary_dest + binary_jump

    def _get_subexpressions(self, expression):
        expression.replace(" ", "")
        subexpressions = re.split('=|;', expression)
        if len(subexpressions) < 3:
            subexpressions.append('null')

        return subexpressions

    def _instruction_type(self, instruction):
        return 'a' if instruction[0] == '@' else 'c'

    def _symbol(self, symbol, address):
        if self.symbol_table.contains(symbol.replace('@', '')):
            return '{0:016b}'.format(self.symbol_table.get_address(symbol.replace('@', '')))
        else:
            self.symbol_table.add_entry(symbol, address)
            return '{0:016b}'.format(address)

    def _dest(self, sub_expression):
        return self.code.get_dest(sub_expression)

    def _comp(self, sub_expression):
        return self.code.get_comp(sub_expression)

    def _jump(self, sub_expression):
        return self.code.get_jump(sub_expression)
