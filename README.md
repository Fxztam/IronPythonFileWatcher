# IronPythonFileWatcher

This demo is a proof of concept for protocolling of file changes (create, update, delete) in a watched directory based on the Microsoft FileSystemWatcher Service.

IronPython is an implementation of Python for the Common Language Infrastructure (CLI), the demo was developed in Microsoft Visual Studio Community 2015 Update 3.

## Motivation

It shows a practice for simple exchanging of data files between different runtime systems and for Low Code Programming in IronPython.

>**Note:**
>Use the directories that are applied to the *`FormsFileWatcher Demo`* : https://github.com/Fxztam/FormsFileWatcher


## Getting Started


### Prerequisites

- IronPython 2.7.7

- Start the *`FormsFileWatcher Demo`* : https://github.com/Fxztam/FormsFileWatcher or using a file editor for modifying

>**Note:**
>You can also simulate file changes by editing in the watcher directory defined in the *`IronWatcherForms.py`*


### Installing

Following steps for installation of the *`IronWatcherForms.py`* and *`IronWatcherForms2.py`* files:

1. Installing IronPython 2.7.7 : http://ironpython.net/

2. Verify the IronPython installation
    ```
    DOS> ipy
    IronPython 2.7.7 (2.7.7.0) on .NET 4.0.30319.42000 (32-bit)
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

2. Create a working directory e.g.  *..\Work-FileWatcher*

3. Copy the files *IronWatcherForms.py* and *`start_IronWatcher.cmd`* to the *`Work-FileWatcher`* directory

4. Modify *`IronWatcherForms.py`* - adapting the File Watcher directory

>**Note:**
>The FormsFileWatcher Demo is using the Windows user temp path as directory root, e.g. :
>*`C:\Users\fmatz\AppData\Local\Temp\formswatch\forms`* for FormsFileWatcher Demo (internal default here).

5. Modify *`start_IronWatcher.cmd`* - adapting the *`ipy.exe`* - command line


## Running the tests

Change to the Work-FileWatcher directory and start the IronPython FileWatcher
```
DOS> start_IronWatcher.cmd
```
and this shows the running demo:

<img src="http://www.fmatz.com/IronWatcher.gif">


## Contributing

This PoC demo was adapted from : http://www.ironpython.info/index.php?title=Watching_the_FileSystem

## Versioning

Proof of Concept version

## Author

Friedhold Matz, November 2017

## License

Free License
