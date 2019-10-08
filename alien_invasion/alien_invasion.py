import pygame
from pygame.sprite import Group

#from alien import Alien
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	#初始化pygame,设置屏幕对象
	pygame.init()
	
	filename = 'store_high_score.json'
	ai_settings = Settings()
	#screen返回的是surface对象
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	
	pygame.display.set_caption("Alien Invasion")
	
	#创建play按钮
	play_button = Button(ai_settings,screen,"play")
	
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings,filename)
	sb = Scoreboard(ai_settings,screen,stats)
	#创建一个用于存储子弹，外星人的编组
	bullets = Group()
	aliens = Group()
	
	#创建外星人群
	#alien = Alien(ai_settings,screen)
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#开始游戏的主循环
	
	while True:
		 #监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()	
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
		#每次循环时都会重绘屏幕
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		
		
run_game()
			