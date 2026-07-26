"""
def read_text(file_path: str) -> str:
    
    read_text(file_path: str) -> str

    Purpose:
    --------
    This function reads the text from a supported file and returns it
    as a single string.

    Parameters:
    -----------
    file_path : str
        The location (path) of the file to read.

        Example:
        file_path = "uploads/resume.pdf"

    Returns:
    --------
    str
        The complete text extracted from the file.
    


    Convert the file path (string) into a Path object.

    Why?
    ----
    A Path object provides useful methods to work with files.

    Example:
        file_path = "uploads/Resume.PDF"

        path = Path(file_path)

        path.name   -> "Resume.PDF"
        path.parent -> "uploads"
        path.suffix -> ".PDF"

    path = Path(file_path)


    Get the file extension and convert it to lowercase.

    Why lower()?
    ------------
    Users may upload files like:

        Resume.PDF
        Resume.Pdf
        Resume.pdf

    All of these become:

        .pdf

    This makes file checking easier and case-insensitive.
    
    suffix = path.suffix.lower()

    
    Check whether the uploaded file is a PDF.

    If suffix == ".pdf", execute the code inside this block.
    
    if suffix == ".pdf":

        
        Open the PDF using PdfReader.

        PdfReader does NOT immediately return the text.
        Instead, it creates a PDF Reader object that gives access
        to every page inside the PDF.

        Example:

            reader.pages

        might contain:

            [
                Page1,
                Page2,
                Page3
            ]
        
        reader = PdfReader(file_path)

        
        Create an empty string.

        Why?

        A PDF may have multiple pages.

        We need one variable to collect the text from every page.

        Initially:

            text = ""

        After Page 1:

            text = "Hello"

        After Page 2:

            text = "HelloPython"

        After Page 3:

            text = "HelloPythonMachine Learning"
        
        text = ""

        
        Loop through every page in the PDF.

        Example:

            reader.pages

        contains

            Page1
            Page2
            Page3

        Python automatically assigns:

            First loop:
                p = Page1

            Second loop:
                p = Page2

            Third loop:
                p = Page3
        
        for p in reader.pages:

            
            Extract text from the current page.

            Example:

                Page1 -> "Hello"

            += means:

                text = text + extracted_text

            'or ""' is a safety check.

            Sometimes extract_text() returns None
            (for example, scanned PDFs or image-only pages).

            Instead of adding None (which causes an error),
            Python uses an empty string.
            
            text += p.extract_text() or ""

            
            Add a newline after every page.

            Without "\\n":

                HelloPythonMachine Learning

            With "\\n":

                Hello

                Python

                Machine Learning
            
            text += "\n"

        
        After all pages have been processed,
        return one string containing the text
        from the entire PDF.
        
        return text
        """

