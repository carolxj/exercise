#! /usr/bin/python3

import os
import time
import logging
import xlwt
import xlrd
import sys

BLACK = 0X7FFF

class ExcelInfo(object):
    excel_fd = 0
    sheet_fd = 0
    row_point = 0

excel = ExcelInfo
filename = time.strftime("%Y-%m-%d-%H%M%S", time.localtime()) + "导出结果.xls"


def logging_init():
    # 创建logger，如果参数为空则返回root logger
    logger = logging.getLogger("")
    logger.setLevel(logging.INFO)  # 设置logger日志等级

    # 创建handler
    output_file = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    log_file = os.path.join(os.path.dirname(__file__) + output_file + ".log")
    fh = logging.FileHandler(log_file, encoding="utf-8")
    ch = logging.StreamHandler()

    # 设置输出日志格式
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    )

    # 为handler指定输出格式，注意大小写
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 为logger添加的日志处理器
    logger.addHandler(fh)
    logger.addHandler(ch)

    return True


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


def read_dev(excel_name):
    excel_fd = xlrd.open_workbook(excel_name)
    excel_sheet = excel_fd.sheet_by_index(0)
    dev_list = excel_sheet.col_values(0)
    logging.info("dev_list: %s", dev_list[0:-1])
    str_list = list(map(str, dev_list[0:-1]))
    logging.info('str_list is: ' + str(str_list))
    logging.info("num_total: %d", len(str_list))

    return str_list


def read_track(excel_name):
    excel_fd = xlrd.open_workbook(excel_name)
    execl_sheet = excel_fd.sheet_by_index(0)
    track_list = execl_sheet.col_values(1)
    logging.info("track_list: %s", track_list[0:-1])
    logging.info("track_total: %d", len(track_list))

    return track_list


def excel_init():
    excel.row_point = 0
    excel.excel_fd = xlwt.Workbook()
    excel.sheet_fd = excel.excel_fd.add_sheet(filename)  # 增加sheet
    excel.sheet_fd.col(0).width = 200 * 18  # 设置第1列列宽
    excel.sheet_fd.col(1).width = 200 * 35  # 设置第2列列宽
    excel.sheet_fd.col(2).width = 200 * 35  # 设置第3列列宽
    excel.sheet_fd.col(3).width = 200 * 15  # 设置第4列列宽
    excel.sheet_fd.col(4).width = 200 * 25  # 设置第5列列宽
    excel.sheet_fd.col(5).width = 200 * 100  # 设置第6列列宽
    excel.sheet_fd.col(6).width = 200 * 30  # 设置第7列列宽
    excel.sheet_fd.col(7).width = 200 * 30  # 设置第8列列宽
    excel.sheet_fd.col(8).width = 200 * 15  # 设置第9列列宽

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
    excel.sheet_fd.write(0, 6, "设备号",
                   style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 7, "快递单号",
                   style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))
    excel.sheet_fd.write(0, 8, "快递公司",
                   style=set_style(BLACK, 260, bold=True, align='', pattern_color='light_orange'))

    excel.excel_fd.save(filename)
    # 从第二行开始写入
    excel.row_point += 1


if __name__ == '__main__':
    # logging_init()
    excel_init()
    dev_list = read_dev(sys.argv[2])
    track_list = read_track(sys.argv[2])
    print(dev_list)
    print(track_list)
    with open(sys.argv[1], "r") as f:
        data = f.readlines()  # 读取文件列表
        print(data)
        col = 0

        for line in data:
            line = line.strip('\n')  # 去除列表中每一个元素的换行符
            if len(line) != 0 and line.isspace() != True:

                if line.find("随身携带-便携路由器【默认：默认；】 ") != -1:
                    line = line[line.find("随身携带-便携路由器【默认：默认；】 ") + len("随身携带-便携路由器【默认：默认；】 "):]
                elif line.find("快递单号：") != -1:
                    line = line[line.find("快递单号：") + len("快递单号："):]
                    try:
                        print("快递单号:", line)
                        index = track_list.index(line) # 查找快递单号位于excel list的哪个位置
                        device_id = dev_list[index] # 通过快递单号的位置查找设备号
                        print("设备号：", device_id)

                        excel.sheet_fd.write(excel.row_point, col, device_id,  # 将找到的设备号写入excel
                                             style=set_style(BLACK, 260, align=''))
                        excel.excel_fd.save(filename)
                        col += 1
                    except Exception as e:
                        print("没有找到快递单号")
                        excel.sheet_fd.write(excel.row_point, col, "没有找到快递单号",  # 没有找到快递单号的时候，写入没有找到快递单
                                             style=set_style(BLACK, 260, align='', pattern_color='red'))
                        excel.excel_fd.save(filename)
                        col += 1

                elif line.find("日期：") != -1:
                    line = line[line.find("日期：") + len("日期："):]
                elif line.find("单号：") != -1:  # 先找快递单号，找不到快递单号后再找单号
                    line = line[line.find("单号：") + len("单号："):]
                elif line.find("快递公司：") != -1:
                    line = line[line.find("快递公司：") + len("快递公司："):]

                if (line[(len(line) - 1):] == ",") or (line[(len(line) - 1):] == "，"):
                    line = line[0:(len(line) - 1)]

                # print(line)

                excel.sheet_fd.write(excel.row_point, col, line,
                                     style=set_style(BLACK, 260, align=''))
                excel.excel_fd.save(filename)
                col += 1
                if col == 9:
                    col = 0
                    excel.row_point += 1

