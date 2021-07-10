from bigchaindb_driver import BigchainDB
import re
from bigchaindb_driver.crypto import generate_keypair
from search import *

bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here
bdb = BigchainDB(bdb_root_url)
# p = r'I前沿'
#
# print(p)

# t=bdb.transactions.get()

t = bdb.assets.get(search='bigchaindb专题讲座')
# bdb.assets.get(search=r'[0-9]')
print(t)
# result=[]
# for i in range(0,len(t)):
#     s_id_t=t[i]['data']['student_id']
#     a_t=search(s_id_t)
#     r_t={
#         'ticket':a_t,
#         'student_id':s_id_t
#     }
#     result.append(r_t)
#
# print(result)
# t2=bdb.assets.get(search='AI前沿' and 'B8副楼报告厅' and 'B7副楼报告厅')
# t3=bdb.assets.get(search='201830680111')
# t4=bdb.outputs.get(public_key='9MMWco81E8fBrBVpHgEFmEsEar8mFbntbHCQLxbwPdvy',spent='false')
# print(t4)
# print('\n\n')
# for i in range(0,len(t4)):
#     temp=bdb.blocks.get(txid=t4[i]['transaction_id'])
#     # print(temp)
#     print(bdb.blocks.retrieve(block_height=str(temp)))
# print(t3[0]['data']['public_key'])

# t1=bdb.transactions.get(asset_id='85b86a8735f6f49d9088c66e9cbb1a886d9a4decda9c0027bb0585eca306ccf0')
# print(t1)
