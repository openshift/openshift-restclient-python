# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function

import argparse
import logging
import sys

from openshift import __version__
from openshift.helper import OpenShiftException

from .docstrings import DocStrings

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
    subparser.add_argument('models', action='store',
                           help=u'List of models for which to generate doc strings. Specify '
                                u'the model Kind using either CamelCase or snake_case.',
                           nargs='*', )
    subparser.add_argument('-v', '--api-version', action='store',
                           help=u'API version. Defaults to v1.',
                           dest='api_version', default='v1')

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

    try:
        globals()['run_{}_cmd'.format(args.subcommand)](**vars(args))
    except OpenShiftException as exc:
        logger.error(exc.message)
        sys.exit(1)
    except Exception as exc:
        logger.error(exc.message)
        sys.exit(1)

    sys.exit(0)


def run_docstrings_cmd(**kwargs):
    """
    Send documentation string and return string to stdout for each model requested

    :param kwargs: parser arguments
    :return: None
    """
    models = kwargs.pop('models')
    api_version = kwargs.pop('api_version')

    if not models:
        raise OpenShiftException("ERROR: you mus provide one or more models for docstrings command.")

    for model in models:
        try:
            strings = DocStrings(model=model, api_version=api_version)
        except OpenShiftException as exc:
            raise
        print("DOCUMENTATION = '''")
        print(strings.documentation)
        print("'''\n")
        print("RETURN = '''")
        print(strings.return_block)
        print("'''\n")
