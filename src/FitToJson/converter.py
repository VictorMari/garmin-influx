import subprocess


def run_fit_csv_tool(input_file, output_file):
    command = [
        "java",
        "-jar",
        "FitCSVTool.jar",
        input_file,
        "-o",
        output_file
    ]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "code": result.returncode,
        }

    except FileNotFoundError:
        print("FitCSVTool.jar not found. Please download")


def converter(input_file, output_file):
    return {}
