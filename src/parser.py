import json


def populate_data(analytic_record: dict, data: dict):
    doc_hash = analytic_record['RP_DOCUMENT_ID']
    if doc_hash  not in data:
        data[doc_hash] = {
            'entity_ids': [],
            'record_count': analytic_record['DOCUMENT_RECORD_COUNT'],
            'missing_indexes': set(range(1, analytic_record['DOCUMENT_RECORD_COUNT'] + 1)),
        }
    data[doc_hash]['entity_ids'].append(analytic_record['RP_ENTITY_ID'])
    data[doc_hash]['missing_indexes'].remove(analytic_record['DOCUMENT_RECORD_INDEX'])


def parse_file(file_path: str) -> dict:
    data = dict()
    with open(file_path, "r") as f:
        for line in f:
            analytic_record = json.loads(line)
            populate_data(analytic_record, data)
    return data

