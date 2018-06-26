#coding=utf-8

def read_in(filename):
    """
    return a bytes object(like "rb")

    read_in(path)

    like:
    read_in(r"c:\1.txt")
    """
    result = b""

    try:
        with open(filename,'rb') as f:
            result = f.read()
    except:pass

    return result

def write_out(filename,data=b""):
    """
    write_out(path,str/bytes)

    like:
    write_out(r"c:\1.txt",data)
    """
    result = False
    
    try:
        with open(filename,"wb") as f:
            if isinstance(data,str):
                f.write(data.encode("utf-8"))
            else:
                f.write(data)

        result = True

    except Exception as e:
        pass

    return result
