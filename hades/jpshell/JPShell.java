/**
   JPShell
   by Matthias Meyer 14.11.1999
*/

package hades.jpshell;

import java.awt.*;
import java.awt.event.*;
import java.io.*;

//import org.python.core.*;

import hades.gui.*;


public class JPShell extends Frame  implements WindowListener, ActionListener, KeyListener{

    protected static MyPythonInterpreter interp;
    protected History history;

    private boolean debug = false;
    private String version = new String("v0.63 03.04.2001");

    protected TextArea textArea;
    protected TextField prompt;
    protected ByteArrayOutputStream printStream = new ByteArrayOutputStream();    


    public JPShell() {
      if (debug)
        System.out.println("Java-Python-Shell ("+version+")");

      history = new History();
      createGui();
      this.pack();
      this.setVisible( true );
    }


    public JPShell (hades.gui.Editor editor) {
      this();
      try {
        initInterp();
        setEditor(editor);
        updatePythonPath();
        execResource( "/hades/jpshell/module/init_jpshell.py" );
        interp.exec("jp_tools._welcome()");
        enter();
      } catch (Exception e) {
        System.out.println("JPShell raise an Error : "+e);
        System.out.println(
   "JPShell-Init-ERROR, HADES_HOME not found in system properties,\n "+
   "we try to use current dir (.)!\n"+
   "(please start with: java -DHADES_HOME=<your_hades_dir> hades.gui.Editor)");
      }
    }


    public JPShell (hades.gui.Editor editor, InputStream jpshell_init) {
      this();
      try {
          initInterp();
          setEditor(editor);
          updatePythonPath();
          execResource( "/hades/jpshell/module/init_jpshell.py" );
          enter();
      } catch (Exception e) {
          System.out.println("JPShell raise an Error: "+e);
          System.out.println("JPShell-Init-ERROR, HADES_HOME not found in system properties,\n "+
                 "we try to use current dir (.)!\n"+
                 "(please start with: java -DHADES_HOME=<your_hades_dir> hades.gui.Editor)");
      }
    }


  public void execResource( String resourcefilename ) {
    InputStream IS = getClass().getResourceAsStream( resourcefilename );
    interp.execfile( IS );
  }


  public void updatePythonPath() {
    String hades_home = System.getProperty("HADES_HOME");
    if (hades_home != null) {
      interp.exec("import sys");
      interp.exec("sys.path.insert(0, '"+hades_home+"/jpshell/module')");
      interp.exec("sys.path.insert(1, '"+hades_home+"/jpshell/examples')");
      interp.exec("sys.path.insert(2, '"+hades_home+"/jpshell/module/objects')");
    } else {
      interp.exec("import sys");
      interp.exec("sys.path.insert(0, './jpshell/module')");
      interp.exec("sys.path.insert(1, './jpshell/examples')");
      interp.exec("sys.path.insert(2, './jpshell/module/objects')");
      System.out.println("jpshell warning: HADES_HOME not found in system properties,\n "+
             "we try to use current dir (.)!\n"+
             "(please start with: java -DHADES_HOME=<your_hades_dir> hades.gui.Editor)");
    }
  }


  protected void createGui() {
    textArea = new TextArea( 20, 80 ); // rows, columns
    prompt   = new TextField( "", 80 );

    setTitle("HADES JPShell "+version);
    setBackground(Color.lightGray);
    textArea.setBackground(Color.lightGray);
    textArea.setFont(new Font("Courier", Font.PLAIN, 12));
    textArea.setEditable(false);

    prompt.setBackground(Color.lightGray);
    prompt.addKeyListener(this);

    add("Center", textArea);
    add("South", prompt);

    addWindowListener(this);
  }
    

  protected void initInterp() {
    interp = new MyPythonInterpreter(printStream);
  }
    
    
    
  protected void enter() {
    String s = prompt.getText();
    prompt.setText("");
    if (debug) System.out.println("->: "+s);
    textArea.append(">>>"+s+"\n");
    try { 
      interp.exec(s);
    } catch (Exception e) {
      if (debug) System.out.println("Exception: "+e);
      textArea.append("Exception: "+e);
    }
    textArea.append(printStream+"\n");
    printStream.reset();
  
    if (s.length() > 0) { 
      history.addCommand(s);
    }
  }



    public void setEditor(Editor editor) {
  if (debug) System.out.println("-> setEditor: "+editor);
  interp.set ("editor", editor);
    }


    public void updateDesign() {
  interp.exec ("updateDesign()");
    }

    
    public void keyPressed(KeyEvent e) {
  if (debug) System.out.println("keyPressed: "+e);
  int keyCode = e.getKeyCode();
  
  switch(keyCode) {
  case 38:
      //up
      if (debug) System.out.println("UP "+history.getIndex());
      prompt.setText(history.prev());
      break;
  case 40:
      //down
      if (debug) System.out.println("DOWN "+history.getIndex());
      prompt.setText(history.next());
      break;
  case 10:
      //enter
      if (debug) System.out.println("ENTER");
      enter();
      break;
  case 68:
      //crtl+d
      if (debug) System.out.println("CTRL+d");
      if (e.isControlDown()) {
    stop();
      }
      break;
  }
    }

    // add the WindowListener stuff
    public void windowDeiconified(WindowEvent e) {
  if (debug) System.out.println("windowDeiconified: "+e);
    }
    
    public void windowIconified(WindowEvent e) {
  if (debug) System.out.println("windowIconified: "+e);
    }
    
    public void windowActivated(WindowEvent e) {
  //if (debug) System.out.println("windowActivated: "+e);
  prompt.requestFocus();
    }
    
    public void windowDeactivated(WindowEvent e) {
  //if (debug) System.out.println("windowDeactivated: "+e);
    }
    
    public void windowOpened(WindowEvent e) {
  if (debug) System.out.println("windowOpened: "+e);
    }
    
    public void windowClosed(WindowEvent e) {
  if (debug) System.out.println("windowClosed: "+e);
    }
    
    public void windowClosing(WindowEvent e) {
  if (debug) System.out.println("windowClosing: "+e);
  stop();
    }


    // add the key stuff
    public void keyTyped(KeyEvent e) {
  //if (debug) System.out.println("keyTyped: "+e);
    }
        
    public void keyReleased(KeyEvent e) {
  //if (debug) System.out.println("keyReleased: "+e);
    }
    
    // add the action handle stuff
    public void actionPerformed(ActionEvent e) {
        String cmd = e.getActionCommand();
        if (debug) System.out.println("action cmd: "+cmd);
    }

    public void stop() {
  this.dispose();
    }

  public static MyPythonInterpreter getInterpreter()
  {
    return interp;
  }

    public String toString() {
  return ("Java-Python-Shell ("+version+")");

    }
}
