import pandas as pd
from argparse import ArgumentParser

from utils import serialize


def prepare_msgs():
    txt = "./logs/msg_roufluax_1007_date_2021_09_12_14_20_34_505712.txt"
    df = pd.read_csv(txt, sep="\n", header=None)
    df[0] = df[0].str.replace(R"(<.+>)|(http.+)", "", regex=True)
    df = df[df[0].astype(bool)]
    df.to_csv(r'./logs/parsed_msgs.txt', header=None, index=None, sep='\n')


def serialize_vocab():
    with open('./logs/parsed_msgs.txt', 'r', encoding='utf-8') as f:
        msgs = f.read()
    vocab = list(sorted(set(msgs)))
    serialize(vocab, "./models/vocab.pickle")


def main():
    parser = ArgumentParser(description="preprocess dataset")
    parser.add_argument("--mode", action="store",
                        help="Choose mode of preprocessor util",
                        choices=["raw-msgs", "serialize-vocab"])
    args = parser.parse_args()
    options = {
        "raw-msgs": prepare_msgs,
        "serialize-vocab": serialize_vocab
    }
    options[args.mode]()


if __name__ == '__main__':
    main()
