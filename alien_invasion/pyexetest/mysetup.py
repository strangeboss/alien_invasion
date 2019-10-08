from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
setup(name="Helloworld",console=["hello_world.py"],)