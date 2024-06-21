# This is my first time creating a beewave GUI application.

I am learning on the fly and making a Demo Hello world GUI app.

From what I understand it is very similar to PYQT and other python UI frameworks.

It has windows boxes.

your GUI bootstrap comes with various files.
In the src (source file) you have your project, where in the folder we have **three intersting files.**

The folder contains : 
```
__inti__.py
__main__.py
and app.py
```

First the `__init__.py` file is just to inform python that this folder is a module.

Second the `__main__.py` file conatins a code segment where it imports the main class from the app.py file.
```
from helloworld.app import main

if __name__ == "__main__":
    main().main_loop()
```
As we can see here `from helloworld.app import main` where helloworld is the folder and .app denotes the app.py file, and lastly it imports the main fuction which hold the UI segment.

Now for the app.py file this is where we code. `:)`