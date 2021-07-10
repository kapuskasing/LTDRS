from bigchaindb_driver import BigchainDB

def get_ticket_id(name):     #  获取讲座票的id，参数为讲座的名字，返回值为讲座的id
    bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here
    bdb = BigchainDB(bdb_root_url)
    t = bdb.assets.get(search=str(name))

    return t[0]['id']