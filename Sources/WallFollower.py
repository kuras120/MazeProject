from copy import deepcopy
from Sources.Player import *


class WallFollower:
	def __init__(self, maze_map):
		self.__map = deepcopy(maze_map)
		self.__refactored_map = []
		self.__player_interaction = []
		self.__output = []

	def refactor_map(self):
		for i in range(128):
			temp = []
			for j in range(128):
				temp.append(self.__map[i*128 + j])
			self.__refactored_map.append(temp)

	def print_coords(self):
		for elem in self.__refactored_map:
			for elem1 in elem:
				print("x: " + elem1.x + " y: " + elem1.y)

	def fill_interaction(self):
		for i in range(128):
			temp = []
			for j in range(128):
				#print("j: " + str(j))
				#print("i: " + str(i))
				player = Player()
				player.point = self.__refactored_map
				player.left = self.__refactored_map[i][j].right_wall
				player.buttom = self.__refactored_map[i][j].buttom_wall
				if j == 127 and not i == 127:
					player.right = True
					player.top = self.__refactored_map[i + 1][j].buttom_wall
				elif i == 127 and not j == 127:
					player.top = True
					player.right = self.__refactored_map[i][j + 1].right_wall
				elif i == 127 and j == 127:
					player.top = True
					player.right = True
				else:
					player.top = self.__refactored_map[i+1][j].buttom_wall
					player.right = self.__refactored_map[i][j+1].right_wall

				temp.append(player)
			self.__player_interaction.append(temp)

	def print_interactions(self):
		for i in range(128):
			for j in range(128):
				print("j: " + str(j))
				print("i: " + str(i))
				print("player left: " + str(self.__player_interaction[i][j].left) + " top: " + str(self.__player_interaction[i][j].top) +
					  " right: " + str(self.__player_interaction[i][j].right) + " buttom: " + str(self.__player_interaction[i][j].buttom))

	def calculate_path(self):
		k = 0
		i = 0
		j = 0
		while k < 20:
			temp = self.__player_interaction[i][j]
			print("gunwo")
			if temp.left:
				temp.rotate_left()
			elif temp.top:
				i = temp.point.x
				j = temp.point.y
				self.__output.append([temp.point.x, temp.point.y])
				temp = self.__player_interaction[i+1][j]
			k += 1

	def get_output(self):
		return self.__output

	def print_output(self):
		print("---------------------------------------")
		for elem in self.__output:
			print("x: " + elem[0] + " y: " + elem[1])

