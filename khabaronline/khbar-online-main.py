
import schedule 
import time 
import os

  
print('Start Scheduler' )
schedule.every(30).seconds.do(lambda: os.system('scrapy crawl khabaronline -s JOBDIR=crawls/khabaronline')) 
print('Next job is set to run at: ' + str(schedule.next_run()))
  
# infinite loop to run the scheduled spider 
while True: 
    schedule.run_pending() 
    time.sleep(1) 