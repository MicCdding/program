''' 
@File :calc_process.py 
@Author:MicClengxiang 
@Emain: 1668362496@qq.com
@Date :2022/9/2616:56 
@Desc : use to calc process
'''

from abc import ABC, abstractmethod


class AbcCalc(ABC):
    @abstractmethod
    def start(self):
        pass
