功能：
1. 抓取指定用户首页详细信息，如用户名、签名、关注、粉丝、赞同数等。
2. 热榜

## 快速开始

1. 配置Python运行环境。创建虚拟环境，安装第三方包
`pip install -r requirements.txt`

2. 修改环境配置。配置文件在`config/spider.yaml`，
把db和reids修改成你自己配置。celery的配置文件在`config/celeryconfig.py`文件，
根据情况修改broker_url和result_backend的配置

3. 创建数据库。先手工创建一个名为zhihu的数据库，然后运行``python config/create_all.py`
创建爬虫所需要的表。

4. 在爬虫程序启动之前，需要预插入一些种子数据。比如你想抓取一个用户，那么就需要在`seed_users`表中插入他的`name`，`name`可以通过打开该用户主页，
查看地址栏的url得到，比如vczh的主页`https://www.zhihu.com/people/excited-vczh/activities`，他的中`name`就是excited-vczh。

5. 配置完成后，通过`celery -A tasks.workers worker -l info`启动worker。

6. 发送任务给worker。通过`python task_execution/user_execute.py`发送抓取用户首页任务。
。通过`python task_execution/hot_list_execute.py`发送抓取热榜任务。