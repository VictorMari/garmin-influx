from pathlib import Path
import shutil
import json
import fitparse



def glob_fit_files(path):
    fit_groups = {}

    for fit_file in Path(path).glob("**/*.fit"):
        if fit_file.parent.name in fit_groups:
            fit_groups[str(fit_file.parent.name)].append(str(fit_file))
        else:
            fit_groups[str(fit_file.parent.name)] = [str(fit_file)]

    return fit_groups


def copy_fit_files(fit_groups):
    dest_dir = Path("data/fitfiles")
    dest_dir.mkdir(parents=True, exist_ok=True)
    for type, files in fit_groups.items():
        dest = (dest_dir / type)
        dest.mkdir(parents=True, exist_ok=True)
        for file in files:
            shutil.copy(file, dest / Path(file).name)


def main():
    fit_files = glob_fit_files("/run/media/labosis/GARMIN")
    copy_fit_files(fit_files)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
