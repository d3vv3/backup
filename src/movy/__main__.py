import os
import logging
import argparse
from pathlib import Path
from movy import movy


__version__ = '0.1.0'


def main():

    home = Path.home()
    logs_folder = os.path.join(home, ".movytool")
    if not os.path.isdir(logs_folder):
        os.mkdir(logs_folder)

    logging.basicConfig(
        filename=os.path.join(logs_folder, 'movy.log'),
        format='%(asctime)s %(name)s %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S',
        level='DEBUG'
    )

    parser = argparse.ArgumentParser(
        description="A cli tool to move your users' group files.",
        epilog='A tool as an exercise :)')
    parser.add_argument('folder', type=str, nargs=1,
                        help='the folder you want to move files from')
    parser.add_argument('group', type=str, nargs=1,
                        help='the group whose files you want to move')
    parser.add_argument('-d', '--dst', type=str, nargs=1, default="./movy",
                        help='the folder to move files to')
    args = parser.parse_args()

    group = args.group[0]
    src = args.folder[0]
    dst = args.dst if type(args.dst) == str else args.dst[0]

    m = movy.Movy(src, group, dst=dst)
    m.run()


if __name__ == '__main__':
    main()
