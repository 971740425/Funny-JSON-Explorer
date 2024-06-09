# 软件工程作业：Funny-JSON-Explorer
Funny-JSON-Explorer(FJE),是一个JSON文件可视化的命令行界面小工具
```shell
fje -f <json file> -s <style> -i <icon family>
```
FJE可以快速切换风格(style),包括：树形(tree),矩形(rectangle);
```shell
├─+name1                                    
|  ├─*name2
│  └─+name3
│     └─*name4: value4
└─*name5

┌─+name1 ───────────────┐
│  ├─*name2 ────────────┤
│  ├─+name3 ────────────┤
│  │  ├─*name4: value4 ─┤
└─*name5 ───────────────┘
```
也可以指定图标族(icon family),为中间节点或叶节点指定一套icon
```shell
┌─+oranges ─────────────────────────┐
│  ├─+mandarin ─────────────────────┤
│  │  ├─*clementine ────────────────┤
│  │  ├─*tangerine: cheap & juicy! ─┤
├─+apples ──────────────────────────┤
│  ├─*gala ─────────────────────────┤
└──┴─*pink lady ────────────────────┘

┌─♦oranges ─────────────────────────┐
│  ├─♦mandarin ─────────────────────┤
│  │  ├─♠clementine ────────────────┤
│  │  ├─♠tangerine: cheap & juicy! ─┤
├─♦apples ──────────────────────────┤
│  ├─♠gala ─────────────────────────┤
└──┴─♠pink lady ────────────────────┘
```
