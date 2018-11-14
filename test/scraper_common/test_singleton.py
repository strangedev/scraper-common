import unittest

from src.scraper_common.singleton import SingletonMeta


class TestSingletonMeta(unittest.TestCase):
    def test_is_singleton_unique(self):
        class TestSingleton(metaclass=SingletonMeta):
            pass

        self.assertIs(TestSingleton(), TestSingleton(), "Singleton was created multiple times.")
