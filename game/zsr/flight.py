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

WIN_IMG_FN = 'win_bg.png'
CHM_IMG_FN = 'symbol.png'
BACKGROUNDCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init() #初始化pygame,为使用硬件做准备


def LOAD_WATER_GAME():
  WATER_BGIMG_FN = 'water.png'
  WATER_IMG_FNS = ['./wb/1.png','./wb/2.png','./wb/3.png','./wb/4.png']
  IMG_TARGET = [     [[310,440],[370,458],[330,500],[468,627]] ,
                           [[470,230],[510,230],[470,310],[640,760]] , \
                         [[580,280],[600,280],[590,320],[680,370]] , \
                         [[600,460],[630,400],[640,500],[710,710]] ]
  background = pygame.image.load(WATER_BGIMG_FN)

  WIN_X = int(background.get_rect().width/4)
  WIN_Y = int(background.get_rect().height/4)

  FONT_WIDTH = background.get_rect().width
  FONT_HEIGHT = background.get_rect().height

  screen = pygame.display.set_mode((int(FONT_WIDTH*1.5),FONT_HEIGHT))

  FONT_0 = pygame.image.load(WATER_IMG_FNS[0]).convert_alpha()
  FONT_1 = pygame.image.load(WATER_IMG_FNS[1]).convert_alpha()
  FONT_2 = pygame.image.load(WATER_IMG_FNS[2]).convert_alpha()
  FONT_3 = pygame.image.load(WATER_IMG_FNS[3]).convert_alpha()
  FONTS = [FONT_0,FONT_1,FONT_2,FONT_3]

  win_bg_pic = pygame.image.load(WIN_IMG_FN).convert_alpha()
  symbol_cursor = pygame.image.load(CHM_IMG_FN).convert_alpha()

  pygame.display.set_caption("Learn Chinese Characters And Oracle!")
  #设置窗口标题
  #加载并转换图像

  tag = False
  CHOSE_ELE = False
  FINISHED_ELE = []
  ELE_NUM = 1
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
        for i in xrange(ii,ii+4):
          i %= 4
          if i not in FINISHED_ELE:
            ELE_NUM = i
            tag = False
            ii += 1
            break
        # ELE_NUM = (GET_CLICK_NUM()+ii)%4
        # ii += 1
        # while ELE_NUM in FINISHED_ELE:
        #   ELE_NUM = (GET_CLICK_NUM()+ii)%4
        #   ii += 1
        #   ii %= 4
        #   tag = False

    screen.fill(BACKGROUNDCOLOR)

    screen.blit(win_bg_pic, (0,0))
    
    x0,x1,x2,x3 = FONT_WIDTH,int(FONT_WIDTH*1.25),FONT_WIDTH,int(FONT_WIDTH*1.25)
    y0,y1,y2,y3 = 0,0,int(FONT_HEIGHT/2),int(FONT_HEIGHT/2)


    screen.blit(FONT_0, (x0,y0))
    screen.blit(FONT_1, (x1,y1))
    screen.blit(FONT_2, (x2,y2))
    screen.blit(FONT_3, (x3,y3))

    pygame.draw.line(screen, BLACK, (x1,y0) , (x1,FONT_HEIGHT))
    pygame.draw.line(screen, BLACK, (x0,y2) , (FONT_WIDTH*2,y2))
    pygame.draw.line(screen, BLACK, (x0,y0) , (x0,FONT_HEIGHT))

    screen.blit(background, (0,0))
    #将背景图画上去
    # if event.type == MOUSEBUTTONDOWN and event.button == 1:
    
    x, y = pygame.mouse.get_pos()
    # print x , y
    #获得鼠标位置
    x-= FONTS[ELE_NUM].get_width() / 2
    y-= FONTS[ELE_NUM].get_height() / 2
    #计算光标的左上角位置
    for i in FINISHED_ELE:
          screen.blit(FONTS[i], (IMG_TARGET[i][0][0],IMG_TARGET[i][0][1]))
    if(CHOSE_ELE):
      if(not tag):
        # if( x < 540 or x > 900 or y < 0 or y > 300):
        if(not HIT_AREA(x,y,IMG_TARGET[ELE_NUM])):    
          screen.blit(FONTS[ELE_NUM], (x, y))
      #把光标画上去

      if(HIT_AREA(x,y,IMG_TARGET[ELE_NUM])):
        screen.blit(FONTS[ELE_NUM],(IMG_TARGET[ELE_NUM][0][0],IMG_TARGET[ELE_NUM][0][1]))
        screen.blit(symbol_cursor, (0, 0))
        pygame.display.update()
        time.sleep(1)
        if(ELE_NUM not in FINISHED_ELE):
          FINISHED_ELE.append(ELE_NUM)
        tag = True
        CHOSE_ELE = False

    if(len(FINISHED_ELE) == 4):
      screen.blit(background, (0,0))
      screen.blit(win_bg_pic, (WIN_X,WIN_Y))
      pygame.display.update()
      time.sleep(5)
      # exit(1)
      return 
    else:
      time.sleep(0.1)
      pygame.display.update()

