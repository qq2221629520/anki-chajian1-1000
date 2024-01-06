from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, qconnect
from datetime import datetime, timedelta

def testFunction() -> None:
 
    # 获取到所有卡片的id
    id_all = mw.col.find_cards("")

    # 获取到所有新卡片的id，也就是未学习的卡片id
    new_card_ids = mw.col.find_cards("is:new")

    # 去掉新卡片的部分，就是即将到期的和已经到期的卡片
    ids = list(set(id_all) - set(new_card_ids))

    
    for id in ids:
        card = mw.col.get_card(id)
        if not card:
            continue
        mw.col.sched.set_due_date(ids, "2")
        mw.col.update_card(card)

    # 接下来是旧卡片的部分




# 创建一个新的菜单项 "test"
action = QAction("test9", mw)

# 设置点击时调用 testFunction
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)
