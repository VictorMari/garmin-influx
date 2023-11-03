import subprocess
import shutil
from pathlib import Path
import json

CONVERTER = Path(__file__).parents[0] / "tools" / "FitCSVTool.jar"

def convert_fit_file(input_file, output_file):
    print("Converting {} to {}".format(input_file, output_file))
    output = {
        "code": None,
        "stdout": None,
        "stderr": None
    }

    command = [
        "java",
        "-jar",
        str(CONVERTER),
        "-b",
        str(input_file),
        str(output_file)
    ]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output["code"] =  result.returncode
        output["stdout"] = result.stdout.decode("utf-8")
        output["stderr"] = result.stderr.decode("utf-8")


    except FileNotFoundError:
        print("FitCSVTool.jar not found. Please download")
        output["stdout"] =  "FitCSVTool.jar not found. Please download",

    except subprocess.CalledProcessError as e:
        print(e.stderr.decode("utf-8"))
        output["code"] =  e.returncode
        output["stdout"] = e.stdout.decode("utf-8")
        output["stderr"] = e.stderr.decode("utf-8")

    return output


def main(args):
    input_file = Path(__file__).parents[1] / "data" / "illetes.fit"
    output_file = Path(__file__).parents[1] / "data" / "illetes.csv"
    result = convert_fit_file(input_file, output_file)

    print(result["code"])
    print(result["stderr"])
    print(result["stdout"])


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