def LOAD_FIRE_GAME():
  FIRE_BGIMG_FN = 'fire.png'
  FIRE_IMG_FNS = ['./fb/1.png','./fb/2.png','./fb/3.png','./fb/4.png']
  IMG_TARGET = [     [[370,480],[486,488],[410,615],[468,627]] ,
                           [[320,400],[570,230],[470,720],[640,760]] , \
                           [[580,430],[620,280],[590,500],[680,370]] , \
                           [[530,635],[630,400],[640,700],[710,710]] ]

  background = pygame.image.load(FIRE_BGIMG_FN)

  WIN_X = int(background.get_rect().width/4)
  WIN_Y = int(background.get_rect().height/4)

  FONT_WIDTH = background.get_rect().width
  FONT_HEIGHT = background.get_rect().height

  screen = pygame.display.set_mode((int(FONT_WIDTH*1.5),FONT_HEIGHT))

  FONT_0 = pygame.image.load(FIRE_IMG_FNS[0]).convert_alpha()
  FONT_1 = pygame.image.load(FIRE_IMG_FNS[1]).convert_alpha()
  FONT_2 = pygame.image.load(FIRE_IMG_FNS[2]).convert_alpha()
  FONT_3 = pygame.image.load(FIRE_IMG_FNS[3]).convert_alpha()
  FONTS = [FONT_0,FONT_1,FONT_2,FONT_3]

  win_bg_pic = pygame.image.load(WIN_IMG_FN).convert_alpha()
  symbol_cursor = pygame.image.load(CHM_IMG_FN).convert_alpha()

  pygame.display.set_caption("Learn Chinese Characters And Oracle!")
  #设置窗口标题
  #加载并转换图像

  tag = False
  CHOSE_ELE = False
  FINISHED_ELE = []
  ELE_NUM = 1
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
        for i in xrange(ii,ii+4):
          i %= 4
          if i not in FINISHED_ELE:
            ELE_NUM = i
            tag = False
            ii += 1
            break
        # ELE_NUM = (GET_CLICK_NUM()+ii)%4
        # ii += 1
        # while ELE_NUM in FINISHED_ELE:
        #   ELE_NUM = (GET_CLICK_NUM()+ii)%4
        #   ii += 1
        #   ii %= 4
        #   tag = False

    screen.fill(BACKGROUNDCOLOR)

    screen.blit(win_bg_pic, (0,0))
    
    x0,x1,x2,x3 = FONT_WIDTH,int(FONT_WIDTH*1.25),FONT_WIDTH,int(FONT_WIDTH*1.25)
    y0,y1,y2,y3 = 0,0,int(FONT_HEIGHT/2),int(FONT_HEIGHT/2)


    screen.blit(FONT_0, (x0,y0))
    screen.blit(FONT_1, (x1,y1))
    screen.blit(FONT_2, (x2,y2))
    screen.blit(FONT_3, (x3,y3))

    pygame.draw.line(screen, BLACK, (x1,y0) , (x1,FONT_HEIGHT))
    pygame.draw.line(screen, BLACK, (x0,y2) , (FONT_WIDTH*2,y2))
    pygame.draw.line(screen, BLACK, (x0,y0) , (x0,FONT_HEIGHT))

    screen.blit(background, (0,0))
    #将背景图画上去
    # if event.type == MOUSEBUTTONDOWN and event.button == 1:
    
    x, y = pygame.mouse.get_pos()
    # print x , y
    #获得鼠标位置
    x-= FONTS[ELE_NUM].get_width() / 2
    y-= FONTS[ELE_NUM].get_height() / 2
    #计算光标的左上角位置
    for i in FINISHED_ELE:
          screen.blit(FONTS[i], (IMG_TARGET[i][0][0],IMG_TARGET[i][0][1]))
    if(CHOSE_ELE):
      if(not tag):
        # if( x < 540 or x > 900 or y < 0 or y > 300):
        if(not HIT_AREA(x,y,IMG_TARGET[ELE_NUM])):    
          screen.blit(FONTS[ELE_NUM], (x, y))
      #把光标画上去

      if(HIT_AREA(x,y,IMG_TARGET[ELE_NUM])):
        screen.blit(FONTS[ELE_NUM],(IMG_TARGET[ELE_NUM][0][0],IMG_TARGET[ELE_NUM][0][1]))
        screen.blit(symbol_cursor, (0, 0))
        pygame.display.update()
        time.sleep(1)
        if(ELE_NUM not in FINISHED_ELE):
          FINISHED_ELE.append(ELE_NUM)
        tag = True
        CHOSE_ELE = False

    if(len(FINISHED_ELE) == 4):
      screen.blit(background, (0,0))
      screen.blit(win_bg_pic, (WIN_X,WIN_Y))
      pygame.display.update()
      time.sleep(2)
      return 
      # exit(1)
    else:
      time.sleep(0.1)
      pygame.display.update()
