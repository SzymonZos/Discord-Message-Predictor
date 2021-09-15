from argparse import ArgumentParser

import pandas as pd

from app.utils import serialize


def prepare_msgs(in_file: str, out_file: str):
    df = pd.read_csv(in_file, sep="\n", header=None)
    df[0] = df[0].str.replace(R"(<.+>)|(http.+)", "", regex=True)
    df = df[df[0].astype(bool)]
    df.to_csv(out_file, header=None, index=None, sep='\n')


def serialize_vocab(in_file: str, out_file: str):
    with open(in_file, 'r', encoding='utf-8') as f:
        msgs = f.read()
    vocab = list(sorted(set(msgs)))
    serialize(vocab, out_file)


_MODE_OPTIONS = {
    "raw-msgs": prepare_msgs,
    "serialize": serialize_vocab
}


def create_parser():
    parser = ArgumentParser(description="preprocess dataset")
    parser.add_argument("-m", "--mode", action="store",
                        help="Choose mode of preprocessor util",
                        choices=_MODE_OPTIONS.keys())
    parser.add_argument("-i", "--in-file", action="store", type=str,
                        help="Choose input file")
    parser.add_argument("-o", "--out-file", action="store", type=str,
                        help="Choose destination of preprocessor output")
    return parser


def main():
    args = create_parser().parse_args()
    _MODE_OPTIONS[args.mode](args.in_file, args.out_file)


if __name__ == '__main__':
    main()
