# import the main window object (mw1) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *


""" def testFunction() -> None:

    #获取所有卡片的数量
    #cardCount = mw.col.cardCount()

    #获取标签是x的所有卡片的 ID
    #ids = mw.col.find_cards("tag:x")

    #显示消息框，展示卡片数量
    #showInfo("Card count: %d" % cardCount)

    #将IDs转换为可读的字符串
    #ids_str = ", ".join(str(id) for id in ids)

    #显示消息框，展示IDs
    #showInfo("卡片 IDs:%s" % ids_str)
 """


""" # 创建一个函数，用于在菜单项被激活时调用
def testFunction() -> None:

    # 获取所有卡组
    decks = mw.col.decks

    # 将卡组名字拼接成一个字符串
    deck_names = ", ".join(str(deck) for deck in decks.all_names_and_ids())  

    # 显示消息框，展示卡组名称
    #showInfo("Deck names: %s" % deck_names)
    showInfo(f"Deck names: {deck_names}") 
"""
   
def testFunction() -> None:
    # 获取所有卡组
    decks = mw.col.decks

    # 将卡组名称拼接成一个字符串
    deck_names = ", ".join(str(deck.name) for deck in decks.all_names_and_ids())

    # 显示消息框，展示卡组名称
    showInfo("Deck names: %s" % deck_names)
    print(deck_names)



# 创建一个新的菜单项 "test"
action = QAction("test1", mw)

# 设置点击时调用 testFunction,
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)




