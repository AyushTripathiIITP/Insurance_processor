
import json
import os

def store_document(file_path, text, classification):
    """
    Simulates storing the document chunks in ElasticSearch.
    Writes the data to a JSON file instead.
    """
    output_dir = os.path.join(os.path.dirname(file_path), "../output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"{os.path.basename(file_path)}.json")

    data = {
        "classification": classification,
        "chunks": text.split('\n'),
    }

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    return output_path
