# -*- coding: utf-8 -*-
# @Time : 2022/5/20 16:53
# @Author : O·N·E
# @File : 01 logging 定义模块.py
import logging


def loggings_test_1():
    logging.debug("python debug")
    logging.info("python info")
    logging.warning("python warning")
    logging.error("python error")
    logging.critical("python critical")


def loggings_test_2():
    logging.basicConfig(level=logging.DEBUG)  # 需要在开头进行设置 中间无效
    logging.debug("python debug")
    logging.info("python info")
    logging.warning("python warning")
    logging.error("python error")
    logging.critical("python critical")


def loggings_test_3():
    logging.basicConfig(filename='logger.log', level=logging.DEBUG)
    logging.debug("python debug")
    logging.info("python info")
    logging.warning("python warning")
    logging.error("python error")
    logging.critical("python critical")


def loggings_test_4():
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.warning('is when this event was logged.')
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('is when this event was logged.')


def logging_test_5():
    logging.basicConfig(filename='logger.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
    logging.debug("python debug")
    logging.info("python info")
    logging.warning("python warning")
    logging.error("python error")
    logging.critical("python critical")


def logging_text_6():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
    name = "张三"
    age = 18
    logging.debug("%s,%s" % (name, age))


if __name__ == '__main__':
    loggings_test_1()  # 默认情况下日志打印只显示大于等于 WARNING 级别的日志
    # loggings_test_2()  # 设置日志打印等级为debug
    # loggings_test_3()  # 日志信息保存到文件.默认情况下是追加写入的模式 filemode='w'写入模式 a 是追加模式
    # loggings_test_4()  # 显示消息时间
    # logging_test_5()  # 更改显示消息格式:消除root
    # logging_text_6()  # 日志中传入变量
