from pymongo import MongoClient
from pprint import pprint

# mongodb://user:user123@localhost27017.mongolab.com:33499/enron
mongodb_url = 'localhost'

def get_server_status():
    client = MongoClient(mongodb_url)

    db = client.admin
    serverStatusResult = db.command('serverStatus')
    pprint(serverStatusResult)


def read_app_account():
    client = MongoClient(mongodb_url)

    db = client.moneyAnalyzerDB
    count = db.appAccounts.find().count()
    print(count)

    appAccount = db.appAccounts.find_one({'name':'RobMartaFam'})
    print(appAccount)


if __name__ == '__main__':
    read_app_account()
