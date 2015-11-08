from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
database = client['app']


# tables
transactions =  database['transactions']
merchant_info = database['merchant_info']
beacon_to_merchant = database['beacon_to_merchant']
beacon_status = database['beacon_status']
namespace_to_merchant = database['namespace_to_merchant']


# store information
merchant = {
        "public_key":  "sbpb_MTVkN2ZhMmQtNTBiZi00MGYyLWIzOTEtODgxODBmYzU4MzU5",
        "private_key": "O8EOz5Z6doFeGDv/9cqSwJKaL6Ylu26x0VNxD7W1CJd5YFFQL0ODSXAOkNtXTToq",
        "name": "SUNAC FOODS",
        "address":"155 CLAREMONT AVE",
        "city":"New York",
        "state":"NY",
        "zip":"10001",
        "tips":[0.18,0.20,0.25],
        "tax":0.09013
    }

merchant_id = merchant_info.insert_one(merchant)

# storing namespace --> merchant
namespace_to_merchant.insert_one({"namespace": "EDD1EBEAC04E5DEFA017", "merchant_id": str(merchant_id.inserted_id)})

# get the merchnat info based on namespace
merchant_id = namespace_to_merchant.find_one({"namespace":namespace})['merchant_id']
merchant_info.find_one({"_id":merchant_id.inserted_id})

#beacon to merchant match
beacon_id = ["d157546925db", "fcdbd748bc8e"]
for x in beacon_id:
    beacon_to_merchant.insert_one({"beacon_id":x, "merchant_id":merchant_id.inserted_id})
    beacon_history.insert_one({"beacon_id":x, "orders":[]})


# beacon_status setup when an order comes

order = [{"name": "gin", "times":1, "price":2.54, "#claimed":0, "claim_users":[]},\
{"name":"grilled_chicken","times":2, "price":3.45, "#claimed":0, "claim_users":[]}]

post = {"order_id":"asdasdad",
 "beacon_id" : beacon_id,
 "select_items":order,
 "timestamp":1314423,
 "payment_status":{"number_of_users":0, "current_total_":0, "users":{},'paid':0},
 "running_total":0
}
