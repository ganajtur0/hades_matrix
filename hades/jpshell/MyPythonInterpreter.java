package hades.jpshell;

import org.python.util.PythonInterpreter;
//import org.python.core.*;

import java.io.*;

// Diese Klasse soll den PythonInterpreter um
// gewünschte Funktionen erweitern
public class MyPythonInterpreter extends PythonInterpreter {
    

    public MyPythonInterpreter () {
	super();
    }


    public MyPythonInterpreter ( ByteArrayOutputStream printStream) {
	this();
	init(printStream);
    }
  

    //leitet die Eingabe um 
    protected void init( ByteArrayOutputStream printStream) {
	set("printStream", printStream);
    }


    //get und set Methoden
    /* 
       public void setScriptPath() {
       String scriptPath = "/jpshell/script";
       Properties properties = new Properties();
       String basePath = properties.getProperty("HADES_HOME");
       set("scriptPath", scriptPath);
       exec("import sys");
       hier muss eine idee her !!!
       exec("sys.path.insert(0, '/usr/home/matthias/hades/jpshell/script')");
       }

       public void setScriptPath(String scriptPath) {
       set("scriptPath", scriptPath);
       }
    */
}