"""
if suffix == ".docx":

Purpose:
--------
Check whether the uploaded file is a Microsoft Word document (.docx).

How does it work?
-----------------
Earlier in the function we extracted the file extension.

Example:

    resume.docx

    suffix = ".docx"

Now Python checks:

    if suffix == ".docx"

Python asks:

    "Is the uploaded file a DOCX file?"

If the answer is YES,
Python executes the code inside this block.

If the answer is NO,
Python skips this block and moves to the next condition.

------------------------------------------------------------

return docx2txt.process(file_path)

Purpose:
--------
Read the contents of the DOCX file and return all the text.

What is docx2txt?
-----------------
docx2txt is a Python library that extracts text from Microsoft Word
(.docx) documents.

Unlike PDFs, we do NOT need to read every page manually.

Why?
----
A DOCX document already stores its text in a format that
docx2txt can read directly.

Example:

    Resume.docx

Contains

    Name: Abhishek

    Skills:
    Python
    Machine Learning

    Experience:
    4 Years

When Python executes

    docx2txt.process(file_path)

it automatically extracts

    Name: Abhishek

    Skills:
    Python
    Machine Learning

    Experience:
    4 Years

Since process() already returns the complete text,
we simply return it immediately.

Notice:

There is no

    text = ""

There is no

    for loop

because docx2txt already reads the entire document for us.

------------------------------------------------------------
------------------------------------------------------------

if suffix in [".txt", ".md", ".py", ".csv"]:

Purpose:
--------
Check whether the uploaded file is one of these plain text files.

Supported extensions:

    .txt   -> Text File
    .md    -> Markdown File
    .py    -> Python Source Code
    .csv   -> Comma Separated Values

What does "in" mean?
--------------------

"in" checks whether something exists inside a collection.

Example:

    fruits = ["Apple", "Mango", "Orange"]

    "Apple" in fruits

Result

    True

Another example

    "Banana" in fruits

Result

    False

Exactly the same happens here.

Python checks

    Is suffix inside

    [
        ".txt",
        ".md",
        ".py",
        ".csv"
    ]

Example 1

Uploaded file

    notes.txt

suffix

    ".txt"

Python checks

    ".txt" in [".txt", ".md", ".py", ".csv"]

Result

    True

Example 2

Uploaded file

    app.py

suffix

    ".py"

Python checks

    ".py" in [".txt", ".md", ".py", ".csv"]

Result

    True

Example 3

Uploaded file

    image.jpg

suffix

    ".jpg"

Python checks

    ".jpg" in [".txt", ".md", ".py", ".csv"]

Result

    False

------------------------------------------------------------

return path.read_text(
    encoding="utf-8",
    errors="ignore"
)

Purpose:
--------
Read the complete contents of the file and return it as a string.

Unlike PDFs,
these files are already plain text.

Python can read them directly.

What is path.read_text()?
-------------------------

It opens the file,
reads everything,
and returns it as one string.

Example

notes.txt

Contains

    Hello
    Python
    Machine Learning

After

    path.read_text()

Python returns

    "Hello
    Python
    Machine Learning"

No loop is required.

No empty string is required.

Why encoding="utf-8"?
---------------------

Computers store text using different encodings.

UTF-8 is the most common encoding.

It supports

    English
    Numbers
    Symbols
    Hindi
    Japanese
    Chinese
    Emojis

Using UTF-8 ensures Python can correctly read most text files.

Why errors="ignore"?
--------------------

Sometimes a file contains invalid or unsupported characters.

Without

    errors="ignore"

Python may stop with an error like

    UnicodeDecodeError

With

    errors="ignore"

Python skips the problematic characters
and continues reading the rest of the file.

This makes the program more robust.

------------------------------------------------------------
------------------------------------------------------------

raise ValueError(
    "Unsupported file type. Upload PDF, DOCX, TXT, MD, PY, or CSV."
)

Purpose:
--------
Stop the program and tell the user that the uploaded
file type is not supported.

What does "raise" mean?
-----------------------

raise means

    "Throw an exception (error)."

Instead of continuing,
Python immediately stops the function
and reports the error.

What is ValueError?
-------------------

ValueError is a built-in Python exception.

It is used when the value provided is invalid.

In this case,

the file extension is not one of the supported types.

Example

Uploaded file

    image.jpg

suffix

    ".jpg"

Python checks

    ".pdf"   -> False

    ".docx"  -> False

    ".txt"   -> False

    ".md"    -> False

    ".py"    -> False

    ".csv"   -> False

Since none of the conditions match,

Python executes

    raise ValueError(
        "Unsupported file type. Upload PDF, DOCX, TXT, MD, PY, or CSV."
    )

Output

    ValueError:
    Unsupported file type.
    Upload PDF, DOCX, TXT, MD, PY, or CSV.

Why do we raise an error?
-------------------------

Without this line,

someone could upload

    image.jpg
    video.mp4
    music.mp3
    archive.zip

The function would not know how to read these files.

Instead of failing silently or producing incorrect output,

we clearly tell the user:

    "This file type is not supported."

This makes the function safer and easier to debug.
"""