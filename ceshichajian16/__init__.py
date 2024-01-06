from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, qconnect

def get_learning_and_review_cards() -> None:
    # 获取学习中的卡片ID
    learning_cards = [card[0] for card in mw.col.db.all("select id from cards where queue = 1")]

    # 获取复习中的卡片ID
    review_cards = [card[0] for card in mw.col.db.all("select id from cards where queue = 2")]

    showInfo(f"Learning Cards IDs: {learning_cards}\nReview Cards IDs: {review_cards}")

# 创建一个新的菜单项 "Get Cards IDs"
action = QAction("Get Cards IDs", mw)

# 设置点击时调用 get_learning_and_review_cards
qconnect(action.triggered, get_learning_and_review_cards)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)
