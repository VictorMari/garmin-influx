import json
import os
from pathlib import Path
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


def load_activity_csv(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_json_activity(path):
    with open(path, 'r') as f:
        return json.load(f)


class InfluxDB:
    def __init__(self) -> None:
        self.client = InfluxDBClient(**{
            'url': os.getenv('INFLUX_HOST'),
            'token': os.getenv('INFLUX_TOKEN'),
        })
        self.org = os.getenv('INFLUX_ORG')
        self.write_mode = SYNCHRONOUS

    def write(self, data_points, bucket=os.getenv('INFLUX_BUCKET')):
        write_api = self.client.write_api(write_options=self.write_mode)
        write_api.write(bucket, self.org, data_points)
        write_api.close()
        print("Inserted:", len(data_points), "points")


class GarminMetrics:
    def __init__(self, activity_data):
        self.activity_data = activity_data

    def generate_points(self):
        fields = [
            "temperature",
            "position_lat",
            "position_long",
            "distance",
            "temperature",
            "cadence"
        ]


        t = 0
        for metric in self.activity_data:
            data_point = Point("garmin_metric") \
                .tag("activity", "openWater") \
                .time(metric["timestamp"], WritePrecision.MS) \
                .field("temperature", 40 + t)
            t += 1
            yield data_point

def main():
    garmin_activity = load_json_activity("data/parsed/Activity_2023-04-08-14-53-57.json")
    metrics = GarminMetrics(garmin_activity)
    influx = InfluxDB()

    print("Using bucket", os.getenv('INFLUX_BUCKET'))
    influx.write([p for p in metrics.generate_points()])
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())