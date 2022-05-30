# -*- coding: utf-8 -*-
# @Time : 2022/5/20 16:51
# @Author : O·N·E
# @File : 02 logging 四大模块.py
"""
logging库采用模块化方法，并提供了几类组件：记录器，处理程序，过滤器和格式化程序。
    记录器（Logger）：提供应用程序代码直接使用的接口。事先编写好
    处理器（Handler）：将日志记录（由记录器创建）发送到适当的目的地。输出为位置：控制台，文件，邮件等
    筛选器（Filter）：提供了更细粒度的功能，用于确定要输出的日志记录。
    格式器（Formatter）：程序在最终输出日志记录的内容格式。
"""
import logging

# 1.记录器
logger = logging.getLogger("root")  # 默认情况下是root
logger.setLevel(logging.DEBUG)
# print(logger)  # 默认情况下是RootLogger 级别是warning

# 2.处理器
"""
常用的handler
    Streamhandler:标准输出stout分发器
    Filehandler:将日志保存到磁盘文件的处理器
    Rotating Filehandler：
    TimedRotatingfilehandler:滚动的多日志输出，按照时间or其他方式去生成多个日志
"""
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)  # 1.即使设置了输出等级，但是记录器的等级是大于处理器的 所以要按照记录器的为主
# 不指定输出级别会默认使用记录器的输出级别
fileHandler = logging.FileHandler(filename='fileHandler.log', mode="a", encoding='utf-8')
fileHandler.setLevel(logging.ERROR)  # 2.要想按照不同的处理器输出不同的级别，需要将记录器的级别设置为最低为debug

# 3.formatter格式
consoleHandlerformatter = logging.Formatter("%(asctime)s|%(levelname)-8s|%(message)s")  # 8位对齐
fileHandlerformatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s:%(message)s")

# 给处理区设置格式
consoleHandler.setFormatter(consoleHandlerformatter)
fileHandler.setFormatter(fileHandlerformatter)

# 记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 定义过滤器
fit = logging.Filter("one")
fileHandler.addFilter(fit)
# 打印日志输出
logger.debug("python debug")
logger.info("python info")
logger.warning("python warning")
logger.error("python error")
logger.critical("python critical")
