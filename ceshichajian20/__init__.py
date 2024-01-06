from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, qconnect
from aqt.gui_hooks import main_window_did_init
from datetime import datetime, timedelta


def testFunction() -> None:
    # 获取到所有正在学习的卡片的id
    learning_cards = [card[0] for card in mw.col.db.all("select id from cards where queue = 1")]

    # 获取到所有正在复习的卡片的id
    review_cards = [card[0] for card in mw.col.db.all("select id from cards where queue = 2")]

    # 定义推迟的天数
    days_to_add = -1

    for id in learning_cards:
        # 获取正在学习的卡片对象
        card = mw.col.get_card(id)

        # 如果卡片不存在，就跳过
        if not card:
            continue

        # 获取当前到期时间，从1970年1月1日开始计算的，这个数很大，要注意
        current_due_days = card.due    

        # 使用 Anki 提供的 set_due_date 方法更改到期时间
        mw.col.sched.set_due_date([id], str(days_to_add))

    # 展示一个已完成的提示信息以及总共有多少张正在学习的卡片
    showInfo("已经将正在学习的卡片推迟了到了明天！！！" + f"总共有 {len(learning_cards)} 张正在学习的卡片被推迟。")

    for id in review_cards:

        # 获取复习中的卡片对象
        card = mw.col.get_card(id)

        # 如果卡片不存在，就跳过
        if not card:
            continue

        # 获取当前到期时间，这个数是从当日算起的，比如后天天到期，那么这个数就是2
        current_due_days = card.due
  
        # 计算新的到期时间（推迟指定天数）
        new_due_days = current_due_days + days_to_add
 
        # 使用 Anki 提供的 set_due_date 方法更改到期时间
        mw.col.sched.set_due_date([id], str(new_due_days))

    # 展示一个已完成的提示信息以及总共有多少张正在复习的卡片
    showInfo("已经将正在复习的卡片推迟了到了明天！！！" + f"总共有 {len(review_cards)} 张正在复习的卡片被推迟。")
    





# 创建一个新的菜单项 "test"
action = QAction("按一下提前一天", mw)

# 设置点击时调用 testFunction
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)