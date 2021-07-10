from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = 'localhost:9984'

bdb = BigchainDB(bdb_root_url)

alice = generate_keypair()

print(alice)

# hello_1 = {'data': {'msg': 'Hello BigchainDB 1!'},}
# hello_2 = {'data': {'msg': 'Hello BigchainDB 2!'},}
# hello_3 = {'data': {'msg': 'Hello BigchainDB 3!'},}
#
# # set the metadata to query for it in an example below
# metadata = {'planet': 'earth'}
#
# prepared_creation_tx = bdb.transactions.prepare(
#     operation='CREATE',
#     signers=alice.public_key,
#     asset=hello_1
# )
# fulfilled_creation_tx = bdb.transactions.fulfill(
#     prepared_creation_tx, private_keys=alice.private_key)
# # bdb.transactions.send_commit(fulfilled_creation_tx)
# print(fulfilled_creation_tx)
# prepared_creation_tx = bdb.transactions.prepare(
#     operation='CREATE',
#     signers=alice.public_key,
#     asset=hello_2
# )
# print(prepared_creation_tx)
# fulfilled_creation_tx = bdb.transactions.fulfill(
#     prepared_creation_tx, private_keys=alice.private_key)
# # bdb.transactions.send_commit(fulfilled_creation_tx)
#
# prepared_creation_tx = bdb.transactions.prepare(
#     operation='CREATE',
#     signers=alice.public_key,
#     asset=hello_3
# )
# fulfilled_creation_tx = bdb.transactions.fulfill(
#     prepared_creation_tx, private_keys=alice.private_key)
# bdb.transactions.send_commit(fulfilled_creation_tx)