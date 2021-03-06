from bigchaindb_driver import BigchainDB

bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here
bdb = BigchainDB(bdb_root_url)  # 创建一个数据库对象

#查询所有学生的讲座票依赖于该函数
def search(student_id):   #  查找某个学生的讲座票，参数为学号，返回值为一个存储讲座票信息的数组

    bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here
    bdb = BigchainDB(bdb_root_url)   # 创建一个数据库对象

    result=[]  #定义返回的学生的讲座票

    # 获取学生的公钥
    s = bdb.assets.get(search=str(student_id))
    if(len(s)==0):   # 如果这个学号没有注册过，则返回空数组
        return []
    student_public_key = s[0]['data']['public_key']


    #查看该公钥作为output的资产，并且该资产未被转移出去
    t = bdb.outputs.get(public_key=student_public_key, spent='false')

    for i in range(1, len(t)):    #  由于学生的第一个资产是自己的信息，所以不考虑在内
        temp = bdb.blocks.get(txid=t[i]['transaction_id'])   #  根据output查询中得到的transaction id查询该资产在区块链中的的块号
        block_temp=bdb.blocks.retrieve(block_height=str(temp))  #  利用块号查询块
        asset_t=bdb.assets.get(search=block_temp['transactions'][0]['asset']['id'])   #根据查询到的块获取讲座票的id，并添加到数组中
        dept=bdb.assets.get(search=block_temp['transactions'][0]['inputs'][0]['owners_before'])  # 查看发该讲座票的部门
        result_t={  # 将讲座票的信息和部门的名字加入的临时变量中
            'ticket':asset_t[0]['data'],
            'dept_name':dept[0]['data']['dept_name']
        }
        result.append(result_t)  # 加入到结果中

    # print(result)
    return result

#查询所有学生的讲座票的函数,无参数,返回值为每个学号及其对应的讲座票
def search_all():
    t = bdb.assets.get(search='student')   #  查询所有学生的信息
    result = []    #  定义结果
    for i in range(0, len(t)):   #  遍历所有学生信息
        student_id_t = t[i]['data']['student_id']  #  获取学生的学号
        asset_t = search(student_id_t)    #  查询该学生的讲座票
        result_t = {   #  将该学生的讲座票和学号对应存储
            'ticket': asset_t,
            'student_id': student_id_t
        }
        result.append(result_t)  #  加入到结果中

    return result