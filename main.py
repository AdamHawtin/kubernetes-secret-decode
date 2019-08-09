import argparse
import sys

from decode_kubernetes_secret import decode_secret, guess_secret_format


def main():
    parser = argparse.ArgumentParser(
        description='Take a kubernetes secret and decode the data fields')
    args = parse_arguments(parser)
    if args.secret:
        secret_string = args.secret.read()
    elif not sys.stdin.isatty():
        secret_string = sys.stdin.read()
    else:
        parser.print_help()
        return 1
    secret_format = args.format or guess_secret_format(secret_string)
    print(decode_secret(secret_string, secret_format=secret_format))


def parse_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('secret', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('--format', type=str, help='Format of the secret', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    exit(main())
