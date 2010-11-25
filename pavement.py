# -*- Import: -*-
from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages
from paver.path import path

version = '0.0'

classifiers = [
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    "Development Status :: 1 - Planning",
    ]

install_requires = [
    # -*- Install requires: -*-
    'setuptools',
    ]

entry_points="""
    # -*- Entry points: -*-
    """

# compatible with distutils of python 2.3+ or later

options(
    # -*- Paver options: -*-
    minilib=Bunch(
        extra_files=[
            # -*- Minilib extra files: -*-
            ]
        ),
    sphinx=Bunch(
        docroot='docs',
        builddir="_build",
        sourcedir=""
        ),
    virtualenv=Bunch(
        packages_to_install=[
            # -*- Virtualenv packages to install: -*-
            "paver",
            "pkginfo", 
            "virtualenv"],
        dest_dir='./virtual-env/',
        install_paver=True,
        script_name='bootstrap.py',
        paver_command_line=None
        ),
    )
        
@task
def strip_feral():
    """strip 44kHz and source files out of the Feral_Dev project to create Feral"""
    try:
        sh("mkdir Feral.rj")
    except Exception:
        pass
    sh("rsync -v --archive --delete --exclude=source --exclude=44100 Feral_Dev.rj/* Feral.rj/")
    
@task
def update_rjlib():
    rj_checkout = path("~/Web/src/rjlib/").expanduser()
    with pushd(rj_checkout):
        sh("git pull")
    sh("rsync -v --archive --delete --exclude=.git %s/rj/* SceneTemplate.rj/rj/" % rj_checkout)