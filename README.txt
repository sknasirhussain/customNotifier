## Welcome to my very own notification alert ##

So i made this one cz i was getting waayy distracted by gaming and was not working at all. So in order to stop myself this was the smallest effort. In this file I will just brief you guys how to use this program.

How to start the app on startup(terminal will be visible to user at startup):-

1. Save your Python program in a suitable location on your computer.
2. Open the Start Menu and search for "Task Scheduler."
3. Click on "Create Basic Task" or "Create Task" in the right-hand panel, depending on your version of Windows.
4. Give your task a name and description.
5. Choose the trigger that you want to use to start the task, such as "At startup”. I selected “At log on” option so that works as well.
6. Choose the action that you want to perform, such as "Start a program."
7. Browse to the location where you saved your Python program and select it.
8. Set any additional options for your task, such as whether to run it with the highest privileges or to stop the task if it runs for too long. Also uncheck everything under the “Power” tab. It just stops the program from running when only on battery power.
9. Click "Finish" to save your task.

Running the program in the background(Hidden from the user):-

1. Open a text editor such as Notepad.
2. Type the following command in the text editor:

	start /b pythonw path\to\your\program.py

Replace "path\to\your\program.py" with the actual path to your Python program. The "start /b" command starts the Python program in the background using the "pythonw.exe" interpreter, which runs the program without displaying a console window.
3. Save the file with a .bat extension. For example, you can save the file as "run_my_program.bat".
4. Move the batch file to a location where it won't be moved or deleted. For example, you can create a folder named "MyProgram" in the root directory of your C: drive and move the batch file there.
5. Then just follow the same steps as mentioned above about creating the task in the windows scheduler. Just instead of uploading the python file here we will upload the batch file.
That's it. Restart your pc or just sign out and sign in and it’s good to go.

Killing the task:

1. Open task manager.
2. Search for a program named terminal or python and just end it.
3. That's all.


Have fun!!
