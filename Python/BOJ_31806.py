import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    
    teams = {}
    for _ in range(N):
        l, r, c = map(int, read().split())
        if c not in teams:
            teams[c] = []
        teams[c].append((l, r))
    
    all_starts = []
    all_ends = []
    
    for c in teams:
        tasks = sorted(teams[c])
        valid_ranges = []
        
        for i in range(len(tasks) - 1):
            l1, r1 = tasks[i]
            l2, r2 = tasks[i+1]
            
            start_s = l2 - M
            end_s = r1 - 1
            
            if start_s <= end_s:
                valid_ranges.append((start_s, end_s))
        
        if not valid_ranges:
            continue
            
        valid_ranges.sort()
        merged_ranges = []
        
        curr_s, curr_e = valid_ranges[0]
        for i in range(1, len(valid_ranges)):
            next_s, next_e = valid_ranges[i]
            
            if next_s <= curr_e + 1:
                curr_e = max(curr_e, next_e)
            else:
                merged_ranges.append((curr_s, curr_e))
                curr_s, curr_e = next_s, next_e
        merged_ranges.append((curr_s, curr_e))
        
        for s, e in merged_ranges:
            all_starts.append(s)
            all_ends.append(e)
            
    all_starts.sort()
    all_ends.sort()
    
    max_count = 0
    curr_count = 0
    i, j = 0, 0
    total_intervals = len(all_starts)
    
    while i < total_intervals:
        if all_starts[i] <= all_ends[j]:
            curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
            i += 1

        else:
            curr_count -= 1
            j += 1
            
    print(max_count)


if __name__ == "__main__":
    solve()