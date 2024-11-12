from garmin_fit_sdk import (
    Decoder, 
    Stream,
    Profile,
)
from pathlib import Path
import json



PROJECT = Path(__file__).parents[1]
ACTIVITIES = PROJECT / "bin" / "Activities"

class SwimmingActivity:
    def __main__(self, messages):
        pass

class ActivityParser:
    def __init__(self):
        self.sessions = {}
        self.messageTypes = {}
        self.file_id = None
        self.message_types = set()
        self.message_names = set()

    def parse(self, messages):
        for message_type in messages.keys():
            self.message_types.add(message_type)

        
    def get_types(self):
        return list(self.message_types)

        



def process_errors(errors):
    for error in errors:
        print(error)


def load_activities():
    options = {
        "apply_scale_and_offset": True,
        "convert_datetimes_to_dates": True,
        "enable_crc_check": True,
        "expand_sub_fields": True,
        "expand_components": True,
        #"convert_types_to_strings": True,
        "convert_datetimes_to_dates": True,
        "merge_heart_rates": True,
    }

    activity_types = {
        "Swimming": SwimmingActivity   
    }

    parser = ActivityParser()

    for fit_file in ACTIVITIES.glob("*.fit"):
        print(f"Processing {fit_file.name}")
        stream = Stream.from_file(fit_file)
        decoder = Decoder(stream)
        #is_well = decoder.check_integrity()
        messages, errors = decoder.read(**options)
        if errors:
            process_errors(errors)
            return 1
        parser.parse(messages)
    
    with open("groups.json", "w+") as f:
        json.dump(parser.get_types(), f, indent=4)  


def main():
    load_activities()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())