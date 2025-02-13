import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

def lecture_des_id_tombola():
    bucket = "BUCKET"
    org = "ORGANISATION"
    token = "TOKEN"
    # Store the URL of your InfluxDB instance
    url = "http://localhost/"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    # Query script
    query_api = client.query_api()
    query = f'from(bucket:"{bucket}")\
    |> range(start: -5000h)'
    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            # results.append((record.get_field(), record.get_value()))
            results.append((record.get_measurement(), record.get_value()))

    print(results)
    return results