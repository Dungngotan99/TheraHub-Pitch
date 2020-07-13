====--RequestLogger.py--====



@description

Python Script to open a simple HTTP server on the localhost (127.0.0.1), listen for HTTP POST and GET Requests, then write out to a txt file in the same directory. After the program is stopped through a keyboard interrupt (CTRL+C), it will call RequestParser to grab the variables from the file and print them. Finally, it will wipe the text file so that another request can be processed.



@use

On windows machines:

Simple Use: Run the batch file called Run RequestLogger, which will handle everything for you. After an entry (formatted properly) is logged, a keyboard interrupt (CTRL+C) will stop the process and display results.
Direct Use: open the command line (cmd.exe), navigate to directory containing the file (or provide full path) and assuming python is installed, the following command should start the server. Again, stopping the program with a keyboard interrupt prints out the variables.



@syntax

py RequestLogger.py {desired_portnumber_here} 



@notes 

This was tested on python version 3.8.3 using port number 8000. Any open port should work, however different versions of python may require using "python" or "python3" in the place of "py"
I reccomend using the free program Postman to send requests when testing, link is included below. The formatting of the file should be an array of strings as specified in the example. 
https://www.postman.com/ 



====--RequestParser.py--====



@description

Python script that reads in data from the newly created text file, converts the lines into an array, and isolates the relevant variables. They will be printed at the end.



@use

On windows machines:

Simple Use: Run the batch file called Run RequestLogger, which will handle everything for you. After a entry (formatted properly) is logged, a keyboard interrupt (CTRL+C) will stop the process and display results 
Direct Use: open the command line (cmd.exe), navigate to directory containing the file (or provide full path) and assuming python is installed, the following command should extract the variables from the POST request



@syntax 

py RequestParser.py {path_to_input_file_here}



@notes

These two files can be used seperately, but calling the parser from the loggger made the most sense. All the file placement and creation can be modified towards whichever directory you need, if using the current directory is inconvenient.
