import subprocess
import shutil
from pathlib import Path


CONVERTER = Path(__file__).parents[0] / "tools" / "FitCSVTool.jar"

def convert_fit_file(input_file, output_file):
    command = [
        "java",
        "-jar",
        str(CONVERTER),
        input_file,
    ]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        data = {
            "code": result.returncode,
            "stdout": result.stdout.decode("utf-8"),
            "stderr": result.stderr.decode("utf-8")
        }
        return data

    except FileNotFoundError:
        print("FitCSVTool.jar not found. Please download")


    except subprocess.CalledProcessError as e:
        print(e.stderr.decode("utf-8"))
        return None



def main(args):
    input_file = Path(__file__).parents[1] / "data" / "illetes.fit"
    output_file = Path(__file__).parents[2] / "data" / "illetes.csv"
    result = convert_fit_file(input_file, output_file)
    print(result)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
