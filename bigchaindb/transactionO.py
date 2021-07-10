from initbdb import bdb,bob,alice
def tarnsactiono():
 #这是紧接着创建后的第一次交易
 testasset = bdb.metadata.get(search='S007')
 #通过资产查询，找到交易ID
 # print(testasset)#这里可以自己打印一下观察查询结果
 """
 [{'data': {'carBrand': '大奔', 'carID': 'S007'},#这里是资产里面的data字段对应的数据
   'id': 'd51ede7124152f8ba5cb40d3bc2d254f0bb9fb1d1e7af0df8dfe3054e6137daa'}#这里就是交易ID
 ]
"""
 c = bdb.transactions.get(asset_id=testasset[0]['id'],operation = 'CREATE'  )  # 这一步通过交易ID进行交易查询可以查看到交易的具体内筒
                    # 为了交易准备需要的参数做准本
 # print(c)
 """
[{'inputs': [{'owners_before': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'], 
               'fulfills': None,
               'fulfillment': 'pGSAIHOXGC76k6onC7r-3nAt1ycb8Ys2JaScNJMK3JCKK2JSgUAACr3uL_EprnL5_zNxL0hiQppM1KKUKLXu3vbREaWI-nsTpJyehLSOI4wBDKe0uA7BeAwNwS2ouF1wPBDeClsL'}],
   'outputs': [{'public_keys': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'], 
                'condition': {'details': {'type': 'ed25519-sha-256',
                                          'public_key': '8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'},
                              'uri': 'ni:///sha-256;t51TF-HyKcVh-B50PSYXRRxuCPyB4f1CS65nilEqyko?fpt=ed25519-sha-256&cost=131072'},
                'amount': '1'}], 
   'operation': 'CREATE',
   'metadata': {'type': 'creat', 'time': '2001-12-30 15:55:89', 'carID': 'S007', 'mileage': '200', 'person': '小明'},
   'asset': {'data': {'carBrand': '大奔', 'carID': 'S007'}},
   'version': '2.0',
   'id': 'd51ede7124152f8ba5cb40d3bc2d254f0bb9fb1d1e7af0df8dfe3054e6137daa'}]
"""
 #这里打印一下，开发过程对于bigchaindb里面数据不太熟悉时可以通过打印一下自己观察一下
 #特别注意的是这里“id”是交易ID，二我们需要用到的是资产ID，对于创建而比较特赦，因为它的资产是‘大奔’这些具体数据而不是ID
 #因此这里将交易ID代替了资产ID
 transfer_asset = {
     'id': c[0]['id'],
 }
 #这里需要的是资产ID因为可以发现这个地方填写的是资产。资产是不变的，交易ID是改变的代表着唯一的交易，
 # 所以这里要特别区分一下，在transactionT中就是后续一般的情况
 output_index = 0
 output = c[0]['outputs'][0]
 transfer_input = {
     'fulfillment': output['condition']['details'],
     'fulfills': {
         'output_index': output_index,
         'transaction_id': c[0]['id'],
     },
     'owners_before': output['public_keys'],
 }
 #这里是交易对象的信息，也就是交易发起人的信息即当前持有者。
 metadata = {
#这里又是自定义的数据，可以设想这是第一次驾驶，把驾驶信息记录下来
        'type': "drive",
        'time': "2001-12-30 15:55:89",
        'carID':'S007',
        'mileage': '200',
        'person':'小明',
        # 自己设计的补充数据,键值对对形式。每次交易都可以重新修改，但最好保持一致。将这个当成数据库中的数据表进行设计。
 }
 prepared_transfer_tx = bdb.transactions.prepare(
     operation='TRANSFER',
     asset=transfer_asset,
     metadata=metadata,
     inputs=transfer_input,
     recipients=alice['public_key'], # .public_key,这里交易对象的公钥，我要把车转给谁，
                                      # 要是仅仅进行汽车行驶里程的记录，汽车没有进行交易，汽车没有易主，那么这里应该还是填Alice的公钥

 )
 fulfilled_transfer_tx = bdb.transactions.fulfill(
     prepared_transfer_tx,
     private_keys=alice['private_key'],  # alice.private_key,这里的私钥就是上一次交易公钥对应的私钥
 )
 # sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)

 # print(sent_teansfer_tx)
"""
[{'inputs': [{'owners_before': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'], 
              'fulfills': None, 
              'fulfillment': 'pGSAIHOXGC76k6onC7r-3nAt1ycb8Ys2JaScNJMK3JCKK2JSgUAACr3uL_EprnL5_zNxL0hiQppM1KKUKLXu3vbREaWI-nsTpJyehLSOI4wBDKe0uA7BeAwNwS2ouF1wPBDeClsL'}], 
              'outputs': [{'public_keys': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'], 
              'condition': {'details': {'type': 'ed25519-sha-256', 'public_key': '8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'}, 
              'uri': 'ni:///sha-256;t51TF-HyKcVh-B50PSYXRRxuCPyB4f1CS65nilEqyko?fpt=ed25519-sha-256&cost=131072'}, 'amount': '1'}], 
              'operation': 'CREATE', 'metadata': {'type': 'creat', 'time': '2001-12-30 15:55:89', 'carID': 'S007', 'mileage': '200', 'person': '小明'}, 
              'asset': {'data': {'carBrand': '大奔', 'carID': 'S007'}}, 
              'version': '2.0', 
              'id': 'd51ede7124152f8ba5cb40d3bc2d254f0bb9fb1d1e7af0df8dfe3054e6137daa'}]

"""
# tarnsactiono()

