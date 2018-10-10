#!/usr/bin/env python3
import binascii
import sys
import array

# Simple tool to analyse .ico files

# bit = 1, byte = 8, WORD = 16bits, DWORD = 32bits
# 2 hex chars = 1 byte, 8 bits
BYTE = 2
WORD = 4
DWORD = 8

# ICONDIR
# I'll define values as (length in hex chars, default value, name)

# WORD: Reserved (must be 0)
idReserved = {'size': WORD, 'offset': 0, 'name': 'idReserved'}

# WORD: Resource Type (1 for icons)
idType = {'size': WORD, 'offset': 4, 'name': 'idType'}

# WORD: How many images?
idCount = {'size': WORD, 'offset': 8, 'name': 'idCount'}

# ICONDIRENTRY: image entries (idCount #)
idEntrySize = (BYTE * 4) + (WORD * 2) + (DWORD * 2)
idEntries = {'size': idEntrySize, 'offset': 12, 'name': 'idEntries'}

# ICONDIRENTRY https://en.wikipedia.org/wiki/ICO_(file_format)
# https://msdn.microsoft.com/en-us/library/ms997538.aspx
# Width, in pixels, of the image
bWidth = {'size': BYTE, 'offset': 0, 'name': 'bWidth'}
# Height, in pixels, of the image
bHeight = {'size': BYTE, 'offset': 2, 'name': 'bHeight'}
# Number of colors in image (0 if >=8bpp)
bColorCount = {'size': BYTE, 'offset': 4, 'name': 'bColorCount'}
# Reserved ( must be 0)
bReserved = {'size': BYTE, 'offset': 6, 'name': 'bReserved'}
# Color Planes
wPlanes = {'size': WORD, 'offset': 8, 'name': 'wPlanes'}
# Bits per pixel
wBitCount = {'size': WORD, 'offset': 12, 'name': 'wBitCount'}
# How many bytes in this resource?
dwBytesInRes = {'size': DWORD, 'offset': 16, 'name': 'dwBytesInRes'}
# Where in the file is this image?
dwImageOffset = {'size': DWORD, 'offset': 24, 'name': 'dwImageOffset'}

try:
    binary = sys.argv[1]
except IndexError as e:
    print("please give me a file to work with")
    exit(1)

try:
    if sys.argv[2]:
        DUMP = True
except IndexError as e:
    DUMP = False


def dword(hexdword):
    hexdword = hexdword[4:8] + hexdword[0:4]
    return(hexdword)


def parsevalues(valueinfo, hexbinary):
    name = valueinfo['name']
    offset = valueinfo['offset']
    size = valueinfo['size']
    slicesize = offset + size
    result = hexbinary[offset:slicesize]
    # if it is not a DWORD (or smaller), it is likely not an int.
    if len(result) > DWORD:
        result = result
    else:
        if size == DWORD:
            result = dword(result)
        result = int(result, 16)

    return {'name': name, 'offset': offset, 'size': size, 'result': result}


def parseidentry(hexidentry):
    parsedvalues = []
    for value in [bWidth, bHeight, bColorCount, bReserved, wPlanes,
                  wBitCount, dwBytesInRes, dwImageOffset]:
            parsedvalues.append(parsevalues(value, hexidentry))
    return parsedvalues


with open(binary, 'rb') as binaryin:
    """read, byteswap (from little endian because windows) and hexlify"""
    BI = array.array('h', binaryin.read())
    BI.byteswap()
    hexbinary = binascii.hexlify(BI)
    for values in idReserved, idType, idCount:
        parsedvalues = parsevalues(values, hexbinary)
        print(parsedvalues)

    idCountinfo = parsevalues(idCount, hexbinary)
    idCounts = idCountinfo['result']
    for idCount in range(1, idCounts + 1):
        dumpdata = None
        idEntry = parsevalues(idEntries, hexbinary)
        parsedidentry = parseidentry(idEntry['result'])
        # lets dump contents of the separate ico files
        for idinfo in parsedidentry:
            if idinfo['name'] is 'dwBytesInRes':
                IDdwBytesInRes = idinfo['result']
            elif idinfo['name'] is 'dwImageOffset':
                IDdwImageOffset = idinfo['result']
        if DUMP:
            with open(binary, 'rb') as binaryin:
                binaryin.seek(IDdwImageOffset)
                idbinary = binaryin.read(int(IDdwBytesInRes))
                dumpdata = binascii.hexlify(idbinary)
        # ugly hack to make output easier to parse
        if dumpdata:
            print({idCount: parsedidentry, 'dumpdata': dumpdata})
        else:
            print({idCount: parsedidentry})

        # add 32 chars to offset because of the icondirentry size
        idEntries['offset'] = (idEntries['offset'] + 32)
