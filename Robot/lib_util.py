#!/usr/bin/python

# Library: utilities

from inspect import stack
from os import path

# debug and trace modes
debug = 0
trace = 0
tr_output = 0  # 0=screen, 1=file
tr_file = '/tmp/util.traces'
f_output = 0

# Set debug mode
def setDebug(m):
    debug = 1 if m else 0

# Get debug mode
def getDebug():
    return debug

# Set trace mode
def setTrace(t):
    trace = 1 if t else 0
		
# Get trace mode
def getTrace():
    return trace

# Set trace output
def setTraceOutput(t):
    tr_output = 1 if t else 0
    if tr_output == 1:
        f_output = open(tr_file, 'a')
    else:
        closeOutput()

# close trace output file
def closeOutput():
    if tr_output == 1:
        f_output.close()

# Get trace output
def getTraceOutput():
    return tr_output

# Returns the source file with the line number
def callingSource(s):
    return "{0:<30s}".format( path.basename(s[1]) + ":{0:5d}".format(s[2]) )

# Display calling function if trace mode is active
def traceCall():
    if trace:
#        for n in range(len(stack())):
#            for e in range(len(stack()[n])):
#                print "niveau {}: elem {}: {}".format( n, e, stack()[n][e] )
        trace( "{0:<30s} {1:<25s}".format( callingSource(stack()[1]), stack()[1][3] ), )
        if len(stack()) > 2:
            trace( "called by {0:<50s} at {1:<20s}".format( stack()[2][4][0].strip(), callingSource(stack()[2]) ), )
        trace("")

#        if n+1 < len(stack()):
#            print "{}: Function '{}' at line {}".format( stack()[n][1], stack()[n+1][4][0].strip(), stack()[n][2] )
#        else:
#            print "{}: at line {}".format( stack()[n][1], stack()[n][2] )
        # test_inspect.py: Function 'foo(val)' at line 12
        #print "{}: Function '{}' called by '{}' at line {}".format( stack()[n][1], stack()[n][4][0].strip(), stack()[n+1][4][0].strip(), stack()[n+1][2] )
        # test_inspect.py: Function 'foo(val)' called by 'essai(7)' at line 12

# Display message if trace mode is active
def trace(t):
    if trace:
        line = "{0:<30s} {1}".format( callingSource(stack()[1]), t )
        if tr_output == 1:
            #fo.write(strftime('%Y%m%d%H%M%S', localtime()) + ',' + str(t) + '\n')
            fo.write(line)

        else:
            print(line)

