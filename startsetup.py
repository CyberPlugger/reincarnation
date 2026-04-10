from os import system
code = '''
pip install twine
python setup.py sdist bdist_wheel
twine upload dist/*
'''.split('\n')
if __name__ == '__main__':
    for command in code:
        system(command)