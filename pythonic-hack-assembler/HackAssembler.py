import sys
from hack_assembler import HackAssembler


def main():
    hack_assembler = HackAssembler(sys.argv[1])
    hack_assembler.assemble()


if __name__ == '__main__':
    main()
