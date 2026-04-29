from scholarly import scholarly
import json
from datetime import datetime
import os
import sys

SCHOLAR_ID = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
RESULTS_DIR = 'results'
DATA_PATH = f'{RESULTS_DIR}/gs_data.json'
SHIELDIO_PATH = f'{RESULTS_DIR}/gs_data_shieldsio.json'

os.makedirs(RESULTS_DIR, exist_ok=True)

if not SCHOLAR_ID:
    print("WARNING: GOOGLE_SCHOLAR_ID is not set, skipping Scholar update.", file=sys.stderr)
    sys.exit(0)

try:
    author: dict = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']: v for v in author['publications']}
    print(json.dumps(author, indent=2))

    with open(DATA_PATH, 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open(SHIELDIO_PATH, 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    print("Scholar data updated successfully.")

except Exception as e:
    print(f"WARNING: Failed to fetch Google Scholar data: {e}", file=sys.stderr)
    if os.path.exists(DATA_PATH):
        print("Existing data preserved, skipping update.", file=sys.stderr)
    else:
        print("No existing data found; writing placeholder to avoid downstream errors.", file=sys.stderr)
        placeholder = {
            "citedby": 0,
            "publications": {},
            "updated": str(datetime.now()),
            "name": "",
        }
        with open(DATA_PATH, 'w') as outfile:
            json.dump(placeholder, outfile, ensure_ascii=False)
        with open(SHIELDIO_PATH, 'w') as outfile:
            json.dump({"schemaVersion": 1, "label": "citations", "message": "N/A"}, outfile, ensure_ascii=False)
