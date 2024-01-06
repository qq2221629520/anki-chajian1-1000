from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, qconnect
from anki.cards import Card

def testFunction() -> None:
    # 获取到所有正在学习的卡片id
    learning_cards = [card for card in mw.col.db.all("select id from cards where queue = 1")]

    for card_id in learning_cards:
        card = mw.col.getCard(card_id[0])  # 获取卡片对象
        question = card.q()#获取卡片的问题
        answer = card.a()#获取卡片的答案
        showInfo(f"Card ID: {card_id[0]}\nQuestion:\n{question}")#f的作用是将字符串中的占位符替换成传入的参数，这里是将占位符替换成卡片的id和问题，\n是换行符

# 创建一个新的菜单项 "test"
action = QAction("test14", mw)

# 设置点击时调用 testFunction
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)
