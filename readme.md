## DataCore

A parameter-scan and data-manage framework tool using python, applicable to any program passing parameters via bash.

### Demo

Run `python core.py`, settings can be found at `setting.py` come with this package, the program scanned is a pseudo program that only return parameters entered.

### Usage

All settings at `setting.py` , which can be divided into two parts:

#### Variables

1. **maximumJobs**: number of workers to run. e.g. with 8 GPU cards, maxmumJobs should be `8`.
2. **command**: the static part of commands to run, this variable is a list of strings, different part of command should be a string. e.g. `['python','./pseudorun.py']`.
3. **settings**: the part of commands which is static at individual workers, this should be a list of lists of strings which are keywords and their value, and the length of this variable should be same with **maximum**. e.g. due to different workers are on different CPU, settings should be `[['-cuda',str(i)] for i in range(8)]`.
4. **parameters**: the part of parameters that actual to scan. This variable should be a dict with keyword be a string of the parameter keyword and content be list of string of values to scan. e.g. scan T from 2.0 to 3.5 and -depth from 1 to 4, so `{"-T":[str(i/10) for i in range(20,36)],"-depthMERA":[str(i+1) for i in range(4)]}`.

#### Functions

1. **before**: the function to run before running command. e.g. to more load file to same location to short command.
2. **process**: the function to process data collected from running command. e.g. grep all numbers and return back.
3. **after**: the function to run after running command. e.g. to more save file to specified locations.
4. **finish**: the function to run at the end of all commands, and have a input of all collected data.