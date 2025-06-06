from typing import Any

from django.views.generic.base import ContextMixin
from django.contrib.auth.models import Group


class AdminCheckMixin(ContextMixin):
    """ Миксин для проверки принадлежности к группе `admin` """

    def get_context_data(self, **kwargs: Any) -> Any:
        """ Миксин для проверки принадлежности к группе `admin` """

        context = super().get_context_data(**kwargs)
        if hasattr(self, 'request'):
            user = self.request.user
            context['is_admin'] = (
                    user.is_authenticated
                    and user.groups.filter(name='admin').exists()
            )
            return context

class ContentManagerCheckMixin(ContextMixin):
    """ Миксин для проверки принадлежности к группе `content manager` """

    def get_context_data(self, **kwargs: Any) -> Any:
        """ Миксин для проверки принадлежности к группе `content manager` """

        context = super().get_context_data(**kwargs)
        if hasattr(self, 'request'):
            user = self.request.user
            context['is_content_manager'] = (
                    user.is_authenticated
                    and user.groups.filter(name='content manager').exists()
            )
            return context