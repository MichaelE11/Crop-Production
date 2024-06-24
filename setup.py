from setuptools import find_packages,setup #thee modele called find packages and setup is importted.
from typing import List #List in important when reading requirements.txt

'''
Since in the requirements -e. was used to triger the pakage finding one must remove it
'''
HYPHEN_E_DOT='-e.'

#create a function that opens the requirements.txt and reads the contents as list
def get_requirements(file_path:str)->List[str]:
    '''
    This will read the content of requirment.txt.
    the file path will be a string that returns a list of string
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # to ensure that \n is not part of the read content replace \n with blanks
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='crop production',
    version='0.0.1',
    author='Ephraim Michael',
    author_email='electmike84@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)