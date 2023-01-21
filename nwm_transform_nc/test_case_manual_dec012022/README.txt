1. Download nc files:

  Go to national-water-model data URL: https://console.cloud.google.com/storage/browser/national-water-model/nwm.20221201/medium_range_mem1
  
  Filter to select only channel_rt files and click on download

  Copy the command and run on the terminal to download the files.


For eg: To download all mem1-mem7, no_da Medium_range channel_rt files:
$ gsutil -m cp -r   "gs://national-water-model/nwm.20221201/medium_range_mem1/*channel*"   "gs://national-water-model/nwm.20221201/medium_range_mem2/*channel"   "gs://national-water-model/nwm.20221201/medium_range_mem3/*channel*"   "gs://national-water-model/nwm.20221201/medium_range_mem4/*channel"   "gs://national-water-model/nwm.20221201/medium_range_mem5/*channel"   "gs://national-water-model/nwm.20221201/medium_range_mem6/*channel"   "gs://national-water-model/nwm.20221201/medium_range_mem7/*channel"   "gs://national-water-model/nwm.20221201/medium_range_no_da"   .


2. Copy mem1 files only to the data folder. 

3. Run the script for Medium_range mem1 - four forecasts (00z,06z,12z,18z) in separate terminals:

$ cd medium_range_mem1		
$ python test_create_timeseries_00z.py 
$ python test_create_timeseries_06z.py 
$ python test_create_timeseries_12z.py 
$ python test_create_timeseries_18z.py 

Repeat Step 2, 3 for mem2-mem7 and no_da. Cleanup the data folder and replace the files with mem2 for mem2 run, mem3 for mem3 run.


For short_range : run the below scripts in seperate terminal
$ cd short_range



-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_00z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_01z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_02z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_03z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_04z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_05z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_06z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_07z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_08z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_09z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_10z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_11z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 14:54 test_create_timeseries_12z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_13z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_14z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_15z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_16z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_17z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_18z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_19z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_20z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_21z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_22z.py
-rw-r--r-- 1 jovyan jovyan  1734 Jan  9 15:05 test_create_timeseries_23z.py

4. Upload the output files to GCP using gsutil:

(notebook) jovyan@jupyter-arpita0911patel:~/Arpita/nwm_transform_nc/medium_range_mem7$ gsutil cp nwm.t20221201* gs://awi-ciroh-persistent/nwm_transform_nc/medium_range/channel_rt



#Short_range:
#(notebook) jovyan@jupyter-arpita0911patel:~/Arpita/nwm_transform_nc$ python create_timeseries.py -l log.txt -d streamflow data/short_range/*
