from io import BytesIO
from django.core.files import File
from PIL import Image
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Topic(models.Model):
    TOPIC_CHOICES = [
        ('air', 'Air'),
        ('water', 'Water'),
        ('food', 'Food'),
        ('housing', 'Housing'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('transportation', 'Transportation'),
        ('sexuality', 'Sexuality'),
    ]
    name = models.CharField(
        max_length=20, choices=TOPIC_CHOICES, default='air')
    slug = models.SlugField(max_length=25)
    topic_image = models.ImageField(
        blank=True, null=True, upload_to='uploads/topics')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('article-reviews', 'Article Reviews'),
        ('book-reviews', 'Book Reviews'),
        ('commentaries', 'Commentaries'),
    ]

    is_new = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    category = models.CharField(
        max_length=25, choices=CATEGORY_CHOICES, default='article-choices', db_index=True)
    topics = models.ManyToManyField(Topic)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(blank=True, null=True,
                              upload_to='uploads/posts/images')
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to='uploads/posts/thumbnails')
    imageurl = models.URLField(blank=True, null=True)
    summary = models.TextField()
    content = RichTextUploadingField()
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    review_item = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['posted_date', 'category', 'author']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
