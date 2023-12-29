# C964 Recommender System (SIM 3)

## IMPORTANT!

- Python 3.10.13 (pyenv)
- Pip 23.0.1 (IMPORTANT)

The packaged version of this app should work out of the box for Mac and Windows.

The user does not need python installed, the packaged apps have everything they need to run.

In your file explorer, navigate to these paths and run the .app/.exe to see the app running.

- release/macos
- release/windows

However, it will be difficult to install this project locally.

This app requires `scikit-surprise`, and this package has a lot of issues. 

It can NOT be installed with pip version 23.1 or above!

The `scikit-surprise` library hasn't added pyproject.toml or wheel yet. 

pip >= v23.1  will NOT install any package that doesn't have those things. `--use-pep517` doesn't help either. 

So you have to install it with pip 23.0.1. Even worse, it doesn't look like it will install on windows even using pip 23.0.1.  

It does install on Mac though! Maybe an older version of pip will work on windows?

I didn't realize the surprise library would be such a pain until after I finished my entire capstone.

I don't think it will be an issue for evaluation, since the packaged apps work just fine and the reports are in pdf/docx.

## Setup

```bash
python -m venv .venv

# If on Mac (project root)
source .venv/bin/activate

# If on Windows (good luck)
.venv\Scripts\Activate
# You might need this first
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# For the duration of this project, please make sure you're using pip 23.0.1 before installing any dependencies in requirements.txt
pip install pip==23.0.1
pip install -r requirements.txt
```

To run the app...

```bash
python src/main.py

# For tests
python src/ratings.test.py

# To package the app
pyinstaller 
```

If you want to look at the model.ipynb jupyter notebook, make sure it's using the .venv environment.

The jupyter notebook extension on vscode will try and upgrade pip before installing anything which screws it up 

I think you can do something like this or fiddle around with it to make it work.

```bash
python -m ipykernel install --user --name=project_env --display-name "Project Environment"
```

# Kaggle Dataset 

Courtesy of Rounak Banik 

https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

License CC0: Public Domain
