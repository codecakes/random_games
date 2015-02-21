"""
Filenames is a list of MTA Subway turnstile text files. A link to an example
MTA Subway turnstile text file can be seen at the URL below:
http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

As you can see, there are numerous data points included in each row of the
a MTA Subway turnstile text file.

You want to write a function that will update each row in the text
file so there is only one entry per row. A few examples below:
A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

Write the updates to a different text file in the format of "updated_" + filename.
For example:
    1) if you read in a text file called "turnstile_110521.txt"
    2) you should write the updated data to "updated_turnstile_110521.txt"

The order of the fields should be preserved. Remember to read through the
Instructor Notes below for more details on the task.

In addition, here is a CSV reader/writer introductory tutorial:
http://goo.gl/HBbvyy

You can see a sample of the turnstile text file that's passed into this function
and the the corresponding updated file in the links below:

Sample input file:
https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
Sample updated file:
https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
"""

from cStringIO import StringIO
import csv

def munge_turnstile_file(fname):
    #one way of wrangling these txt files
    dump_str = ''
    with open(fname) as f:
        mta = f.readlines()

    for line in mta:
        sects=line.strip('\n').strip().split(',')
        prefix = sects[:3]
        suffix = sects[3:]
        dump_str += '\n'.join([', '.join(prefix + suffix[0+i:5+i]) \
        for i in xrange(0,len(suffix), 5)])
        dump_str += '\n'

    with open('updated_' + fname, 'wb+') as fw:
        fw.write(dump_str)

def txt2csv_turnstile_file(fname):
    #using csv to wrangle these files
    dump_str = ''
    rdio = StringIO(open(fname).read())
    mta=csv.reader(rdio, delimiter=',')

    for line_list in mta:
        line_list[-1] = line_list[-1].strip()
        prefix = line_list[:3]
        suffix = line_list[3:]
        dump_str += '\n'.join([', '.join(prefix + suffix[0+i:5+i]) \
        for i in xrange(0,len(suffix), 5)])
        dump_str += '\n'

    with open('updated_' + fname, 'wb+') as fw:
        fw.write(dump_str)

def fix_turnstile_data(filenames):
    #main file
    for name in filenames:
        #munge_turnstile_file(name)
        txt2csv_turnstile_file(name)


########### MOREPUNISHMENT BELOW #####################

def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file.

    For example, if file_1 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...

    and another file, file_2 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 3 ...
    line 4 ...
    line 5 ...

    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
    with open(output_file, 'w') as master_file:
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       for filename in filenames:
                # your code here
                with open(filename) as rd:
                    iter_rd = rd.xreadlines()
                    iter_rd.next() #ignore first line assuming header
                    for line in iter_rd:
                        master_file.write(line)
                        master_file.write('\n')
