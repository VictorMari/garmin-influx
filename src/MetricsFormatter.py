import json
from pathlib import Path

def load_activity_csv(path):
    with open(path, 'r') as f:
        return json.load(f)


def main():
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())