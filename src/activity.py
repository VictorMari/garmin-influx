from garmin_fit_sdk import Decoder, Stream
from pathlib import Path


PROJECT = Path(__file__).parents[1]
ACTIVITIES = PROJECT / "bin" / "Activities"

class SwimmingActivity:
    def __main__(self, messages):
        pass



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
        "convert_types_to_strings": True,
        "convert_datetimes_to_dates": True,
        "merge_heart_rates": True,
    }

    activity_types = {
        "Swimming": SwimmingActivity   
    }

    for fit_file in ACTIVITIES.glob("*.fit"):
        print(f"Processing {fit_file.name}")
        stream = Stream.from_file(fit_file)
        decoder = Decoder(stream)
        #is_well = decoder.check_integrity()
        messages, errors = decoder.read(**options)
        process_errors(errors)




def main():
    load_activities()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())