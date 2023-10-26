import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

GitHub_REPO_NAME = "Kidney_Disease_Classification_MLflow"
GitHub_AUTHOR_USER_NAME = "SunilKumar-ugra"
SRC_REPO = "Kidney_Disease_CnnClf"
GitHub_AUTHOR_EMAIL = "ugargolsunilkumar@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=GitHub_AUTHOR_USER_NAME,
    author_email=GitHub_AUTHOR_EMAIL,
    description="Kidney Stone Classification",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{GitHub_AUTHOR_USER_NAME}/{GitHub_REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{GitHub_AUTHOR_USER_NAME}/{GitHub_REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
