from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'page'
        verbose_name_plural = "pages"
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Content(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    class Meta:
        db_table = 'item'
        verbose_name_plural = "items"
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Item(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    path = models.CharField(max_length=500, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'item'
        verbose_name_plural = "items"
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class ContentByItem(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


    class Meta:
        db_table = 'content_by_item'
        verbose_name_plural = "content by items"
        ordering = ['content']

    def __unicode__(self):
        return '%s - %s' % (self.content, self.item)

    def __str__(self):
        return '%s - %s' % (self.content, self.item)


class ContentGet(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'content_get'
        verbose_name_plural = "content gets"
        ordering = ['content']

    def __unicode__(self):
        return '%s' % (self.content)

    def __str__(self):
        return '%s' % (self.content)


class ContentGetValue(models.Model):
    content_by_item = models.ForeignKey(ContentByItem, on_delete=models.CASCADE)
    value = models.TextField(blank=True, null=True)
    type_content = models.CharField(max_length=10, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'content_get_value'
        verbose_name_plural = "content get values"
        ordering = ['content_get_value']

    def __unicode__(self):
        return '%s' % (self.content_by_item)

    def __str__(self):
        return '%s' % (self.content_by_item)

