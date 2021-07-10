from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here
bdb = BigchainDB(bdb_root_url)
alice=generate_keypair()
bob=generate_keypair()
print(alice.public_key)
print(alice.private_key)
print(bob.public_key)
print(bob.private_key)
# print(bob)
# print(alice)
# bobpublice='2635d3tcKkRiXvKss97pEZZaga64UZz2wrd6jgYN1qzD'
# bobprivate='GKMwAD2ctXS6kiyyWeLVt2cjJ9P8MjjmopySpSFhAfr1'
# apublic='8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3'
# aprivate='6tC48gmc9dsbEbtb536zipg8jh4jFUQ4PyhiD9oFqddc'
# bob={'public_key':'2635d3tcKkRiXvKss97pEZZaga64UZz2wrd6jgYN1qzD',"private_key":'GKMwAD2ctXS6kiyyWeLVt2cjJ9P8MjjmopySpSFhAfr1'}
# alice={'public_key':'8nDWownPHdAML5VmSgbjSrerLqavDpozfqAM8USSNUX3',"private_key":'6tC48gmc9dsbEbtb536zipg8jh4jFUQ4PyhiD9oFqddc'}
































def transcation(sid,bid,cid,ckey,bkey,time):
    testmatadata = bdb.metadata.get(search=sid)
    # print(testmatadata)
    b1 = ''
    for i in testmatadata:
        if i['metadata']['type'] == 'distribute':
            b1 = i['id']
    b = bdb.transactions.get(asset_id=b1)
    # testmatadata1 = bdb.metadata.get(search="123")
    asset_id = b[0]['asset']['id']
    # print(asset_id)
    transfer_asset = {
        'id': asset_id, }
    output_index = 0
    output = b[0]['outputs'][0]
    # print(output)
    transfer_input = {
        'fulfillment': output['condition']['details'],
        'fulfills': {
            'output_index': output_index,
            'transaction_id': b[0]['id'],
        },
        'owners_before': output['public_keys'],
    }
    print(transfer_input['owners_before'])
    metadata1 = {
        'sid': sid,
        'bid': bid,
        'cid': cid,
        'type': "transaction",
        'time':time#datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }
    prepared_transfer_tx = bdb.transactions.prepare(
        operation='TRANSFER',
        asset=transfer_asset,
        metadata=metadata1,
        inputs=transfer_input,
        recipients=ckey#'7TYbbqibFuL4J5bYpFUPKESpdfGCwbPKPJi9tHphUQmz',  # bob.public_key,
    )
    fulfilled_transfer_tx = bdb.transactions.fulfill(
        prepared_transfer_tx,
        private_keys=bkey#'C77dxQ1QvjVkgV34s2zA96evu8rjdgLcUkvfgGLV4uAy',  # alice.private_key,
    )
    sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)
    print(sent_transfer_tx)
# p=transcation('test002','15521265685',"15521265684",'3jeBcqsLJ9sYo3fXWvV15iEGqv5GunfFawNjNDsdt8Ru','CTVqWErE8XN9skXX3StBHKtZU4tYviHRSoNYaBb4xkYA','22:27:05')