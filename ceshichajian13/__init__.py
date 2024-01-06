from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, qconnect
from aqt.gui_hooks import main_window_did_init
from datetime import datetime, timedelta
import sys

def testFunction() -> None:
    # 获取到所有卡片的id
    id_all = mw.col.find_cards("")

    # 获取到所有新卡片的id，也就是未学习的卡片id
    new_card_ids = mw.col.find_cards("is:new")

    

    card1 = mw.col.sched.getCard() #获取一张当前卡组的卡片
    card2 = mw.col.sched.getCard() #再获取一张当前的卡片
    current_review_card1 = mw.reviewer.card#应该是获取到了当前牌组的卡片。
    if current_review_card1:
        question = current_review_card1.question()
        answer = current_review_card1.answer()
        card_id = current_review_card1.id
        showInfo(f"Card ID: {card_id}\nQuestion:\n{question}")
    if card1:
        question = card1.question()
        answer = card1.answer()
        card_id = card1.id
        showInfo(f"Card ID: {card_id}\nQuestion:\n{question}")
    if card2:
        question = card2.question()
        answer = card2.answer()
        card_id = card2.id
        showInfo(f"Card ID: {card_id}\nQuestion:\n{question}")


# 创建一个新的菜单项 "test"
action = QAction("test13", mw)

# 设置点击时调用 testFunction
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)
