# -*- coding: utf-8 -*-
# @Time : 2022/5/26 16:55
# @Author : O·N·E
# @File : 04 logging配置
import logging.config

logging.config.fileConfig("logging.conf")

rootlogger = logging.getLogger("root")
# 添加颜色更加区分
# rootlogger.debug('\x1b[36m{}\x1b[0m'.format('This is debug Logger'))
# rootlogger.info('\x1b[1;31m{}\x1b[0m'.format('This is warn Logger'))
# rootlogger.warning('\x1b[1;4;31m{}\x1b[0m'.format('This is error Logger'))
# rootlogger.error('\x1b[35m{}\x1b[0m'.format('This is omitted Logger'))
# rootlogger.critical('\x1b[32m{}\x1b[0m'.format('This is normal Logger'))
a = "abc"
apploglogger = logging.getLogger("applog")
# apploglogger.debug("this is applog logger")
try:
    int(a)
except Exception as e:
    apploglogger.warning(e)
    apploglogger.exception(e)
