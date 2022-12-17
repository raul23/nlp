import argparse
import time
# Examples from Wikipedia
text1 = """
"""

text2 = """
"""

text3 = """
"""

text4 = """
"""


def setup_argparser():
    msg = 'Find language of a text'
    parser = argparse.ArgumentParser(
        description='',
        usage=f"python %(prog)s [OPTIONS]\n\n{msg}",
        # ArgumentDefaultsHelpFormatter
        # HelpFormatter
        # RawDescriptionHelpFormatter
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    choices = [1, 2]
    choices_msg = ', '.join(map(str, choices))
    parser.add_argument('-m', '--method', metavar='METHOD', dest='method', choices=choices,
                        default=1, type=int,
                        help=f'Method to use to find language of text. Choices are: [{choices_msg}]')
    parser.add_argument(
        '-d', '--download', action='store_true',
        help='Whether to download necessary nltk resoures for the selected method')
    return parser


if __name__ == '__main__':
    parser = setup_argparser()
    args = parser.parse_args()
    texts = [text1, text2, text3, text4]
    method_msg = f'Finding language of text with method #{args.method}'
    print(method_msg)
    time.sleep(1)
