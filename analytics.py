#!/usr/bin/env python
# coding: utf-8

import subprocess

def run_r_script(r_script, args):
    """
    Run an R script and check if it has terminated.

    Parameters
    ----------
    r_script : str
        Path to the script.
    args : str
        Arguments to be passed to R (identified by commandArgs() R function)
    Returns
    -------
    returncode : 
        If not terminated, returns None
    """
    r_cmd = "Rscript --vanilla"
    process = subprocess.Popen(' '.join([r_cmd, r_script, args]), 
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    
    rc = process.poll()
    return rc