# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:48:08 2020

@author: Administrator
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Gammatranslation():
    def __init__(self):
        pass

    def gammatraslation(self, s_c_img, gamma):
        gamma_result = [np.power(i / 255.0, gamma) * 255.0 for i in range(0, 256)]
        gamma_result = np.round(gamma_result).astype(np.uint8)  # 将运算结果转换为图像灰度值类型。
        return cv2.LUT(s_c_img, gamma_result)  # 使用查找表完成gamma变换。

    # 绘制灰度直方图
    def drawhist(self, img, tname):
        hist, bin_edges = np.histogram(img.ravel(), bins=256, range=(0, 256))
        plt.subplot(111)
        plt.plot(0.5 * (bin_edges[:-1] + bin_edges[1:]), hist, color="blue")
        plt.xlim(0, 300)  # 设置横轴的上下限
        plt.xticks(np.linspace(0, 300, 7), size=10)  # 设置图像上横轴的区间分段。
        plt.title(tname)
        plt.savefig(f'{gama_ls[i]}.jpg')


filename = 'image.jpg'
img = cv2.imread(filename)
g_source = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gama_ls = [0.1, 0.5, 1.5, 3.0, 5.0]
g_translation = Gammatranslation()

for i in range(5):
    gama_result = g_translation.gammatraslation(g_source, gama_ls[i])
    plt.subplot(111)
    plt.imshow(gama_result)
    plt.title(f'The gammatranslation result(γ = {gama_ls[i]})')
    plt.savefig(f'γ = {gama_ls[i]}.jpg')
    plt.show()
    print(gama_ls[i])
    g_translation.drawhist(gama_result, f"The result of γ = {gama_ls[i]}")
    plt.show()

