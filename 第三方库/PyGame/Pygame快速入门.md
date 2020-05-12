<!-- TOC -->

- [简介](#%e7%ae%80%e4%bb%8b)
- [准备工作](#%e5%87%86%e5%a4%87%e5%b7%a5%e4%bd%9c)
- [基础对象](#%e5%9f%ba%e7%a1%80%e5%af%b9%e8%b1%a1)
  - [屏幕对象](#%e5%b1%8f%e5%b9%95%e5%af%b9%e8%b1%a1)
  - [游戏主循环](#%e6%b8%b8%e6%88%8f%e4%b8%bb%e5%be%aa%e7%8e%af)
  - [Surface 和 Rects](#surface-%e5%92%8c-rects)
  - [Blit 和 Flip](#blit-%e5%92%8c-flip)
  - [Sprites](#sprites)
  - [用户输入](#%e7%94%a8%e6%88%b7%e8%be%93%e5%85%a5)
  - [Groups](#groups)
  - [自定义事件](#%e8%87%aa%e5%ae%9a%e4%b9%89%e4%ba%8b%e4%bb%b6)
  - [碰撞](#%e7%a2%b0%e6%92%9e)

<!-- /TOC -->

# 简介

PyGame 是 `SDL库`的 Python包装器(wrapper)。SDL 是一个跨平台库，支持访问计算机多媒体硬件（声音，视频，输入等）。SDL 非常强大，但美中不足的是，它是基于 C语言的，而 C语言比较难懂，因此我们采用 PyGame！

![img][img@1]

**在本文中，我们将介绍 PyGame的基本逻辑和冲突检测，以及如何在屏幕上绘图和将外部文件导入游戏中。**

# 准备工作

执行 `pip install pygame` ，安装 Pygame库

新建一个 .py文件，然后输入如下代码

```python
# 导入 pygame
import pygame
# 导入 pygame 中的一些常量
from pygame.locals import *

# 初始化所有导入的PyGame模块，在做其他操作之前必须调用该函数
pygame.init()
```

与其它 Python程序一样，我们首先导入想要使用的模块。这里，我们导入 `pygame 和 pygame.locals` ，后续我们将使用其中的一些常量。最后一行会初始化所有导入的 PyGame 模块，在做其它操作之前必须执行调用该函数！

# 基础对象

## 屏幕对象

首先，我们需要一张画布，我们称之为 “屏幕”，它是我们绘画的平台。为了创建一个屏幕，我们需要调用 `pygame.display` 中的 set_mode 方法，然后向 `set_mode()` 传递包含屏幕窗口**宽度和高度的元组**。

```python
import pygame
from pygame.locals import *

pygame.init()

# 创建一个 800*600 的窗口
screen = pygame.display.set_mode((800, 600))
# 设置窗口名称
pygame.display.set_caption("飞机大战")
```

![img][img@2]

运行上述代码，将会弹出一个窗口，然后又立即消失，一点都不酷嘛，对吧？ 

下一节，我们将介绍游戏的主循环，它将确保只有在我们给它正确的输入时程序才会退出。

## 游戏主循环

游戏主循环/事件循环是所有操作放生的地方。在游戏过程中，它不断更新游戏状态，渲染游戏画面和收集输入指令。创建循环时，需要确保我们有办法跳出循环，退出应用。

为此，我们将同时介绍一些基本的用户输入指令。所有的用户输入（和我们稍后提到的其它事件）都会进入 **PyGame的事件队列**，通过调用 `pygame.event.get()` 可以访问该队列。这将返回一个包含队列里所有事件的列表，我们循环这个列表，并针对相应的事件类型做出反应。现在，我们只关心 `KEYDOWN` 和 `QUIT` 事件。

```python
# 用户保证主循环运行的变量
running = True

# 主循环
while running:
    # for 循环遍历事件队列
    for event in pygame.event.get():
        # 检测 KEYDOWN 事件：KEYDOWN 是 pygame.locals 中定义的常量
        if event.type == KEYDOWN:
            # 如果按下 ESC 那么主循环停止
            if event.key == K_ESCAPE:
                running = False
        # 如果用户点击 X ，终止主循环
        elif event.type == QUIT:
            running = False
```

将上述代码添加到之前的代码下，并运行。应该会看到一个空的窗口，只有你按下 `ESC键` 或者出发一个 `QUIT 事件`，否则这个窗口不会消失。

## Surface 和 Rects

Surface 和 Rects 是 PyGame 中的基本构件。可以将 Surface 看作一张白纸，你可以在上面随意绘画。我们的屏幕对象也是一个 Surface。它们可以包含图片。Rects 是 Surface 中矩形区域的表示。

让我们创建一个 50*50 像素的 Surface，然后给它涂色。由于屏幕是黑色的，所以我们使用白色进行涂色，然后调用 get_rect() 在 Surface 上得到一个矩形区域和 Surface 的 x 轴 和 y 轴。

```python
# 创建 Surface 并设定它的长度和宽度
surf = pygame.Surface((50, 50))
# 设定 Surface 的颜色
surf.fill((255, 255, 255))
# 得到矩形区域及坐标
rect = surf.get_rect()
print(rect)
# <rect(0, 0, 50, 50)>
```

## Blit 和 Flip

仅仅只是创建了 Surface 并不能在屏幕上看到它。为此我们需要将这个 **Surface绘制（Bilt）到另一个 Surface上**。`Bilt`是一个专业术语，意思就是绘图。你仅仅只能从一个 Surface Blit 到另一个 Surface 上，我们的屏幕对象就是一个 Surface 对象。以下是我们如何将 surf 画到屏幕上：

```python
# 将 surf 画到屏幕 x：400 ， y：300的坐标上
screen.blit(surf, (400, 300))
# 更新屏幕
pygame.display.flip()
```

blit() 有两个参数：**要画的 Surface** 和在 **源Surface 上的坐标**。此处我们使用屏幕的中心，但是当你运行代码是，你会发现我们的 surf 并没有出现在屏幕的中心。这是因为 **blit() 是从左上角开始画 surf**。

注意在 blit之后的 `pygame.display.filp()` 的调用。flip将会更新自上次 flip后的整个屏幕，两次 flip之间发生的修改都会在屏幕上显示。没有调用 flip() 那就什么也不会出现！

## Sprites

什么是 Sprites ? 从编程术语来讲，Sprites 是屏幕上事物的二维表法。本质上来讲，Sprites就是一个图片。

Pygame提供一个叫做 **Sprites 的基础类**，他就是用来扩展的，可以包含想要在屏幕上呈现的对象一个或多个图形表示。我们将会扩展 Sprite 类，这样可以使用它的内建方法。我们称这个新的对象为 Player。

Player将扩展 Sprite，现在只有两个属性：surd 和 rect，我们也会给 surf 涂色，如之前 Surface 例子，只是现在 Surface 属于 Player

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
```

现在我们将上述代码整合在一起：

```python
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("飞机大战")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


player = Player()
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        # 将 surf 画到屏幕上
        screen.blit(player.surf, (400, 300))
        pygame.display.flip()
```

运行上述代码，你会在屏幕中心看到一个白色的矩形

如果将 screen.blit(player.surf, (400, 300)) 改成 screen.blit(player.surf, player.rect) , 你觉得会发生什么？rect 的前两个属性分别是 **rect 左上角的 x 和 y 轴坐标**。当你将rect传递给blit，它会根据**这个坐标画 surface**。我们后续将使用它控制 player移动。

## 用户输入

现在开始才是最有趣的部分，我们要把 player 变得可控制。PyGame中有一个事件方法 `pygame.key.get_pressed()`，get_pressed()方法返回一个队列，其中包含了所有按键事件组成的元组，我们把它放在循环中，这样我们将获取每一帧的按键。

```python
pressed_keys = pygame.key.get_pressed()
```

现在我们写一个方法，接收上面那个元组，并根据按下键定义 sprite的行为，代码如下：

```python
    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip((0, -5))
        if keys[K_DOWN]:
            self.rect.move_ip((0, 5))
        if keys[K_LEFT]:
            self.rect.move_ip((-5, 0))
        if keys[K_RIGHT]:
            self.rect.move_ip((5, 0))
```

`K_UP`，`K_DOWN`，`K_LEFT`，`K_RIGHT` 对应键盘上的 上，下，左，右 方向键。我们判断这些键是否按下，如果它为真，那么我们使用 `move_ip()` 方法朝响应的方向移动 rect。

现在你可以使用方向键移动矩形块了，也许你注意到了，你可以将矩形块移出屏幕，这可能并不是你想要的，所以我们需要在 update() 方法中添加一些逻辑，检测矩阵的坐标是移出了屏幕；如果移出了边界，那么就将它放回在边界上。

```python
    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip((0, -5))
            # 如果 rect 的顶部超出边界 ，那么将它放回边界上
            self.rect.top = 0 if self.rect.top <= 0 else self.rect.top
        if keys[K_DOWN]:
            self.rect.move_ip((0, 5))
            self.rect.bottom = 600 if self.rect.bottom >= 600 else self.rect.bottom
        if keys[K_LEFT]:
            self.rect.move_ip((-5, 0))
            self.rect.left = 0 if self.rect.left <= 0 else self.rect.left
        if keys[K_RIGHT]:
            self.rect.move_ip((5, 0))
            self.rect.right = 800 if self.rect.right >= 800 else self.rect.right
```

现在我们添加一些敌人！  
首先我们创建一个新的 sprite类，命名为 Enemy，依照创建 player的格式创建：

```python
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((68, 236, 44))
        self.rect = self.surf.get_rect(x=random.randint(50, 400), y=400)
        self.speed = random.randint(5, 15)

    def update(self):
        self.rect.move_ip((0, -self.speed))
        if self.rect.bottom <= 0:
            self.kill()
```

以上有几点需要说明。首先，当我们在 surface 上调用 `get_rect` 时，我们将 y 坐标设置为 400 ， x 坐标为一个随机数，因为我们希望**敌人随机出现**。我们还是用 random 设置敌人的速度属性，这样敌人就有快有慢！

敌人的 update() 方法没有参数限制（我们不关心敌人的输入），只要让它们向着屏幕上方以一定的速度移动就可以了。update 方法最后有一个 if语句**检测敌人是否通过了屏幕上方边界**。当它们通过边界后，我们调用 Sprite的内建方法 `kill()`删除它们，这样它们就不会再被渲染出来。

> kill不会释放被它们占用的内存，需要你确保不在引用它们，以便 Python的垃圾回收器回收。

## Groups

PyGame 提供的另一个很有用的对象时 sprite的 `Groups`。诚如其名，是 **Sprite的集合**。为什么我们要使用 sprite.Groups 而不是列表呢？因为 sprite.Groups它有一些内建的方法，**有助于解决碰撞和更新问题**。  

那现在就创建一个 Group，用来包含游戏中所有的 Sprite。我们也可以为敌人创建一个 Group。当我们调用 Sprite 的 `kill()` 方法时，会将其从所在的全部 Group 中删除。

```python
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# 将 player 添加到 all_sprites 中
all_sprites.add(player)
```

现在有了 `all_sprites` 的 group，我们接着改变对象渲染方式，只要渲染 group中的所有对象即可：

```python
for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)
```

现在，任何放到 `all_sprites` 中的对象对会被渲染出来。

## 自定义事件

现在我们为敌人创建了一个 sprite.Group，但是并没有实际的敌人。那怎样才能在屏幕上出现敌人呢？我们当然可以在刚开始的时候创建一堆的敌人，但是这样游戏玩不了几秒。

为此，我们创建一个自定义事件，它每隔几秒就会触发创建一批敌人。

创建自定义事件十分容易，只要命名即可：

```python
ADDENEMY = pygame.USEREVENT + 1
```
  
> 注意：自定义事件本质上就是整数常量，又因为比 `USEREVENT` 小的数值已经被内置函数占据，所以创建的自定义事件都要比 `USEREVENT` 大，这就是我们为什么设定它为 `USEREVENT+1`

定义好事件之后，我们需要将它插入事件队列中，因为整个游戏过程中都要创建它们，所有我们还要设置一个定时器，可以通过 PyGame的 `time()` 实现

```python
pygame.time.set_timer(ADDENEMY, 250)
```
> 注意：set_timer() 只能用来将事件插入到 PyGame 事件队列中，不能做其它任何事情。

这行代码告诉 PyGame 每隔250毫秒触发一次 ADDENEMY 事件。这是在主游戏循环之外执行的，不过在整个游戏中都处于执行状态。现在我们添加一些监听事件的代码：

```python
for event in pygame.event.get():
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    elif event.type == QUIT:
        running = False
    elif event.type == ADDENEMY:
        # 如果监听到 ADDENEMY事件，新建一个敌人，并添加至 enemys 中
        new_enemy = Enemy()
        enemys.add(new_enemy)
```

现在我们会监听 `ADDENEMY` 事件，当它触发时，将创建一个 Enemy 类的实例。然后我们将实例添加到 enemys这个 `Sprite Group`（后续用它来**检测碰撞**）

## 碰撞

这才是 PyGame 的魅力所在！写碰撞检测代码（collision code）很难，但是 PyGame 提供了很多碰撞检测方法，你可以在 [这里](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect) 查看其中的一部分。本次使用 [spritecollideany](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollideany) 。  
spritecollideany() 接收一个 Sprite对象和一个 Sprite.Group，检测 Sprite对象是否和Sprite.Group中的 Sprite 发生碰撞。这样我们就可以拿 player 和 敌人所在的 Sprite Group 对比，检测 player 是否被敌人 击中，代码实现如下：

```python
if pygame.sprite.spritecollideany(player, enemys):
    # 如果发生碰撞，玩家角色死亡！
    player.kill()
```

目前完整代码如下：

```python
import random
import pygame
from pygame.locals import *

# 初始化初始化所有导入的PyGame模块
pygame.init()

# 设置游戏窗口宽高
W_WIDTH = 400
W_HEIGHT = 600

# 创建游戏窗口
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
# 设置窗口标题
pygame.display.set_caption("别碰我!")


class Player(pygame.sprite.Sprite):
    """玩家类"""

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(x=int(W_WIDTH / 2), y=50)

    def update(self, keys):
        """设置只能左右移动"""
        if keys[K_LEFT]:
            self.rect.move_ip((-5, 0))
            self.rect.left = 0 if self.rect.left <= 0 else self.rect.left
        if keys[K_RIGHT]:
            self.rect.move_ip((5, 0))
            self.rect.right = W_WIDTH if self.rect.right >= W_WIDTH else self.rect.right


class Enemy(pygame.sprite.Sprite):
    """敌人类"""

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((68, 236, 44))
        self.rect = self.surf.get_rect(x=random.randint(0, W_WIDTH), y=W_HEIGHT)
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip((0, -self.speed))
        if self.rect.bottom <= 0:
            self.kill()


# 创建游戏背景 Surface
background = pygame.Surface((W_WIDTH, W_HEIGHT))
background.fill((0, 0, 0))

# 创建users 玩家Group 以及 enemys 敌人Group
enemys = pygame.sprite.Group()
users = pygame.sprite.Group()
player = Player()
users.add(player)

# 设置自定义事件
ADDENEMY = USEREVENT + 1
# 设置定时器每250ms生成一次自定义事件
pygame.time.set_timer(ADDENEMY, 250)

running = True
# 控制游戏执行的速度
clock = pygame.time.Clock()

while running:
    # 设置游戏的帧速,每秒为60帧
    clock.tick(60)
    # 获取按键事件
    pressed_keys = pygame.key.get_pressed()

    # 绘制背景
    screen.blit(background, (0, 0))
    # 绘制users Group
    for user in users:
        screen.blit(user.surf, user.rect)
        player.update(pressed_keys)
    # 绘制enemys Group
    for enemy in enemys:
        screen.blit(enemy.surf, enemy.rect)
        enemy.update()

    # 监听事件
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemys.add(new_enemy)
            # print(enemys)

    # 碰撞检测
    if pygame.sprite.spritecollideany(player, enemys):
        player.kill()
        print("GAME OVER!!!!")
        running = False

    # 更新屏幕
    pygame.display.flip()
```

最终我们实现的效果如下：

![img][img@3]


[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/pygame%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/04-22_01.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/pygame%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/04-22_02.png
[img@3]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/pygame%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/04-22_04.gif