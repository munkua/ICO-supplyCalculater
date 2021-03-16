# projectName = input('프로젝트 명은?')
# totalSupply = int(input('총 공급량은?'))
# totalVestingTerm = int(input('총 vesting 날은?'))

# totalVestingList = [0 for i in range(totalVestingTermfire)]

while(1) :
    # 필수 내용
    # 총공급량, 총 vesting 날, TGE 당시 물량, 베스팅 시작하는 날, 베스팅 간격
    # 
    teamWho = input('vesting 대상은?')
    teamVestingDay = int(input('vetsing 날은?'))

    teamTGESupply = int(input('TGE 당시 공급량은?'))

    teamVestingDay = int(input('TGE 이후 vesting 날은?'))
    
    teamVestingStart = int(input('TGE 후 언제부터 VESTING 시작하나요?'))
    teamVestingTerm = int(input('팀 베스팅 간격은?'))

    teamTotalVestingList = [0 for i in range(teamTotalVestingDay)]
    teamVestingList = [0 for i in range(teamVestingDay)]

    supplyWithoutTGE = teamTotalSupply - teamTGESupply # tge 제외한 물량
    termVestingAmount = supplyWithoutTGE / (teamVestingDay // teamVestingTerm) # tge 제외한 리스트에 들어갈 물량들

    for i in range(0, len(teamVestingList), teamVestingTerm):
        teamVestingList[i] = termVestingAmount

    print(teamTotalVestingList)