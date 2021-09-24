#!/usr/bin/env python

import argparse
import sys
import textwrap

from utils import dotdict, load_config
from tendible import Tendible


VERSION     = "0.0.1-alpha"

DEFAULT_CLI_ARGS = {
    "generic_args": (
        (
            ('--config',),
            dict(
                default="tendible-config.yaml",
                help='path to tendible-config.yaml'
            ),
        ),
        (
            ('--version',),
            dict(
                action='version',
                version=VERSION
            ),
        ),
        (
            ("--debug",),
            dict(
                action="store_true",
                help="enable tendible debug output logging (default=False)"
            ),
        ),
        (
            ("--logfile",),
            dict(
                help="log output messages to a file (default=None)"
            ),
        ),
    ),
}

def print_common_usage():
    print(textwrap.dedent("""
        These are common tendible commands:
            execute a playbook contained in tendible-config.yaml:
                tendible run

        `tendible --help` list of optional command line arguments
    """))

def add_args_to_parser(parser, args):
    for arg in args:
        parser.add_argument(*arg[0], **arg[1])

def run(config):
    for playbook in config.playbooks:
        extra_flags = None
        extra_vars  = None
        playbook    = dotdict(playbook)
        if 'extra_vars' in playbook:
            extra_vars = playbook.extra_vars

        if 'extra_flags' in playbook:
            extra_flags = playbook.extra_flags

        obj = Tendible(
            inventory   = ".",
            playbook    = playbook.name,
            extra_vars  = extra_vars,
            extra_flags = extra_flags
        )
        obj.run()

def main(sys_args=None):

    parser = argparse.ArgumentParser(
        prog        = "tendible",
        description = "Use 'tendible' (with no arguments) to see basic usage"
    )

    subparser = parser.add_subparsers(
        help="Command to invoke",
        dest='command',
    )
    add_args_to_parser(parser, DEFAULT_CLI_ARGS['generic_args'])
    subparser.required = True

    run_subparser = subparser.add_parser(
        'run',
        help="Run tendible in the foreground"
    )
    # add_args_to_parser(run_subparser, DEFAULT_CLI_ARGS['generic_args'])

    if len(sys.argv) == 1:
        parser.print_usage()
        print_common_usage()
        parser.exit(status=0)
    
    vargs   = vars(parser.parse_args(sys_args))
    config  = dotdict(load_config(vargs.get('config')))

    if vargs.get('command') == 'run':
        run(config)

if __name__ == "__main__":
    main()