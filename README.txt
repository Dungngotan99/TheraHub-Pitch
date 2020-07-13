====--RequestLogger.py--====



@description

Python Script to open a simple HTTP server on the localhost (127.0.0.1), listen for HTTP POST and GET Requests, then write out to a txt file in the same directory



@use

On windows machines:

Simple Use: Run the batch file called Run RequestLogger, which will handle everything for you
Direct Use: open the command line (cmd.exe), navigate to directory containing the file (or provide full path) and assuming python is installed, the following command should start the server



@syntax

py RequestLogger.py {desired_portnumber_here} 



@notes 

This was tested on python version 3.8.3 using port number 8000. Any open port should work, however different versions of python may require using "python" or "python3" in the place of "py"
I reccomend using the free program Postman to send requests when testing, link is included below.
https://www.postman.com/ 



====--RequestParser.py--====



@description

Python script that reads in data from the newly created text file, converts the lines into an array, and isolates the relevant variables. They will be printed at the end.



@use

On windows machines:

Simple Use: Run the batch file called Run RequestLogger, which will handle everything for you
Direct Use: open the command line (cmd.exe), navigate to directory containing the file (or provide full path) and assuming python is installed, the following command should extract the variables from the POST request



@syntax 

py RequestParser.py {path_to_input_file_here}



@notes

These two files can be used seperately, but the batch file is the easiest way to coordinate both. All the file placement and creation can be modified towards whichever directory you need, if using the current directory is inconvenient.
