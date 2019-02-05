import random

import itchat
import time


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])


def randomBless():
    blessings = ["春节到，春节到，春节到了真热闹；鞭炮响，焰火亮，孩子脸上露微笑；庆团圆，送祝福，好运福运皆来到。祝你新年快乐，日子一天更比一天好，好运连连！",
                 "张灯结彩闹新春，合家团圆享天伦。喜气洋洋访亲友，笑语盈盈情意久。天地一派幸福景，愿友春节好心情。吉祥如意身旁绕，爱情事业皆欢笑。愿你春节快乐！",
                 "春节未到，祝福先到；家人未到，问候先到；红包未到，福气先到；鞭炮未到，心意先到。愿你在新的一年里：事事顺利，好运连连！",
                 "春节佳节到，向你问个好，身体倍健康，心情特别好；好运天天交，口味顿顿妙。最后祝您及您的家人：猪年好运挡不住，猪年财源滚滚来，好运连连！",
                 "红灯高挂幸福摇，鞭炮齐鸣天地欢；日子美美心情好，阖家欢乐大团圆；敬杯美酒送好友，遥寄祝福无限好；祝你猪年交好运，心想事成万事顺，好运连连！",
                 "春风舞起猪年到，一帆风顺开门笑。只愿来年灿烂耀，一生辉煌幸福跳。愿君家和万事旺，犹如雨后春笋窜。幸福生活似蜜甜，广进洋财大把赚。祝你猪年，身体健康幸福享，美满家庭乐无限，好运连连！",
                 "猪年到来笑哈哈，吉祥如意好年景。身体健康无烦恼，心想事成大事业。子孙满堂一大帮，庆贺猪年好热闹。愿你猪年高寿享，美满家庭万事安，好运连连！",
                 "春风舞翩翩，香花绽笑颜。心头情无限，微信来拜年。愿友爱情甜，事业翻新篇。幸福绕身边，健康到永远。恭祝你春节快乐，好运连连！",
                 "新年的喜气飘扬万家，甜蜜的美满斟满富贵，喜庆的春联写满吉祥，璀璨的烟花绽放希望，深情的友谊恒久留香，温馨的祝福充满真挚。祝朋友新年快乐，新年吉祥，好运连连！",
                 "春联喜庆，写满生活的向往。窗花漂亮，披上幸福的霓裳。钟声倒数，收藏所有的希望。爆竹噼啪，奏响新年的乐章。烟花升腾，点缀除夕的吉祥！猪年春节快乐，好运连连！"]
    return random.sample(blessings, 1)[0]


itchat.auto_login()
itchat.send('Hello, filehelper', toUserName='filehelper')
# itchat.run()
itchat.send(u'测试消息发送', 'filehelper')

groupList = itchat.get_chatrooms()
print(groupList)
# for group in groupList:
#     okWord = u'🎉🎉[红包][红包][猪头][猪头]亲爱的群友们，蔡神爷给你带来了新年祝福~  ' + randomBless() + "\nMade by WindAI[红包][红包]🎉🎉"
#     print(okWord, group['UserName'])
#     itchat.send(okWord, group['UserName'])
#     time.sleep(1)

friendList = itchat.get_friends(update=True)[1:]

for friend in friendList:
    # 如果是真正发送，把下面的方法改为　itchat.send(REAL_SINCERE_WISH%(friend['DisplayName']or friend['NickName']),friend['UserName'])
    print(randomBless())
    okWord = u'🎉🎉[红包][红包]亲爱的%s，蔡神爷给你带来了新年祝福~  ' + randomBless() + "\nMade by WindAI[猪头][猪头][红包][红包]🎉🎉"
    print(okWord % (friend['DisplayName'] or friend['NickName']),
          friend['UserName'])
    itchat.send(okWord % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
    # print(friend['DisplayName'], friend['NickName'])
    time.sleep(1)
# itchat.send(u'测试消息发送 WindAI', users[0]['UserName'])
