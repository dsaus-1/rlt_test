from src.db.config import db, client, DB_COLLECTION
from src.main import dir_path

from bson import decode_file_iter


async def do_insert(db, collection_name, path_to_file):
     with open(path_to_file, 'rb') as documents:
         await db[collection_name].insert_many(decode_file_iter(documents))


async def fetch_all_data(db, collection_name):
    collection = db[collection_name]
    cursor = collection.find({})

    async for document in cursor:
        print(document)


if __name__ == '__main__':
    loop = client.get_io_loop()
    loop.run_until_complete(do_insert(db, DB_COLLECTION, f'{dir_path}/sampleDB/sample_collection.bson'))
    #loop.run_until_complete(fetch_all_data(db, DB_COLLECTION))