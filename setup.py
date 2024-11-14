from setuptools import setup, find_packages

setup(
    name="my_health_assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.0.134",
        "langchain-community>=0.1.0",
        "faiss-cpu>=1.7.2",
        "openai>=0.27.0",
        "langgraph>=0.1.0"
    ],
    entry_points={
        'console_scripts': [
            'my_health_assistant=my_health_assistant.main:main'
        ]
    }
)
