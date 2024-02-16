point = 0 #你的分数
import time
def o(text): #等效于 print , 只是增加了暂停, 类似于 ChatGPT
    for char in text:
        print(char, end='', flush=True)  # 使用 end='' 避免换行，flush=True 立即输出
        time.sleep(0.05)  # 暂停 0.05 秒
    print()  # 打印换行符，以便下一行文本能够另起一行
#另一版的open ai, 在d1的捡钱部分
def o2(text):
    for char in text:
        print(char, end='', flush=True)  # 使用 end='' 避免换行，flush=True 立即输出
        time.sleep(1)  # 暂停 1 秒
    print()  # 打印换行符，以便下一行文本能够另起一行

o('\n')
copyright_en = "All Rights Reserved. © 2024 Survive618 Ad-TEAM."
copyright_cn = "版权所有 © 2024 求生618 Ad-TEAM。保留所有权利。此游戏基于开源协议，遵循开源精神。"
#版权声明
o(copyright_en)
o(copyright_cn)

o('The day 1')
o('叮铃铃, 起床铃在你耳边响起...你周围的舍友都起来了, 但是现在是 7:00 AM, 距离跑操铃响起还有 15 分钟.')
while True: #第一天 - 早上
    o('你想做什么？\n(输入 [1] 「起床」去刷牙, 输入 [2] 继续「睡懒觉」, 输入[0] 退出 《求生618》)')
    get_up_or_sleep = input('你的选择: ')
    if get_up_or_sleep == '1': #刷牙发现不能刷
        o('你选择了起床.')
        o('你跟着舍友一起起床, 可你还是晚了一步, 洗手池旁围着许多舍友. 这使得你很烦恼. 你只能被迫先进入卫生间上厕所了.')
        time.sleep(1)
        o('你上完了厕所. 发现情况「有所好转」, 有一个舍友已经洗完脸刷完牙了. 此时是 7:05 AM.')
        while True:
            o('你想做什么？\n(输入 [1] 「刷牙」, 输入 [2] 直接「去跑操」')
            tooth_or_run = input('你的选择: ')
            if tooth_or_run == '1': #继续刷牙
                o('你选择了刷牙.')
                time.sleep(1.1)
                o('你刷完了牙. 此时是 7:06 AM.')
                o('你整理好了你的个人物品, 然后快步走向1楼. [你获得了 10 积分]')
                point = point + 10
                break
            if tooth_or_run == '2': #直接去跑操
                o('你选择了直接去跑操.')
                o('你直接去跑操, 其他舍友们都看在眼里. 他们开始嫌弃你, 就因为你的不卫生. 但是你似乎并不在乎. [你获得了 0 积分]')
                break
            else:
                o('n')
                o('你输入的不是 [1] 或者 [2]. 请重新尝试.')
        print('\n---------------------')
        o('第一天 第一章 第一幕: 早晨 - 起床 [已完成] '+'你目前的积分: ' + str(point))
        print('---------------------\n')
        o('\n你下了楼梯, 来到宿舍1楼表层. 此时是 7:08 AM')
        while True: 
            o('你想做什么? \n(输入 [1] 去「买早餐」, 输入 [2] 直接「去操场」)')
            buy_breakfast_or_run = input('你的选择: ')
            if buy_breakfast_or_run == '1': #去买早餐
                o('你选择了买早餐.')
                time.sleep(1.2)
                o('你进入了食堂, 发现还是有不少人的. 你挤到了卖包子的队伍中排起队来. 此时是 7:12 AM.')
                time.sleep(1.3)
                o('突然, 跑操的音乐突然响起. 你看了看钟, 竟发现现在已经是「7:15 AM」了.')
                o('你一向害怕迟到, 做什么事都严格要求自己. 但是, 看着还有6个人的短队列, 你还是选择了继续排队.')
                time.sleep(1.4)
                o('你终于拿到了你的包子. 不过, 现在已经是 7:17 PM 了. [你获得了 5 积分]')
                point = point + 5
                o('看着还在涌入食堂的其他人, 你陷入了沉思, 思考着是否去商店「买东西」.')
                o('前车之鉴让你觉得不会迟到, 所以你没有犹豫多久, 二话不说直接前往商店买东西. 此时是 7:18 AM. [你获得了 10 积分]')
                point = point + 10
                time.sleep(1.5)
                o('你来到了商店. 商店阿姨一看到你, 就大声说:"就是你, 昨天顺我们的东西没付钱! 今天既然看到了你, 就不要怪我不仁慈了! 赶紧还钱! 你欠我们 10 元!"')
                o('你十分惊慌, 但是为了以后, 你还是还了钱, 然后立马奔向操场. 此时是 7:20 AM [你获得了 -10 积分]')
                point = point - 10
                o('你奔到了操场. 此时已经是 7:21 AM 了. 跑操铃已经结束. 同时, 你也被学生会列入「迟到」名单. 这让你很失落, 决定以后都不超时了. [你获得了 -10 积分]')
                point = point - 10
            if buy_breakfast_or_run == '2': #去操场
                o('你选择了去操场.')
                o('这时的操场并没有多少人. 你休息了一会. [你获得了 5 积分]')
                time.sleep(1.2)
                o('过了一会, 跑操铃响起. 此时是 7:15 AM')
                o('你再次休息了一会.')
                time.sleep(1.3)
                o('又过了一会, 跑操铃结束. 此时是 7:21 AM. 学生会来到你的班级检查人数. 突然, 你的同学跑了过来, 学生会把他列入「迟到」名单.你的内心暗自高兴.')
            else:
                o('\n')
                o('你输入的不是 [1] 或者 [2]. 请重新尝试.')
            #循环结束
            print('\n---------------------')
            o('第一天 第一章 第二幕: 早晨 - 跑操 [已完成] '+'你目前的积分: ' + str(point))
            print('---------------------\n')
            break
        break
    if get_up_or_sleep == '2': #继续睡懒觉
        o('你选择继续睡觉.')
        time.sleep(1.2)
        o('过了一会, 跑操铃响起.')
        o('你立马从被窝中起来, 用 30s 的时间叠好被子. 你又觉得没有时间, 于是直接去操场了.')
        o('还在洗手池刷牙的舍友看了你一眼, 心里想这人怎么这么「不讲卫生」. 但是你并不在乎. 此时是 7:16 AM. [你获得了 -10 积分]')
        point = point - 10
        time.sleep(1.3)
        o('你下到了1楼, 然后快速奔向操场. 险些没被学生会记名字. [你获得了 0 积分]')
        point = point + 0
        
        print('\n---------------------')
        o('第一天 第一章 第一幕: 早晨 - 起床 [已完成]')
        print('---------------------')

        print('\n---------------------')
        o('第一天 第一章 第二幕: 早晨 - 跑操 [已完成] '+'你目前的积分: ' + str(point))
        print('---------------------\n')
        break
    if get_up_or_sleep == '0': #退出《求生618》
        exit()
    else:
        o('\n')
        o('你输入的不是 [1], [2] 或者 [0]. 请重新尝试.')

