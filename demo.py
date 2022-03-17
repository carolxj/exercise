'''
    汇率转换器
'''
# 字面意思： 输入功能
str_usd = input('请输入美元')
# 作用：从终端中获取输入的信息，存到程序变量中
int_usd = int(str_usd)
result = int_usd * 6.9
print(result)

# !/usr/bin/python3

import xlwt
import time
import logging

with open("expressage.txt", "r") as f:  # 打开文件
    data = f.readlines()  # 读取文件列表
    print(data)
    for line in data:
        line = line.strip('\n')  # 去除列表中每一个元素的换行符
        if len(line) != 0 and line.isspace() != True:
            print(line)

BLACK = 0X7FFF


class ExcelInfo(object):
    excel_fd = 0
    sheet_fd = 0
    row_point = 0


excel = ExcelInfo
filename = time.strftime("%Y-%m-%d-%H%M%S", time.localtime()) + "导出结果.xls"


def set_style(font_color, height, bold=False, pattern_color='', align='center'):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.bold = bold
    font.height = height
    font.colour_index = font_color

    borders = xlwt.Borders()  # 为样式创建边框
    borders.left = 0
    borders.right = 0
    borders.top = 0
    borders.bottom = 0

    alignment = xlwt.Alignment()  # 设置排列
    if align == 'center':
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
    else:
        alignment.horz = xlwt.Alignment.HORZ_LEFT
        alignment.vert = xlwt.Alignment.VERT_BOTTOM

    if pattern_color != '':
        pattern = xlwt.Pattern()  # 一个实例化的样式类
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
        pattern.pattern_fore_colour = xlwt.Style.colour_map[pattern_color]  # 背景颜色
        style.pattern = pattern

    style.font = font
    style.borders = borders
    style.alignment = alignment

    return style


def excel_init():
    excel.excel_fd = xlwt.Workbook()
    excel.sheet_fd = excel.excel_fd.add_sheet(filename)  # 增加sheet
    excel.sheet_fd.col(0).width = 200 * 10  # 设置第1列列宽
    excel.sheet_fd.col(1).width = 200 * 25  # 设置第2列列宽
    excel.sheet_fd.col(2).width = 200 * 25  # 设置第3列列宽
    excel.sheet_fd.col(3).width = 200 * 10  # 设置第4列列宽
    excel.sheet_fd.col(4).width = 200 * 15  # 设置第5列列宽
    excel.sheet_fd.col(5).width = 180 * 40  # 设置第6列列宽
    excel.sheet_fd.col(6).width = 360 * 15  # 设置第7列列宽
    excel.sheet_fd.col(7).width = 360 * 15  # 设置第7列列宽

    # 写第一行数据
    excel.sheet_fd.write(0, 0, "价格",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 1, "单号",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 2, "日期",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 3, "姓名",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 4, "电话号码",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 5, "地址",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 6, "快递单号",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 7, "快递公司",
                         style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))

    excel.excel_fd.save(filename)
    # 从第二行开始写入
    excel.row_point = 1

    excel_init()

    if __name__ == '__main__':
        excel_init()

        with open("expressage.txt", "r", encoding='gbk') as f:
            col = 0  # 写入的第几列
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                if ((len(line) != 0) and (line.isspace() != True)):

                    if (line.rfind('日期：') != -1):
                        line = line[line.rfind('日期：') + len('日期：'):]
                    elif (line.rfind('快递单号：') != -1):
                        line = (line[line.rfind('快递单号：') + len('快递单号：'):])
                    elif (line.rfind('快递公司：') != -1):
                        line = (line[line.rfind('快递公司：') + len('快递公司：'):])
                    elif (line.rfind('随身携带-便携路由器【默认：默认；】 ') != -1):
                        line = (line[line.rfind('随身携带-便携路由器【默认：默认；】 ') + len('随身携带-便携路由器【默认：默认；】 '):])
                    elif (line.rfind('单号：') != -1):
                        line = (line[line.rfind('单号：') + len('单号：'):])
                    print(line)
                    excel.sheet_fd.write(excel.row_point, col, line,
                                         style=set_style(BLACK, 280, bold=False, align=''))
                    excel.excel_fd.save(filename)

                    col += 1  # 写一个后，列加1
                    if col == 8:  # 写满8列后，从下一行的第1列开始写
                        col = 0
                        excel.row_point += 1


