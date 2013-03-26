from setuptools import setup

setup(
    name='Pizza Suicide Club',
    version='1.0',
    long_description=__doc__,
    packages=['psc_app', 'psc_app.pages', 'psc_app.posts', 'psc_app.users', 'psc_app.zodiac'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'BeautifulSoup>=0.8',
        'Flask-WTF>=0.8',
        'Flask>=0.9',
        'SQLAlchemy>=0.7.9',
        'Flask-SQLAlchemy>0.16',
        'Tempita>=0.5.1',
        'WTForms>=1.0.2',
        'micawber>=0.2.5',
        'psycopg2>=2.4.6',
        'sqlalchemy-migrate>=0.7.2'
        ]
    )
