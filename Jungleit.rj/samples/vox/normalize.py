#! /usr/bin/env python
import subprocess
# import argparse
import sys
import shlex
import shutil
from path import path

def run_process(plain_old_command_string=None, *command_args):
    """run a command given in a string and return the output"""
    comm = []
    if isinstance(plain_old_command_string, basestring):
        comm = shlex.split(plain_old_command_string)
    comm.extend(command_args)
    return subprocess.Popen(
      comm,
      stdout=subprocess.PIPE
    ).communicate()[0]

def flen(f):
    """length of soundfile"""
    return float(run_process('soxi', '-D', f))

def fpad(f, dur=2):
    """pad file to `dur` seconds"""
    f = path(f)
    curr_dur = flen(f)
    if curr_dur>dur:
        raise ValueError(
            "file is already too long at %f seconds" % curr_dur)
    
    orig = list(f.splitext())
    orig.insert(1, '.orig')
    orig = path(''.join(orig))
    f.move(orig)
    return run_process('sox', orig, f, 'pad', '0', str(dur-curr_dur))

    
    
def pad_files(*files):
    for f in files:
        print fpad(f)
        
    
    
if __name__=='__main__':
    # parser = argparse.ArgumentParser()
    
    print pad_files(*sys.argv[1:])