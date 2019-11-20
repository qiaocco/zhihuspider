from celery import Celery

celery_app = Celery("client")
celery_app.config_from_object("config.celeryconfig")


def run():
    # celery_app.send_task(
    #     "celery_app.task1.import_feed", queue="normal_queue", routing_key="feed.123"
    # )
    # 1. 指定queue参数，直接发送到指定的queue
    # 2. 指定routing_key参数，按照routing_key规则发送到对应的queue
    # 3. 两个都指定, 实验下来，routing_key比较优先，原因不知道

    celery_app.send_task("tasks.user.user")


if __name__ == "__main__":
    run()
