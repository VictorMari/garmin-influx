import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUX_TOKEN")
org = "labosisorg"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "pytest2"

write_api = write_client.write_api(write_options=SYNCHRONOUS)

arr = []

for value in range(5):
    arr.append(
        Point("garmin_activity")
        .tag("activity", "openWater")
        .field("temperature", 40 + value)
    )


print("Inserting", len(arr), "points")
write_api.write(bucket=bucket, org="labosisorg", record=arr)
