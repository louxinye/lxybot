# lxybot
基于qqbot写的一个小插件，用于osu!新人群  
qqbot框架地址: https://github.com/pandolia/qqbot  
只要能用qqbot，应该就能用本插件(可能需要额外安装两个库requests和pickle)  

插件说明:  
将这些文件放入…\\\.qqbot-tmp\plugins中  
lxybot.py是主插件，qqbot开启时加载这个就ok  
其余.py文件是用于插件内各种功能实现单独写的方法  
bot_bomb 地雷和手雷系统  
bot_game 咩羊游戏  
bot_getmsg 输出各类帮助说明和用户列表信息  
bot_health 健康系统  
bot_IOfile 本地化存储pkl文件  
bot_msgcheck 判断各类用户指令是否合法并回馈(例如!roll)  
bot_noise 判断本条qq消息被复读了几次  
bot_osu osu!相关内容  
bot_protect 保护系统  
bot_sentence 执行禁言和踢人  

注意事项:  
1.请在加载插件前确认是否有三个本地文件(健康列表，保护列表和bp监视列表)。
你可以用bot_IOfile方法(其实就是pickle)先在本地对应位置创建这三个文件，内容均为空列表。
或者如果不想使用这些功能，可以把相关代码删去或者注释。  
2.bp监视功能并未优化，容易造成卡顿，慎用。
