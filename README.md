* [Langchain crash course for beginners](https://youtu.be/lG7Uxts9SXs?si=0CxHPGlGftY_wZU9)
* [Gabriel Jonay vera email](https://mail.google.com/mail/u/0/#search/alu0101398198%40ull.edu.es/FMfcgzGwHLqjpMrwkdSvJkkQXLWJvKss) 26/10/2023


## Versions

```
➜  crash-course-for-beginners pyenv --version
pyenv 2.3.23
➜  crash-course-for-beginners pyenv versions
  system
* 3.11.4 (set by /Users/casianorodriguezleon/.pyenv/version)
➜  crash-course-for-beginners python --version
Python 3.11.4
```

## venv

The `venv` module supports creating lightweight *virtual environments*, 
each with their own independent set of Python packages installed in their site directories. 

A virtual environment is created on top of an existing Python installation, known as the virtual environment’s *base* Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

* [venv](https://docs.python.org/3/library/venv.html)

Creation of virtual environments is done by executing the command `venv`:

```
python -m venv /path/to/new/virtual/environment
```

Running this command 
1. creates the target directory (creating any parent directories that don’t exist already) and 
2. places a `pyvenv.cfg` file in it with a home key pointing to the Python installation from which the command was run (a common name for the target directory is `.venv`). 
3. It also creates a `bin` subdirectory containing a copy/symlink of the Python binary/binaries (as appropriate for the platform or arguments used at environment creation time). 
4. It also creates an (initially empty) `lib/pythonX.Y/site-packages subdirectory`. If an existing directory is specified, it will be re-used. 

So I executed:

```
➜  crash-course-for-beginners python -m venv .venv
```

Took some time. A folder `. venv` appears.

Once an environment has been created, you may wish to **activate** it, e.g. by
sourcing an activate script in its bin directory.

A virtual environment may be **activated** using a script in its binary directory (`bin` on POSIX). This will prepend that directory to your `PATH`, so that 
1. running python will invoke the environment’s Python interpreter and 
2. you can run installed scripts without having to use their full path. 

The invocation of the activation script is platform-specific (<venv> must be replaced by the path to the directory containing the virtual environment):

```
$ source <venv>/bin/activate
```
So I executed:

```
➜  crash-course-for-beginners source .venv/bin/activate
(.venv) ➜  crash-course-for-beginners 
```

Notice that the prompt changed to indicate that the environment is active.

Now I proceed to install the dependencies:

```
(.venv) ➜  crash-course-for-beginners git:(main) ✗ pip install langchain openai streamlit python-dotenv
... # lots of output
[notice] A new release of pip is available: 23.1.2 -> 23.3.1
[notice] To update, run: pip install --upgrade pip
```

Then I created a file called `.env` with the following content:

```
OPENAI_API_KEY=sk-...
```
 
 Remember: The key is the one I'm using for `shai`.

I am using the `dotenv` module to load the environment variables from the `.env` file:

- Branch `llm-only` has the initial code using `dotenv` to load the environment variables from the `.env` file and the `openai` module and the `from langchain.llms import OpenAI` module.


```
(.venv) ➜  crash-course-for-beginners git:(main) ✗ python main.py
{'animal_type': 'cat', 'text': '\n\n1. Felix \n2. Tiger \n3. Shadow \n4. Gizmo \n5. Rocky'}
```