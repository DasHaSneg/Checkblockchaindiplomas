import os

import flask_uploads
from cert_core.cert_store import CertificateStore
from flask import Flask, render_template, redirect, url_for, request
from flask.views import View
from flask_uploads import UploadSet, configure_uploads, DATA
from simplekv.fs import FilesystemStore
import certificate_store_bridge
import verifier_bridge
from views.award_view import AwardView

from views.verify_view import VerifyView

app = Flask(__name__)

filesJson = UploadSet('filesjson', DATA)

app.config['UPLOADED_FILESJSON_DEST'] = 'static/JsonFiles'
configure_uploads(app, filesJson)


class GenericView(View):
    methods = ['GET', 'POST']

    def __init__(self, template):
        self.template = template

        super(GenericView, self).__init__()

    def dispatch_request(self):
        folder = './static/JsonFiles'
        filelist = [f for f in os.listdir(folder) if f.endswith(".json")]
        for f in filelist:
            os.remove(os.path.join(folder, f))

        if request.method == 'POST' and 'filesjson' in request.files:
            file = request.files['filesjson']
            args = {"method": "POST"}

            if bool(file.filename):
                try:
                    filename = filesJson.save(request.files['filesjson'])
                    sfilename = filename.rsplit(".", 1)[0]
                    return redirect(url_for('award', certificate_uid=sfilename))
                except flask_uploads.UploadNotAllowed:
                    args["file_null_error"] = 1
                    return render_template("index.html", args=args)

        return render_template(self.template, args=0)


app.add_url_rule('/', view_func=GenericView.as_view('index', template='index.html'))
app.add_url_rule(rule='/<certificate_uid>', endpoint='award',
                 view_func=AwardView.as_view(name='award', template='award.html',
                                             view=certificate_store_bridge.award))
app.add_url_rule('/verify/<certificate_uid>',
                 view_func=VerifyView.as_view('verify', view=verifier_bridge.verify))

###################################конфигурация папки######################
kv_store = FilesystemStore('./static/JsonFiles')
cert_store = CertificateStore(kv_store)

###########################################################################
if __name__ == '__main__':
    app.run()
