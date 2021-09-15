import unittest

from app.preprocess import create_parser


class PreprocessParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()


class AbbreviationTest(PreprocessParserTest):
    def test_mode(self):
        val = 'raw-msgs'
        parsed = self.parser.parse_args(['-m', val])
        self.assertEqual(parsed.mode, val)

    def test_input_file(self):
        val = './logs/logs.txt'
        parsed = self.parser.parse_args(['-i', val])
        self.assertEqual(parsed.in_file, val)

    def test_output_file(self):
        val = './logs/data.txt'
        parsed = self.parser.parse_args(['-o', val])
        self.assertEqual(parsed.out_file, val)


class FullParamNameTest(PreprocessParserTest):
    def test_mode(self):
        val = 'raw-msgs'
        parsed = self.parser.parse_args(['--mode', val])
        self.assertEqual(parsed.mode, val)

    def test_input_file(self):
        val = './logs/logs.txt'
        parsed = self.parser.parse_args(['--in-file', val])
        self.assertEqual(parsed.in_file, val)

    def test_output_file(self):
        val = './logs/data.txt'
        parsed = self.parser.parse_args(['--out-file', val])
        self.assertEqual(parsed.out_file, val)


if __name__ == '__main__':
    unittest.main()
