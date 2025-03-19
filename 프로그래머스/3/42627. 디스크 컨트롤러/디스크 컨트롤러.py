import heapq

def solution(jobs):
    now = 0 # 현재 시각
    last_start = -1 # 마지막 완료 시각
    
    finished_job_count = 0
    finished_job_return_time = 0
    
    hq = []
    
    while finished_job_count < len(jobs):

        for job_index in range(len(jobs)):
            # 넣을 때가 되었는지 확인
            job=jobs[job_index]
            job_s = job[0]; job_l = job[1]
            if last_start < job_s <= now :
                heapq.heappush(hq,[job_l,job_s,job_index])
                
        # print(now,hq,finished_job_return_time)
        
        if hq: # 처리할 게 있다면 처리한다.
            during_time, start_time, job_index = heapq.heappop(hq)
            last_start = now
            now += during_time # 작업 모두 완료한 후
            finished_job_return_time += now - start_time # 작업 완료 시점 - 작업 요구 시점
            finished_job_count+=1

        else:
            now+=1
    
    return finished_job_return_time//len(jobs)