from bigchaindb_driver import BigchainDB

def transaction(student_id,name,dept_public_key,dept_private_key):   #   给学生发讲座票，参数为学号和讲座票的名字,部门的公钥和私钥

    bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here

    bdb = BigchainDB(bdb_root_url)#定义一个数据库的对象

    id_t = bdb.assets.get(search=str(name))

    ticket_id=id_t[0]['id']

    #获取学生的公钥
    s=bdb.assets.get(search=str(student_id))
    # print(s)
    student_public_key=s[0]['data']['public_key']


    t=[]

    output_t = bdb.outputs.get(public_key=dept_public_key, spent='false')
    for i in range(1, len(output_t)):
        temp = bdb.blocks.get(txid=output_t[i]['transaction_id'])
        block_t=bdb.blocks.retrieve(block_height=str(temp))
        if block_t['transactions'][0]['asset']['id']==ticket_id:
            t=block_t['transactions']
            break

    num=0
    output_index = 0
    for j in range(0,len(t[0]['outputs'])):
        if t[0]['outputs'][j]['public_keys'][0]==dept_public_key:
            num=t[0]['outputs'][j]['amount']
            output_index=j
            break
    # print(t)
    # print(num)

    transfer_asset = {
        'id': ticket_id,
    }

    output = t[0]['outputs'][output_index]
    transfer_input = {
        'fulfillment': output['condition']['details'],
        'fulfills': {
            'output_index': output_index,
            'transaction_id': t[0]['id'],
        },
        'owners_before': output['public_keys'],
    }

    prepared_transfer_tx = bdb.transactions.prepare(
        operation='TRANSFER',
        asset=transfer_asset,
        inputs=transfer_input,
        recipients=[([student_public_key],1),([dept_public_key],int(num)-1)],
    )

    fulfilled_transfer_tx = bdb.transactions.fulfill(
        prepared_transfer_tx,
        private_keys=dept_private_key,  # 用部门私钥签名
    )

    sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)

    # print(sent_transfer_tx)