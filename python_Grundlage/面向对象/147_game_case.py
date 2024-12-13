# _*_ coding: utf-8 _*_
# @Time: 05.09.2024 14:09
# @Author: Qi Wang
# @File: 147_game_case
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113
import tttttrandom

class Game:
    # 类属性，游戏的最高分
    top_score = 0
    count = 0
    def __init__(self, name):
        # 定义实例属性name
        self.name = name

    @staticmethod  # 静态方法
    def show_help():
        print('help information for the game')

    @classmethod  # 类方法， 这行代码叫做装饰器，只要出现就代表下面是类方法。括号里是不是cls无所谓
    def show_top_score(cls): # 这里调用的是class属性， 也可以改成self
        print(f'The top score of this game is {Game.top_score}')  # Game也可以改成cls
        print('_' * 100)

    def start_game(self):
        Game.count += 1
        print(f'{self.name} has started the game {Game.count} times, ', end='')
        score = tttttrandom.randint(10, 100)
        print(f'the score of this game is {score}')
        if score > Game.top_score:
            # 修改最高分
            Game.top_score = score

Jack = Game('Jack')
Jack.start_game()
Jack.show_top_score()
Jack.start_game()
Jack.show_top_score()
Jack.start_game()
Jack.show_top_score()
Jack.show_help()


