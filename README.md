# docker_tianchi
这是天池上比赛【入门】Docker练习场 的满分通过代码,适用于从未接触docker的新手

## 比赛链接
[【入门】Docker练习场]()

## 文件说明
- Dockerfile : 用于构建临时容器等操作.
- hello_world : docker容器中要运行的主程序.
- run.sh : 在Dockerfile的最后一行会调用run.sh,进而调用hello_world.py.
- result.json : result文件,最后也会重新生成.