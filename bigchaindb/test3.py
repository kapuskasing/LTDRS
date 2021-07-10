from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair


def regester(student_id):
    bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here

    bdb = BigchainDB(bdb_root_url)

    t = bdb.assets.get(search=str(student_id))#查看该学号是否已经注册过

    if(len(t)!=0):
        return [];

    # 产生一个key对
    temp_key = generate_keypair()

    # 定义一个字典来存储key
    temp = {'public_key': temp_key.public_key, "private_key": temp_key.private_key}

    infoAsset = {
        'data': {
            'student_id':str(student_id),
            'public_key': temp_key.public_key,
        }
    }

    metadata = {
        'type': "creat",
        'person':'test',
    }

    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=temp['public_key'],  # alice.public_key,
        asset=infoAsset,
        # metadata=metadata
    )
    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx,
        private_keys=temp['private_key']  # alice.private_key,
    )
    sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)

    print(sent_creation_tx)

    return temp

