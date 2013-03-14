# -*- coding:utf-8 -*-


import sys, argparse


def parseArgumentsExample() :

    print 'Parsing the command line : {}'.format(sys.argv)

    parser = argparse.ArgumentParser()
    parser.add_argument('STRING1', help='String positional argument')
    parser.add_argument('INT1', help='Int positional argument', type=int)
    parser.add_argument('--optional1', '-o', help='optional argument requiring a value')
    parser.add_argument('--verbose', '-v', help='optional argument representing a boolean', action='store_true')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--optional2', help='optional argument requiring a value', choices=['DEBUG', 'INFO'])
    group.add_argument('--optional3', '-a', help='optional argument', action='count', default=0)
    
    args = parser.parse_args()

    print 'optional1 : {} - {}'.format(type(args.optional1), args.optional1)
    print 'optional2 : {} - {}'.format(type(args.optional2), args.optional2)
    print 'optional3 : {} - {}'.format(type(args.optional3), args.optional3)
    print 'verbose : {} - {}'.format(type(args.verbose), args.verbose)

    if args.verbose :
        print '%s %d' % (args.STRING1, args.INT1 * 100)

    return(0) 


def main() :

    parseArgumentsExample()

    return(0)


if __name__ == '__main__' :
    main()