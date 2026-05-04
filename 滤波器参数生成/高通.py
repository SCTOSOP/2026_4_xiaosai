'''
Author: 在百慕大钓鱼的人 mayuzhuonor@proton.me
Date: 2026-04-20 11:58:08
LastEditors: 在百慕大钓鱼的人 mayuzhuonor@proton.me
LastEditTime: 2026-04-25 21:35:17
FilePath: /2026_4_xiaosai/滤波器参数生成/高通.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from scipy import signal

fs = 50000.0
fc = 90.0

b, a = signal.butter(
    N=4,
    Wn=fc,
    btype='highpass',
    fs=fs
)

print("b =", b)
print("a =", a)