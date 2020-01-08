from django.db import models

class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 200)
	article_text = models.TextField('текст статьи')
	pub_date = models.DateTimeField('дата публикации')
		
	def __str__(self):
		return self.article_title