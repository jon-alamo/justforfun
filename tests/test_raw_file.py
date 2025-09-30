import unittest
import os
from pathlib import Path
import src.parser as parser


DATA_DIR = Path("data/")


class TestFeedRecordFileFormat(unittest.TestCase):

    def setUp(self):
        if not hasattr(self, 'file_path'):
            self.skipTest("Attribute file_path is not set.")
        if not os.path.exists(self.file_path):
            self.skipTest(f"Data file {self.file_path} does not exist.")

    def test_feed_record_file_not_empty(self):
        with self.subTest(feed_file=self.file_path.name):
            try:
                self.parsed_data = parser.parse_file(self.file_path)
            except parser.json.JSONDecodeError as e:
                self.fail(f"JSON decoding failed: {e}")
            self.assertTrue(len(self.parsed_data) > 0, f"Parsed file {self.file_path} is empty.")



class TestFeedRecordFileContent(unittest.TestCase):

    def setUp(self):
        self.parsed_data = parser.parse_file(self.file_path)
        self.missmatches = []        
        self.missing_indexes = []
        for story_hash, story_data in self.parsed_data.items():
            if len(story_data['entity_ids']) != story_data['record_count']:
                self.missmatches.append(
                    f"{story_hash} (expected: {story_data['record_count']}, found: {len(story_data['entity_ids'])}."
                )
            if len(story_data['missing_indexes']) > 0:
                self.missing_indexes.append(
                    f"{story_hash} indexes {tuple(story_data['missing_indexes'])} missing."
                )


    def test_feed_record_file_matches_count(self):
        with self.subTest(feed_file=self.file_path.name):
            self.assertEqual(len(self.missmatches), 0, f"Record count mismatches found for stories {', '.join(self.missmatches)}.")

    def test_feed_record_missing_indexes(self):
        with self.subTest(feed_file=self.file_path.name):
            self.assertEqual(len(self.missing_indexes), 0, f"Missing indexes found for stories {', '.join(self.missing_indexes)}.")

