# Presentation
The `ragtime-projects` repo contains projects built using **Ragtime** 🎹.

# Getting started
## Install the package
Make sure you have already installed the Ragtime 🎹 package. If not, just run:
```shell
pip install ragtime
```

## Create your project
Then choose a folder where you will create your Ragtime 🎹 projects. In this folder, create a `main.py` containing:
```python
from ragtime import config
config.init_project(name='your_project', init_type='copy_base_files')
```
and run it.

This will create a subfolder named `your_project` containing:
- folder `expe`: contains 4 sub-folders containing the data which will be created at each step of your experiments
- folder `logs`: the logs associated with your project
- folder `res`: contains templates for the file exports
- `config.py`: configuration for logs, default folders...
- `keys.py`: API keys
- `.gitignore`: tells not to sync the `keys.py` file
- `classes.py`: your classes to define the Prompter and Retrievers you may use
- `main.py`: the file containing the `main` function for your project
- `LICENSE`: MIT by default - don't forget to add you name / company in it
- `README.md`: your project's doc

# Examples
Several examples are given to illustrate how to use Ragtime 🎹:
- [What do LLM think?](what_do_llm_think/README.md)
- [Google NQ](google_nq/README.md)

# Package repo
If you are looking for the package, not the examples, [it is here](https://github.com/recitalAI/ragtime-package).