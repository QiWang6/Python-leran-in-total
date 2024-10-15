# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: app02
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import APIRouter
from typing import Union, Optional

app02 = APIRouter()


# 路径函数中声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数，
# 就是 url? 之后用 & 分割的 key-value 键值对。
@app02.get("/jobs/{kd}")
# 没有默认参数时前端必须输入, Union的作用是使输入可以是两种类型中的一种(类型声明)
# Union 是当有多种可能的数据类型时使用，比如函数有可能根据不同情况有时返回 str 或返回 list，那么就可以写成 Union[list, str]
# Optional 是 Union 的一个简化，当数据类型中有可能是 None 时，比如有可能是 str 也有可能是 None，则 Optional[str]，相当于 Union[str, None]
async def get_jobs(kd, xl: Union[str, None] = None, gj: Optional[str] = None):
    # 基于kd，xl， gj数据库查询岗位信息
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }