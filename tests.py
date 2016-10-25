import requests
from lxml import html
from parser import LeoParser
from fetcher import LeoFetcher
from wordextractor import WordExtractor
import unittest


class TestParser(unittest.TestCase):

    def test_extract_translation_nouns(self):
        parser = LeoParser()
        with open('resources/story-search.xml', 'r') as hall:
            data = hall.read()
        result = parser.extract_translation_nouns(data)
        self.assertTrue(16, len(result))
        expected = [{"en":"story", "de":"die Geschichte"},
                    {"en":"story", "de":"das Geschoss"},
                    {"en":"story", "de":"der Stock"},
                    {"en":"story", "de":"das Stockwerk"},
                    {"en":"story", "de":"die Etage"},
                    {"en":"story", "de":"der Artikel"},
                    {"en":"story", "de":u'die Erz\xe4hlung'},
                    {"en":"story", "de":"der Schwank"},
                    {"en":"story line", "de":"die Story"},
                    {"en":"saga", "de":"die Story"},
                    {"en":"story", "de":u'der D\xf6ntje'},
                    {"en":"story", "de":u'das Gescho\xdf'},
                    {"en":"story", "de":u'die M\xe4r'},
                    {"en":"story line", "de":"die Handlung"},
                    {"en":"story proper", "de":"das Vollgeschoss"},
                    {"en":"story line", "de":"Handlung einer Geschichte"}]
        self.assertListEqual(expected, result)

    def test_extract_translation_nouns_IT(self):
        parser = LeoParser()
        baseUrl = "http://dict.leo.org/dictQuery/m-vocab/ende/query.xml"
        timeParam = "2016-10-25T20:41:00.011Z"
        url = baseUrl + "?tolerMode=nof&lp=ende&lang=en&rmWords=off&rmSearch=on&search=story&searchLoc=0&resultOrder=basic&multiwordShowSingle=on&pos=0&sectLenMax=100&n=1"
        sess = requests.session()
        result = sess.get(url)
        xml = result.content
        results = parser.extract_translation_nouns(xml)
        self.assertEqual(69, len(results))

    def test_search_english_word(self):
        fetcher = LeoFetcher()
        parser = LeoParser()
        xml = fetcher.search_english_word("en", "story")
        results = parser.extract_translation_nouns(xml)
        self.assertEqual(69, len(results))

    def test_word_extractor(self):
        extractor = WordExtractor()
        rawText = "What? Wait! Stop now. We-are-the-champs. & $%^&*()!@"
        expected = ["What", "Wait", "Stop", "now", "We", "are", "the", "champs"]
        actual = extractor.get_words_from_text(rawText)
        self.assertListEqual(actual, expected)
