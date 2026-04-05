from setuptools import setup
import setup_translate

pkg = 'Extensions.MovieTagger'
setup(name='enigma2-plugin-extensions-movietagger',
       version='3.0',
       description='Add tags to recorded movies, to sort a large list of movies',
       package_dir={pkg: 'MovieTagger'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE', 'maintainer.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
