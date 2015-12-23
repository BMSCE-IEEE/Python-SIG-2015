Python SIG 2015, BMSCE, Bangalore
Class 0 - 11-9-15

This is the readme file that should help you get Python running on your laptop.

FOR WINDOWS USERS:

a. Install it from http://python.org/download, or run the .msi setup file if you have taken it in the last class.
b. Make sure you install Python 2, not Python 3.
c. If after you install it python still isn't recognized (type "python" in the terminal program),
   then in PowerShell enter this:
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
e. Close PowerShell and then start it again to make sure Python now runs. If it doesn't,
restart may be required.

FOR MAC USERS:

a. Find the "Terminal" program by searching on Spotlight (that's what it's called isn't it?(and yes, I know that's
what it is called, trying to maintain an informal tone to appear approachable, don't you see? :P))
b. Python should run. Try typing "python".

FOR LINUX USERS:

a. What are you using Linux for then? Google it!
(b. On a serious note, very similar to Mac.)
---------------------
TEXT EDITOR/IDE:
	Most of the people who got pen drives have got the setup for Liclipse IDE. I myself haven't used it
	and don't intend to. So you can use either IDLE (default; installed with Python) or a text editor
	(like Sublime Text) with the command line. At this stage, everything is more or less the same.

	Also, if you like the Python interactive shell, you could consider installing IPython.
	But then again, "At this stage, everything is more or less the same."

--Pranav

Sources:
	Most of the procedure of the section "FOR WINDOWS USERS" is a modified form of a part of
    The Hitchhiker's Guide to Python (http://docs.python-guide.org/en/latest/starting/install/win/)
