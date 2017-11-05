# IronPythonFileWatcher

This demo is a Proof of Concept for protocolling file changes (create, update, delete) in a watched directory based on the Microsoft FileSystemWatcher Service.

## Motivation

It shows a good practice for simple exchanging of data files between different runtime systems and for Low Code Programming in IronPython.

IronPython is a implementation of Python for the Common Language Infrastructure (CLI), the demo was developed in Microsoft Visual Studio 2015 Community Edition.

NOTE: Use the directories that are applied to the FormsFileWatcher demo: https://github.com/Fxztam/FormsFileWatcher

## Getting Started

Following

### Prerequisites

- IronPython 2.x

- Installing the FormsFileWatcher demo: https://github.com/Fxztam/FormsFileWatcher

### Installing

Following steps for installation:

1. Installing IronPython: 

2. Verify the IronPython installation
    ```
    DOS> ipy
    IronPython 2.7.7 (2.7.7.0) on .NET 4.0.30319.42000 (32-bit)
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

2. Create a working directory
    ```
    DOS> mkdir Work-FileWatcher
    ```

3. Copy the files IronWatcherForms.py and start_IronWatcher.cmd into the Work-FileWatcher directory

4. Modify IronWatcherForms.py

5. Mopdify start_IronWatcher.cmd

6. Change to the Work-FileWatcher directory and start the IronPython FileWatcher
    ```
    DOS> start_IronWatcher.cmd
    ```
7. Quit the alert :

and you will see:


## Running the tests

Explain how to run the automated tests for this system

<img src="http://www.fmatz.com/IronWatcher.gif">

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Author

Friedhold Matz, November 2017

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

