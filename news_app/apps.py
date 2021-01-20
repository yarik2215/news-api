from django.apps import AppConfig


class NewsAppConfig(AppConfig):
    name = 'news_app'

    def ready(self) -> None:
        from .tasks import init_reset_upvotes_task
        init_reset_upvotes_task()
