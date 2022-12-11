from hack_assembler import HackAssembler


def main():
    file_path = "Add.asm"
    hack_assembler = HackAssembler(file_path)
    hack_assembler.assemble()


if __name__ == '__main__':
    main()