# WATER_BGIMG_FN = 'water.png'
# WATER_IMG_FNS = ['./wb/1.png','./wb/2.png','./wb/3.png','./wb/4.png']
# IMG_TARGET = [     [[310,440],[370,458],[330,500],[468,627]] ,
#                          [[470,230],[510,230],[470,310],[640,760]] , \
#                          [[580,280],[600,280],[590,320],[680,370]] , \
#                          [[600,460],[630,400],[640,500],[710,710]] ]


# FIRE_BGIMG_FN = 'fire.png'
# FIRE_IMG_FNS = ['./fb/1.png','./fb/2.png','./fb/3.png','./fb/4.png']
# FIRE_IMG_TARGET = [     [[370,480],[486,488],[410,615],[468,627]] ,
#                          [[320,400],[570,230],[470,720],[640,760]] , \
#                          [[580,430],[620,280],[590,500],[680,370]] , \
#                          [[530,635],[630,400],[640,700],[710,710]] ]


# pygame.init() #初始化pygame,为使用硬件做准备

def LOAD_START():
  START_BG_FN = "./icon/f_icon.jpg"
  START_ICONS = []
  background = pygame.image.load(START_BG_FN)
  # FONT_WIDTH = background.get_rect().width
  # FONT_HEIGHT = background.get_rect().height

  FONT_WIDTH = 1080
  FONT_HEIGHT = 1091

  screen = pygame.display.set_mode((int(FONT_WIDTH*1.5),FONT_HEIGHT))
  pygame.display.set_caption("Learn Chinese Characters And Oracle!")
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      if event.type == MOUSEBUTTONDOWN and event.button == 1:
        return

    screen.fill(BACKGROUNDCOLOR)
    screen.blit(background, (0,0))
    pygame.display.update()

while True:
  LOAD_START()
  LOAD_FIRE_GAME()
  LOAD_WATER_GAME()

# background = pygame.image.load(WATER_BGIMG_FN)

# WIN_X = int(background.get_rect().width/4)
# WIN_Y = int(background.get_rect().height/4)

# FONT_WIDTH = background.get_rect().width
# FONT_HEIGHT = background.get_rect().height

# screen = pygame.display.set_mode((int(FONT_WIDTH*1.5),FONT_HEIGHT))

