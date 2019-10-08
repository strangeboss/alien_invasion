import json
class GameStats():
	#跟踪游戏的统计信息
	def __init__(self,ai_settings,filename):
		#初始化统计信息
		self.ai_settings = ai_settings
		self.filename = filename
		self.reset_stats()  #在init()里面调用方法的好处是什么？？？？
		#游戏刚启动时处于活动状态
		self.game_active = False
		#在任何情况下都不应重置最高得分
		self.high_score = self.read_high_score()
		
	def reset_stats(self):
		#初始化在游戏运行期间可能变化的统计信息
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
	
	def store_high_score(self):
	#存储最高分	
		with open(self.filename,'w') as f:
			json.dump(self.high_score,f)	
	
	def read_high_score(self):
	#读取最高分
		with open(self.filename,'r') as f:
			content = json.load(f)
			return content
			
	def update_high_score(self):
		#更新最高分数
		msg = self.read_high_score()
		#print(msg)
		if int(msg) < self.high_score:
			#self.high_score = int(msg)
			self.store_high_score()		