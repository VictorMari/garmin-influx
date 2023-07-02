import json
import subprocess
import shutil
import pandas as pd
from pathlib import Path


def run_fit_csv_conversion_process(input_file, output_file):
    command = [
        "java",
        "-jar",
        "FitCSVTool.jar",
        input_file,
    ]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        data = {
            "code": result.returncode,
            "stdout": result.stdout.decode("utf-8"),
            "stderr": result.stderr.decode("utf-8")
        }

        if data["code"] == 0:
            destination = Path(output_file)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(input_file.replace(".fit", ".csv"), str(destination))

        return data

    except FileNotFoundError:
        print("FitCSVTool.jar not found. Please download")


def converter(input_file, output_file):
    return {}


def clean_up_fit_data(fit_data):
    for record in fit_data:
        for field_name in list(record.keys()):
            if str(record[field_name]) in ["unknown", "NaN"]:
                del record[field_name]

    return fit_data


def csv_to_json(input_file, output_file):
    dataframe = pd.read_csv(input_file, low_memory=False)
    #dataframe.dropna(inplace=True)
    #dataframe.drop(columns=["unknown"], inplace=True)
    json_data = dataframe.to_dict(orient="records")
    clean_up_fit_data(json_data)

    with Path(output_file).open("w+") as f:
        json.dump(json_data, f, indent=4)
    return json_data


def main():
    run_fit_csv_conversion_process("data/fitfiles/Activity/2023-04-13-20-25-48.fit",
                                   "data/parsed/2020-12-31-12-00-00.csv")
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
