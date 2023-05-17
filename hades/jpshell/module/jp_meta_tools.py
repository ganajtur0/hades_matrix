import re    
import jp_os
import jp_tools
import jp_design_os


def help(pattern=""):
    ''' <None> help([pattern])   
    help diplays the help of all methods which are matched with the pattern.
    The help format is:
    <return-value> method(arguments[,optional arguments])
    For examble:
    - help("info") or
    - help()
    '''

    p = re.compile(pattern)

    if (p.match(str(help.__name__) or str(help.__doc___))):
	print "NAME %-15s - SYNTAX %-20s" %(help.__name__, help.__doc__)
    if (p.match(str(doReload.__name__) or str(doReload.__doc___))):
	print "NAME %-15s - SYNTAX %-20s" %(doReload.__name__, doReload.__doc__)
    jp_tools.getHelp(jp_design_os, pattern)
    jp_tools.getHelp(jp_os, pattern)
    jp_tools.getHelp(jp_tools, pattern)
   
   
def doReload():
    ''' <None> do_reload()   
    do_reload reimports the basic modules (jp_tools, jp_design, jp_os).
    '''
    reload(jp_tools)
    reload(jp_design_os)
    reload(jp_os)
#    reload(jp_self_test)


#def doSelfTest(mode):
#    ''' <None> doSelfTest(mode)
#    mode=1 test enable and 0 disaple the test
#    '''
#    if (mode):
#	import jp_self_test
#	
#	try:
#	    jp_self_test.test_jp_tools()
#	except:
#	    print "jp_self_test error: ", sys.exc_type, sys.exc_value
