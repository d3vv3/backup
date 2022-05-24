import os
import logging
import argparse
from pathlib import Path
import backup


__version__ = '0.1.0'


def main():

    home = Path.home()
    logs_folder = os.path.join(home, ".backuptool")
    if not os.path.isdir(logs_folder):
        os.mkdir(logs_folder)

    logging.basicConfig(
        filename=os.path.join(logs_folder, 'backup.log'),
        format='%(asctime)s %(name)s %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S',
        level='DEBUG'
    )

    parser = argparse.ArgumentParser(
        description="A cli tool to backup your users' group files.",
        epilog='A tool as an exercise :)')
    parser.add_argument('folder', type=str, nargs=1,
                        help='the folder you want to backup files from')
    parser.add_argument('group', type=str, nargs=1,
                        help='the folder you want to backup')
    parser.add_argument('-d', '--dst', type=str, nargs=1, default="./backup",
                        help='the folder to backup files to')
    args = parser.parse_args()

    group = args.group[0]
    src = args.folder[0]
    dst = args.dst if type(args.dst) == str else args.dst[0]

    b = backup.Backup(src, group, dst=dst)
    b.run()


if __name__ == '__main__':
    main()
