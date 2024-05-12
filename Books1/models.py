from django.db import models
# Create your models here.


class book_category(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class books(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ISBN = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='Books1/', blank=True, null=True)
    year = models.IntegerField()
    genre = models.ForeignKey(to="book_category", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.price}'



class reviews(models.Model):
    comment = models.TextField()
    star_given = models.IntegerField()
    user = models.CharField(max_length=100, blank=True, null=True)
    book_title = models.ForeignKey(to="books", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment} {self.book_title}'


class author(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


# class book_author(models.Model):
#     author = models.ForeignKey(to="author", on_delete=models.CASCADE)
#     book = models.ForeignKey(to="books", on_delete=models.CASCADE)
#     review = models.ForeignKey(to="reviews", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.author} {self.book}'

