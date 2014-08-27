Scratch
=======

## Overview

Scratch is a simple Sublime Text plugin that makes it easy to create scratch files for code snippets and notes. These files are saved in single location for easy searching and access later.

##Usage
### Basic Usage
1. In Sublime Text Go to ```File > New Scratch File``` 
2. A new file is opened. The file is named "*number*.*extension*". *number* is an integer that is set to one more than the last saved Scratch file name. *extension* is a user-configurable extension.  

  **Example**  
  ```File > New Scratch File``` to open "0.py". Save the file.  
  ```File > New Scratch File``` to open "1.py".

###Changing File Extensions Quickly
To quickly change the extension of a Scratch file: 

1. Set the first line of the file to contain *only* the new extension you want to switch to.  
2. Save the file
3. The file now has the the new extension

  **Example**  
  ```File > New Scratch File``` to open "0.py".  
  Type ".js" as the only text in the first line.  
  Save the file.  
  The file is now named "0.js" 

## Configuration
By default Scratch will save files to ```~/Documents/Scratch``` with the extension ```.py```. You can change these settings using the following flags in your package settings:
```
{
    "save_path": "~/Documents/Scratch",
    "extension" : ".py"
}
```
