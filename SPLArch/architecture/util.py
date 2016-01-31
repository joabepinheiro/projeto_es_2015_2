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


def render_to_latex(template, context, context_instance=None):
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

    tempf = NamedTemporaryFile(dir=os.getcwd()+'/temp')
    tempf.close()
    tempf = codecs.open(tempf.name, 'w', 'utf-8')
    tempf.write(body)
    tempf.close()
    for i in range(3):
        os.system('pdflatex -interaction nonstopmode -output-directory %s %s' %
                  (os.path.split(tempf.name)[0], tempf.name))
    return open(tempf.name + '.pdf', 'rb').read()


