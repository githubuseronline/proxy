#!/usr/bin/python

from optparse import OptionParser, OptionGroup


if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('-i', '--interface', action='store', default='127.0.0.1',
                                           help='interface for listening', 
                                           metavar='[interface]')
#    parser.add_option('-p', '--port', )

    (options, args) = parser.parse_args()

    print(options.interface)
    print(options.interface)
