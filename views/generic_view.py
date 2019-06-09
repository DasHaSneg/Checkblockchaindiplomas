import os

import flask_uploads
from flask.views import View
from flask import render_template, request, redirect, url_for

from app import filesJson


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
