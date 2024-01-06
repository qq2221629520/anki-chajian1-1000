# 改变按钮的颜色 
from aqt import mw, gui_hooks
from aqt.theme import theme_manager

def buttonColours(buttons_tuple, reviewer, card):
    config = mw.addonManager.getConfig(__name__)
    button_count = mw.col.sched.answerButtons(card)

    # Set theme colours
    configColours = config['colours-dark'] if theme_manager.night_mode else config['colours']
    #如果是夜间模式，就用夜间模式的颜色，否则就用白天模式的颜色，configColours是一个字典，key是按钮数量，value是一个列表，列表里面是颜色。

    colours = configColours.get(str(button_count) + ' answers')
    #colours是一个列表，字典里对应4 answers的key，相对应的value是一个列表，列表里面是颜色。["#EB212E", "#FFC600", "#30B700", "#00AEEF"]

    # if coulours found in config
    if colours:

        # Create new list of coloured buttons
        coloured_buttons = []
        #用于存放颜色的列表

        for button in buttons_tuple:
            #假设buttons_tuple = ( (1, "Button 1"),(2, "Button 2"),(3, "Button 3"),(4, "Button 4"),) 是一个二元元组，每个元是一个二元元组，第一个元素是按钮的编号，第二个元素是按钮的文字

            text = button[1]  #表示每个按钮的文字，因为这是在循环中

            # See if colour exists else paint black
            try:
                colour = colours[button[0] - 1]#button[0]是按钮的编号，可能是1、2、3、4，button[0] - 1是按钮的编号减1，因为列表是从0开始的，所以减1
            except IndexError:
                colour = "black"  #当按钮的编号不是1、2、3、4时，就用黑色，因为超出了列表的范围，一共就四个颜色，所以按钮的编号不能超过4

            # Add colour to button
            font = "<font color='{}'>{}</font>".format(colour, text)#有两个占位符，第一个是颜色，第二个是按钮的文字，颜色就用config文件里面预设的颜色，按钮的文字就是原来的文字，没有变吧。format的作用是将字符串中的占位符替换成传入的参数，这里是将占位符替换成颜色和按钮的文字
            #上面这一行代码就改变了按钮的颜色，将按钮的文字用颜色包裹起来，这样就改变了按钮的颜色

            coloured_buttons.append((button[0], font))#第一次循环改变一个按钮，第二次循环改变两个按钮，第三次循环改变三个按钮，第四次循环改变四个按钮。
        return tuple(coloured_buttons)#即使return在for循环外部，但是却能返回全部的for循环迭代后的coloured_buttons，是一个元组，每个元素是一个二元元组，第一个元素是按钮的编号，第二个元素是按钮的文字，文字已经改变了颜色
    else:
        return buttons_tuple #如果没有找到颜色，就使用默认的颜色，此插件不起作用。

gui_hooks.reviewer_will_init_answer_buttons.append(buttonColours)