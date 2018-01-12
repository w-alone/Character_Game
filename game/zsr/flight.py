# -*- coding: utf8 -*-
import pygame, sys, random
from pygame.locals import *
import time
from sys import exit #向sys模块借一个exit函数用来退出程序

def HIT_AREA(x,y,area):
  if(x > area[0][0] and x < area[1][0]):
    if(y > area[0][1] and y < area[2][1]):
      return True
  return False

def GET_CLICK_NUM():
  return 1

win_image_filename = 'win_bg.png'
background_image_filename = 'water.png'
mouse_image_filenames = ['./wb/1.png','./wb/2.png','./wb/3.png','./wb/4.png']
mouse_image_targets = [  [[367,469],[516,458],[367,615],[468,627]] ,
                         [[500,230],[570,230],[500,720],[640,760]] , \
                         [[580,210],[650,210],[590,370],[680,370]] , \
                         [[630,560],[680,560],[640,700],[710,710]] ]
HIT_TAG = [False,False,False,False]
checkmark_image_filename = 'symbol.png'
BACKGROUNDCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)
#指定图像文件名称


pygame.init() #初始化pygame,为使用硬件做准备
background = pygame.image.load(background_image_filename)
font_file_width = background.get_rect().width
font_file_height = background.get_rect().height
# print font_file_width,font_file_height
screen = pygame.display.set_mode((int(font_file_width*1.5),font_file_height))

mouse_cursor_0 = pygame.image.load(mouse_image_filenames[0]).convert_alpha()
mouse_cursor_1 = pygame.image.load(mouse_image_filenames[1]).convert_alpha()
mouse_cursor_2 = pygame.image.load(mouse_image_filenames[2]).convert_alpha()
mouse_cursor_3 = pygame.image.load(mouse_image_filenames[3]).convert_alpha()
mouse_cursors = [mouse_cursor_0,mouse_cursor_1,mouse_cursor_2,mouse_cursor_3]
win_bg_pic = pygame.image.load(win_image_filename).convert_alpha()
symbol_cursor = pygame.image.load(checkmark_image_filename).convert_alpha()
# pygame.mouse.set_visible(False)
# screen = pygame.display.set_mode((480, 650), 0, 32)
# screen = pygame.display.set_mode(background.get_rect().width,background.get_rect().height)
#创建了一个窗口

pygame.display.set_caption("PlaneFight!")
#设置窗口标题
#加载并转换图像

tag = False
CHOSE_ELE = False
FINISHED_ELE = []
ELE_NUM = -1
ii = 0;
while True:
#游戏主循环

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      #接收到退出事件后退出程序
      pygame.quit()
      exit()
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
      CHOSE_ELE = True
      ELE_NUM = (GET_CLICK_NUM()+ii)%4
      ii += 1
      tag = False

  screen.fill(BACKGROUNDCOLOR)
  
  x0,x1,x2,x3 = font_file_width,int(font_file_width*1.25),font_file_width,int(font_file_width*1.25)
  y0,y1,y2,y3 = 0,0,int(font_file_height/2),int(font_file_height/2)

  screen.blit(mouse_cursor_0, (x0,y0))
  screen.blit(mouse_cursor_1, (x1,y1))
  screen.blit(mouse_cursor_2, (x2,y2))
  screen.blit(mouse_cursor_3, (x3,y3))

  pygame.draw.line(screen, BLACK, (x1,y0) , (x1,font_file_height))
  pygame.draw.line(screen, BLACK, (x0,y2) , (font_file_width*2,y2))
  pygame.draw.line(screen, BLACK, (x0,y0) , (x0,font_file_height))

  screen.blit(background, (0,0))
  #将背景图画上去
  # if event.type == MOUSEBUTTONDOWN and event.button == 1:
  
  x, y = pygame.mouse.get_pos()
  # print x , y
  #获得鼠标位置
  x-= mouse_cursors[ELE_NUM].get_width() / 2
  y-= mouse_cursors[ELE_NUM].get_height() / 2
  #计算光标的左上角位置
  for i in FINISHED_ELE:
        screen.blit(mouse_cursors[i], (mouse_image_targets[i][0][0],mouse_image_targets[i][0][1]))
  if(CHOSE_ELE):
    if(not tag):
      # if( x < 540 or x > 900 or y < 0 or y > 300):
      if(not HIT_AREA(x,y,mouse_image_targets[ELE_NUM])):    
        screen.blit(mouse_cursors[ELE_NUM], (x, y))
    #把光标画上去

    if(HIT_AREA(x,y,mouse_image_targets[ELE_NUM])):
      screen.blit(mouse_cursors[ELE_NUM],(mouse_image_targets[ELE_NUM][0][0],mouse_image_targets[ELE_NUM][0][1]))
      screen.blit(symbol_cursor, (0, 0))
      pygame.display.update()
      time.sleep(1)
      if(ELE_NUM not in FINISHED_ELE):
        FINISHED_ELE.append(ELE_NUM)
      tag = True
      CHOSE_ELE = False

  time.sleep(0.1)
  pygame.display.update()
