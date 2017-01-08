#SRTF
number_of_Processes=0
arival_time=[]
burst_time=[]
x=[]
count=0
time=0
n=0
avg=0
end=0
turndaround_time=0
print "enter the number of Processes range of 1 to 10:\n"
number_of_Processes=input()
print "enter arrival time\n"
for index in range(number_of_Processes):
    arival_time.append(input())
print "enter burst time\n"
for index in range(number_of_Processes):
    burst_time.append(input())
for index in range(number_of_Processes):
    x.append(burst_time[index])
    burst_time[9]=9999;
while count!=number_of_Processe:
     smallest=9
     for index in range(number_of_Processes):
         if arival_time[index]<time and burst_time[index]<burst_time[smallest] and burst_time[index]>0:
              smallest=index
         
      burst_time[ smallest]-
      if burst_time[smallest]=0:
          count++
          end=time+1
          avg=avg+end-arival_time[smallest]-x[smallest]
          turndaround_timet=turndaround_timetend-arival_time[smallest]
    time++

print "\n\nAverage waiting time ",avg/number_of_Processes
    printf("Average Turnaround time",turndaround_time/number_of_Processes
 
 

    
    
 
