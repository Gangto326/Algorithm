import sys

read = sys.stdin.read().split()
iterator = iter(read)

N, M = int(next(iterator)), int(next(iterator))

check_list = [False for _ in range(N+1)]
person_count = int(next(iterator))

for i in range(person_count):
    check_list[int(next(iterator))] = True

party_group = [set() for _ in range(N+1)]
parties = []


def DFS(node):
    for person in party_group[node]:
        if not check_list[person]:
            check_list[person] = True
            DFS(person)


for _ in range(M):
    count = int(next(iterator))
    party_people = [int(next(iterator)) for _ in range(count)]
    parties.append(party_people)

    for i in range(count):
        for j in range(count):
            if i != j:
                party_group[party_people[i]].add(party_people[j])

for i in range(1, N+1):
    if check_list[i]:
        DFS(i)

answer = sum(all(not check_list[p] for p in party) for party in parties)
print(answer)