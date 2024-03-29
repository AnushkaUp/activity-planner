from django.db.models import QuerySet, Manager
from django.db import models


class BaseQuerySet(QuerySet):
    def get_active(self, *args, **kwargs) -> QuerySet:
        return self.get(is_active=True, *args, **kwargs)

    def filter_active(self, *args, **kwargs) -> QuerySet:
        return self.filter(is_active=True, *args, **kwargs)


class BaseModelManager(Manager):
    def get_queryset(self) -> QuerySet:
        return BaseQuerySet(self.model, using=self._db)
