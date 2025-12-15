from App.datasets import get_all_dataset_metadata
from App.database import conn

print(get_all_dataset_metadata(conn))
