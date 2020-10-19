from setuptools import setup

setup(name = 'owl',
      version = '0.1',
      description ='owl is a very simple language under development intended to be part of ombakwarna as macro language',
      scripts = ['owl'],
      url='https://github.com/megatharun/owl',
      author ='Megat Harun Al Rashid bin Megat Ahmad',
      author_email ='megatharun@gmail.com',
      license ='GPL2',
      packages =['ombakwarna-owl'],
      install_requires =[
          'numpy',
          'termcolor',
      ],
      zip_safe=False)
