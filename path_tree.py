# @Time: 2024/10/17 
# @Author: Qi Wang
# @File: path_tree
# @Project: Python-leran-in-total
# @Quelle:

from pathlib import Path
import sys

p = Path('C:\Python\Heima_pythonProject')

print(p.name)
pit = p.iterdir() # 返回一个迭代器，包含p下所有文件夹和文件
print(p.is_file())
print(p.is_dir())


tree_str = ''


def generate_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '    |' * n + '-' * 4 + \
                    str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


if __name__ == '__main__':
    # 命令参数个数为2并且目录存在存在
    if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        generate_tree(Path(sys.argv[1]), 0)
    else: # 当前路径
        generate_tree(Path.cwd(), 0)
    print(tree_str)