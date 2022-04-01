# Calculatrix

![logoCalculatrix](https://raw.githubusercontent.com/Yagi-404/Calculatrix/3602494affe10d7c1e541ac537df5e0ba7b55130/assets/logo.svg)

## What is Calculatrix ?

Calculatrix is a project where I'll create plenty of calculators in a lot of differents languages.
I know this sounds stupid but if you want to waste your time and contribute, you can...

## List of currents languages

- Python
- Web (JavaScript, HTML, CSS)
- C
- C++

More languages will be aivilable soon 👀.

## Installation

### - Python 🐍

#### Depedencies

- Python 3 or >
- [Pyinstaller](https://pypi.org/project/pyinstaller/) is optional
- Git

After you're done with installations, open a new terminal session and type:

```sh
# this clone the repo
# and go to the repo folder

$ git clone https://github.com/Yagi-404/Calculatrix
$ cd \Calculatrix\python\
```

#### Native Python

For native Python (no modules), you can type:
```sh
$ python <file to execute>.py
```

Type `Crtl` + `C` to stop the program.

#### Pyinstaller

*Pyinstaller* is a Python module that allows you to compile Python code into an .exe file.
This is an extra feature if you want to increase the execution speed.
To install Pyinstaller, you need :

- Python 3.6 .. 3.10
- PIP (it's better to have the latest version)
- Windows 8 or + (32/64 bits) 
OR
MacOS X (32/64 bits)
OR
Any version of GNU/Linux

Now, type in a terminal:
```sh
# install the module

$ pip install pyinstaller

# compile

$ pyinstaller ./path/to-your/file_to_compile.py
```
This should make a lot of new folders.

You should fine compiled files on dist/ and __ pycache __/ directories.

### Web version 🌐

#### Depedencies

- Git

After you're done with installations, go to [this website](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/Yagi-404/Calculatrix/tree/main/src/web).
You just have to *unzip* the file. 

If you have an issue when typing operations, here are two solutions :

1. **Make sure that you launched the calculator with a localhost**. You can open a localhost with Node.js, Live Server on VSCode and there are other solutions.

1. **If you don't want to install other things, you need to put the JavaScript into the HTML file.**
To do this, follow those steps :

>> - Open your JavaScript file with a text editor/IDE.
>> - Copy the code.
>> - Open your index.html file with a text editor/IDE.
>> - Write this at the end of the file:
```html
<script>
    // your code here
</script>
```
If you are still dealing with an issue, make an Issue, or try sove it making a Pull Request.

## Licence

This project is under the [MITLicense](https://mit-license.org/).
