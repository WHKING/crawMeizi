# -*- coding: utf-8-*-
__author__ = 'lihailin'
__email__ = '1501210931@qq.com'
__date__ = '2018年5月10日'

import xmFactory

if __name__ == '__main__':
    factoryDi81 = xmFactory.FactoryDi81()  # 创建一个工厂
    crawDi81 = factoryDi81.creatDi81()  # 产生一个产品
    crawDi81.crawlRun()  # 产品使用