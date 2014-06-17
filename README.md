# %%sb


## Install

```python
In [1]: %install_ext https://raw.githubusercontent.com/yhat/sb-magic/master/sbmagic.py
Installed sbmagic.py. To use it, type:
  %load_ext sbmagic

In [2]: %load_ext sbmagic
```

## Basic commands


```python
In [3]: %sb config
|----------------------------------------------|
| Username | Password | Server                 |
|----------------------------------------------|
| yhat     | ******** | http://SCIENCEBOX_URL/ |
|----------------------------------------------|

In [4]: %sb help
NAME:
   sb - Command line tool for use with Yhat sciencebox.

USAGE:
   sb [global options] command [command options] [arguments...]

VERSION:
   1.0.0

COMMANDS:
   config		Setup global config (--reset to reset)
   download		Download a file from the server
   init			Initialize a new project
   ls			See what files live on the server
   open			Open your sciencebox instance in a browser.
   push			Push a file to the server
   rm			Remove a file or directory on the server
   run			Runs a command on the server
   schedule		Schedules a command to be run on a certain date/time
   schedule-show	Shows the scheduled jobs
   sync			Sync a project with your server
   help, h		Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --generate-bash-completion
   --version, -v		print the version
   --help, -h			show help
```

## Run cell on server

```python
In [7]: %%sb run
   ...: for i in range(10):
   ...:     print "sciencebox rocks"
   ...:
Syncing data with Yhat Sciencebox
Checking which files have changed...
    ===> /.sb_magic_job-1bec5826-1d95.py
    ===> /.yhatproj
2 / 2  100.00 % 
Uploading changed files...
2 / 2  100.00 % 
Done!
Executing job on server.
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
sciencebox rocks
```
