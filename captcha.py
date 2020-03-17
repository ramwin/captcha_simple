#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-17 16:49:15

import os
from PIL import Image, ImageFont, ImageDraw
class captcha(object):
    def __init__(self, text='captcha',
        width=0,height=0,fontsize=24,border=10):
        self.font = ImageFont.truetype(font='./font.ttf', size=fontsize)
        self.text = text
        self.width = width
        self.height = height
        self.fontsize = fontsize
        self.border = border
        self.image = None
    def get_font_size(self):
        return self.font.getsize(self.text)
    def getsize(self):
        if self.width == 0:
            self.width = self.get_font_size()[0] + 2*self.border
        if self.height == 0:
            self.height = self.get_font_size()[1] + 2*self.border
        return (self.width, self.height)
    def getimage(self):
        img = Image.new(mode="RGB", size=self.getsize(), color=(255,255,255))
        draw = ImageDraw.Draw(img)
        draw.text((self.border,self.border), self.text, font=self.font, fill="#000")
        self.image = img
        return self.image
    def save(self,filepath='./test.png'):
        if not self.image:
            self.getimage()
        self.image.save(filepath)


def test():
    a = captcha(text='testLewffsdajfl')
    a.save('./test.png')

if __name__ == '__main__':
    test()