# FONT_0 = pygame.image.load(WATER_IMG_FNS[0]).convert_alpha()
# FONT_1 = pygame.image.load(WATER_IMG_FNS[1]).convert_alpha()
# FONT_2 = pygame.image.load(WATER_IMG_FNS[2]).convert_alpha()
# FONT_3 = pygame.image.load(WATER_IMG_FNS[3]).convert_alpha()
# FONTS = [FONT_0,FONT_1,FONT_2,FONT_3]

# # win_bg_pic = pygame.image.load(WIN_IMG_FN).convert_alpha()
# # symbol_cursor = pygame.image.load(CHM_IMG_FN).convert_alpha()

# pygame.display.set_caption("Learn Chinese Characters And Oracle!")
# #设置窗口标题
# #加载并转换图像

# tag = False
# CHOSE_ELE = False
# FINISHED_ELE = []
# ELE_NUM = 1
# ii = 0;
# while True:
# #游戏主循环
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       #接收到退出事件后退出程序
#       pygame.quit()
#       exit()
#     if event.type == MOUSEBUTTONDOWN and event.button == 1:
#       CHOSE_ELE = True
#       for i in xrange(ii,ii+4):
#         i %= 4
#         if i not in FINISHED_ELE:
#           ELE_NUM = i
#           tag = False
#           ii += 1
#           break
#       # ELE_NUM = (GET_CLICK_NUM()+ii)%4
#       # ii += 1
#       # while ELE_NUM in FINISHED_ELE:
#       #   ELE_NUM = (GET_CLICK_NUM()+ii)%4
#       #   ii += 1
#       #   ii %= 4
#       #   tag = False

#   screen.fill(BACKGROUNDCOLOR)

#   screen.blit(win_bg_pic, (0,0))
  
#   x0,x1,x2,x3 = FONT_WIDTH,int(FONT_WIDTH*1.25),FONT_WIDTH,int(FONT_WIDTH*1.25)
#   y0,y1,y2,y3 = 0,0,int(FONT_HEIGHT/2),int(FONT_HEIGHT/2)


#   screen.blit(FONT_0, (x0,y0))
#   screen.blit(FONT_1, (x1,y1))
#   screen.blit(FONT_2, (x2,y2))
#   screen.blit(FONT_3, (x3,y3))

#   pygame.draw.line(screen, BLACK, (x1,y0) , (x1,FONT_HEIGHT))
#   pygame.draw.line(screen, BLACK, (x0,y2) , (FONT_WIDTH*2,y2))
#   pygame.draw.line(screen, BLACK, (x0,y0) , (x0,FONT_HEIGHT))

#   screen.blit(background, (0,0))
#   #将背景图画上去
#   # if event.type == MOUSEBUTTONDOWN and event.button == 1:
  
#   x, y = pygame.mouse.get_pos()
#   print x , y
#   #获得鼠标位置
#   x-= FONTS[ELE_NUM].get_width() / 2
#   y-= FONTS[ELE_NUM].get_height() / 2
#   #计算光标的左上角位置
#   for i in FINISHED_ELE:
#         screen.blit(FONTS[i], (IMG_TARGET[i][0][0],IMG_TARGET[i][0][1]))
#   if(CHOSE_ELE):
#     if(not tag):
#       # if( x < 540 or x > 900 or y < 0 or y > 300):
#       if(not HIT_AREA(x,y,IMG_TARGET[ELE_NUM])):    
#         screen.blit(FONTS[ELE_NUM], (x, y))
#     #把光标画上去

#     if(HIT_AREA(x,y,IMG_TARGET[ELE_NUM])):
#       screen.blit(FONTS[ELE_NUM],(IMG_TARGET[ELE_NUM][0][0],IMG_TARGET[ELE_NUM][0][1]))
#       screen.blit(symbol_cursor, (0, 0))
#       pygame.display.update()
#       time.sleep(1)
#       if(ELE_NUM not in FINISHED_ELE):
#         FINISHED_ELE.append(ELE_NUM)
#       tag = True
#       CHOSE_ELE = False

#   if(len(FINISHED_ELE) == 4):
#     screen.blit(background, (0,0))
#     screen.blit(win_bg_pic, (WIN_X,WIN_Y))
#     pygame.display.update()
#     time.sleep(5)
#     exit(1)
#   else:
#     time.sleep(0.1)
#     pygame.display.update()
