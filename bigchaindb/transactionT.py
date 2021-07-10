from initbdb import bdb,bob,alice
def tarnsactiont():
 #这是紧接着创建后的第二次及以上交易
 testasset = bdb.metadata.get(search='S007')#首先首先首先通过metadata查询交易ID
 #此时会出现多条信息，显而易见的。其结果按时间先后顺序排序，我们需要最后一条结果。
 # print(testasset)
 #这里可以自己打印一下观察查询结果
 """
[{'id': 'd51ede7124152f8ba5cb40d3bc2d254f0bb9fb1d1e7af0df8dfe3054e6137daa', 'metadata': {'type': 'creat', 'time': '2001-12-30 15:55:89', 'carID': 'S007', 'mileage': '200', 'person': '小明'}}, 
{'id': 'ca9e9eb2486735f13eba4ef038c7cd72132eace385b6c36496139b595d41aec7', 'metadata': {'type': 'drive', 'time': '2001-12-30 15:55:89', 'carID': 'S007', 'mileage': '200', 'person': '小明'}}]
"""
 c = bdb.transactions.get(asset_id=testasset[len(testasset)-1]['id'])  # 这一步通过交易ID进行交易查询可以查看到交易的具体内筒
 # print(c)
 """
[{'inputs': [{'owners_before': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'], 
            'fulfills': {'transaction_id': 'd51ede7124152f8ba5cb40d3bc2d254f0bb9fb1d1e7af0df8dfe3054e6137daa',
             'output_index': 0}, 
             'fulfillment': 'pGSAIHOXGC76k6onC7r-3nAt1ycb8Ys2JaScNJMK3JCKK2JSgUA7SlF01QMrRIUuqowT60eADhDQK12ZQ9vr1poPrFwuL5HliBwoKX0LoLn-8eiaguD8eV7V409VEKD_Yu6k6dkA'}],
 'outputs': [{'public_keys': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'], 
                'condition': {'details': {'type': 'ed25519-sha-256', 'public_key': '8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'},
                 'uri': 'ni:///sha-256;t51TF-HyKcVh-B50PSYXRRxuCPyB4f1CS65nilEqyko?fpt=ed25519-sha-256&cost=131072'}, 'amount': '1'}],
'operation': 'TRANSFER',
'metadata': {'type': 'drive', 'time': '2001-12-30 15:55:89', 'carID': 'S007', 'mileage': '200', 'person': '小明'},
 'asset': {'id': 'd51ede7124152f8ba5cb40d3bc2d254f0bb9fb1d1e7af0df8dfe3054e6137daa'}, 
 'version': '2.0',
'id': 'ca9e9eb2486735f13eba4ef038c7cd72132eace385b6c36496139b595d41aec7'}]
"""
 #这里打印一下，开发过程对于bigchaindb里面数据不太熟悉时可以通过打印一下自己观察一下
 #这里可以看到asset已经变成ID了，这里的ID也是我们后续进行交易所需要用到的资产ID，”ca9e9……“这个是交易ID
 #因此这里将交易ID代替了资产ID
 transfer_asset = {
     'id': c[0]['asset']['id'],
 }
 #区别所在，由于create完成后的第一笔交易没有资产ID因此将交易ID代替成资产ID，现在后续的交易都有资产ID存在因此需要注意这里
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
        'mileage': '500',
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
 sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)
 print(sent_transfer_tx)
"""
{'asset': {'id': 'd51ede7124152f8ba5cb40d3bc2d254f0bb9fb1d1e7af0df8dfe3054e6137daa'}, 
'id': '576f93592fbdefc48ea91b82eee29330c32e34c959c4ce265baa22a6f13a6a21', 
'inputs': [{'fulfillment': 'pGSAIHOXGC76k6onC7r-3nAt1ycb8Ys2JaScNJMK3JCKK2JSgUBxhloYw_4z96omUAFvO8VCA_6ZHFq5fRm3KQ2sSJ9WWOpdRqNGnzpCRsAIjrBwAF36-HEaKV2zrHpXFSNwd70H', 
              'fulfills': {'output_index': 0, 'transaction_id': 'ca9e9eb2486735f13eba4ef038c7cd72132eace385b6c36496139b595d41aec7'}, 
              'owners_before': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3']}], 
'metadata': {'carID': 'S007', 'mileage': '500', 'person': '小明', 'time': '2001-12-30 15:55:89', 'type': 'drive'}, 
'operation': 'TRANSFER', 
'outputs': [{'amount': '1', 'condition': {'details': {'public_key': '8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3', 'type': 'ed25519-sha-256'},
 'uri': 'ni:///sha-256;t51TF-HyKcVh-B50PSYXRRxuCPyB4f1CS65nilEqyko?fpt=ed25519-sha-256&cost=131072'},
  'public_keys': ['8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3']}],
   'version': '2.0'}


"""
tarnsactiont()