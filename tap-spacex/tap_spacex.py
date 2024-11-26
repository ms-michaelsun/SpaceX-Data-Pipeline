import singer
import pandas as pd
import numpy as np

LOGGER = singer.get_logger()

schema = {
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'rocket': {'type': 'string'},
        'success': {'type': ['number', 'null']},
        'date_utc': {'type': 'string', 'format': 'date-time'},     
    }
}

def main():
    url = 'https://api.spacexdata.com/v4/launches'
    df = pd.read_json(url)
    df = df.replace({np.nan: None})

    records = df.to_dict(orient = 'records')

    singer.write_schema('launches', schema, 'id')
    singer.write_records('launches', records)


if __name__ == '__main__':
    main()