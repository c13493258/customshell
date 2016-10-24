#!/usr/bin/python3.5
from cmd import Cmd

import os,time,getpass,pwd,grp 



class commands(Cmd):
    def do_quit(self, args):
        print("Quitting from system")
        raise SystemExit

    def do_pw(self,args):
        child = os.fork()
        if (child == 0):
            path=os.getcwd()
            print(path)
        os.waitpid(0,0)
        print("child finished getting current directory")
    def do_ifc(self,args):
        child = os.fork()
        if child == 0:
            if args == "":
                os.system("ifconfig eth0")
            else:
                os.system("ifconfig" + args)
        os.waitpid(0,0)
        print("child finished ifconfig display")
    def do_dt(self,args):
        ctime = time.strftime("%Y%m%d%H%M%S")
        print(ctime)
    def do_ud(self,args):
        username = getpass.getuser()
        uid = pwd.getpwnam(username).pw_uid
        gid = pwd.getpwnam(username).pw_gid
        gname = grp.getgrgid(gid).gr_name

        home = os.getenv("HOME")
        hinfo = os.stat(home)
        inodetable=hinfo.st_ino

        print(str(uid) + "," + str(gid) + "," + username + "," + gname + str(inodetable))



    def help_ud(self):
        print("display user information")

    def help_pw(self):
        print("print the current directory")
    def help_quit(self):
        print("Exits the shell")
    def help_ifc(self):
        print("prints information for network devices. defaults to eht0")
    def help_dt(self):
        print("prints time and date in YYYYMMDDhhmmss format")

shell = commands()
shell.prompt = '>'
shell.cmdloop('starting shell')
