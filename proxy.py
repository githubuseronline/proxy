#!/usr/bin/python

from optparse import OptionParser, OptionGroup


if __name__ == '__main__':

    ################################################################################

    # Parse command line args and options

    ################################################################################
    parser = OptionParser(description='DNS Proxy.')

    serv_opts = OptionGroup(parser, 'Basic options for proxy.')
    serv_opts.add_option('-i', '--interface', default='127.0.0.1',
                         help='Interface for proxy. By default is %default')
    serv_opts.add_option('-p', '--port', default='53',
                         help='Proxy port. By default is 53')
    serv_opts.add_option('-t', '--tcp', action='store_true', default='False',
                         dest='transport', help='UDP is a default transport.')
    parser.add_option_group(serv_opts)

    (options, args) = parser.parse_args()

    print(options.transport)
