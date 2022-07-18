#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

def Delete_ipynb_checkpoints(folder):
    for root, dirs, files in os.walk(folder):
        for name in dirs:
            if(name.endswith(".ipynb_checkpoints")):
                path = os.path.join(root, name)
                try:
                    shutil.rmtree(path)
                except EnvironmentError:
                    print('Error! Folder cannot be deleted! (%s)\n\n\n\n\n\n\n\n' %path)
                    sys.exit()
                    
                print('Delete %s' %path)

