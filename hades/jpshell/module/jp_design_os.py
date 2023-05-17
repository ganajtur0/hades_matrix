import re
import string
from jarray import *
from java.util import Vector
from java.awt import Point
from hades.manager import DesignManager
from hades.signals import SignalStdLogic1164
from hades.symbols import SymbolManager, WireSegment, SolderDot
from hades.simulator import Port
from hades.jpshell import JPWrapper

def setEditor(edi):
    ''' <None> setEditor(editor)
    The current editor-object is replaced to the editor-argument.
    '''
    global editor
    editor = edi


def getEditor():
    ''' editor getEditor()
    getEditor return the current editor-object.
    '''
    global editor
    return editor


def getEditorByDesign(design_name):
    ''' editor  getEditorByDesign(design_name)
    getEditorByDesign return the editor, thats contains the design 
    specified by his name.
    '''
    editor = getEditor()
    editor_list = editor.getEditors()    
 
    while(editor_list.hasMoreElements()):
	e = editor_list.nextElement()
	if (e.getDesign().getName() == design_name):
	    jp_design_os.setEditor(e)

	    
def updateDesign():
    ''' <None> updateDesign()
    updateDesign update the interpreters design-object with the design 
    get from the editor-object.
    ''' 
    global design
    editor = getEditor()
    design = editor.getDesign()


def getDesign():
    ''' <design> getDesign()
    getDesign return the current design-object, if there
    is no interpreter design-object, the "updateDesign()" method
    is called.
    '''
    global design
    try: 
	return design
    except NameError:
	updateDesign()
	return design


def setDesign(d):
    ''' <None> setDesign(design)
    setDesign change the global interpreter design-object.
    '''
    global design
    design = d


def openDesign(resourcename):
    ''' <None> openDesign(resourcename)
    openDesign try to open a hades-file (.hds) specified 
    by the resourcename in a new HADES-Editor and update the
    design. 
    For examble:
    - openDesign("/hades/examples/simple/dlatch.hds")
    '''
    editor = getEditor()
    editor.doOpenDesign(resourcename, 0)
    updateDesign()


def openNewEditorWithDesign(resourcename):
    ''' <None> openNewEditorWithDesign(resourcename)
    openDesign try to open a hades-file (.hds) specified 
    by the resourcename in a new HADES-Editor. 
    For examble:
    - openNewEditorWithDesign("/hades/examples/simple/dlatch.hds")
    '''
    global design
    try:
	tmp_editor = getEditor()
	editor = tmp_editor.doCreateNewEditorWithDesign(resourcename)
	setEditor(editor)
    except:
	print "jp_stl.openNewEditorWithDesign error: ", sys.exc_type, sys.exc_value


def infoDesign():
    ''' <None> infoDesign()
    infoDesign displays all the info about the design and its components.
    '''
    d = getDesign()
    print d
    e = d.getComponents()
    while(e.hasMoreElements()):
	tmp = e.nextElement()
	print "%-20s - %-20s" %(tmp.getName(), tmp.getFullName())
	

def pwd():
    ''' <string> pwd()
    pwd displays and return the current design-path.
    '''
    path = getDesign()
    e = path.getComponents()
    if (e.hasMoreElements()):
	tmp = e.nextElement()
	tmp_path = tmp.getFullName()
	tmp_list = string.split(tmp_path, '/')
	path = tmp_list[:-1]
	print path
    return path


def ls(pattern=""):
    ''' <vector> ls([pattern=None])
    ls diplays all objects from the design-path which
    are matched with the pattern
    For example:
    - ls("design")
    '''
    p = re.compile(pattern)
    
    d = getDesign()
    e = d.getComponents()
    while (e.hasMoreElements()):
	tmp = e.nextElement()
	tmp_name = tmp.getName()
        tmp_info = tmp.toString()
	m = p.match(tmp_name)
	n = p.match(tmp_info)
	if (m or n):
	    print "%-20s - %20s" %(str(tmp.getName()), str(tmp))
	
   	
def cd(design_name):
    ''' <None> cd(design_name)
    cd change the design-path, to the "design_name".
    For example:
    - cd("..") change to the parent design
    - cd("/") change to the topdesign
    '''
    d = getDesign()
    if (design_name == ".."):
	design = d.getParent()
    elif (design_name == "/"):
	design = editor.getDesign()
    else:
        design = d.getComponent(design_name)
    setDesign(design)


def getByName(name):
    ''' <None> get(name)
    getByName return the sim-object specified by his name.
    '''
    d = getDesign()
    sim_object = d.getComponent(name)
    return sim_object


