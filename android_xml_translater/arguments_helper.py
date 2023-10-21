import argparse
import re
import os

try:  # Normal way
    from android_xml_translater import DEFAULT_INPUT_FILE, DEFAULT_DESTINATION, DEFAULT_SOURCE
except ImportError:  # For main tests
    from .axt import DEFAULT_INPUT_FILE, DEFAULT_DESTINATION, DEFAULT_SOURCE

try:  # Normal way
    from __version__ import __version__
except ImportError:  # For tests
    from .__version__ import __version__


def get_arguments(arguments):
    parser = argparse.ArgumentParser(
        description="Script to translate Android strings.xml",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file" + os.linesep +
             "example : android-xml-translater -f C:\\strings.xml" + os.linesep +
             "(default: %(default)s)",
        default=DEFAULT_INPUT_FILE
    )

    parser.add_argument(
        "-s",
        "--source",
        help="Input language" + os.linesep +
             "example : google-images-downloader -s en" + os.linesep +
             "(default: %(default)s)",
        default=DEFAULT_SOURCE
    )

    parser.add_argument(
        "-t",
        "--target",
        help="Target languages" + os.linesep +
             "example : android-xml-translater -t fr es de",
        nargs='+',
        required=True
    )

    parser.add_argument(
        "-d",
        "--destination",
        help="Translations destination" + os.linesep +
             "example : android-xml-translater -d C\\my\\destination" + os.linesep +
             "(default: %(default)s)",
        default=DEFAULT_DESTINATION
    )

    parser.add_argument(
        "-v",
        "--version",
        help="Show android-xml-translater version",
        action="version"
    )

    parser.version = __version__

    return parser.parse_args(arguments)
