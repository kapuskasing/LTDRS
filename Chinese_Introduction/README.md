# LTDRS（Lecture Ticket Distribution & Record System）
基于bigchainDB的讲座票分发记录系统

## 目录
- [项目介绍](#Introduction)
- [技术背景](#Background)
- [开发目的](#Development)
- [安装配置](#Installation)
- [使用方法](#Usage)
- [License](#License)

## 项目介绍 <a name="Introduction"></a>
这是一款基于bigchainDB的讲座票分发记录系统，主要利用了bigchainDB分布式数据库和传统区块链的主要优点，使得在该系统的每一张发放的讲座票与对应的人都有所记录，保证了讲座票分发过程的效率与公平性。

## 技术背景 <a name="Background"></a>
BigchainDB，中文名为巨链数据库，它将分布式数据库和传统区块链的主要优点组合在一起，是一个具有区块链属性（例如，去中心化，不变性，自治性）和数据库属性（例如，高事务处理率，低延迟，结构化数据的索引和查询）的软件。对比起传统的单机数据库服务器，BigchainDB数据库能够更好的解决由于规模增大而导致的增加、删除、修改、查询的效率问题；而对比起传统的区块链，BigchainDB真正做到了“去中心化“。总而言之，该数据库（2.0版本）主要的特殊功能包括去中心化，拜占庭容错，不可篡改，自治性，低延迟以及结构化数据索引和查询。</br>
要研究BigchainDB这些特殊功能的实现方法，首先要了解BigchainDB的架构。在BigchainDB2.0版本中，在BigchainDB网络中的每一个节点都有部署有一个BigchainDB服务器和一个独立的MongoDB数据库，BigchainDB服务器就是建立在MongoDB数据库的基础上，由MongoDB数据库对来自于BigchainDB服务器的数据进行存储，使得BigchainDB具有分布式数据库的特性，各个节点之间的通信则是由Tendermint协议决定，该协议运行在BigchainDB服务器之上，各个节点就是通过Tendermint进行通信，并以此实现共识，实现BigchainDB的区块链特性。</br>
下面是基于对BigchainDB架构对这些特殊功能实现方法的讨论：</br>
1. 去中心化和拜占庭容错：BigchainDB是去中心化的和拜占庭容错的，由于Tendermint是拜占庭容错的，而在BigchainDB网络中，每个节点之间就是通过Tendermint来实现各个节点的mongodb的联网和共识，并在此基础上进行通信，因此整个BigchainDB的网络是拜占庭容错的，即多达三分之一的节点可以以任意方式失败不会破坏网络内部的共识，因此在BigchainDB网络中没有单点故障。又由于BigchainDB网络中每个节点都有自己的本地MongoDB数据库，并且整个BigchainDB网络没有单一所有者，没有单一控制点，单点故障问题又被排除，因此BigchainDB是去中心化的。
2. 不可篡改：BigchainDB是不可篡改的，一旦数据被存储在了BigchainDB中，就不能进行修改和删除，或者进行这些操作时会留下一些痕迹，是可检测的。BigchainDB使用几种策略来实现实际的不可篡改。最基本的策略是不提供API来更改或擦除存储的数据，另一个策略是每个节点都具有独立MongoDB数据库中所有数据的完整副本，还有一个策略是所有交易都以密码方式签名，每一次数据的改变都要有私钥进行签名，因此每次进行修改删除操作时一定会留下一点的可检测的痕迹。
3. 自治性：BigchainDB作为拥有区块链特性的数据库，也具有资产使用者控制资产的概念，其他任何人都不能对不属于自己的资产进行操作。在BigchainDB中只有资产的所有者才能转移该资产，因为每一次资产转移都必须由所有者的私钥进行签名才可以进行，以此实现自治性。
4. 低延迟：BigchainDB对于交易的处理的延时比较低。由于基于Tendermint实现共识的网络可以较快地（通常为几秒）将交易打包到新提交的区块中，因此采用Tendermint进行通信和实现共识的BigchainDB具有低延迟的特点。
5. 结构化数据索引和查询：BigchainDB的查询和索引的数据可以具有独特的结构。BigchainDB 2.0网络中的每个节点都有自己的本地MongoDB数据库。这意味着每个节点操作者可以根据MongoDB数据库的功能自由地决定向外提供的接口、使用这些接口方法，途径以及进行索引和查询的结构。
在BigchainDB中，实现传统分布式数据库的特性的是每个节点都具有的MongoDB数据库，而实现区块链特性则是依赖于BigchainDB服务器和Tendermint。

## 开发目的 <a name="Development"></a>
校园内讲座票的管理较为混乱，缺乏有效的证明和凭证。讲座票从学校部门转移到学生部门后，缺乏管理和跟踪途径，导致讲座票给予和转移的无序性、不可靠性提高，造成了后期在综测等考核前，讲座票钱物交易的行为盛行，俗称“黑市”交易，严重违背了发放讲座票的初衷。因此，我们希望通过利用BigchainDB的特点，开发一个应用系统，提供给学校，部门以及学生使用，使部门能够根据需求明确申请讲座票数量，向学生分发讲座票，并且防止学生间进行讲座票交易，确保讲座票机制的公平性。</br>
因此我们希望用过开发一款程序，提供一个不可篡改、安全可靠的系统来保证讲座票分发的公平和有效性。


## 安装配置 <a name="Installation"></a>
我们使用了ubuntu18.04的iso内跑前后端系统，在bigchaindb、MongoDB、Terminate Node的运行下，使用flask框架下的pycharm生成可视化界面进行操作。

* 客户端：使用浏览器打开网页按照提示即可使用
* 服务端：

安装环境：Ubuntu18.04、python version>=3.4.2。
安装bigchaindb数据库以及python所需的驱动包bigchaindb-driver，并根据驱动编程。具体如下：

1. 根据官方给的安装方式pip install -U bigchaindb-driver安装驱动（首先要安装python3和pip）
![avatar](/images/installation1.png)
1. 利用sudo apt install mongodb安装mongodb
![avatar](/images/installation2.png)
3. 利用pip install flask安装flask
![avatar](/images/installation3.png)
4. 利用pip3 install bigchaindb安装bigchaindb
![avatar](/images/installation4.png)
5. 利用bigchaindb -y configure mongodb进行配置
![avatar](/images/installation5_1.png)
![avatar](/images/installation5_2.png)
6. 下载tendermint并安装
![avatar](/images/installation6.png)</br>
（bigchainDB基于tendermint开发，由于国内从GitHub下载项目速度很慢，所以示例通过第三方下载好后再解压安装）

7. 开启bigchainbd服务
![avatar](/images/installation7.png)
8. 运行部署服务端代码

## 使用方法 <a name="Usage"></a>
![avatar](/images/usage1.png)
首页：
![avatar](/images/usage2.png)
学生端：
![avatar](/images/usage3.png)
注册：（返回公私钥）
![avatar](/images/usage4.png)
登陆：
![avatar](/images/usage5.png)
查询：
![avatar](/images/usage6.png)
部门端：发讲座票
![avatar](/images/usage7.png)
学生端接收到：
![avatar](/images/usage8.png)


## License <a name="License"></a>
[MIT](LICENSE)