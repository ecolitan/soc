#!/bin/bash

python -m trace --trace --ignore-module=socket,SocketServer,threading,sre_compile,sre_parse,encoder,decoder,re,os,__init__,struct,scanner,hex_codec,codecs,functools gameserver.py
