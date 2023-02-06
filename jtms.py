#!/opt/homebrew/bin/python3.11

from src.cmd_parsers import parse_cmd
from src.exceptions import ArgumentNotFoundError
from src.convertes import Converter
from src.readers import StdinReader, FileReader
from src.stdouts import ConsoleStdout
from src.translators import Translator


if __name__ == "__main__":
    try:
        file_name = parse_cmd()
        reader = FileReader(file_name)
    except ArgumentNotFoundError:
        reader = StdinReader()
    translator = Translator(reader)
    data = translator.translate_data()
    converter = Converter(data)
    models = converter.to_model()
    console = ConsoleStdout(models)
    console.print()
