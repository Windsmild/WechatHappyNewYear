import random

import itchat
import time


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])


def randomBless():
    blessings = ["狗年第一天，一心一意送你祝福：祝你事业发达第一，平安健康第一，婚姻美满第一，家庭和谐第一，赚钱发财第一，开心快乐第一，轻松悠闲都是第一。",
                 "健康是最佳的礼物，知足是最大的财富，信心是最好的品德，关心是最真的问候，牵挂是最深的思念，祝福是最美的话语。祝新年快乐!平安幸福!",
                 "愿你狗年万事顺，得意洋洋满面春!欢快的歌声尽情飘，温暖的春风暖心潮。万千的喜气多热闹，吉祥的日子要来到。发条短信问个好，财源广进吉星照。万事顺利开怀笑，狗年幸福乐逍遥。",
                 "除夕夜，千里迢迢把家赶；心思念，酸甜苦辣在心间；年夜饭，平安吉祥共团圆；喜开颜，快乐吉祥永相伴。祝狗年除夕快乐，团团圆圆幸福满！",
                 "拜年礼包新配方，包含：十分关心十分甜蜜十分健康十分好运十分快乐十分吉祥十分幸福十分如意十分美满。愿你除夕快乐，狗年幸福满溢！",
                 "祝君新年好！新年新面貌！新年新心情！新年新开始！新年新运气！新朋旧友齐愿你，万事总如意，钱途千万里！",
                 "狗年到，短信早，祝福绕，人欢笑，生活好，步步高，重环保，健康牢，多关照，新目标，加力跑，乐淘淘。新春祝你事事好，生活妙，工资高！",
                 "新年祝你事业如日中天，恋人亲密无间，薪水上万成千，快乐无际无边，烦恼渺如云烟，逍遥胜似神仙!我买了二斤时尚，购了三斤浪漫，自制八斤快乐，从心底切下一吨关怀，做个狗年大礼送给你!",
                 "新年我把好运送到，祝您抱着平安，拥着健康，揣着幸福，搂着温馨，携着快乐，牵着财运，拽着吉祥，迈入狗年，快乐度过每一天! "]
    return random.sample(blessings, 1)[0]


itchat.auto_login(hotReload=True)
# itchat.run()
# itchat.send(u'测试消息发送', 'filehelper')

groupList = itchat.get_chatrooms(update=True)
print(groupList)
for group in groupList:
    okWord = u'🎉🎉[红包][红包][小狗][小狗]亲爱的群友们，大帅比给你带来了新年祝福~  ' + randomBless() + "\nMade by WindAI[红包][红包]🎉🎉"
    print(okWord, group['UserName'])
    itchat.send(okWord, group['UserName'])
    time.sleep(1)

friendList = itchat.get_friends(update=True)[1:]

for friend in friendList:
    # 如果是真正发送，把下面的方法改为　itchat.send(REAL_SINCERE_WISH%(friend['DisplayName']or friend['NickName']),friend['UserName'])
    print(randomBless())
    okWord = u'🎉🎉[红包][红包]亲爱的%s，大帅比给你带来了新年祝福~  ' + randomBless() + "\nMade by WindAI[小狗][小狗][红包][红包]🎉🎉"
    print(okWord % (friend['DisplayName'] or friend['NickName']),
          friend['UserName'])
    itchat.send(okWord % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
    # print(friend['DisplayName'], friend['NickName'])
    time.sleep(1)
# itchat.send(u'测试消息发送 WindAI', users[0]['UserName'])
