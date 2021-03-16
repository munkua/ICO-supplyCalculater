# projectName = input('프로젝트 명은?')
# totalSupply = int(input('총 공급량은?'))

# totalVestingList = [0 for i in range(totalVestingTermfire)]

while(1) :
    teamName = input('팀 이름은?')
    teamTotalSupply = int(input('팀 총 공급량은?'))
    teamTotalVestingTerm = int(input('팀 총 vesting 날은?'))
    teamVestingStart = int(input('팀 베스팅 시작 날짜는?'))
    teamVestingTerm = int(input('팀 베스팅 간격은?')) # 여기부터 구현 다시 시작

    teamVestingList = [0 for i in range(teamTotalVestingTerm)]
    dailyVesting = teamTotalSupply / (teamTotalVestingTerm - teamVestingStart) 
    teamVestingList[teamVestingStart] = dailyVesting

    for i in range(teamVestingStart, teamTotalVestingTerm) :
        teamVestingList[i] = teamVestingList[i-1] + dailyVesting

    for i in range(len(teamVestingList)) :
        print(i , ' = ', teamVestingList[i])