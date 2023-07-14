def getMinRooms(meetingTimings):
    # Write your code here
    events = []
    for i in meetingTimings:
        a=i[0]; b=i[1]
        events.append([a,1])
        events.append([b,-1])
    events.sort()
    count = 0
    max_count = 0
    for x,e in events:
        count+=e
        max_count=max(max_count, count)
    return max_count

print(getMinRooms([[1,4],[1,5],[5,6],[6,10],[7,9]]))