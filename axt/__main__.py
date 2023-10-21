import sys
import os

from axt import AndroidXMLTranslater
from arguments_helper import get_arguments

DEFAULT_INPUT_FILE = os.path.join(".", "strings.xml")
DEFAULT_DESTINATION = os.path.join(".")


def main(argv=None):
    if not argv:
        argv = sys.argv[1:]

    arguments = get_arguments(argv)

    translater = AndroidXMLTranslater(file=arguments.file, destination=arguments.destination, source=arguments.source)

    for target in arguments.target:
        translater.translate(target)


if __name__ == "__main__":
    main(sys.argv[1:])
