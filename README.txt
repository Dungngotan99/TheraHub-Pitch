--RequestLoggerServer.py--



@description

Python Script to open a simple HTTP server on the localhost (127.0.0.1), listen for HTTP POST and GET Requests, then parse their data in a user-readable format



@use

On windows machines:

Simple Use: Run the batch file called Run RequestLogger, which will handle everything for you
Direct Use: open the command line (cmd.exe), navigate to directory containing the file (or provide full path) and assuming python is installed, the following command should start the server



@syntax

py RequestLogger.py desired_portnumber_here 



@notes 

This was tested on python version 3.8.3 using port number 8000. Any open port should work, however different versions of python may require using "python" or "python3" in the place of "py"
I reccomend using the free program Postman to send requests when testing, link is included below.
https://www.postman.com/ 