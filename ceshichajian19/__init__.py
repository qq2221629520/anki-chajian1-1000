#获取当前卡组的一张卡片（正在学习的，正在复习的，）
#卡片都有字段
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction, qconnect

def testFunction() -> None:
    # 获取当前选择的卡片
    current_card = mw.reviewer.card

    # 检查卡片是否存在
    if current_card:
        # 获取卡片的笔记对象
        current_note = current_card.note()

        # 获取卡片字段的值
        front_field_value = current_note['正面']
        back_field_value = current_note['背面']

        # 打印卡片信息
        showInfo("Front field value: %s" % front_field_value)
        showInfo("Back field value: %s" % back_field_value)
    else:
        showInfo("No card selected.")

def addTestMenuItem() -> None:
    # 创建一个新的菜单项 "test"
    action = QAction("Test", mw)

    # 设置点击时调用 testFunction
    qconnect(action.triggered, testFunction)

    # 将其添加到工具菜单
    mw.form.menuTools.addAction(action)

# 在插件加载时添加菜单项
addTestMenuItem()
