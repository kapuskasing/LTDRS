from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from flask import Flask,render_template,request

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
            'type':'student'
        }
    }

    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=temp['public_key'],  # alice.public_key,
        asset=infoAsset,
    )
    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx,
        private_keys=temp['private_key']  # alice.private_key,
    )
    sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)

    return temp

app=Flask(__name__)

@app.route('/')
def regester_UI():
    return render_template('test.html')

@app.route('/regester', methods=['POST','GET'])
def re():
    if request.method=='POST':
        student_id = request.form['student_id']
        re1 = regester(student_id)
        print(type(re1))
        return render_template('regester.html', result=re1)


if __name__ == '__main__':
    app.run()