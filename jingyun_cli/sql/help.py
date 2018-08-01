#! /usr/bin/env python
# coding: utf-8

import sys
from functools import partial
from jingyun_cli.util.help import help_value, error_and_exit

__author__ = '鹛桑够'

conf_path_help = {"en": "", "cn": "配置文件所在的路径，默认会读取DB_CONF_PATH这个环境变量"}
dir_help = {"en": "", "cn": "会读取该目录下相应的文件。表结构.json，存储过程.procedure，视图.view，触发器.trigger，函数.function"}
file_help = {"en": "", "cn": "表结构描述文件，必须以.json结尾"}
fptv_file_help = {"en": "", "cn": "存储过程，视图，或者触发器，函数描述文件，必须表结构.json，存储过程.procedure，视图.view，触发器.trigger，函数.function结尾"}
create_help = {"en": "", "cn": "根据描述，批量新建表或者存储过程，视图，或者触发器，函数"}
handle_file_help = {"en": "", "cn": "正在处理文件%s"}


help_keys = filter(lambda x: x.endswith("_help"), locals().keys())
help_dict = dict()
for key in help_keys:
    help_dict[key[:-5]] = locals()[key]


g_help = partial(help_value, help_dict)

