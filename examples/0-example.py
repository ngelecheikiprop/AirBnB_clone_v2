#!/usr/bin/python3
import cmd

class TestCmd(cmd.Cmd):
    intro = 'ngelechei playing around'
    prompt = '(test)'

    def do_test(self, args):
        """
        argt = args.partition(" ")
        if argt[0][0] == "\"" and argt[0][-1] == "\"" :
            print("has quotation marks")
        """
        argv = args.split()
        for arg in argv:
            print(arg)
if __name__=="__main__":
    TestCmd().cmdloop()
