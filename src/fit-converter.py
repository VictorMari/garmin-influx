import subprocess
import shutil
from pathlib import Path
import json


CONVERTER = Path(__file__).parents[1] / "bin"/ "FitCSVTool.jar"
ACTIVITIES = Path(__file__).parents[1] / "bin" / "Activities"
OUTPUT = Path(__file__).parents[1] / "reports"

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

    except subprocess.CalledProcessError as e:
        output["code"] =  e.returncode
        output["stdout"] = e.stdout.decode("utf-8")
        output["stderr"] = e.stderr.decode("utf-8")

    return output


def main(args):
    for activity in ACTIVITIES.glob("*.fit"):
        activity_output = OUTPUT / activity.with_suffix(".csv").name
        result = convert_fit_file(activity, activity_output)

    print("code: ", result["code"])
    print("stderr: ", result["stderr"])
    print("stdout: ", result["stdout"])


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
