#!/usr/bin/python

import sys

from .validator import Validator


def main():
    if len(sys.argv) == 1:
        print(
            "Syntax: {} [-a <org>/<basepath>] [-f <file>] [-u <url>] [-e <kafka>/<space>/<series>]".format(
                sys.argv[0]), file=sys.stderr)
        print(" -a: autosearch; find appropriate compose files on GitHub")
        print(" -f: filebased; load docker-compose from a docker-compose file")
        print(" -fl: filebased list; load paths or URLs as lines from a text file")
        print(" -u: urlbased; direct URL or path specification")
        print(
            " -fi: filters; you can select filters as any as you want:\n    for more info flag --fih might be helpful!")
        print(
            "Example: {} -a elastest/deploy -fi 'Duplicate Keys,Top level property'".format(
                sys.argv[0]))
        sys.exit(1)

    autosearch = None
    filebasedlist = None
    filebased = None
    urlbased = None
    filters = []

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-a":
            autosearch = sys.argv[i + 1]
        elif sys.argv[i] == "-fl":
            filebasedlist = sys.argv[i + 1]
        elif sys.argv[i] == "-f":
            filebased = sys.argv[i + 1]
        elif sys.argv[i] == "-u":
            urlbased = sys.argv[i + 1]
        elif sys.argv[i] == "-fi":
            filters = sys.argv[i + 1]
            filters = filters.split(',')
        elif sys.argv[i] == "--fih":
            print(
                "Whole list of fliters is here!\n \n ====>  'Duplicate Keys','Top level property','Duplicate ports','Container name','Labels','Typing mistakes', 'DNS', 'Duplicate expose'\n \n How to use it? \n\n EZ!\n\n Something like this\n\n python validator-cli.py -a elastest/deploy -fi 'Duplicate Keys,Top level property' \n\n\t *****Warning*****\n\n Makesure that you enter this arg as a string!\n\n\t *****************")
            sys.exit(1)

        i += 1

    my_validator = Validator()
    my_validator.validator(autosearch, filebasedlist, urlbased, filebased, filters)


if __name__ == "__main__":
    main()
