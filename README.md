# Splitmer
A tool to split large pdfs into individual chapters.


## Installation

Clone Repository:
    
    - git clone https://github.com/qkcire/splitmer.git

Download dependency:
    
    - pip install pypdf2

## Instructions

First, create a `ch.txt` document and enumerate each chapter in the following format:
    
    [CH #] [CH_TITLE] [STARTING PAGE #] [ENDING PAGE #]
Seperate each chapter with a newline.

### Example using http://discrete.openmathbooks.org/pdfs/dmoi-tablet.pdf


    00 introduction_and_preliminaries 1 56
    01 counting 57 134
    02 sequences 135 196
    . . . 
    05 additional_topics 295 324

Next, run script with the following format:
    
    python3 splitmer.py [*.pdf] ch.txt [PAGE # OFFSET]

Note: the [`PAGE # OFFSET`] argument variable is used to ignore the first pages of the pdf leading up to the first chapter. 
To calculate the offset, navigate to the first chapter (which in our math pdf begins at page 17) and subtract 1. the offset is 16. 

Using the math textbook linked above, move the pdf into the same directory as the script along with the `ch.txt` document and begin the script as follows:


    python3 splitmer.py dmoi-tablet.pdf ch.txt 16

## Known issues and how to fix them

Once in a while you'll come across this error followed by a loop until the script crashes:

    $ python3 splitmer.py corrupted.pdf ch.txt 13
    Splitting pdf . . .
    Traceback (most recent call last):
        File "splitmer.py", line 42, in <module>
            splitter(cmnd_line_arg_list[0])
        File "splitmer.py", line 19, in splitter
            pdf_writer.write(out)
    . . .

From my research, this error has to do with the corrupted pdf metadata. To fix, install `ghostscript` and follow the instructions here: https://superuser.com/a/282056 