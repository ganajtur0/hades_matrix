# Java-Python-Shell-Standart-Skript
# os: Generic Operating System Services  
import re
import os
import sys
import java.lang.reflect
import jp_os
import jp_tools
import jp_design_os
import jp_sim_control

def _welcome():
    ''' <None> welcome()
    welcome diplays the welcome start text.
    '''
    print """
    Welcome to the HADES-Script-Shell

    use the help() command for displaing all available
    methods, or try help(\"help\"). 
    If there is a different between the design in the 
    HADES-editor and the shell, please use the
    updateDesign() command. 
    """


def infoObject(object, pattern=""):
    ''' <None> infoObject(object[, pattern])   
    infoObject displays a list of all methods which are machted
    with the pattern.
    '''
    p = re.compile(pattern)

    object_class = object.getClass()
    print object_class
    object_methods = object_class.getMethods()
    for method in object_methods:
	if (p.match(method.toString())):
	    print method


def getHelp(module, pattern=""):
    ''' <None> getHelp(module)
    get_help displays the document string of all methods in a module
    which are matched with the pattern.
    '''
    p = re.compile(pattern)
        
    l = dir(module)
   
    for field in l:
	#print field
        field = eval(module.__name__+"."+field)
	#print field
        if ( (hasattr(field,"__doc__") and (p.match(str(field.__name__)))) ):
            print "NAME %-15s - SYNTAX %-20s" %(field.__name__, field.__doc__)


def info(pattern=""):
    ''' <None> info([pattern])
    info displays all global items which are matched with the pattern.
    '''
    p = re.compile(pattern)
    for (key, value) in globals().items(): 
	if ((key[1:2] != '__') and ( (p.match(str(key))) or (p.match(str(value))) )):
	    print "%-20s - %-20s" %(key, value)


def fullUpdate():
    ''' <None> fulUpdate()
    the basics toplevel objects design und simulator are updated.
    '''
    global design, simulator, editor
    editor = jp_design_os.getEditor()
    design = jp_design_os.getDesign()
    simulator = jp_sim_control.getSimulator()


#def exec_example(example):
#    ''' <None> exec_example(example)
#    exec_example execute a example, that have to be available.
#    '''
#    try:
#	#example_path = jp_os.getPath() + os.sep + scriptPath + "examples" +  os.sep
#	#execfile(example_path + example)
#	execfile(example)
#    except:
#	print "Error:", sys.exc_type, sys.exc_value
##
#older stuff, have to change to jp_os!!!
#def restart():
#    "restarts the Java-Python-Shell"
#    execfile(scriptPath+os.sep+'JP-Std-Script.py')
#def source(filename):
#    "execfile in scriptpath"
#    execfile(scriptPath+os.sep+filename)
#def show():
#    "show all python scripts in scriptpath"
#    list = os.listdir(scriptPath)
#    for file in list:
#	if (file[-3:] == ".py"):
#	    print file
    
#def edit():
#    "under construction, sorry"
#    from hades import jpshell
    #myedit = new hades.jpshell.MyEdit()
    #myedit.setSize(500,400)
    #myedit.show()
   




