# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2015 Government of Canada
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

# TotalOzone example 1
# Create a totalozone extcsv object and write it to file
# Using data from: http://woudc.org/archive/Archive-NewFormat/TotalOzone_1.0_1/stn031/dobson/2014/20140401.Dobson.Beck.076.NOAA-CMDL.csv

import os
import logging
from collections import OrderedDict
import woudc_extcsv


# setup logging
datetime_format = '%a, %d %b %Y %H:%M:%S'
msg_format = '[%(asctime)s] [%(levelname)s] [%(message)s]'
logging.basicConfig(filename='totalozone-example1.log',
                    format=msg_format,
                    datefmt=datetime_format,
                    level=logging.DEBUG)

LOGGER = logging.getLogger(__name__)

# new extcsv object
extcsv = woudc_extcsv.Writer(template=True)
extcsv.filename = 'totalozone-extcsv-example1.csv'

# add data here
extcsv.add_comment('This file was generated by WODC_TO_CSX v1.0 using WODC 80-column formatted data.')
extcsv.add_comment('\'na\' is used where Instrument Model or Number are not available.')
extcsv.add_data('CONTENT','WOUDC,TotalOzone,1.0,1')
extcsv.add_data('DATA_GENERATION','2014-08-28,NOAA-CMDL,0.0')
extcsv.add_data('PLATFORM','STN,031,MAUNA LOA,USA')
extcsv.add_data('INSTRUMENT','Dobson,Beck,076')
extcsv.add_data('LOCATION','19.533,-155.574,3405')
extcsv.add_data('TIMESTAMP','+00:00:00,2014-04-01')
extcsv.add_data('DAILY','2014-04-01,0,2,283,,,,18', field='Date,WLCode,ObsCode,ColumnO3,StdDevO3,UTC_Begin,UTC_End,UTC_Mean,nObs,mMu,ColumnSO2')
extcsv.add_data('DAILY','2014-04-08,0,0,288,,,,23')
extcsv.add_data('DAILY','2014-04-09,0,0,279,,,,23')
extcsv.add_data('DAILY','2014-04-10,0,0,273,,,,24')
extcsv.add_data('DAILY','2014-04-11,0,0,274,,,,21')
extcsv.add_data('DAILY','2014-04-12,0,2,271,,,,18')
extcsv.add_data('DAILY','2014-04-13,0,2,274,,,,18')
extcsv.add_data('DAILY','2014-04-14,0,0,283,,,,23')
extcsv.add_data('DAILY','2014-04-15,0,0,285,,,,23')
extcsv.add_data('DAILY','2014-04-16,0,0,284,,,,23')
extcsv.add_data('DAILY','2014-04-17,0,0,280,,,,22')
extcsv.add_data('DAILY','2014-04-18,0,2,268,,,,18')
extcsv.add_data('DAILY','2014-04-19,0,2,271,,,,18')
extcsv.add_data('DAILY','2014-04-20,0,2,264,,,,18')
extcsv.add_data('DAILY','2014-04-21,0,0,278,,,,23')
extcsv.add_data('DAILY','2014-04-22,0,0,276,,,,21')
extcsv.add_data('DAILY','2014-04-23,0,0,280,,,,23')
extcsv.add_data('DAILY','2014-04-24,0,0,269,,,,22')
extcsv.add_data('DAILY','2014-04-25,0,0,275,,,,21')
extcsv.add_data('DAILY','2014-04-26,0,2,278,,,,18')
extcsv.add_data('DAILY','2014-04-28,0,0,296,,,,21')
extcsv.add_data('DAILY','2014-04-29,0,0,291,,,,23')
extcsv.add_data('DAILY','2014-04-30,0,0,294,,,,21', table_comment='    1992 Coefficients in use')
extcsv.add_data('TIMESTAMP','+00:00:00,2014-04-30', field='UTCOffset,Date,Time', index=2)
extcsv.add_data('MONTHLY','2014-04-01,279,8.3,23', field='Date,ColumnO3,StdDevO3,Npts')

# write out file to disk
woudc_extcsv.dump(extcsv)

