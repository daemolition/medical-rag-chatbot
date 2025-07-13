from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()
    
setup(
    name="Medical RAG Chatbot",
    version="0.1",
    author="Christopher Abanilla",
    packages=find_packages(),
    install_requires=requirements,
)