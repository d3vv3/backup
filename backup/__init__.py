import grp
import sys
import logging
import argparse
from pathlib import Path

home = str(Path.home())

logging.basicConfig(
    filename=f'{home}/.backuptool/backup.log',
    format='%(asctime)s %(levelname)s:%(name)s %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S',
    level='INFO'
)

parser = argparse.ArgumentParser(
    description="A cli tool to backup your users' group files.",
    epilog='A tool as an exercise :)')
parser.add_argument('group', type=str, nargs=1,
                    help='the folder you want to backup')
parser.add_argument('-d', '--dst', type=str, nargs=1, default='./backup',
                    help='the folder to backup to')

args = parser.parse_args()

group = args.group[0]

try:
    grp.getgrnam(group)
except KeyError:
    logging.error('Group %s does not exist', group)
    sys.exit()
