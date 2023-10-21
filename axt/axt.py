import os
import codecs
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

DEFAULT_INPUT_FILE = os.path.join(".", "strings.xml")
DEFAULT_DESTINATION = os.path.join(".")
DEFAULT_SOURCE = 'auto'

DEFAULT_ENCODING = "UTF-8"


class AndroidXMLTranslater:
    def __init__(self, file=DEFAULT_INPUT_FILE, destination=DEFAULT_DESTINATION, source=DEFAULT_SOURCE):
        self.file = file
        self.destination = destination

        self.file_name = os.path.basename(self.file)
        self.source = source

        with codecs.open(self.file, "r", DEFAULT_ENCODING) as file:
            self.data = file.read()

    def translate(self, target):
        translator = GoogleTranslator(source=self.source, target=target)

        xml_file = BeautifulSoup(self.data, "xml")

        string_tags = xml_file.find_all('string')
        plurals_tags = xml_file.find_all('plurals')

        for tag in string_tags:
            if tag.has_attr('translatable') and tag['translatable'] == 'false':
                tag.decompose()
                continue

            tag.string = translator.translate(tag.text)

        for tag in plurals_tags:
            if tag.has_attr('translatable') and tag['translatable'] == 'false':
                tag.decompose()
                continue

            item_tags = tag.find_all("item")

            for item_tag in item_tags:
                item_tag.string = translator.translate(item_tag.text)

        target_folder = os.path.join(self.destination, target)
        os.makedirs(target_folder, exist_ok=True)

        target_file = os.path.join(target_folder, self.file_name)

        with codecs.open(target_file, "w+", DEFAULT_ENCODING) as file:
            file.write(str(xml_file))
