#!/bin/bash

set -e

python3 create_dataset_json.py
curl -XPOST "http://localhost:9200/_bulk" -H 'Content-Type: application/json' --data-binary @lyrics_data.json
rm lyrics_data.json
