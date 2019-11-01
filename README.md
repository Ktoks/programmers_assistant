# Programmer's Assistant

> Using voice recognition software
> Create an 'ai' that can run commands you speak (in linux terminal in the background)?
> when the command has completed running, bring the terminal display to the forefront to show the output
> so our program will hold a database of words mapped to command-line commands

## First time use

> python3 programmers_assistant.py user_name
> if configuration file doesn't exist:
> jarvis will run through and get configuration options from the user
> some will be required, some will be optional

## Regular use

> python3 programmers_assistant.py user_name [config]
> if configuration file exists:
> run jarvis on the current folder in terminal
> user_name links to database of regular commands and preferences

### Updating Config

> if arg[3] == config
> re-open configuration and ask if you want to overwrite, or add a configuration

## While running jarvis

### Waiting for start command

> Default use while jarvis is running:
> arg[0] = start command (default = jarvis)
> arg[1] = cd to location arg[1](
> test command = cd to location where tests on codebase can be run
> run command = cd to location where code can be run
> build command = cd to location where compiling can be run,
> ssh command = ssh to location where one would ssh to
> etc...)
> arg[2] = language currently working with
> arg[3] = first command
> arg[n] = end of commands to run in current directory
> arg[n+1] = stop command (default = jarvis)

## Psuedo-code implementation

### init

```python
# create an init function initializes data-members
    # data-members:
    # locationMap = {map of words to locations}
    # config = {map of configured settings}
    # mLocation
    # mLanguage
```

### Main

```python
# create a main function that runs jarvis in the background
    # wait for input from user's voice
    # when user's 'start' command is heard, call voiceRecognition
    # run analyzeSentence on output from voiceRecognition which calls
    # findDirectory, findLanguage, and matchCommands
    # run showDisplay on output from analyzeSentence
```

### Voice Recognition

```python
# create a voiceRecognition function that recieves voice input from the user
    # wait for user's 'stop' command
    # parse the input into a string
    # return the sentence string
```

### Analyze Sentence

```python
# create an analyzeSentence function that recieves 'sentence string' splits the string into words(arg[]) to pass to other functions
    # call findDirectory(arg[1]) that saves mapped directory into datamember
    # call findLanguage(arg[2]) that configures which language I'm working with
    # call matchCommands(arg[3]) that returns command string using mConfig datamember for formatting
```

### Find Directory

```python
# create a findDirectory function that recieves arg[1] and returns directory to run in
    # look up arg[1] and get the directory it maps to:
    # dir1 = 'test' directory
    # dir2 = 'run' directory
    # dir3 = 'build' directory
    # dir4 = 'ssh' directory
    # etc...
```

### Find Language

```python
# create a findLanguage function that recieves arg[2] and returns the database's saved options for a language
    # if arg[2] ==
    # python: use python configurations
    # c: use c configurations
    # c++: use c++ configurations
    # etc...
```

### Match Commands

```python
# create a matchCommands function that recieves arg[3], runs commands, and returns the display:
    # apply configurations from args[0-2]
    # run commands from arg[3]
    # run display, wait for exit command or x pressed on window
```

### Show Display

```python
# create a showDisplay function that recieves arguments and spawns display in forefront after completing command(difficult?),
# or spawns a new linux terminal with config from args[1-3], moving it to the forefront when the command completes
    # creates a new display or new terminal for each command sentence the user inputs
    # should kill any processes it has spawned in the background, then display the output?
    # waits for the exit command or x to be press to close the display window
    # only shuts itself down when quit command issued
```
