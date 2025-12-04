from distutils.core import setup
setup(
  name = 'jetson_python_drv8825',
  packages = ['jetson_python_drv8825'],
  version = '0.3',
  license='gpl-3.0',
  description = 'Python library to controll a stepper motor with a DRV8825 driver connected to a Jetson',
  author = 'Joseph Tighe',
  author_email = 'josephjtighe@gmail.com',
  url = 'https://github.com/joseph-tighe15/jetson_python_drv8825',
  download_url = 'https://github.com/joseph-tighe15/jetson_python_drv8825/archive/v0.3-alpha.tar.gz',
  keywords = ['drv8825', 'control', 'steppermotor', 'stepper', 'motor', 'Jetson'],
  install_requires=[
          'Jetson.GPIO',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
