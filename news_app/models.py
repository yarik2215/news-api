from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _


class News(models.Model):

    title = models.CharField(_("title"), max_length=525)
    link = models.URLField(_("link"), max_length=255)
    author = models.CharField(_("author"), max_length=255)
    upvotes = models.IntegerField(_("upvoutes"), default=0)
    creation_date = models.DateField(_("creation date"), auto_now_add=True)

    class Meta:
        ordering = ["-creation_date", "-upvotes"]

    def __str__(self) -> str:
        """
        Return title.
        """
        return self.title

    def upvote(self) -> None:
        """
        Increase upvotes counter
        """
        self.upvotes += 1
        self.save()

    def reset_upvotes(self):
        self.upvotes = 0
        self.save()


class Comment(models.Model):
    """
    Comment model. Refers to news post.
    """

    news = ForeignKey(
        "News", on_delete=CASCADE, verbose_name=_("post"), related_name="comments"
    )
    author = models.CharField(_("author"), max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(_("creation date"), auto_now_add=True)

    class Meta:
        ordering = ['-creation_date'] 