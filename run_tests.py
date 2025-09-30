import unittest
import os
import tests.test_raw_file as test_raw_file
import pathlib


DATA_DIR = pathlib.Path('data/')


def load_tests():
    suite = unittest.TestSuite()
    for file in DATA_DIR.glob("*"):
        if file.is_file():

            class TestFeedRecordFileFormat(test_raw_file.TestFeedRecordFileFormat):
                pass

            TestFeedRecordFileFormat.file_path = file
            TestFeedRecordFileFormat.__name__ = "TestFeedRecordFileFormat"
            suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestFeedRecordFileFormat))

            class TestFeedRecordFileContent(test_raw_file.TestFeedRecordFileContent):
                pass

            TestFeedRecordFileContent.file_path = file
            TestFeedRecordFileContent.__name__ = "TestFeedRecordFileContent"
            suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestFeedRecordFileContent))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests())
