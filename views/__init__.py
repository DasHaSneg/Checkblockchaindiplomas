import certificate_store_bridge
import verifier_bridge
from views.award_view import AwardView
from views.generic_view import GenericView
from views.verify_view import VerifyView


def add_rules(app):
    app.add_url_rule('/', view_func=GenericView.as_view('index', template='index.html'))
    app.add_url_rule(rule='/<certificate_uid>', endpoint='award',
                     view_func=AwardView.as_view(name='award', template='award.html',
                     view=certificate_store_bridge.award))
    app.add_url_rule('/verify/<certificate_uid>',
                     view_func=VerifyView.as_view('verify', view=verifier_bridge.verify))