from bigchaindb_driver import BigchainDB

# 创建讲座票，参数为学校的公钥，私钥，讲座的信息，如名字，时间，地点,讲座票类型，分数，主办部门,以及讲座票的数量
# 主办部门应该是发该讲座票的部门
def create(school_public_key,school_private_key,name,time,location,type,score,dep_name,num):

    bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here

    bdb = BigchainDB(bdb_root_url)#定义一个数据库的对象

    ticketAsset = {    #  the ticket asset
        'data': {
            'name':name,
            'time':time,
            'location':location,
            'type':type,
            'score':score,
        }
    }

    #为学校创建讲座票
    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=school_public_key,  # public_key of school,
        recipients=[([school_public_key],num)],
        asset=ticketAsset,
    )
    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx,
        private_keys=school_private_key # private_key of school,
    )
    sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)  # commit the ticket

    temp=sent_creation_tx   # 该资产

    # 获取部门的public key
    dept_t=bdb.assets.get(search=str(dep_name))
    dept_public_key=dept_t[0]['data']['public_key']

    #学校将该资产发给部门
    transfer_asset = {
        'id': temp['id'],
    }

    output_index = 0
    output = temp['outputs'][0]

    transfer_input = {
        'fulfillment': output['condition']['details'],
        'fulfills': {
            'output_index': output_index,
            'transaction_id': temp['id'],
        },
        'owners_before': output['public_keys'],
    }

    prepared_transfer_tx = bdb.transactions.prepare(
        operation='TRANSFER',
        asset=transfer_asset,
        inputs=transfer_input,
        recipients=[([dept_public_key],num)],
    )
    fulfilled_transfer_tx = bdb.transactions.fulfill(
        prepared_transfer_tx,
        private_keys=school_private_key,  # private_key,这里的私钥就是上一次交易公钥对应的私钥
    )

    bdb.transactions.send_commit(fulfilled_transfer_tx)  # 提交