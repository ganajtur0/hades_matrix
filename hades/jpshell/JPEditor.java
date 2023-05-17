package hades.jpshell;

//import hades.gui.Editor;

public class JPEditor extends hades.gui.Editor {

    public JPEditor() {
   	super();	
    }
    
    public static void main( String argv[] ) {
	JPEditor edi = new JPEditor();
	JPShell jpshell = new JPShell(edi);
        jpshell.setVisible( true );
    }
} 


