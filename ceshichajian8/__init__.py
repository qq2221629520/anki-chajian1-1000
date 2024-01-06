
from aqt import mw
from aqt.qt import QLabel, QVBoxLayout, QDockWidget, QWidget, Qt
from aqt.gui_hooks import deck_browser_did_render






# import the main window object (mw1) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *


def testFunction() -> None:

    
    ids = mw.col.find_cards("is:due")#获得所有到期的卡片的id，包括学习中的卡片！！！


    #mw.col.sched.set_due_date(ids, "1")
    card = mw.col.sched.getCard()#获取一张当前卡组的卡片，对下面代码无影响
    if not card:
        return
    for id in ids:
        card = mw.col.get_card(id)
        card.ivl += 1  #将所有到期卡片，变为明天到期，点两次是后天到期
        mw.col.update_card(card)#更新卡片

        
        
        

    


# 创建一个新的菜单项 "test"
action = QAction("test8", mw)

# 设置点击时调用 testFunction,
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)