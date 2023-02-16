import logging
# 设置⽇志等级和输出⽇志格式
logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.debug('log debug')
logging.info('log info')
logging.warning('log warn')
logging.error('log error')
logging.critical('log crit')
