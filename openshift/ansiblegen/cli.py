# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function

import argparse
import logging
import sys

from openshift import __version__

logger = logging.getLogger(__name__)

from logging import config

LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'openshift': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'ERROR'
        }
    }

AVAILABLE_COMMANDS = {
    'help':       'Display this help message',
    'version':    'Display openshift version information',
    'modules':    'Generate one or more Ansible modules',
    'docstrings': 'Generate doc strings for a particular Ansible module',
}


def subcmd_modules_parser(parser, subparser):
    pass


def subcmd_help_parser(parser, subparser):
    pass


def subcmd_version_parser(parser, subparser):
    pass

def subcmd_docstrings_parser(parser, subparser):
    pass


def commandline():
    parser = argparse.ArgumentParser(description=u'Uses the OpenShift API models to generate Ansible artifacts')
    parser.add_argument('--debug', action='store_true', dest='debug',
                        help=u'enable debug output', default=False)

    subparsers = parser.add_subparsers(title='subcommand', dest='subcommand')
    subparsers.required = True
    for subcommand in AVAILABLE_COMMANDS:
        logger.debug('Registering subcommand %s', subcommand)
        subparser = subparsers.add_parser(subcommand, help=AVAILABLE_COMMANDS[subcommand])
        globals()['subcmd_%s_parser' % subcommand](parser, subparser)

    args = parser.parse_args()

    if args.debug:
        # enable debug output
        LOGGING['loggers']['openshift']['level'] = 'DEBUG'
    config.dictConfig(LOGGING)

    if args.subcommand == 'help':
        parser.print_help()
        sys.exit(0)

    if args.subcommand == 'version':
        print("{0} version is {1}".format(__name__, __version__))
        sys.exit(0)

    if args.subcommand == 'generate':
        print("generate")

    sys.exit(0)
