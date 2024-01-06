#推迟到期日期

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

    card1 = mw.col.sched.getCard()#获取一张正在学习的卡片
    card2 =card1.id#获取card1的id

    for id in card2:


    #if  card:
        card = mw.col.get_card(id)#通过id获得卡片
        question = card.question()
        answer = card.answer()
        showInfo("question:\n%s" % question)
    #else:    
       # sys.exit()


    # 去掉新卡片的部分，就是即将到期的和已经到期的卡片
    ids = list(set(id_all) - set(new_card_ids))

    # 定义推迟的天数
    days_to_add = 1
    
    # 遍历所有卡片，并进行更改
    for id in ids:

        # 获取卡片对象
        card = mw.col.get_card(id)

        # 如果卡片不存在，就跳过
        if not card:
            continue

        # 获取当前到期时间（以天数为单位）
        current_due_days = card.due
    
        # 计算新的到期时间（推迟指定天数）
        new_due_days = current_due_days + days_to_add
    
        # 使用 Anki 提供的 set_due_date 方法更改到期时间
        mw.col.sched.set_due_date([id], str(new_due_days))

    # 显示提示信息，提示信息的内容为已经将所有到期的，和即将到期的卡片推迟了一天。
    showInfo("已经将所有到期的、即将到期的卡片统统推迟了一天。")

# 创建一个新的菜单项 "test"
action = QAction("test12", mw)

# 设置点击时调用 testFunction
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)