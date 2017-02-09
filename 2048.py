# -*- coding: utf-8 -*-

__author__ = 'hongwing'

'''
2048 python version
info: 基本逻辑满足的2048
extensions: 可以返回上一步（easily implemented）
'''

import random

game = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
color = [2,4,8,16,32,64,128,256,512,1024,2048]

# 生成初始局
def InitGame(counter):
	for i in xrange(0,counter):
		ProductNewColor()
		
# 当前游戏状态		
def CurrentState():
	res = []
	for item in game:
		temp = []
		for x in item:
			temp.append(x)
		res.append(temp)
	return res

def isOperationEffected(old, new):
	isEffected = False 
	for i in xrange(0,4):
		for j in xrange(0,4):
			if old[i][j] != new[i][j]:
				isEffected = True
				break		
	return isEffected
			
# 移动后产生新的数字
def ProductNewColor():
	producer = True
	# test
	while producer:
		test = -1
		for i in game:
			for j in i:
				if j == 0:
					test = 0
		if test == -1:
			print '\n************Game 2048 0VER'

		index_x = random.randint(0,3)
		index_y = random.randint(0,3)
		# print index_x, index_y

		if game[index_x][index_y] == 0:
			game[index_x][index_y] = 2
			producer = False


			


# 显示游戏界面
def DisplayGame():
	for x in game:
		print x


# 滑动操作(向右滑动)
def OperatorLeftToRight():
	for i in xrange(0,4):
		RowLTR(game[i])
		RowLTR(game[i])


# 单行操作
def RowLTR(arr):
    for i in xrange(3,0,-1):
    	# 找到下一个不为0的位置
    	nextIndex = -1
    	for j in xrange(i-1,-1,-1):
    		if (arr[j] != 0):
    			nextIndex = j
    			break

    	if (nextIndex != -1):
    		# 找到
    		# isOperated = True
    		if (arr[i] == 0):
    			arr[i] = arr[nextIndex]
    			arr[nextIndex] = 0
    		elif (arr[i] == arr[nextIndex]):
    			arr[i] = arr[i]*2
    			arr[nextIndex] = 0


# 滑动操作(向左滑动)
def OperatorRightToLeft():
	for x in xrange(0,4):
		RowRTL(game[x])
		RowRTL(game[x])

# 单行操作
def RowRTL(arr):
	for i in xrange(0,3):
		nextIndex = -1
		for j in xrange(i+1,4):
			if arr[j] != 0:
				nextIndex = j
				break

		if nextIndex != -1:
			# isOperated = True
			if arr[i] == 0:
				arr[i] = arr[nextIndex]
				arr[nextIndex] = 0
			elif arr[i] == arr[nextIndex]:
				arr[i] = arr[i]*2
				arr[nextIndex] = 0


# 滑动操作(向上滑动)
def OperatorBottomToTop():
	for i in xrange(0,4):
		arr = []
		# 提取
		for item in game:
			arr.append(item[i])
		ColumnBTT(arr)
		# 恢复
		index = 0
		for item in game:
			item[i] = arr[index]
			index = index + 1

# 单列操作
def ColumnBTT(arr):
	RowRTL(arr)
	RowRTL(arr)


# 滑动操作(向下滑动)
def OperatorTopToBottom():
	for i in xrange(0,4):
		arr = []
		# 提取
		for item in game:
			arr.append(item[i])
		ColumnTTB(arr)
		# 恢复
		index = 0
		for item in game:
			item[i] = arr[index]
			index = index +1


# 单列操作
def ColumnTTB(arr):
	RowLTR(arr)
	RowLTR(arr)

# 游戏 开始
def StartGameLoop():
	InitGame(2)
	i = 1
	old = []
	new = []
	while True:
		print '----------------'
		DisplayGame()
		print '----------------'
		old = CurrentState()
		operator = (int)(raw_input("please input your operation\n'0--Toward Right L2R'\n'1--Toward Left R2L'\n'2--Toward Top B2T'\n'3--Toward Bottom T2B'\n==>"))
		# isOperated = False
		if operator == 0:
			OperatorLeftToRight() # 向右
		if operator == 1:
			OperatorRightToLeft() # 向左
		if operator == 2:
			OperatorBottomToTop() # 向上
		if operator == 3:
			OperatorTopToBottom() # 向下
		new = CurrentState()
		if isOperationEffected(old, new):
			ProductNewColor()

if __name__ == '__main__':
	StartGameLoop()



    
