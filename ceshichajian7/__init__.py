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

    
    ids = mw.col.find_cards("is:due")


    #mw.col.sched.set_due_date(ids, "1")
    card = mw.col.sched.getCard()
    if not card:
        return
    for id in ids:
        card = mw.col.get_card(id)
        question = card.question()
        answer = card.answer()
        showInfo("question:\n%s" % question)

    


# 创建一个新的菜单项 "test"
action = QAction("test7", mw)

# 设置点击时调用 testFunction,
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)