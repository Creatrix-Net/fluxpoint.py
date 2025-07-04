from setuptools import setup
import re

pakage_name = 'fluxpoint'
requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open(f'{pakage_name}/__init__.py') as f:
    version_match = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if version_match:
        version = version_match.group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],  # skipcq : BAN-B607
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
with open('README.rst') as f:
    readme = f.read()

extras_require = {
    'speed': [
        "aiohttp[speedups]>=3.8.1"
    ],
    'docs': [
        'sphinx',
        'sphinxcontrib_trio',
        'sphinxcontrib-websupport',
        'sphinx-autoapi',
        'typing-extensions'
    ]

}

packages = [
    pakage_name,
    f'{pakage_name}.paths'
]

setup(
    name='fluxpoint.py',
    author='Dhruva Shaw',
    url='https://github.com/Creatrix-Net/fluxpoint.py',
    project_urls={
        "fluxpoint.py API wrapper Docs": "https://fluxpointpy.dhruvashaw.in",
        "Official Api Docs": "https://docs.fluxpoint.dev/api",
        "Get Api Token": "https://fluxpoint.dev/api/access",
        "Offcial Fluxpoint discord server": "https://discord.gg/fluxpoint",
        "Support server for api wrapper": "https://discord.gg/vfXHwS3nmQ",

        "Repository": "https://github.com/Creatrix-Net/fluxpoint.py",
        "Examples Directory": "https://github.com/Creatrix-Net/fluxpoint.py/tree/master/examples",
        "Issue tracker": "https://github.com/Creatrix-Net/fluxpoint.py/issues",
    },
    version=version,
    packages=packages,
    license='GNU GENERAL PUBLIC LICENSE',
    description='A Python wrapper for the Fluxpoint API',
    keywords="fluxpoint api, api, wrapper, async wrapper",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    package_data={"fluxpoint": ["py.typed"]},
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
