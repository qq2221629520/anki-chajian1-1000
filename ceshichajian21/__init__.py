from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, qconnect

def showCardFrontBack(card_id: int) -> None:  #传入一个卡片的id，→ none表示的是没有返回值
    # 查询卡片正面和反面内容
    card_data = mw.col.db.first(  #first表示的是查询第一条数据
        


        """
        SELECT n.flds                           --这是 SQL 查询的选择部分，它指定我们要从数据库中选择的列。在这里，我们选择了笔记表 notes 中的 flds 列，该列通常包含笔记的内容。
                                                --卡片不能直接修改的，卡片的内容是从笔记中获取的，所以我们要先获取到笔记的内容，然后再获取到卡片的内容
        FROM cards c                            --这是 SQL 查询的 from 部分，它指定我们要从数据库中选择的表。在这里，我们选择了卡片表 cards。
        JOIN notes n ON c.nid = n.id            --这是 SQL 查询的 join 部分，它指定我们要连接的表。在这里，我们连接了卡片表 cards 和笔记表 notes，以便我们可以在同一查询中访问它们。
        WHERE c.id = ?                          --这是 SQL 查询的 where 部分，它指定我们要选择哪些行。在这里，我们选择了卡片表 cards 中 id 列的值等于我们传入的参数的行。
        """,


        card_id,                                # 这是我们传入的参数，它将替换查询中的问号。
    )

    if card_data:   #如果card_data存在
        flds_str = card_data[0]
        flds_list = flds_str.split('\x1f')  # 使用 \x1f 分割字段名字符串
        card_content = dict(zip(flds_list, card_data[1:]))  # 将字段名和对应的内容组合成字典
        # 显示各个字段的内容
        showInfo(f"\n字段内容: {flds_list}")
    else:
        showInfo(f"找不到卡片 ID 为 {card_id} 的内容")


            #将字段内容写入到文件中，每查询到一条数据就写入一条数据
    
    with open('ceshi.txt','a',encoding='utf-8') as f:
        f.write(f"\n字段内容: {flds_list}")
        f.write('\n')
        



def testFunction() -> None:
    # 获取到所有正在复习的卡片的id
    review_cards = [card[0] for card in mw.col.db.all("SELECT id FROM cards WHERE queue = 2")]

    if review_cards:
        # 显示第一个正在复习的卡片的正面和反面内容
        showCardFrontBack(review_cards[0])
        showCardFrontBack(review_cards[1])
        showCardFrontBack(review_cards[2])

    else:
        showInfo("没有正在复习的卡片")

# 创建一个新的菜单项 "test"
action = QAction("test21", mw)

# 设置点击时调用 testFunction
qconnect(action.triggered, testFunction)

# 将其添加到工具菜单
mw.form.menuTools.addAction(action)
