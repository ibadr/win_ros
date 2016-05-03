# Software License Agreement (BSD License)
#
# Copyright (c) 2013, Yujin Robot, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Yujin Robot nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

##############################################################################
# Imports
##############################################################################

import sys
import os
from urllib.request import urlopen

##############################################################################
# Private Functions
##############################################################################

def generate_setup_bat_text():
    # overlay or standard
    text =  """
REM This is a file auto-generated to assist in a usable win-ros
REM command line environment.
"""
    home_drive = os.environ['HOMEDRIVE']
    program_files = home_drive + r'\Program Files'
    program_files_x86 = home_drive + r'\Program Files (x86)'
    visual_studio_12_env_x86 = program_files_x86 + r'\Microsoft Visual Studio 12.0\VC\vcvarsall.bat';
    windows_sdk_env = program_files + r'\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd';

    text += "\n"

    if os.path.isfile(visual_studio_12_env_x86):
        text += "@REM Environment settings for Visual Studio\n"
        text += '@call "' + visual_studio_12_env_x86 + '" x86\n'
        text += '@REM call "' + windows_sdk_env + '" /x86 /Release\n'
    else:
        text += "@REM Could not find Visual Studio 2013, please\n"
        text += "@REM install and configure by hand [Visual Studio 2013]\n"
        text += '@REM call "' + windows_sdk_env + '" /x86 /Release\n'
        text += '@REM "' + visual_studio_12_env_x86 + '" x86\n'
    text += '@REM Colours are a god awful ugly canary yellow or vomit green\n'
    text += '@color 7\n'
    text += "\n"
    return text

##############################################################################
# Public Functions
##############################################################################


def write_setup_bat(base_path):
    text = generate_setup_bat_text()
    setup_path = os.path.join(base_path, 'setup.bat')
    with open(setup_path, 'w') as f:
        f.write(text)


def write_toplevel_cmake(base_path, toplevel_cmake_url):

    u = urlopen( toplevel_cmake_url )
    local_file = open(os.path.join(base_path, 'CMakeLists.txt'), 'wb')
    local_file.write(u.read())
    local_file.close()


def is_invalid_workspace(src_path):
    '''
      Checks for source directory and source CMakeLists.txt.

      @return Error string if not valid, otherwise None
    '''
    error_str = None
    if not os.path.isdir(src_path):
        error_str = "[no %s]"% src_path
    if not os.path.isfile(os.path.join(src_path, 'CMakeLists.txt')):
        # Could copy it in from src/catkin/cmake/toplevel.cmake instead of aborting
        error_str = "[no %s/CMakeLists.txt]"% src_path
    if error_str:
        return "+++ invalid workspace %s. Create a source workspace with 'winros_init_workspace'."%error_str
    return None
