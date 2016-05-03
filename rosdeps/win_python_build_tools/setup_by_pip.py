from distutils.core import setup


setup(name='winros-python-build-tools',
      version= '0.2.5',
      packages=['win_ros'],
      package_dir = {'':'src'},
      package_data = {'win_ros': [
           'cmake/MsvcConfig.cmake',
           'cmake/MsvcOverrides.cmake',
           ],
           'catkin_pkg': [
             'templates/groovy/CMakeLists.txt.in',
             'templates/groovy/metapackage.cmake.in',
             'templates/groovy/package.xml.in',
           ]
        },
      scripts = ["scripts/wstool.bat",
                 "scripts/rosversion.bat",
                 "scripts/catkin_create_pkg.bat",
                 "scripts/catkin_find_pkg.bat",
                 "scripts/winros_make.py", "scripts/winros_make.bat",
                 "scripts/winros_init_build.py", "scripts/winros_init_build.bat",
                 "scripts/winros_init_workspace.py", "scripts/winros_init_workspace.bat"],
      author = "Daniel Stonier",
      author_email = "d.stonier@gmail.com",
      url = "https://github.com/stonier/win_python_build_tools",
      download_url = "http://files.yujinrobot.com/windows/python/2.7/",
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License" ],
      description = "Python tools for a win_ros build environment",
      long_description = """\
Python tools for managing a win_ros build environment (vcstools, rosinstall, wstool, rospkg.
""",
      license = "BSD"
      )
