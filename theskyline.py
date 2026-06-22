import heapq

def getSkyline(buildings):
    # Collect all events: (x_coordinate, type, height)
    # Start event has negative height, end event has positive height
    events = []
    for left, right, height in buildings:
        events.append((left, -height, right))
        events.append((right, height, 0))
    
    # Sort events. If x matches, process start (negative height) before end.
    events.sort(key=lambda x: (x[0], x[1]))
    
    # Priority Queue to store heights. We use negative for max-heap behavior.
    # Initialize with 0 height (the ground) to handle gaps.
    pq = [0]
    
    # Map to lazy-delete heights that are no longer active
    delayed_removals = {}
    
    # Tracks the current max height
    prev_max_height = 0
    result = []
    
    for x, neg_h, right in events:
        if neg_h < 0:
            # Start of a building
            height = -neg_h
            heapq.heappush(pq, -height)
        else:
            # End of a building
            delayed_removals[right] = delayed_removals.get(right, 0) + 1
            
        # Clean up the max heap: remove heights that have expired
        while pq and pq[0] in delayed_removals and delayed_removals[pq[0]] > 0:
            delayed_removals[pq[0]] -= 1
            if delayed_removals[pq[0]] == 0:
                del delayed_removals[pq[0]]
            heapq.heappop(pq)
            
        # Get the current maximum height
        current_max_height = -pq[0]
        
        # If the max height changes, record this as a critical point
        if current_max_height != prev_max_height:
            result.append([x, current_max_height])
            prev_max_height = current_max_height
            
    return result

# Example Usage:
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(getSkyline(buildings))
