#! /usr/bin/python2
# -*- coding: UTF-8 -*-
""" This is my first module
There is not relation between all these functions
"""

class step(object):
    """class which defines a step"""
    def __init__(self,action="Action",result=False):
        self.action=action
        self.result=result
    def method(self):
        """method TBD"""
        print("{}".format(self.action))

class dsrFile(object):
    """class which defines a dsr file"""
    def __init__(self,filename):
        self.filename=filename
        #add test, check if file exist, else create it
        from xml.dom.minidom import parse
        self.__doc__ = parse(filename)
    def start(self):
        import datetime
        startTime = datetime()
        pass
    def method(self):
        """method TBD"""
        print("{}".format(self.action))
    def addStep(self, step):
        pass
    def write(self):
        #dom to string
        pass

def main():
    pass

if __name__ == "__main__":
    main()
	
