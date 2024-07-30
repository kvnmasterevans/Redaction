English_Learner_Detector.py is actually not used in this version of the program
I'll remove it as soon as I figure out how to do that.
~Sorry.


            TRANSCRIPT REDACTOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program will read and redact transcript .pdf images from a folder


-First install all dependencies:
open-cv
numpy
fitz
easyocr
json
nltk
difflib


-Use a terminal to enter commands:

    process single transcript:
    python main.py run <transcript-name.pdf> <Folder name>
        eg. python main.py run 000000001.pdf Transcripts

    process all transcripts:
    python main.py run all <Folder name>
        eg. python main.py run all Transcripts



