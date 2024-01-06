from aqt import mw
from aqt.qt import QLabel, QVBoxLayout, QDockWidget, QWidget, Qt
from aqt.gui_hooks import deck_browser_did_render

class InfoDockWidget(QDockWidget):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("信息栏")
        self.setAllowedAreas(Qt.AllDockWidgetAreas)  # 允许在任何地方放置 Dock Widget
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)  # 禁用任何特性
        self.setWidget(QWidget(self))
        self.layout = QVBoxLayout(self.widget())

# 在全局作用域定义一个 Dock Widget 对象，确保只创建一次
info_dock_widget = InfoDockWidget()

def displayInfo(deck_browser):
    # 获取主窗口对象
    main_window = mw

    # 创建一个包含信息的标签
    info_label = QLabel("你好，Anki!")

    # 创建一个包含标签的布局
    layout = QVBoxLayout()
    layout.addWidget(info_label)

    # 创建一个新的 QWidget
    widget = QWidget(main_window)
    widget.setLayout(layout)

    # 将新的 QWidget 添加到 Dock Widget 中
    info_dock_widget.layout.addWidget(widget)

    # 如果 Dock Widget 尚未附加到主窗口，则附加
    if not info_dock_widget.isVisible():
        main_window.addDockWidget(Qt.BottomDockWidgetArea, info_dock_widget)

# 注册 displayInfo 函数到 deck_browser_did_render 钩子
#deck_browser_did_render.append(displayInfo)
