from django.forms import ModelForm

from .models import Bookmark


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ('date_created', 'date_updated', 'owner')

    def __init__(self, **kwargs):
        self._owner = kwargs.pop('owner', None)
        super(BookmarkForm, self).__init__(**kwargs)

    def save(self, commit=True):
        if not self.instance.pk:
            if not self._owner:
                raise TypeError("No owner was set.")
            self.instance.owner = self._owner
        return super(BookmarkForm, self).save(commit)