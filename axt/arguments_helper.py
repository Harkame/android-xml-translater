import argparse
import re
import os

try:  # Normal way
    from axt import DEFAULT_INPUT_FILE, DEFAULT_DESTINATION, DEFAULT_SOURCE
except ImportError:  # For main tests
    from .__main__ import DEFAULT_INPUT_FILE, DEFAULT_DESTINATION, DEFAULT_SOURCE

try:  # Normal way
    from __version__ import __version__
except ImportError:  # For tests
    from .__version__ import __version__


def get_arguments(arguments):
    parser = argparse.ArgumentParser(
        description="Script to download images from a \"Google Images\" query",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Google Images queries" + os.linesep +
             "example (single)   : google-images-downloader -q cat",
        default=DEFAULT_INPUT_FILE
    )

    parser.add_argument(
        "-s",
        "--source",
        help="Google Images queries" + os.linesep +
             "example (single)   : google-images-downloader -q cat",
        default=DEFAULT_SOURCE
    )

    parser.add_argument(
        "-t",
        "--target",
        help="Translation targets" + os.linesep +
             "example (single)   : android-xml-translater -t fr" + os.linesep +
             "example (multiple) : google-images-downloader -t fr de es",
        nargs='+',
        required=True
    )

    parser.add_argument(
        "-d",
        "--destination",
        help="Translation targets" + os.linesep +
             "example : android-xml-translater -d C\\my\\destination",
        default=DEFAULT_DESTINATION
    )

    parser.add_argument(
        "-v",
        "--version",
        help="Show google-images-downloader version",
        action="version"
    )

    parser.version = __version__

    return parser.parse_args(arguments)
