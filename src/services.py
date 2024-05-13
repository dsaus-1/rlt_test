from pymongo import ASCENDING
import asyncio, datetime
from src.db.config import db, DB_COLLECTION


async def check_current_dete(collection_dict):
    dataset = []
    labels = []
    async for line in collection_dict:
        dataset.append(line['value'])
        _id = line["_id"]
        year = _id.get("year", 1)
        month = _id.get("month", 1)
        day = _id.get("day", 1)
        hour = _id.get("hour", 0)
        labels.append(datetime.datetime(year, month, day, hour).strftime('%Y-%m-%dT%H:%M:%S'))

        result = {'dataset': dataset, 'labels': labels}
        return result

async def get_data(db, collection_name, dt_from, dt_upto, group_type):
    dt_from_obj = datetime.datetime.strptime(dt_from, '%Y-%m-%dT%H:%M:%S')
    dt_upto_obj = datetime.datetime.strptime(dt_upto, '%Y-%m-%dT%H:%M:%S')

    group_type_dict = {
        "year": {"$year": "$dt"},
        "month": {"$month": "$dt"}
    }
    g_type = group_type.lower()

    if g_type == "day":
        group_type_dict["day"] = {"$dayOfMonth": "$dt"}
    elif g_type == "hour":
        group_type_dict["day"] = {"$dayOfMonth": "$dt"}
        group_type_dict["hour"] = {"$hour": "$dt"}


    if g_type in ['month', 'day', 'hour']:

        pipeline = [
            {
                "$match": {
                    "dt": {"$gte": dt_from_obj, "$lte": dt_upto_obj}
                }
            },
            {
                "$group": {
                    "_id": group_type_dict,
                    "value": {"$sum": "$value"}
                }
            },
            {
                "$sort": {
                    "_id.month": ASCENDING,
                    "_id.day": ASCENDING,
                    "_id.hour": ASCENDING,
                }
            },
        ]

        collection = db[collection_name]

        dataset = []
        labels = []

        async for line in collection.aggregate(pipeline):
            dataset.append(line['value'])
            _id = line["_id"]
            year = _id.get("year", 1)
            month = _id.get("month", 1)
            day = _id.get("day", 1)
            hour = _id.get("hour", 0)
            labels.append(datetime.datetime(year, month, day, hour).strftime('%Y-%m-%dT%H:%M:%S'))

        return {'dataset': dataset, 'labels': labels}
