import fitparse
import json
from pathlib import Path
from garmin_fit_sdk import Decoder, Stream, Profile
import pandas as pd

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

        collector = []

        def mesg_listenerf(mesg_num, message):
            if mesg_num == Profile['mesg_num']['RECORD']:
                collector.append(message)

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

        return collector


class PandasFit:
    def __init__(self, path):
        self.path = path

    def parse(self):
        print("Parsing .fit file", self.path)
        df = pd.read_csv(self.path)
        return df

def main():
    fit_path = Path("data/parsed/2023-04-08-14-53-57.csv")
    fit_pd_data = PandasFit(fit_path).parse()
    fit_pd_data.to_json("data/parsed/travesia-04-08_indexed.json", orient="index", indent=4)

if __name__ == "__main__":
    import sys
    sys.exit(main())