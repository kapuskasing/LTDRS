# LTDRS（Lecture Ticket Distribution & Record System）
A lecture ticket distribution record system based on BigchainDB.

Chinese version of introduction, please refer to [中文介绍](./Chinese_Introduction/README.md).


## Table of Contents
- [Introduction](#Introduction)
- [Background](#Background)
- [Development Purpose](#Development)
- [Functions](#Functions)
- [Application Scenarios](#Scenarios)
- [Installation](#Installation)
- [Usage](#Usage)
- [Members](#Members)
- [License](#License)

## Introduction <a name="Introduction"></a>
This is a lecture ticket distribution record system based on BigchainDB, which mainly utilizes the main advantages of BigchainDB distributed database and traditional blockchain, so that every lecture ticket issued in this system and its corresponding person can be recorded, which ensures the efficiency and fairness of lecture ticket distribution process.

## Background <a name="Background"></a>
BigchainDB, Chinese called giant chain database, it will be the major advantages of the distributed database and traditional block chain together, is one who has a block chain attributes (for example, decentralization, invariance, autonomy) and attribute database (for example, high transaction rates, low latency, structured data indexing and query) software. Compared with the traditional stand-alone database server, BigchainDB database can better solve the efficiency problems of increasing, deleting, modifying and querying caused by the scale increase; In contrast to the traditional blockchain, BigchainDB is truly "decentralized". In summary, the main special features of the database (version 2.0) include decentralization, Byzantine fault tolerance, immutability, autonomy, low latency, and structured data indexing and querying. </br>
To study the implementation of these special features of BigchainDB, we must first understand the architecture of BigchainDB. In BigchainDB 2.0 version, each node in the BigchainDB network is deployed with a BigchainDB server and an independent MongoDB database. BigchainDB server is built on the basis of MongoDB database. The data from BigchainDB server is stored by MongoDB database, which makes BigchainDB have the characteristics of distributed database. The communication between nodes is determined by Tendermint protocol, which runs on BigchainDB server. It is through Tendermint that each node communicates and thus achieves consensus and the blockchain features of BigchainDB. </br>
The following is a discussion of the implementation of these special functions based on the BigchainDB architecture: </br>
1. Decentralization and Byzantine Fault Tolerance: BigchainDB is decentralized and Byzantine fault-tolerant. As Tendermint is Byzantine fault-tolerant, in the BigchainDB network, each node uses Tendermint to realize the networking and consensus of MongoDB of each node, and then communicates on this basis. Therefore, the entire BigchainDB network is Byzantine fault tolerant, that is, up to one third of the nodes can fail in any way without breaking the consensus within the network, so there is no single point of failure in the BigchainDB network. In addition, because each node in the BigchainDB network has its own local MongoDB database, and the whole BigchainDB network has no single owner, no single control point, and single point of failure is eliminated, BigchainDB is decentralized.
2. Immutable: BigchainDB is immutable. Once data is stored in BigchainDB, it cannot be modified or deleted, or it can leave traces that are detectable. BigchainDB uses several strategies to achieve actual immutability. The most basic policy is not to provide an API to change or erase the stored data. Another policy is that each node has a complete copy of all the data in its own MongoDB database. Another policy is that all transactions are cryptographically signed, and each data change is signed with a private key. Therefore, there must be a little detectable trace left every time a modification or deletion is made.
3. Autonomy: BigchainDB, as a database with blockchain characteristics, also has the concept of asset user control of assets, and no one else can operate on assets that do not belong to them. In BigchainDB, only the owner of the asset can transfer the asset, because each asset transfer must be signed by the owner's private key to achieve autonomy.
4. Low latency: BigchainDB has low latency for transaction processing. Since a consensus network based on Tendermint can package a transaction into a newly committed block quickly (usually in a few seconds), BigchainDB, which uses Tendermint for communication and consensus implementation, features low latency.
5. Structured Data Indexing and Querying: BigchainDB's queries and indexed data can have unique structures. Each node in the BigchainDB 2.0 network has its own local MongoDB database. This means that each node operator has the freedom to decide which interfaces to provide, how to use those interfaces, and what structure to index and query, based on the capabilities of the MongoDB database.
In BigchainDB, the traditional distributed database features are implemented by the MongoDB database that is owned by each node, while the implementation of blockchain features depends on BigchainDB server and Tendermint.
## Development Purpose <a name="Development"></a>
The management of lecture tickets on campus is chaotic, and there is a lack of effective certificates and vouchers. After the transfer of lecture tickets from the school department to the student department, the lack of management and tracking channels leads to the increase of disorder and unreliability in the giving and transfer of lecture tickets. As a result, before the comprehensive test and other examinations, the transaction of money and goods of lecture tickets is prevalent, which seriously violates the original intention of issuing lecture tickets. Therefore, we hope to develop an application system for schools, departments and students by taking advantage of the characteristics of BigchainDB, so that departments can clearly apply for lecture tickets according to their needs, distribute lecture tickets to students, and prevent students from trading lecture tickets to ensure the fairness of lecture ticket mechanism. </br>
Therefore, we hope to develop a program to provide an immutable, secure and reliable system to ensure the fairness and effectiveness of lecture ticket distribution.

## Functions <a name="Functions">
![avatar](/images/use_case.png)
1. Login: Each user should log in with his or her own public key and private key. If the public key and private key do not match, the user will not be given login.
2. Search lecture tickets: Each student can check his or her own lecture tickets. The school, as the administrator, should have the ability to check the lecture tickets of all students and designated students.
3. Transfer of lecture tickets: After creating the lecture tickets, the school should transfer the lecture tickets to each department, and the department should also have the function of distributing the lecture tickets to designated students.
4. Create lecture tickets: the department will apply for lecture tickets from the school, provide the information of lecture tickets and the required quantity, and the school will have the ability to approve the application and create lecture tickets for the department.


## Application Scenario  <a name="Scenarios"></a>
In this system, we have designed three different users: administrators, student departments and students. Let's look at a simple example:

(1) Suppose that a new learning department is set up in the School of Software. The minister needs to register the name of the department in the student department and obtain a unique pair of keys through which the minister can log in. After logging in successfully, the minister can fill in an application form and submit it to the school administrator for review. Such as:

```
Activity name: one to one help learning
Event time: 2020.6.28-2020.8.1
Venue: A1 Teaching Building, University Town Campus
Number of tickets: 300
```
The form information is unique in the chain, eliminating the possibility of creating invalid activities repeatedly. If approved, the department account will get the lecture ticket asset created by the administrator.
After that, when the activity was carried out, the staff of the department could collect the student numbers of the students who participated in the activity and register them in the department account. Meanwhile, the department account also added additional conditions to the output: when these assets were to be transferred, the password signature of the department account was required, thus eliminating the possibility of lecture ticket trading. The lecture tickets have been transferred to the students.

(2) The administrator side will give the administrator a default account. After logging in, the administrator can view the activity declaration of the department side and choose not to reject the modification or pass the activity. If through the activity, the asset with the corresponding information is also created and transferred to the corresponding department. In addition, the administrator can also publish the activity information, and the activity information link can be displayed on the student side for students to click and view.
In addition, the administrator also has the right to finally count the total number of lecture tickets, that is, he can query the legal lecture tickets owned by all students, or query the legal lecture tickets owned by a specific student through the student number.

(3) When entering the university, students can use their student ID to register and obtain their own account (i.e. public-private key pair) on the registration page of the student side, and then students can log in their account through the key pair.
After logging in the account, students can query the lecture tickets they own by inputting their student ID. Of course, the number of lecture tickets is the information that can be made public, and students can also query others' lecture ticket information by entering their student numbers, but we do not open the port to query all students' information.

## Installation <a name="Installation"></a>
We use Ubuntu 18.04's ISO running front and back end system, and use PyCharm under Flask framework to generate visual interface under BigchainDB, MongoDB, Terminate Node.

* Client: 
Use the browser to open the web page and follow the prompts to use.

![avatar](/images/module.png)
* Server:

Installation environment: Ubuntu18.04, Python version>=3.4.2</br>
Install the BigchainDB database and the driver package BigchainDB-driver for Python, and program according to the driver. The details are as follows:

1. Install the BigchainDB in the line of professional guide```pip install -U BigchainDB-driver```(please install python3 & pip first)</br>
![avatar](/images/installation1.png)

2. use ```sudo apt install mongodb``` to install mongodb</br>
![avatar](/images/installation2.png)

3. Install flask using ```pip install flask```</br>
![avatar](/images/installation3.png)

4. Install BigchainDB using ```pip3 install BigchainDB```</br>
![avatar](/images/installation4.png)

5. BigchainDB-y Configure MongoDB</br>
![avatar](/images/installation5_1.png)
![avatar](/images/installation5_2.png)

6. Download Tendermint and install it</br>
![avatar](/images/installation6.png)</br>
(BigchainDB is developed based on Tendermint. Because it is very slow to download the project from GitHub in China, the example can be downloaded by a third party and then unzip and install.)

7. Start BigChainBD service:</br>
![avatar](/images/installation7.png)

8. Run the deployment server code
## Usage <a name="Usage"></a>
![avatar](/images/usage1.png)

home:</br>
![avatar](/images/usage2.png)

The students side:</br>
![avatar](/images/usage3.png)

Registration:(return the public and private key)</br>
![avatar](/images/usage4.png)

Login:</br>
![avatar](/images/usage5.png)

Query: </br>
![avatar](/images/usage6.png)

The department side: distribution of lecture tickets</br>
![avatar](/images/usage7.png)

Student side receives:</br>
![avatar](/images/usage8.png)

## Project Members <a name="Members"></a>

- [Xavi](https://github.com/HeXavi8) - **Xavi He** &lt; 825308876@qq.com&gt; (he/him)
- [kapuskasing](https://github.com/kapuskasing) - **Kapuskasing Su** &lt; 1243038585@qq.com&gt; (he/him)

## License <a name="License"></a>
[MIT](./LICENSE)
