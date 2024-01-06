from aqt import mw
from aqt.qt import QLabel, QVBoxLayout, QWidget
from aqt.gui_hooks import deck_browser_did_render

def displayInfo(deck_browser):
    # 获取卡组下方的主窗口对象
    main_window = mw
    # 创建一个包含信息的标签
    info_label = QLabel("Hello, Anki!")

    # 创建一个包含标签的布局
    layout = QVBoxLayout()
    layout.addWidget(info_label)

    # 在卡组下方添加一个新的 QWidget
    widget = QWidget(main_window)
    widget.setLayout(layout)

    # 获取卡组下方的 QVBoxLayout
    bottom_layout = main_window.findChild(QWidget, "bottomLayout").layout()

    # 添加新的 QWidget 到 QVBoxLayout 中
    bottom_layout.addWidget(widget)

# 注册 displayInfo 函数到 deck_browser_did_render 钩子
deck_browser_did_render.append(displayInfo)
