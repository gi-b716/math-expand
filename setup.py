import setuptools #导入setuptools打包工具
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="mathexpand", # 用自己的名替换其中的YOUR_USERNAME_
    version="1.3.0",    #包版本号，便于维护版本
    author="GavinCQTD",    #作者，可以写自己的姓名
    author_email="gavingan2012@gmail.com",    #作者联系方式，可写自己的邮箱地址
    description="A math expand package",#包的简述
    long_description=long_description,    #包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com/gi-b716/math-expand",    #自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',    #对python的最低版本要求
)