#noon - [中午 & 晚上] = 一天
o('叮铃铃. 吃饭的时间到了. 此时是 「11:40 AM」.')
o('你一听到下课铃就快速冲出教室, 奔向食堂.')
while True:
    o('你想做什么？\n(输入 [1] 去买 「8.5元」的饭(饭+菜+肉), 输入 [2] 去买「4.5元」的饭(饭+菜), 输入 [0] 退出《求生618》)')
    buy8_5_or4_5 = input('你的选择: ')
    if buy8_5_or4_5 == '1':
        o('你选择了去买8.5元的饭.')
        o('你二话不说直接奔向 8.5元 餐区域, 付了一碗香香的「米饭」, 「菜」和「肉」的钱. [你获得了 20 积分]\n[这使你充满了决心...]')
        point = point + 20
        o('你把它端上了2楼, 可是你的 8.5元 餐耗了你10分钟的时间, 这让你没法抢到空调位, 你失望极了, 但是看着你手里那香喷喷的饭菜和肉, 你还是选择去没有空调的座位坐.')
        time.sleep(1)
        o('过了一会, 食堂的广播突然响起 Beyond 的 《不再犹豫》. 你高兴极了, 因为你很喜欢听 Beyond 的歌.')
        time.sleep(1.1)
        o('又过了一会, 你吃完了那碗饭. 你现在感觉非常饱而满足. 此时是 12:10 PM. [你获得了 5 积分]')
        point = point + 5
        o('刚把碗放下, 准备走出食堂的时候, 你看到地上竟然有 50 元钱.')
        
        print('\n---------------------')
        o('第一天 第二章 第一幕: 中午 - 午餐 [已完成] '+'你目前的积分: ' + str(point)) #day 1
        print('---------------------\n')

        while True:
            o('你想做什么？\n(输入 [1] 「独吞」这张钱, 输入 [2] 把钱交到「政教处」)')
            use_money_or_bring = input('你的选择: ')
            if use_money_or_bring == '1': #独吞 50 元
                o('你选择了独吞这张钱.')
                o('你以迅雷不及掩耳之势捡起了这张 50 元 RMB, 险些被人看到. 你的内心一直在想着怎么用掉这张钱. [你获得了 -5 积分]')
                point = point - 5
                o('除了食堂后, 你火速地上宿舍楼, 想把得到的 "战利品" 放到书包的隐蔽地方.')
                time.sleep(1.2)
                o('刚上到 6 楼, 广播里就传出一个声音')
                o('寻物启事: 有哪位同学见到今天中午掉在食堂门口的一张 50 元钱? 若有拾到, 麻烦交到政教处或 2303 班 麟疆淼. 寻物启事再播放一遍...')
                o2('...')
                o('你感到有点愧疚. 但心想还是不还到政教处了.')
                o('这一天, 你很害怕, 怕政教处的人查监控看到你捡钱不还的样子.')
                o2('...')
                o('就这样, 你在害怕中度过了「第 1 天」.')
                
                print('\n---------------------')
                o('第一天 第二章 第二幕: 中午&晚上 - 50 元钱 [已完成] '+'你目前的积分: ' + str(point))
                print('---------------------\n')
                break
            if use_money_or_bring == '2': #交到政教处
                o('你选择了把钱交到政教处.')
                time.sleep(1.2)
                o('你来到了政教处. 这里人很多. 包括那个「麟疆淼」.')
                o('你勇敢地踏进政教处的大门, 手里紧握着那张「50 元」.')
                o('\n')
                o('政教处的人说:"你是来还钱的吗?"')
                o('你支支吾吾地说:"是...是我...那个, 「麟疆淼」在哪..."')
                o('「麟疆淼」说:"在这儿. 谢谢你帮我找到了钱. 要是钱不见了, 我这周的生活费就凑不够了."')
                o('你说:"没事, 钱找到了就行. 赶紧去充钱吧."')
                o('\n')
                o('就这样, 你还了钱, 你在开心中度过了「第 1 天」. [你获得了 30 积分]')
                point = point + 30
                
                print('\n---------------------')
                o('第一天 第二章 第二幕: 中午&晚上 - 50 元钱 [已完成] '+'你目前的积分: ' + str(point))
                print('---------------------\n')
                
                break #退出 捡钱 的循环
            else:
                o('\n')
                o('你输入的不是 [1] 或者 [2]. 请重新尝试.')
        break #退出 吃饭 的循环
    if buy8_5_or4_5 == '2': #买 4.5的饭
        o('你选择了买4.5元的饭.')
        o('你刚踏入食堂内部, 发现了很诡异的事情.')
        o('\n')
        o('******************')
        o('4.5 元饭区竟没有开.')
        o('******************')
        o('\n')
        o('你很失望. 转身便走向商店, 可是你欠商店钱的事突然浮现在你的脑子里, 你害怕她们要你还钱.')
        o('运气很好, 他们并没有认出你. 为此, 你既愧疚又开心.')
        o('就这样, 你度过了这一天')
        
        print('\n---------------------')
        o('第一天 第二章 第一幕: 中午 - 午/晚餐 [已完成] '+'你目前的积分: ' + str(point)) #day 1
        print('---------------------\n')

        break
    
    if buy8_5_or4_5 == '0': #退出 618
        exit()
    else:
        o('\n')
        o('你输入的不是 [1], [2] 或者 [0]. 请重新尝试.')    