def get(pattern=""):
    ''' <vector> ls([pattern=""])
    get return all objects from the design-path which
    are matched with the pattern
    For example:
    - all_designs = get("design")
    '''
    result = Vector()
    p = re.compile(pattern)
    
    d = getDesign()
    e = d.getComponents()
    while (e.hasMoreElements()):
	tmp = e.nextElement()
	tmp_name = tmp.getName()
        tmp_info = tmp.toString()
	m = p.match(tmp_name)
	n = p.match(tmp_info)
	if (m or n):
	    result.addElement(tmp)
    if(len(result)==1):
        return result[0]
    else:
        return result


# design manipulation
def addComponent(c, c_name=None):
	'''<void> addComponent(SimObject, [c_name])
	add an SimObject to the current design,
	his name is the second option.
	'''
	d = getDesign()
	
	if string.find(str(c.getClass()), "org.python.proxies.") != -1:
		jpw = JPWrapper()
		jpw.setEditor(d.getEditor())
		jpw.setPyObj(c)
		jpw.setPorts(c.ports)
		jpw.setPyWriteArgs(c.pyWriteArgs)
		tmp = str(c.__class__)
		#print tmp
		jpw.setPyModul(string.split(tmp,'.')[0])
		jpw.setPyClass(string.split(tmp,'.')[1])
		# change the reference of the SimObject, to JPWrapper
		c = jpw

	if c_name == None:
		d.addComponent(c)
	else:
		d.addComponent(c, c_name)


def addComponentWithSymbol(c, pos, c_name=None, mirror=None):
	'''<void> addComponentWithSymbol(SimObject, position, [c_name=None], [mirror=None])
	add an SimObject to the current designi with an Symbol,
	his name is the second option and it can by mirrored.
	'''
    
	d = getDesign()
	editor = getEditor()

	if string.find(str(c.getClass()), "org.python.proxies.") != -1:
		jpw = JPWrapper()
		jpw.setEditor(d.getEditor())
		jpw.setPyObj(c)
		jpw.setPorts(c.ports)
		jpw.setPyWriteArgs(c.pyWriteArgs)
		tmp = str(c.__class__)
		#print tmp
		jpw.setPyModul(string.split(tmp,'.')[0])
		jpw.setPyClass(string.split(tmp,'.')[1])
		# change the reference of the SimObject, to JPWrapper
		c = jpw

	if c_name == None:
		d.addComponent(c)
	else:
		d.addComponent(c, c_name)

	c.setVisible( 1 )

	symbol_c = SymbolManager.getSymbolManager().getSymbol( c )

	if mirror != None:
		if "X" in mirror or "Y" in mirror or "R" in mirror:
			symbol_c.setOrientation(mirror)
   
	c.setSymbol(symbol_c)
    
	c.getSymbol().setTrafo(editor.getObjectCanvas().getTrafo())
	c.getSymbol().move(pos.x, pos.y)
    
	editor.insertIntoObjectList( c.getSymbol() )


def connect(sender, sender_port_name, receiver, receiver_port_name, signalName=None):
    '''<void> connect(sender, sender_port_name, receiver, receiver_port_name, [signalName=None]
    the sender with his port are connected to the receivers port, the name fort his signal
	is an option argument.
    '''
    d = getDesign()
    editor = getEditor()
    
    #print "connect",sender, sender_port_name, receiver, receiver_port_name
    sender_port = sender.getPort(sender_port_name) 
    receiver_port = receiver.getPort(receiver_port_name)
    
    signal = sender_port.getSignal()
    if  signal == None:
        signal = SignalStdLogic1164()
        signal.connect(sender_port)
    else:
        #signal.connect(sender_port)
        signal.addSender(sender_port)

    if receiver_port.getSignal() == None:
        signal.connect(receiver_port)
    else:
        #signal.connect(receiver_port)
        signal.addReceiver(receiver_port)

    if signalName!=None:
        signal.setName(signalName)

    d.addSignal(signal)
    #editor.insertIntoObjectList( signal )
    return signal


def connectWithSignalPos(pos_sender, sender_port_name, pos_receiver, receiver_port_name, signalName=None, wire_points=None):
	'''<void> connectWithSignalPos(pos_sender, sender_port_name, pos_receiver, receiver_port_name, [signalName=None], [wire_points=None]
	the sender at the specified position  with his port are connected to the receivers port.
	The name for his signal and the wire-point are optional arguments.
	'''
	#print "cPos",findSimObject(pos_sender), pos_sender
	
	connectWithSignal(findSimObject(pos_sender), sender_port_name, findSimObject(pos_receiver), receiver_port_name, signalName, wire_points)
	

