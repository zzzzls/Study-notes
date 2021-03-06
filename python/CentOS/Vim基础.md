<!-- TOC -->

- [什么是 vim?](#%e4%bb%80%e4%b9%88%e6%98%af-vim)
- [Vim 的三种模式](#vim-%e7%9a%84%e4%b8%89%e7%a7%8d%e6%a8%a1%e5%bc%8f)
  - [查看模式](#%e6%9f%a5%e7%9c%8b%e6%a8%a1%e5%bc%8f)
    - [移动光标](#%e7%a7%bb%e5%8a%a8%e5%85%89%e6%a0%87)
    - [滚动屏幕](#%e6%bb%9a%e5%8a%a8%e5%b1%8f%e5%b9%95)
    - [搜索替换](#%e6%90%9c%e7%b4%a2%e6%9b%bf%e6%8d%a2)
    - [删除，复制与粘贴](#%e5%88%a0%e9%99%a4%e5%a4%8d%e5%88%b6%e4%b8%8e%e7%b2%98%e8%b4%b4)
  - [查看模式>>编辑模式](#%e6%9f%a5%e7%9c%8b%e6%a8%a1%e5%bc%8f%e7%bc%96%e8%be%91%e6%a8%a1%e5%bc%8f)
  - [查看模式>>命令模式](#%e6%9f%a5%e7%9c%8b%e6%a8%a1%e5%bc%8f%e5%91%bd%e4%bb%a4%e6%a8%a1%e5%bc%8f)

<!-- /TOC -->

# 什么是 vim?

Vim 是一个类似 Vi 的功能强大，高度可定制的文本编辑器，在 Vi 的基础上改进和增加了很多特性。被亲切的称为 "编辑器之神" ！

# Vim 的三种模式

作为一个命令行编辑器，只能通过命令指令的方式完成浏览，编辑和检索操作，必须了解编辑工具操作过程中不同的操作模式

- **查看模式** | 浏览模式 | 可视模式 （ Visual ）：只能查看文档内容，不能进行编辑和修改
- **编辑模式** | 插入模式 （ insert ）：可以编辑和修改文档内容
- **命令模式** | 末行模式 （ command ）：通过输入的指令完成具体的特殊功能的操作

## 查看模式

查看模式下，最核心的是文件内容的浏览查看，在命令行模式下只能通过光标的移动完成内容的移动展示

### 移动光标

|按键|描述|
|:---:|:---|
|h|向左移动一个字符|
|j|向下移动一个字符|
|k|向上移动一个字符|
|l|向右移动一个字符|
|20j|向下移动20行|
|0 \| ^|移动到本行开头|
|$|移动到本行末尾|
|H|移动到当前屏幕最上方 **[ head ]**|
|M|移动到当前屏幕中央 **[ middle ]**|
|L|移动到当前屏幕最下方 **[ last ]**|
|gg|移动到当前文件第一行|
|G|移动到当前文件最后一行|

### 滚动屏幕

|按键|描述|
|:---:|:---|
|Ctrl+u|向上滚动半页 **[ up ]**|
|Ctrl+d|向下滚动半页 **[ down ]**|
|Ctrl+b|向上滚动一页 **[ back ]**|
|Ctrl+f|向下滚动一页 **[ front ]**|

### 搜索替换

|按键|描述|
|:---:|:---|
|/word|从当前光标**向后**搜索名称为 word 的字符串|
|?word|从当前光标**向前**搜索名称为 word 的字符串|
|n|使用 / 时，n 向后搜索，使用 ? 时，n 向前搜索|
|N|与 n 相反|
|n1,n2s/word1/word2/g|n1 与 n2 是数字。在n1 与 n2 之间寻找 word1 这个字符串，并将该字符串取代为 word2|
|1,$s/word1/word2/g|从第一行到最后一行寻找word1字符串，并将该字符串替换为word2|
|1,$s/word1/word2/gc|同上，替换前显示提示字符给用户确认是否替换|

### 删除，复制与粘贴

|按键|描述|
|:---:|:---|
|x \| X|x为向后删除一个字符 [ 相当于 **del** ]，X 为向前删除一个字符 [ 相当于 **backspace** ]|
|nx|n为数字，连续向后删除 n 个字符|
|dd|删除光标所在的那一行|
|ndd|删除光标所在的向下 n 行|
|dgg|删除光标所在行到第一行的数据|
|dG|删除光标所在行到最后一行的数据|
|d$|删除光标所在处到该行的最后一个字符|
|d0|删除光标所在处到改行的第一个字符|
|yy|复制光标所在行|
|nyy||
|ygg||
|yG||
|y$||
|y0||
|p \| P|p 在光标所在行下方粘贴内容，P 在光标所在行上方粘贴内容|
|J|使光标所在行的数据与下一行结合为一行|
|u|撤销上一个动作|
|Ctrl+r|重做上一个动作|
|**.**|重复上一个动作|

## 查看模式>>编辑模式

|按键|描述|
|:---:|:---|
|i \| I|i 从光标前面开始输入，I 从行首开始输入|
|a \| A|a 从光标后面开始输入，A 从行末开始输入|
|o \| O|o 下一行插入内容，O 上一行插入内容|
|r|替换光标位置的字符|
|R|直接替换输入，直到按下 ESC 为止，类似 Insert 按键|
|Esc|退出编辑模式，回到查看模式|

## 查看模式>>命令模式

|按键|描述|
|:---:|:---|
|:w|将编辑的数据写入硬盘档案中|
|:q|离开vim|
|!|强制的意思|
|:wq|保存后退出|
|:x|保存后退出|
|:q!|不保存强制退出|
|:w [filename]|另存为 filename|
|:r [filename]|将另一个文件中内容读入到当前文件中|
|:! command|暂时离开vim到指令模式下指定一个指令，例如: `! ls`|
|:n|直接跳转到第 n 行|
|:set nu|显示行号|
|:set nonu|取消行号|
