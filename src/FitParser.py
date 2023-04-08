import fitparse
import json
from garmin_fit_sdk import Decoder, Stream, Profile

class GenericFit:
    def __init__(self, path):
        self.path = path

    def parse(self):
        fitfile = fitparse.FitFile(self.path)

        # Get all data messages that are of type 'record'
        for record in fitfile.get_messages('record'):
            # Print the values of the data fields we're interested in
            print(record.get_value('timestamp'))
            print(record.get_value('position_lat'))
            print(record.get_value('position_long'))
            print(record.get_value('distance'))


class GarminFit:
    def __init__(self, path):
        self.path = path

    def parse(self):
        print("Parsing .fit file", self.path)
        stream = Stream.from_file(str(self.path))
        decoder = Decoder(stream)

        def mesg_listenerf(mesg_num, message):
            if mesg_num == Profile['mesg_num']['RECORD']:
                print(json.dumps(message, indent=4))

        messages, errors = decoder.read(
            apply_scale_and_offset=True,
            convert_datetimes_to_dates=False,
            convert_types_to_strings=False,
            expand_sub_fields=True,
            expand_components=True,
            merge_heart_rates=True,
            mesg_listener=mesg_listenerf,
        )
        if len(errors) > 0:
            print("Found errors", errors)

def main():
    f = GenericFit("data/fitfiles/Activity/2023-04-07-13-57-08.fit")
    gf = GarminFit("data/fitfiles/Activity/2023-04-07-13-57-08.fit")
    gf.parse()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())