def connectWithSignal(sender, sender_port_name, receiver, receiver_port_name, signalName=None, wire_points=None):
    '''<void> connectWithSignal(sender, sender_port_name, receiver, receiver_port_name, [signalName=None], [wire_points=None]
    the sender with his port are connected to the receivers port, with an grafical Signal.
	The name for his signal and the wire-point are optional arguments.
    '''
    d = getDesign()
    editor = getEditor()

    receiver = getByName(receiver.getName())
    sender = getByName(sender.getName())

    signal = connect(sender, sender_port_name, receiver, receiver_port_name, signalName)
    
    signal.setVisible(1)
    pos_sender_port = sender.getSymbol().getPortPosition(sender_port_name)
    pos_receiver_port = receiver.getSymbol().getPortPosition(receiver_port_name)
    
    ws = WireSegment(signal)
    if wire_points==None:
        wp = array([pos_sender_port, pos_receiver_port], Point)
    else:
        stmt = "array([pos_sender_port,"+str(wire_points)+", pos_receiver_port], Point)"
        #print stmt
        #wp = array([pos_sender_port, wire_points, pos_receiver_port], Point)
        wp = eval(stmt)
        
    ws.setPoints(wp)
    signal.addSegment(ws)
    
    signal.setTrafo( editor.getObjectCanvas().getTrafo() )
    signal.createVertexTable()
    signal.rebuildSolderDots()
    editor.insertIntoObjectList( signal )


def connectToSignal(obj, obj_port, target_signal, WP, at_pos=1):
    '''<void>  connectToSignal(obj, obj_port, target_signal, WP)
    this method connect the SimObject to an existing Signal.
    '''
    #TODO wo bliebt der SolderDot....
    d = getDesign()
    editor = getEditor()
    canvas = editor.getObjectCanvas()
     
    signal = d.getSignal(target_signal)	

    signal.connect(obj.getPort(obj_port))
    
    segment = editor.findNearestWireSegment( WP, 200)
    obj_pos = obj.getSymbol().getPortPosition(obj_port)

    #then change end start point of existing segment
    wcp_org = segment.getPoints()
    #print len(wcp_org), wcp_org
    tmp_wcp = zeros (len(segment.getPoints())+3, Point)
    #print tmp_wcp, at_pos 
    
    i = 0
    for wp in wcp_org[0:at_pos]:
        #print i
        tmp_wcp[i]	= wp
        i = i + 1

	#tmp_wcp[0:at_pos] = wcp_org[0:at_pos]
    #print "head", tmp_wcp 

    tmp_wcp[at_pos] = WP
    tmp_wcp[at_pos+1] = obj_pos
    tmp_wcp[at_pos+2] = WP
    #print "middle", tmp_wcp 

    i = at_pos+3
    for wp in wcp_org[at_pos:len(wcp_org)]:
        #print i
        tmp_wcp[i]	= wp
        i = i + 1

    #tmp_wcp[at_pos+3:len(wcp_org)-1] = wcp_org[at_pos+3:len(wcp_org)-1]
    #print "tail", tmp_wcp 
    
    #print len(tmp_wcp), tmp_wcp 

    #i = 0
    #for wp in segment.getPoints():
    #    print i, wp
    #    tmp_wcp[i] = segment.getPoints()[i]
    #    i = i + 1
    #print tmp_wcp
	
    #startP = segment.getPoints()[0]
    #endP = segment.getPoints()[len(segment.getPoints())-1] 
    #TODO bug wcp = array ([startP, WP, obj_pos, WP, endP], Point)
    segment.setPoints( tmp_wcp )
    segment.setTrafo( canvas.getTrafo() )

    #sd = SolderDot( signal, WP )
    #sd.setTrafo( canvas.getTrafo() );
    #signal.addSolderDot(sd)

    signal.createVertexTable()
    signal.rebuildSolderDots()
    editor.insertIntoObjectList( signal )


def clearDesign():
    d = getDesign()

    editor = getEditor()
    editor.doDeleteAll()
    editor.removeProbesFromAllSignals()
    
    signals = d.getSignals()   
    while signals.hasMoreElements():
        signal = signals.nextElement()
        signal.disconnectAll()
        d.deleteSignal( signal )
        editor.deleteFromObjectList( signal )    
    editor.getObjectCanvas().doFullRedraw()

def findSimObject( wp ):
	editor = getEditor()
	return editor.findSimObject(wp)

def findSignal( wp ):
	editor = getEditor()
	return editor.findSymbolOrSignal(wp)
