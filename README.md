# movy

A cli tool to move your files for a specified group.

## Usage

```
usage: movy-cli [-h] [-d DST] folder group

A cli tool to move your users' group files.

positional arguments:
  folder             the folder you want to move files from
  group              the group whose files you want to move

optional arguments:
  -h, --help         show this help message and exit
  -d DST, --dst DST  the folder to move files to

A tool as an exercise :)
```

## Contribute

1. Clone this repository.
2. `pip install -r requirements-dev.txt`.
3. Apply your changes.
4. Run the tests by running `pytest` on the root directory.

## Building

1. Make sure you have `dh` installed (`sudo apt install dh-python`).
2. `pip install stdeb`.
3. `python setup.py --command-packages=stdeb.command bdist_deb`.

## Considerations

### Considered and implemented

1. The program is only allowed to run once at a time.
2. It will move all the files (not dirs) owned by the group.
3. If the folder of the file owned by the group wasn't owned by the group, it will create the folder owned by the user executing the move.
4. It will ask the user to allow overwrite if the target folder exists.
5. Source, target and group existance are checked.
6. Similar approach to Syncthing on `Send only mode`, where if two moves are called, it will add the new files and keep the old ones that have not been overwritten.
7. Permissions are kept as the original files.
8. The program needs the source folder and the group name in order to run.
9. Logs are stored in the user's home under `~/.movytool/movy.log`

### Considered but not implemented

1. Check if there were changes on the new files being moved (in case of overwrite).
2. Use a `tar.gz` or tape archive to store the files (and save space).
3. Implement hardlinks.
4. Optimization.
