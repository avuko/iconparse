# iconparse
Simple python tool to parse icon files

`iconparse.py` takes two positional arguments: first an .ICO file and possibly a second argument to trigger the `dump` function (can be any string).

Sample output:

```bash
./iconparse.py visualstudio/win.vs2013/app.ico 
{'name': 'idReserved', 'offset': 0, 'size': 4, 'result': 0}
{'name': 'idType', 'offset': 4, 'size': 4, 'result': 1}
{'name': 'idCount', 'offset': 8, 'size': 4, 'result': 8}
{1: [{'name': 'bWidth', 'offset': 0, 'size': 2, 'result': 32},
{'name': 'bHeight', 'offset': 2, 'size': 2, 'result': 32},
{'name': 'bColorCount', 'offset': 4, 'size': 2, 'result': 0},
{'name': 'bReserved', 'offset': 6, 'size': 2, 'result': 16},
{'name': 'wPlanes', 'offset': 8, 'size': 4, 'result': 0},
{'name': 'wBitCount', 'offset': 12, 'size': 4, 'result': 0},
{'name': 'dwBytesInRes', 'offset': 16, 'size': 8, 'result': 744},
{'name': 'dwImageOffset', 'offset': 24, 'size': 8, 'result': 134}]}
[...snip...]
```

```bash
./iconparse.py visualstudio/win.vs2013/app.ico dump
{'name': 'idReserved', 'offset': 0, 'size': 4, 'result': 0}
{'name': 'idType', 'offset': 4, 'size': 4, 'result': 1}
{'name': 'idCount', 'offset': 8, 'size': 4, 'result': 8}
{1: [{'name': 'bWidth', 'offset': 0, 'size': 2, 'result': 32},
{'name': 'bHeight', 'offset': 2, 'size': 2, 'result': 32},
{'name': 'bColorCount', 'offset': 4, 'size': 2, 'result': 0},
{'name': 'bReserved', 'offset': 6, 'size': 2, 'result': 16},
{'name': 'wPlanes', 'offset': 8, 'size': 4, 'result': 0},
{'name': 'wBitCount', 'offset': 12, 'size': 4, 'result': 0},
{'name': 'dwBytesInRes', 'offset': 16, 'size': 8, 'result': 744},
{'name': 'dwImageOffset', 'offset': 24, 'size': 8, 'result': 134}],
'dumpdata': b'280000002000000040000000010004000000000000000000000000000000000000
000000000000000000000000008000008000000080800080000000800080008080000080808000c0
c0c0000000ff0000ff000000ffff00ff000000ff00ff00ffff0000ffffff00aaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaa000000000000000000000000000000007777777777777777777777777777777078
888888888888888888888888888870787ffffffffffffffffffffffffff870787fffffffffffffff
fffffffffff870787ffffffffffffffffffffffffff870787ffffffffffffffffffffffffff87078
7ffffffffffffffffffffffffff870787ffffffffffffffffffffffffff870787fffffffffffffff
fffffffffff870787ffffffffffffffffffffffffff870787ffffffffffffffffffffffffff87078
7ffffffffffffffffffffffffff870787ffffffffffffffffffffffffff870787fffffffffffffff
fffffffffff870787ffffffffffffffffffffffffff870787ffffffffffffffffffffffffff87078
7ffffffffffffffffffffffffff870787ffffffffffffffffffffffffff870787fffffffffffffff
fffffffffff870787ffffffffffffffffffffffffff8707877777777777777777777777777787078
88888888888888888888888888887078444444444444444444400000000070784444444444444444
44488088088070784444444444444444444880880880707844444444444444444444444444447078
88888888888888888888888888887077777777777777777777777777777770aaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000'}
[...snip...]
```
