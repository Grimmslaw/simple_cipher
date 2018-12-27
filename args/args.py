import argparse


def parse():
    parser = argparse.ArgumentParser(description="A simple (and simplistic) cipher tool.")

    parser.add_argument('cipher', choices=['caesar', 'vigenere', 'autokey'],
                        help="the type of cipher to use ('caesar', 'vigenere', or 'autokey')",
                        metavar='CIPHER')

    parser.add_argument('mode', choices=['encrypt', 'decrypt'],
                        help="either 'encrypt' or 'decrypt'", metavar='MODE')

    parser.add_argument('target', help='the target to encrypt/decrypt',
                        metavar='TARGET')

    parser.add_argument('-k', '--key', dest='key',
                        help='the key (numeric shift for caesar or keyword for vigenere)',
                        metavar='key')

    parser.add_argument('-y', '--type', dest='target_type', default='string',
                        help="whether target is a 'string' or a 'file'; default is 'string'",
                        metavar='type')

    parser.add_argument('-o', '--output', dest='output', default=None,
                        help='filepath to write output to; if not supplied, output is written to stdout',
                        metavar='out')

    parser.add_argument('-x', '--strip', dest='strip_frmt', action='store_true')

    return parser.parse_args()
