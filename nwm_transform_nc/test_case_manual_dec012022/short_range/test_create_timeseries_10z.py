from create_timeseries import create_time_series
import time

logfile = "log_short_range_test.txt"
output_file = "nwm.t10z.short_range.channel_rt.conus.nc"
data_variables = ["streamflow"]
chunk_size = 5120
max_memory = 1e9
time_variable = "time"
reference_time_variable = "reference_time"
removed_global_attributes = ""
skip_missing = False

start_time = time.time()
print("running short_range files")
input_files_short_range = [
    "data/nwm.t10z.short_range.channel_rt.f001.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f002.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f003.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f004.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f005.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f006.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f007.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f008.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f009.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f010.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f011.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f012.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f013.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f014.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f015.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f016.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f017.conus.nc",
    "data/nwm.t10z.short_range.channel_rt.f018.conus.nc",
]

output = create_time_series(
    input_files_short_range,
    output_file,
    data_variables,
    time_variable,
    reference_time_variable,
    chunk_size,
    max_memory,
    removed_global_attributes,
    skip_missing,
)
print(time.time() - start_time)