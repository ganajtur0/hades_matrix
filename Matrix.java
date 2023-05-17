package hades.models.io;

import hades.gui.PropertySheet;
import hades.models.PortStdLogic1164;
import hades.models.StdLogic1164;
import hades.models.Const1164;
import hades.simulator.Port;
import hades.simulator.SimObject;
import hades.simulator.Simulatable;
import hades.signals.Signal;
import hades.symbols.Circle;
import hades.symbols.Symbol;
import hades.utils.StringTokenizer;
import java.io.PrintWriter;
import java.awt.Color;
import jfig.canvas.FigDrawable;
import jfig.objects.FigObject;
import jfig.objects.FigCompound;
import jfig.objects.FigAttribs;

public class Matrix extends SimObject implements Simulatable{

  protected int MATRIX_DIM = 3;
  protected int MATRIX_PORTS = 6;

  protected Circle[][] LEDs;

  protected Color medium_gray;

  protected FigCompound display;

  protected StdLogic1164 value_U;

  public Matrix() {
    // super();

    ports = new Port[MATRIX_PORTS];

    ports[0] = new PortStdLogic1164(this, "A1", Port.IN, null);
    ports[1] = new PortStdLogic1164(this, "B1", Port.IN, null);
    ports[2] = new PortStdLogic1164(this, "C1", Port.IN, null);
    ports[3] = new PortStdLogic1164(this, "A0", Port.IN, null);
    ports[4] = new PortStdLogic1164(this, "B0", Port.IN, null);
    ports[5] = new PortStdLogic1164(this, "C0", Port.IN, null);

    value_U = (StdLogic1164)Const1164.__U;

  }
  
  public void setSymbol(Symbol s) {
    symbol = s;
    symbol.setInstanceLabel(name);
    initDisplay();
  }
  
  private final void initDisplay() {

    display = new FigCompound();
    display.setTrafo(getSymbol().getTrafo());
    medium_gray = new Color(120,120,120);
    LEDs = new Circle[MATRIX_DIM][MATRIX_DIM];

    int i, j;

    for (i = 0; i<MATRIX_DIM; ++i)
        for (j = 0; j<MATRIX_DIM; ++j)
            LEDs[i][j] = new Circle();

    LEDs[0][0].initialize( "1200 1200 300 300" );
    LEDs[0][1].initialize( "1600 1200 300 300" );
    LEDs[0][2].initialize( "2000 1200 300 300" );
    LEDs[1][0].initialize( "1200 1600 300 300" );
    LEDs[1][1].initialize( "1600 1600 300 300" );
    LEDs[1][2].initialize( "2000 1600 300 300" );
    LEDs[2][0].initialize( "1200 2000 300 300" );
    LEDs[2][1].initialize( "1600 2000 300 300" );
    LEDs[2][2].initialize( "2000 2000 300 300" );

    for (i = 0; i<MATRIX_DIM; ++i){
        for (j = 0; j<MATRIX_DIM; ++j){
            FigAttribs attr = LEDs[i][j].getAttributes();
            attr.fillStyle = attr.SOLID_FILL;
            attr.fillColor = medium_gray;
            attr.currentLayer = 5;
            LEDs[i][j].setAttributes(attr);
        }
    }

    for (i = 0; i<MATRIX_DIM; ++i)
        for (j = 0; j<MATRIX_DIM; ++j)
            display.fastAddMember(LEDs[i][j]);

    Symbol symbol = getSymbol();
    display.setObjectPainter(symbol.painter);
    symbol.addMember(display);

    // showState();

  }

  private final void showState() {

    if (getSymbol() == null || !getSymbol().isVisible()) return;
    
    Signal anode_signal;
    Signal cathode_signal;

    Color color;

    for (int y = 0; y<MATRIX_DIM; ++y){
        for (int x = 0; x<MATRIX_DIM; ++x){
                
            anode_signal = ports[y].getSignal();
            cathode_signal = ports[x+3].getSignal();

            color = value_U.getColor();

            if (!(anode_signal == null || cathode_signal == null)){
                
                StdLogic1164 anode_value   = (StdLogic1164)anode_signal.getValue();
                StdLogic1164 cathode_value = (StdLogic1164)cathode_signal.getValue();

                if (cathode_value.is_0())
                    color = anode_value.getColor();

            } 

            Circle c = LEDs[y][x];

            FigAttribs attr = c.getAttributes();
            attr.fillColor = color;

            c.setAttributes(attr);
        }
    }

    if (getSymbol().painter != null)
        getSymbol().painter.paint((FigDrawable)display, 60);
  }
  
  public void elaborate(Object arg) {
      showState(); 
  }
  
  public void evaluate(Object arg) {
    if (visible)
      showState(); 
  }
  
  public String toString() {
    return "MatrixLED: " + getFullName();
  }
}

