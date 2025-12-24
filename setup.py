from setuptools import setup, find_packages

setup(
    name="my_leetcode",    # 包名（自定义）
    version="0.1",
    packages=find_packages(),  # 自动找到util包
    install_requires=[],       # 依赖包（如有）
)
