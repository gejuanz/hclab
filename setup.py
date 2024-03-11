from setuptools import setup, find_packages

setup(
    name='hclab',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'httpcat-sdk',
        'myhttpcat',
        'myhcat',
        'httpcatlab'
    ],
    author='gejuanz',
    author_email='gejuanz@outlook.com',
    description='hclab',
    license='MIT',
    keywords='hclab',
    url='https://github.com/gejuanz/hclab',
    download_url='https://github.com/gejuanz/hclab',
    project_url='https://github.com/gejuanz/hclab',
    project_urls={
        "Source":"https://github.com/gejuanz/hclab",
    }
)

