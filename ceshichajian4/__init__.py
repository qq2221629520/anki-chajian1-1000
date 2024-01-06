# import the main window object (mw1) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

def testFunction() -> None:
	
    # totalreviews的数据类型是int
	totalreviews = mw.col.db.scalar("""select count(id) from revlog""")
	
    # 将totalreviews转换为str
	totalreviews = str(totalreviews)
	
	time = mw.col.db.first("""select sum(time) from revlog""")
	
	ttime = time if time != None else 0
    # 用shouInfo函数显示totalreviews
	showInfo(totalreviews)
	showInfo(str(ttime))


# 创建一个新的菜单项 "test"
action = QAction("test4", mw)

# 设置点击时调用 testFunction,
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)