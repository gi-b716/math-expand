del build
del dist
del mathexpand.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*