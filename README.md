TRANSCRIPT REDACTOR
=====

This program will read and redact transcript .pdf images from a folder


Setup
-------------------

Create a virtual environment

```
python -m venv .venv --prompt Redactor
```

Activate the environment (Linux/Mac OS)

```
source .venv/bin/activate
```

Activate the environment (Windows, Powershell)

```
& .venv\bin\Activate.ps1
````

Install all dependencies:

```
pip install -e .
```

Usage
-----

Use a terminal to enter commands.

To process single transcript:

    python src/main.py run <transcript-name.pdf> <Folder name>

eg. `python main.py run 000000001.pdf Transcripts`

To process all transcripts:

    python main.py run all <Folder name>

eg. `python main.py run all Transcripts`



