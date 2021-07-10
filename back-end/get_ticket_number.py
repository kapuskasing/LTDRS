from bigchaindb_driver import BigchainDB


def get_ticket_number(name, dep_name):  # 查找讲座的数量，参数为讲座票的名字和部门的名字,返回值为数量

    bdb_root_url = 'localhost:9984'  # BigchainDB Root URL

    bdb = BigchainDB(bdb_root_url)  # 定义一个数据库的对象

    # 获取部门的public key
    dept_t = bdb.assets.get(search=str(dep_name))
    dept_public_key = dept_t[0]['data']['public_key']

    id_t = bdb.assets.get(search=str(name))  # 根据讲座票的名字获取讲座票资产

    ticket_id = id_t[0]['id']  # 获取讲座票资产的id

    t = []  # 存储查询的讲座票的事务的中间变量

    output_t = bdb.outputs.get(public_key=dept_public_key, spent='false')  # 利用部门的public key查找该部门现拥有的讲座票资产
    for i in range(1, len(output_t)):  # 遍历这些资产查找目标讲座票,由于部门的第一个资产为部门信息，因此跳过
        temp = bdb.blocks.get(txid=output_t[i]['transaction_id'])  # 通过事务id查询区块高度
        block_t = bdb.blocks.retrieve(block_height=str(temp))  # 通过区块高度查询事务的具体内容
        if block_t['transactions'][0]['asset']['id'] == ticket_id:  # 判断事务的资产是否为该讲座票
            t = block_t['transactions']  # 是则将该事务存储到中间变量
            break

    num = 0  # 部门目前拥有的讲座票数量，用于后面发讲座票时维持总数不变

    for j in range(0, len(t[0]['outputs'])):  # 遍历事务的输出，查找该部门拥有的数量和索引
        if t[0]['outputs'][j]['public_keys'][0] == dept_public_key:  # 判断该输出是否对应于部门
            num = t[0]['outputs'][j]['amount']  # 是则获取数量
            break

    return num
