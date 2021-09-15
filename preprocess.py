import pandas as pd
from argparse import ArgumentParser

from utils import serialize


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


def main():
    parser = ArgumentParser(description="preprocess dataset")
    parser.add_argument("--mode", action="store",
                        help="Choose mode of preprocessor util",
                        choices=["raw-msgs", "serialize-vocab"])
    parser.add_argument("--in-file", action="store", type=str,
                        help="Choose input file")
    parser.add_argument("--out-file", action="store", type=str,
                        help="Choose destination of preprocessor output")
    args = parser.parse_args()
    options = {
        "raw-msgs": prepare_msgs,
        "serialize-vocab": serialize_vocab
    }
    options[args.mode](args.in_file, args.out_file)


if __name__ == '__main__':
    main()
