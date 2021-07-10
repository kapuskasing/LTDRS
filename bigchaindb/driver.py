from regester import *
from create import *
from transaction import *
from search import *
from get_ticket_id import *
# from search_all import *
from dept_regester import *
from get_ticket_number import *
# print("为学号为 201830680118 的学生注册")
#t=dept_regester(666)
# print("科技部要为bigchaindb专题讲座申请130张0.5分的德育分讲座票")
# print("该学生的公私钥为：",t)
# t=get_ticket_number('bigchaindb专题讲座2','文体部2')
#print(t)

# t=dept_regester('文体部2')
#
# print(t)
#create('5oTnDb8B35WXDbxhvGie9FA8v9fwcbF8nKirjuf8Ln4Q','2JpMkspfoevLzdyT5ksoto5AYcGKCgV2P3kiSzVN4mAy',
 #   'bigchaindb专题讲座','2020-6-13, 19:01','B7副楼报告厅',score=0.5,type='德育分',dep_name='666',num=130)
# print("申请成功！")
# bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here

# bdb = BigchainDB(bdb_root_url)
# t=bdb.assets.get(search="bigchaindb专题讲座")
# print("查询学号为201830680118的学生的讲座票")
# print("由于之前该学生之前获取到一张讲座票，因此返回一个带有一张讲座票的数组")
t=search(1)
print(t)
# print("为学号为 201830680118 的学生发bigchaindb专题讲座的讲座票")
#
# transaction(201830680028,'bigchaindb专题讲座2','515ErSxXp7NXed3hnVMhVv6L7UStP6F87KKHpzmU32tD','4RESssKCd2TikHjMFm352EdhD6GbLgp8QAEV7YWUmjU9')
# # #
# print("讲座票分发成功！")
# print("查询学号为201830680118的学生的讲座票")
# print("由于有给这位学生发了讲座票，因此这位学生有一张讲座票")
# t=search(201830680025)
# print(t)

# t=search_all()
# print(t)

# get_ticket_id('区块链技术')