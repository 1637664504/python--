import struct

def bytes_to_int32(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<i",var)[0]
    else:
        ret = struct.unpack(">i",var)[0]
    return ret

def bytes_to_uint32(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<I",var)[0]
    else:
        ret = struct.unpack(">I",var)[0]
    return ret

def bytes_to_int64(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<q",var)[0]
    else:
        ret = struct.unpack(">q",var)[0]
    return ret

def bytes_to_uint64(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<Q",var)[0]
    else:
        ret = struct.unpack(">Q",var)[0]
    return ret

def bytes_to_int16(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<h",var)[0]
    else:
        ret = struct.unpack(">h",var)[0]
    return ret

def bytes_to_uint16(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<H",var)[0]
    else:
        ret = struct.unpack(">H",var)[0]
    return ret

def bytes_to_int8(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<b",var)[0]
    else:
        ret = struct.unpack(">b",var)[0]
    return ret

def bytes_to_uint8(var,little_end=True)->int:
    if little_end:
        ret = struct.unpack("<B",var)[0]
    else:
        ret = struct.unpack(">B",var)[0]
    return ret

def bytes_to_float32(var,little_end=True)->float:
    if little_end:
        ret = struct.unpack("<f",var)[0]
    else:
        ret = struct.unpack(">f",var)[0]
    return ret

def bytes_to_float64(var,little_end=True)->float:
    if little_end:
        ret = struct.unpack("<d",var)[0]
    else:
        ret = struct.unpack(">d",var)[0]
    return ret