#第二天 2/1
o('The day 2')
o('熟悉的起床铃再次响起. 今天的你决定早起. 现在是 7:00 AM')
o('让我们来回忆一下昨天晚上老师讲的事情吧!')
o('------------------------') #开始回忆, 进入爬山剧情
o('8:00 PM, Monday')
time.sleep(1)
o('班主任: "额学校刚发了个通知啊, 给你们看看..."')
time.sleep(1.1)
o('班主任: "啊就是呢明天不上课啊, 学校准备让你们放松放松, 去到野外自由探索. 去的地方就离学校不远啊, 你们明天准备好就行, 记得听从学校的安排."')
time.sleep(1.2)
o('*教室里一片热闹*')
time.sleep(1.3)
o('班主任: *拍拍桌子*')
o('*教室突然安静了下来*')
o('班主任: "那么吵干什么? 又不是去送死, 就一个爬山而已, 至于这么激动吗? 好我们继续回到这题..."')
o('------------------------')
o('\n') #换行, 使其进入真正的爬山环节

o('宿舍里面的人都起来了, 他们迅速地刷完牙洗完脸, 快速收拾东西去爬山了. 你也不例外.')
time.sleep(1.4)
o('过了一会, 你和你的舍友都准备好了. 他们准备冒险一波, 一起去一个大山洞探索.')
print('\n---------------------')
o('第二天 第一章 第一幕: 早晨 - 起床 [已完成] '+'你目前的积分: ' + str(point)) #day 2
print('---------------------\n')

