import json
from pathlib import Path

from .FitToJson import converter
from .Influx import parser
from PyInquirer import prompt


def list_activity_files(path: Path):
    for file in path.glob("Activity/*.fit"):
        yield file


class Interface:
    def __init__(self):
        self.data_path = Path("data/fitfiles")

    def prompt_activity_selection(self):
        activity_list = list_activity_files(self.data_path)
        questions = [
            {
                "type": "list",
                "name": "activity",
                "message": "Select an activity",
                "choices": [{
                    "name": activity.name,
                    "value": activity
                } for activity in activity_list],
                "pageSize": 3
            },
            {
                "type": "checkbox",
                "name": "operation",
                "message": "Select an operation",
                "choices": [
                    {
                        "name": "Convert to JSON",
                        "checked": True,
                        "value": "convert_JSON"
                    },
                    {
                        "name": "convert to JSON and upload to InfluxDB",
                        "value": "convert_JSON_upload_Influx"
                    }
                ]
            }
        ]
        answer = prompt(questions)
        print(answer)


def main():
    interface = Interface()
    interface.prompt_activity_selection()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
