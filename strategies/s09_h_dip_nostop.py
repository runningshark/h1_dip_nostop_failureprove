# -*- coding: utf-8 -*-
import copy
from . import s08_h_dip as base

META = copy.deepcopy(base.META)
META.update(id="s09_h_dip_nostop", name="超卖接多（不止损）", verdict="危险", order=9,
            summary="和上一个完全相同，只是不设止损，亏了就拿着等价格回来。胜率看起来非常高。",
            finding="第 5 课：胜率 90%，但少数几笔大亏把所有小赚都吃掉，最差一笔 −27%，持仓中最深浮亏 −34%。全绿的带单记录背后通常是这种结构；加上杠杆，这种幅度足以爆仓。")
META["logic"][2] = ("止损", "没有。亏了就拿着，最多拿 7 天")
META["name"] = "超卖接多（不止损）"
for p in META["params"]:
    if p["key"] == "stop":
        p["value"] = 0.0

build = base.build
