package hades.jpshell;

import java.io.*;
import hades.simulator.*;
import hades.signals.Signal;
import hades.models.*;
//import hades.symbols.*;
//import hades.gui.Console;
//import hades.gui.Editor;
import hades.utils.StringTokenizer;

import org.python.util.PythonInterpreter;
//import org.python.core.*;

/** 
 * JPWrapper - a subclass of SimObject used as base class 
 *               for logic gates in JPython.
 *               Signals are expected to be StdLogic1164 objects.
 *
 * @author M.Meyer
 * @version 0.1   19.04.2000
 */
public class  JPWrapper 
       extends  SimObject
       implements  Simulatable, 
                   hades.utils.ContextToolTip,
                   java.io.Serializable {


	private static PythonInterpreter interp = null;
	//private Editor editor;
	private JPWrapper pyObj;
	public String pyModul;
	public String pyClass;
	public String pyWriteArgs;
	private boolean debug = false;
	public Port[] ports;
  	public double t_delay = 5.0E-9; // 5 ns


  public JPWrapper() { 
    super();
	if (debug)
    	System.out.println("JPWrapper construktor ends");
  }


  public double getDelay() { return t_delay; }
  
  public void setDelay( double t ) 
  { 
  	if (pyObj != null)
		pyObj.setDelay(t);
  	t_delay = t; 
  }

  public void setDelay( String s ) { 
    try {
      t_delay = Double.valueOf( s ).doubleValue();
    }
    catch( Exception e ) {
      message( "-E- JPWrapper.setDelay(): " + e );
      t_delay = 5.0E-9;
      message( "-I- resetting to default value, delay = " + t_delay );
    }
	pyObj.setDelay(t_delay); 
  }

  public void configure() {
    if (debug) message( "-I- starting to configure this " + toString() );
    String[] fields = { "instance name:", "name",
                        "gate delay [sec]:", "delay" }; 

    propertySheet = hades.gui.PropertySheet.getPropertySheet( this, fields );
    propertySheet.setHelpText(  "Specify instance name and gate delay:" );
    propertySheet.setVisible( true );
  }


  public String getSymbolResourceName() {
  	return pyObj.getSymbolResourceName();
  }


  	public boolean initialize( String s ) 
	{ 
		if (debug)
			System.out.println("JPWrapper initialize.."+s);
		StringTokenizer st = new StringTokenizer( s );
		int n_tokens = st.countTokens();
		try
		{
			versionId = Integer.parseInt( st.nextToken() );
			if (n_tokens >= 2) 
			{
				t_delay   = Double.valueOf( st.nextToken()).doubleValue();
			}
			
			if (n_tokens >= 3) 
			{
				pyModul = st.nextToken();
				pyClass = st.nextToken();
				if (n_tokens >= 4)
				{
					pyWriteArgs = st.nextToken();
					if (debug)
						System.out.println("JPWrapper pyWriteArgs:"+pyWriteArgs);
				}
				pyObj = createJPObject(pyModul, pyClass, pyWriteArgs); 
				pyObj.setName(name);
				pyObj.setDelay(t_delay);
				//this.ports=pyObj.getPorts();
				//super.setPorts(ports);
				this.ports=pyObj.ports;
				setPorts(ports);
				
				Port tmpPort;
				for (int i=0; i<ports.length; i++)
	    		{
					tmpPort = ports[i];
		    		tmpPort.setParent(this);
				}

			}
		}
		catch (Exception e)
		{
			if (debug)
				System.out.println("JPWrapper error "+e);
		}
		
		return true;
	}

	//JPWrapper used as an ObjectFactory....':-) 
	public JPWrapper createJPObject(String pyModul, String pyClass, String args)
	{
		if(debug)
			System.out.println("createJPObject: "+pyModul+","+pyClass+","+args);

		if (interp == null)
		{
			if(debug)
				System.out.println("erzeuge interp");
			interp = JPShell.getInterpreter();
			if (interp == null)
			{
				interp = new PythonInterpreter();
				updatePythonPath();
				interp.set ("editor", editor);
				execResource( "/hades/jpshell/module/init_jpshell.py" );
			}
		}
		interp.exec("from "+pyModul+" import "+pyClass);
		interp.exec("pyObj = "+pyClass+"()");
		
		if (args == null || args.equals("null"))
		{
			if (debug)
				System.out.println("null args");
		}
		else
		{
			if (args.length() > 0)
			{
				if (debug)
					System.out.println("JPWrapper args:"+args);
				interp.exec("pyObj.setArgs('"+args+"')");
			}
		}
		Class javaClass = new JPWrapper().getClass();
		pyObj = (JPWrapper) interp.get("pyObj", javaClass);
		//pyObj.setName(name);
		//this.ports=pyObj.getPorts();
		//super.setPorts(ports);

		//interp = null;
		return pyObj;
	}


  	public void write( java.io.PrintWriter ps )
  	{
		if (debug)
    		System.out.println( " " + versionId + " " + t_delay + " " + pyModul + " " + pyClass + " " + pyWriteArgs);
    	ps.print( " " + versionId + " " + t_delay + " " + pyModul + " " + pyClass + " " + pyWriteArgs);
	}


  public void elaborate( Object arg ) {
    if (debug) message( "-I- " + toString() + ".elaborate()...ignored." );
	pyObj.elaborate(arg);
  }

	public void evaluate( Object arg ) 
	{
		if (debug)
			System.out.println("JPWrapper.elaborate(arg)...ignored."+arg );
		pyObj.evaluate(arg);
	}

  public void scheduleEvent( Signal        signal, 
                             double        time, 
                             StdLogic1164  value,
                             Port          port ) 
  {
    simulator.scheduleEvent(
      SimEvent1164.createNewSimEvent( signal, time, value, port )
    );
  }


  public void scheduleEventAfter( Signal        signal, 
                                  double        delay,
                                  StdLogic1164  value,
                                  Port          port ) 
  {
    double time = simulator.getSimTime() + delay;
    simulator.scheduleEvent(
      SimEvent1164.createNewSimEvent( signal, time, value, port )
    );
  }



  /**
   * create a copy of the current JPWrapper with the same gate delay.
   */
  public SimObject copy() {
  		System.out.println("copy: "+this.pyModul+", "+this.pyClass+", "+this.pyWriteArgs);
		JPWrapper tmpPyObj = createJPObject(this.pyModul,this.pyClass,this.pyWriteArgs);
    	JPWrapper clone = (JPWrapper) super.copy();
  		System.out.println("copy: huhu ");
		
		clone.pyObj = tmpPyObj;
		
		clone.setPyModul(pyModul);
		clone.setPyClass(pyClass);
		clone.setPyWriteArgs(pyWriteArgs);
		Port[] tmp_p = tmpPyObj.ports;
		if (debug)
			System.out.println("tmp_p: "+tmp_p+"tmp_p: "+tmp_p.length);
		clone.ports = tmp_p; 
		
		Port tmpPort;
		for (int i=0; i<clone.ports.length; i++)
	    {
			tmpPort = clone.ports[i];
		    tmpPort.setParent(clone);
		}
						
		clone.setPorts(clone.ports);
    	clone.setDelay( this.getDelay() );
   
    	return clone;
  }



  /**
   * construct a (short) tool tip message for a SimObject.
   * This method should be overridden as needed.
   */
  public String getToolTip( java.awt.Point position, long millis ) {
    return   getName() + "\n"
           + getClass().getName() + "\n"
           + "delay=" + t_delay;
 
  }


  /** 
   *  toString() - the usual info method 
   */
  public String toString() {
    return "JPWrapper: " + getFullName();
  }

/* end JPWrapper.java */


	public void setPyObj(JPWrapper pyObj)
	{
		this.pyObj = pyObj;
		Port[] ports = pyObj.ports;
		Port tmpPort;
		for (int i=0; i<ports.length; i++)
		{
			tmpPort = ports[i];
			tmpPort.setParent(this);

		}
		t_delay = pyObj.t_delay;
		pyWriteArgs = pyObj.pyWriteArgs;
	}
	
/*	public void setClonePyObj(JPWrapper clone, JPWrapper pyObj)
	{
		JPWrapper tmpPyObj = null;
		System.out.println(pyObj.pyModul+","+pyObj.pyClass+","+pyObj.pyWriteArgs);
		System.out.println("clone "+clone.pyModul+","+clone.pyClass+","+clone.pyWriteArgs);
		System.out.println("this "+this.pyModul+","+this.pyClass+","+this.pyWriteArgs);
		try
		{
			tmpPyObj = (JPWrapper) pyObj.clone();
			System.out.println("debug huhu 1");
		}
		catch(CloneNotSupportedException e)
		{
			System.out.println("JPWrapper clone error: "+pyObj+" not clonable"+e);
		}
		clone.pyObj = tmpPyObj;
		//Port[] ports = clone.getPorts();
		Port[] ports = tmpPyObj.getPorts();
		Port tmpPort;
		for (int i=0; i<ports.length; i++)
		{
			tmpPort = ports[i];
			tmpPort.setParent(clone);
		}
		clone.t_delay = tmpPyObj.t_delay;
		clone.pyWriteArgs = tmpPyObj.pyWriteArgs;
	}
*/

	public JPWrapper getPyObj()
	{
		return pyObj;
	}
	
	public void updatePythonPath()
	{
		String hades_home = System.getProperty("HADES_HOME");
		if (hades_home != null)
		{
			interp.exec("import sys");
			interp.exec("sys.path.insert(0, '"+hades_home+"/jpshell/module')");
			interp.exec("sys.path.insert(1, '"+hades_home+"/jpshell/examples')");
			interp.exec("sys.path.insert(2, '"+hades_home+"/jpshell/module/objects')");
		} 
		else 
		{
			interp.exec("import sys");
			interp.exec("sys.path.insert(0, './jpshell/module')");
			interp.exec("sys.path.insert(1, './jpshell/examples')");
			interp.exec("sys.path.insert(2, './jpshell/module/objects')");
			if (debug)
				System.out.println("JPWrapper-Init-ERROR, HADES_HOME not found in system properties,\n "+
					   "we try to use current dir (.)!\n"+
					   "(please start with: java -DHADES_HOME=<your_hades_dir> hades.gui.Editor)");
		}
	}

	public void execResource( String resourcefilename )
	{
 		InputStream IS = getClass().getResourceAsStream( resourcefilename );
	    interp.execfile( IS );
	}

/*	public void setEditor(Editor e)
	{
		if (debug)
			System.out.println("JPWrapper setEditor: "+e);
		editor = e;
	}
*/
	public void setPyModul(String s)
	{
		pyModul = s;
	}
	
	public void setPyClass(String s)
	{
		pyClass = s;
	}

	public void setPyWriteArgs(String s)
	{
		if (debug)
			System.out.println("JPWrapper pyargs "+s);
		pyWriteArgs = s;
	}
/*
	public void setPorts(Port[] new_ports) 
	{
		if (debug)
			System.out.println("JPWrapper setPorts: "+ports+" to "+new_ports);
		ports=new_ports;
		super.setPorts(ports);
	}
	
	public Port[] getPorts() 
	{
		if (debug)
			System.out.println("JPWrapper getPorts: "+ports);
		if (pyObj != null)
			return pyObj.getPorts();
		else	
			return ports;
	}
*/
}

