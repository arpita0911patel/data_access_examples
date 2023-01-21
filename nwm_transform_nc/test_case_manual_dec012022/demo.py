import netCDF4
import os
from os.path import basename
import sys

input_file = "nwm.t16z.analysis_assim_extend_no_da.channel_rt.tm02.conus.nc"
if not os.path.isfile(input_file):
        raise ValueError('Input file %s does not exist' % input_file)

print(type(input_file))
data_set = netCDF4.Dataset(input_file, 'r')
print(data_set)
all_variables = data_set.variables
print(all_variables)

#all_dimensions = set(input_file.dimensions)