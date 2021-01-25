#!/bin/bash
: '
if running the specified python program gives any
type of error, then that error will be redirected from the error stream (stderr)
to the output stream (stdout),
where the ERROR variable will store the value from the output stream
'
ERROR=$(${1} ${2} ${@:3} 2>&1 > /dev/null)

: '
if ERROR is empty (meaning there was nothing to store from the output stream),
then that means no error was detected; the script will exit
'
if [ -z "$ERROR" ]; then
    echo $(${1} ${2} ${@:3})
    exit 1
fi

python3 errorMessageSearch.py $ERROR 



