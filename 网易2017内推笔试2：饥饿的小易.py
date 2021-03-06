'''
[编程题] 饥饿的小易
时间限制：1秒
空间限制：32768K
小易总是感觉饥饿，所以作为章鱼的小易经常出去寻找贝壳吃。
最开始小易在一个初始位置x_0。对于小易所处的当前位置x，他只能通过神秘的力量移动到 4 * x + 3或者8 * x + 7。
因为使用神秘力量要耗费太多体力，所以它只能使用神秘力量最多100,000次。
贝壳总生长在能被1,000,000,007整除的位置(比如：位置0，位置1,000,000,007，位置2,000,000,014等)。
小易需要你帮忙计算最少需要使用多少次神秘力量就能吃到贝壳。 
输入描述:
输入一个初始位置x_0,范围在1到1,000,000,006


输出描述:
输出小易最少需要使用神秘力量的次数，如果使用次数使用完还没找到贝壳，则输出-1

输入例子1:
125000000

输出例子1:
1
'''

'''
解题思路：广度优先搜索算法（bfs）
  仍然是广度优先搜索算法，思路参考解救小易，不过内存使用过多，无法AC，估计还有其他巧妙的方法
  1、先遍历初始数集合，判断集合中的数的位置上是否有贝壳，若有陷阱，返回0；若无，则把初始数放入已经搜索过的数的集合searched。
  把初始数分别进行两次神秘力量的移动，得到的新数放入待搜索数集合中
  2、遍历结束后，变换次数超过限制，则输出为-1
  3、若未超限制，把待搜索集合放入bfs，进行迭代搜索，搜索过程中用num记录迭代次数
'''

'''
代码运行结果：
内存超限:您的程序使用了超过限制的内存
case通过率为40.00%
'''

x0 = int(input())

shell = 1000000007
count = 0


def bfs(current_list, num):
    wait_list = set()
    for each in current_list:
        if each % shell == 0:
            return 0
        else:
            wait_list.add(4*each+3)
            wait_list.add(8*each+7)
    num += 1
    if num <= 100000:
        temp = bfs(wait_list, num)
        if temp == -1:
            return -1
        else:
            return 1 + temp
    else:
        return -1
init = set()
init.add(x0)
print(bfs(init, 0))
