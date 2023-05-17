package hades.jpshell;

import java.util.*;

//!!! noch nicht 1.2 !!!! //

public class History extends Vector {

    protected int historyIndex;
    
    public History() {
	super();
	historyIndex = size();
    }

    public void addCommand(Object o) {
	addElement(o);
	historyIndex=size();
    }

    public String prev() {
	String s;
	if (historyIndex > 0 && !isEmpty()) {
	    historyIndex--;
	    s = (String) elementAt(historyIndex);
	} else if (historyIndex == 0 && !isEmpty()) {
	    s = (String) firstElement();
	} else {
	    s = "";
	}
	return s;
    }

    public String next() {
	String s;
	if (historyIndex < size()-1 && !isEmpty()) {
	    historyIndex++;	    
	    s = (String) elementAt(historyIndex);
	} else {
	    historyIndex = size();
	    s = "";
	}
	return s;
    }

    public int getIndex() {
	return historyIndex;
    }

}
