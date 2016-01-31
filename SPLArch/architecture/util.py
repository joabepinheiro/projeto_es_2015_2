from django.template.loader import render_to_string
from django.core.files.temp import NamedTemporaryFile

from subprocess import Popen, PIPE
import tempfile
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import os
import shutil

from SPLArch.architecture.TemporaryDirectory import *


def render_to_latex2(template, context, context_instance=None):
    import os, codecs
    body = render_to_string(template, context, context_instance)
    #TODO: there is still a lot of HTML codes to replace here
    body = body.replace('&quote;', '"')
    body = body.replace('&quot;', '"')
    body = body.replace('&apos;', '\'')
    body = body.replace('&amp;', '\&')
    body = body.replace('&#39;', '\'')
    body = body.replace('<br>', '\\')
    body = body.replace('#', '\\#')

    tempf = NamedTemporaryFile(dir=os.getcwd()+'\\temp')
    tempf.close()
    tempf = codecs.open(tempf.name, 'w', 'utf-8')
    tempf.write(body)
    tempf.close()
    for i in range(3):
        os.system('pdflatex -interaction nonstopmode -output-directory %s %s' %
                  (os.path.split(tempf.name)[0], tempf.name))
    return open(tempf.name + '.pdf', 'rb').read()


def render_to_latex(template, context, context_instance=None):

    template = get_template(template)
    context = Context(context)
    rendered_tpl = template.render(context).encode('utf-8')
    # Python3 only. For python2 check out the docs!

    with TemporaryDirectory(dir=os.path.join(os.getcwd(), 'temp')) as tempdir:

        # Create subprocess, supress output with PIPE and
        # run latex twice to generate the TOC properly.
        # Finally read the generated pdf.
        for i in range(2):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()
    r = HttpResponse(content_type='application/pdf')
    # r['Content-Disposition'] = 'attachment; filename=texput.pdf'
    r.write(pdf)
    return r
