from flask import render_template
from views.renderable_view import RenderableView


class AwardView(RenderableView):
    def __init__(self, template, view):
        super(AwardView, self).__init__(template, view)

    def dispatch_request(self, *args, **kwargs):
        view_model = self.view(*args, **kwargs)
        return render_template(self.template, **view_model)
