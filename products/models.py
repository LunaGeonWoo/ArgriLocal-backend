from django.db import models
from common.models import CommonModel
from django.core.validators import MinValueValidator


class Product(CommonModel):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return self.name
