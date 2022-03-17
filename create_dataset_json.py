import json
from collections import deque
from typing import Union

from datasets import Dataset, DatasetDict, load_from_disk


class LyricsDataset(Dataset):
    path: str
    _dataset: Union[Dataset, DatasetDict]

    def __init__(self, path):
        self.path = path
        self._dataset = load_from_disk(self.path)

    @property
    def dataset(self) -> Union[Dataset, DatasetDict]:
        return self._dataset

lyrics = LyricsDataset(path="./data/assets/melon_lyrics_v2")

def create_data_json_file(dataset: Dataset):
    queries = deque()
    # for i in range(1, len(dataset)+1):
    for i in range(1,4):
        request = {
            "create" : {
                "_index": "lyrics",
                "_id": i,
            }
        }
        data = {
            "artists": dataset[i]['artists'],
            "context": dataset[i]['context'],
            "genre": dataset[i]['genre'],
            "issue_date": dataset[i]['issuedate'],
            "song_id": dataset[i]['song_id'],
            "song_name": dataset[i]['song_name'],
            "song_org_id": dataset[i]['song_org_id'],
            "song_tags": dataset[i]['song_tags'],
            "song_tags_tfidf": dataset[i]['song_tags_tfidf']
        }
        queries.append(request)
        queries.append(data)

    with open("lyrics_data.json", "a") as file:
        while queries:
            file.write(json.dumps(queries.popleft()) + "\n")

create_data_json_file(lyrics.dataset)
