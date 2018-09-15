from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms import RadioSelect
from django.http import JsonResponse


class AutocompleteRenderMixin(object):

    def render_to_response(self, context):
        return JsonResponse({
            'results': self.get_results(context),
            'pagination': {
                'more': self.has_more(context)
            }
        })


class FormControlWidgetMixin(object):
    def __init__(self, *args, **kwargs):
        super(FormControlWidgetMixin, self).__init__(*args, **kwargs)
        for fname in self.fields:
            if isinstance(self.fields[fname].widget, RadioSelect):
                continue
            if('enabled' in self.fields[fname].widget.attrs):
                self.fields[fname].widget.attrs.update({'disabled': 'true'})
            else:
                self.fields[fname].widget.attrs.update({'class': 'form-control'})


class ManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_perm('main.is_manager')


class ApplicantOrManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_perm('main.is_applicant') or self.request.user.has_perm('main.is_manager')