def join_climb_team2(): #这个def是用来做如果不加入的话会做什么 (会强制加入队伍), join_climb_team = 1 和 2(增加强制语) 都调用了这个def
    global point #声明 point 为全局变量
    o('你和舍友来到了一座山上. 山很高, 在你眼里学校像一个篮球那么小.')
    o('每个人的身上都有一个定位器, 利用一个软件即可查看位置信息, 它不能录音 (远程), 但是能打电话. 这是学校特地为学生们做的, 怕学生与老师失去联系.')
    o('舍友们似乎都不在乎这个小玩意.')
    o('*他们在呼唤你一起进入那个他们期待已久的大洞穴*')
    time.sleep(1)
    o('你快步跟了上去, 和你的舍友在一起.')
    time.sleep(1.1)
    o('\n')
    o('你和你的舍友们很快就来到了一个大山洞面前.')
    o('山洞黑漆漆的, 一眼望不到底. 你有点害怕了.')
    time.sleep(1.2)
    o('你的舍友们都有些害怕. 但是总得有个人做领头羊.')
    o('领头羊「小迪」说: "走啊, 有啥值得害怕的? 不就一个山洞吗? 我们留个记号就完事了, 肯定能出来."')
    o('小迪又说: "记得在重要的地方画上标记, 不然我们都可能出不来!"')
    o('小迪: "走吧."')
    o('谈话间你们走进了大山洞... [你获得了 20 积分]')
    point = point + 20
    print('\n---------------------')
    o('第二天 第二章 第一幕: 爬山 [已完成] '+'你目前的积分: ' + str(point)) #day 2 <2/2 - 1 爬山>
    print('---------------------\n')

    o('\n')
    o('你们向大山洞的深处进发, 突然看到了分岔路.')
    o('两条路深不见底, 你们犹豫了起来.')
    o('你们决定分开探索.')
    o('小迪: "我们分开探索, 一半人去左边, 另一半人去右边. 到中午 12:30 的时候我们回到分岔路口汇报情况. 如果另一半没回到这里的话就去另一半那边看看.')
    o('你们分成了两队.\n')
    while True:
        o('你想做什么? \n(输入 [1] 去「左边的隧道」, 输入 [2] 去「右边的隧道」)')
        left_or_right = input('你的选择: ')
        if left_or_right == '1':
            o('你选择了去左边的隧道.')
            o('你和几名同学一起进入了左边的隧道. [你获得了 15 积分]')
            point = point + 15
            o('走着走着, 你们离洞口越来越远. 你又有点害怕了.')
            time.sleep(1.3)
            o('过了一会, 你到了隧道深处, 可最后却发现是一堵墙. 你们失望极了, 不过看了看手中的定位器, 发现现在已经是 12:25 PM 了. 你们只好回去和右边队伍汇报情况了.')
            break #退出隧道选择循环
        if left_or_right == '2':
            o('你选择了去右边的隧道.')
            o('你和几名同学一起进入了右边的隧道. [你获得了 15 积分]')
            point = point + 15
            o('走着走着, 你离隧道口越来越远了.')
            time.sleep(1.3)
            o('这个隧道又大又长, 你们走了很久都没有走到尽头.')
            o('时间一分一秒地走着, 很快就来到了 12:25 PM. 你们只好决定返回, 去和左边隧道的人汇报情况. [你获得了 10 积分]')
            point = point +10          
            break #退出隧道选择循环
        else:
            o('\n')
            o('你输入的不是 [1] 或者 [2]. 请重新尝试.')           
    print('\n---------------------')
    o('第二天 第二章 第二幕: 探索 [已完成] '+'你目前的积分: ' + str(point)) #day 2 <2/2 - 2 探索>
    print('---------------------\n')

while True: #循环, 选择是否跟随, 最终都会指向跟随 (你别无选择)
    o('你想做什么？\n(输入 [1] 加入并跟随你的舍友「一起去山洞冒险」, 输入 [2] 跟随别的同学, 输入 [0] 退出《求生618》)')
    join_climb_team = input('你的选择: ')
    if join_climb_team == '1': #直接跟随舍友爬山
        o('你选择了加入并跟随你的舍友「一起去山洞冒险」')
        join_climb_team2()
        break #退出选择队伍的循环
    if join_climb_team == '2':
        o('你选择了跟随别的同学.')
        o('你去到 617 宿舍, 发现 617 宿舍居然空无一人.')
        o('你也不好意思去找女生一起去登山. 无奈, 你只好跟着你的舍友一起去登山.')
        o('\n')
        join_climb_team2()
        break
    if join_climb_team == '0':
        exit()
    else:
        o('\n')
        o('你输入的不是 [1], [2] 或 [0]. 请重新尝试.')