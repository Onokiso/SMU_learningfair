# 개발 방향
# 1. 카드 덱 리스트 만들기
# 2. 딜러 규칙 만들기
# 3. 승률 계산기 만들기
# 4. 게임 내 규칙 만들기

#블랙잭 규칙
#1. 베팅 금액을 정한다. 돈은 건 만큼 받는다.
#2. 딜러가 먼저 덱에서 카드를 뽑는다. 이때 딜러는 카드를 모두 공개한다. 딜러는 16이하면 히트, 17이상이면 스테이. A는 무조건 11로 계산.
#3. 플레이어도 두장을 받는다. 이때 플레이어가 할 수 있는 선택은 힛, 스테이, 더블다운이 있다.
#4.
print()
print('          _____                          ')
print('         |A .  | _____                    ')
print('         | /.＼ ||A ^  | _____             ')
print('Black    |(_._)|| / ＼||A _  | _____      ')
print('   Jack  |  |  ||＼ / || ( ) ||A_ _ |     ')
print('         |____V||  .  ||(_ _)||( v )|   ')
print('                |____V||  |  ||＼ / |     ')
print('                       |____V||  .  |       ')
print('                              |____V|       ')
print()
print()
# 1. 카드 덱 리스트 만들기
import random
Card = {'스페이드A':1, '스페이드2':2, '스페이드3':3, '스페이드4':4, '스페이드5':5, '스페이드6':6, '스페이드7':7, '스페이드8':8, '스페이드9':9, '스페이드10':10,'스페이드J':10,'스페이드Q':10,'스페이드K':10,'하트A':1,'하트2':2, '하트3':3, '하트4':4, '하트5':5, '하트6':6, '하트7':7, '하트8':8, '하트9':9, '하트10':10,'하트J':10, '하트Q':10, '하트K':10,'클로버A':1,'클로버2':2, '클로버3':3, '클로버4':4, '클로버5':5, '클로버6':6, '클로버7':7, '클로버8':8, '클로버9':9, '클로버10':10,'클로버J':10, '클로버Q':10, '클로버K':10,'다이아몬드A':1,'다이아몬드2':2, '다이아몬드3':3, '다이아몬드4':4, '다이아몬드5':5, '다이아몬드6':6, '다이아몬드7':7, '다이아몬드8':8, '다이아몬드9':9, '다이아몬드10':10,'다이아몬드J':10, '다이아몬드Q':10, '다이아몬드K':10}
Deck_List = list(Card.keys())#블랙잭 게임에 쓰일 카드 리스트

# 핸드 총합 계산
def Calculate_Score(v1, v2):
    result = v1 + v2
    return result

# 2. 게임시작메뉴
PlayerTurn = 0
DealerStart = 0
Result = 0
n = 3
print('블랙잭을 즐길 수 있는 파이썬 프로그램입니다.')
print('A를 입력하시면 게임을 시작합니다.')
print('B를 입력하시면 블랙잭 규칙을 설명합니다.')
GameStart = input('A 또는 B를 입력해주세요: ')
if GameStart == 'B':
    print('규칙설명')
    print('모든 카드의 합이 21에 가까운 사람이 이기는 게임입니다!')
    print('하지만 카드의 합이 21을 초과한다면 게임에서 패배합니다.')
    print('처음 2장의 카드를 받고 카드를 더 받을지(Hit) 멈출지(Stay)를 선택하실 수 있습니다.')
    print('딜러의 경우에는 기본적으로 제공되는 카드 2장이 16 이하면 무조건 히트, 17 이상이면 무조건 스테이합니다.')
    print('그럼 게임을 시작하겠습니다.')
    print()
    GameStart = 'A'
# 3. 플레이어 카드 뽑기
# 딜러 순서 끝나고 플레이어턴 변수 1로 만들기
if GameStart == 'A':
    print("당신은 카드를 뽑습니다.")
    print("………")
    print()
    print('              __      ')                                         
    print("        _..-''--'----_.    ")                                    
    print("      ,''.-''| .---/ _`-._         ")                            
    print("    ,' \ \  ;| | ,/ / `-._`-.         ")                         
    print("  ,' ,',\ \( | |// /,-._  / /          ")                        
    print("  ;.`. `,\ \`| |/ / |   )/ /          ")                         
    print(" / /`_`.\_\ \| /_.-.'-''/ /                                ")    
    print("/ /_|_:.`. \ |;'`..')  / /                ")                     
    print("`-._`-._`.`.;`.\  ,'  / /               ")                       
    print("    `-._`.`/    ,'-._/ /                 ")                      
    print("      : `-/     \`-.._/            ")                            
    print("      |  :      ;._ (            ")                              
    print("      :  |      \  ` \      ")                                   
    print("       \         \   |                  ")                       
    print("        :        :   ;                ")                         
    print("        |           /             ")                             
    print("        ;         ,'          ")                                 
    print("       /         /           ")                                  
    print("      /         /           ")                                   
    print("               /     ")
    print()
    print()
    Player_Hand = random.sample(Deck_List, 2)
    Deck_List = list(set(Deck_List) - set(Player_Hand)) #덱에서 뽑은 카드 빼기
    print("당신이 뽑은 카드는", Player_Hand, "입니다.")
    Player_HandSum = Calculate_Score(Card[Player_Hand[0]], Card[Player_Hand[1]])
    print("현재까지 카드의 총 합은", Player_HandSum, "입니다.")
    print()
    #이제 선택문 삽입
    print("이제 선택하실 차례입니다.")
    Player_Choice = input("Hit or Stay: ")
    Player_turn=3
    while Player_Choice == 'Hit':
        print()
        print("당신이 %d 번째 카드를 뽑습니다." %Player_turn)
        print("………")
        New_card=random.sample(Deck_List, 1)
        print("뽑은 카드는", New_card, "입니다.")
        Player_HandSum = Calculate_Score(Player_HandSum, Card[New_card[0]])
        print("현재까지 카드의 총 합은", Player_HandSum, "입니다.")
        if Player_HandSum > 21:
            print('Bust! 총합이 21을 넘었습니다. 당신은 패배하였습니다...')
            break
        else:
            Player_turn = Player_turn+1
            print("이제 선택하실 차례입니다.")
            Player_Choice = input("Hit or Stay: ")
    if Player_Choice == 'Stay':
        print('스테이 하셨습니다.')
        print()
        print('이제 딜러가 카드를 뽑습니다.')
        DealerStart = 1

        
# 4. 딜러 카드 뽑는 규칙
if DealerStart == 1:
    #덱 리스트에서 랜덤하게 두장을 뽑고 딜러규칙에 따라 카드를 더 뽑거나 스테이
    Dealer_Hand = random.sample(Deck_List, 2)
    Deck_List = list(set(Deck_List) - set(Dealer_Hand))
    print("………")
    print()
    print()                                                                      
    print()                                                                      
    print("                                 .;:;'..                        ")      
    print("                                 ;ooc,;;.                         ")    
    print("                                .lxkxoc;.                           ")  
    print("                                'oococ,;'                             ")
    print("                                 ,c;;'.'.                             ")
    print("                                .;c,...,'                             ")
    print("                            .;;;cdo:,..::;;,;'                        ")
    print("                          .cOOl,,;;;cl::,.';xx:.                      ")
    print("                         .cxkx;...cxOK0l....cxdc.                     ")
    print("                        .cxxdc'.....c0d'....;okx:.                    ")
    print("                       .ckxl,........,'......:xxdc.                   ")
    print("                  , dOkl,  .............  .:oxko'                  ")
    print("                    ,oOKOo,   ....  ....  .   .;dOK0o.               ") 
    print("                 .;cokxlc,. . .'..   ... ... ...:ok0Od:.              ")
    print("................;odl,;,.','''',,'....,,..,:'.,'''.;c::ol,.............")
    print("...............,;;,,............... .... ........':cc:;;;,'.'.........")
    print(".'''..'''...'''..'',;;''''',,,,,,,''''''''',,'''',;;::;,'..'''...'''..")
    print("''...........'''''','.....'',;::;,'''''''';::,'''....',,,,','.........")
    print("........',,,'''.........',;;,;;;,'.......',,,,,;,'........'',,,,,''...")
    print("......................',,;;;,,,,'.........,;,;;,,,,'..................")
    print("...........................''''............'''''......................")
    print()
    print()
    print("딜러가 뽑은 카드는",Dealer_Hand, "입니다.")
    Dealer_HandSum = Calculate_Score(Card[Dealer_Hand[0]], Card[Dealer_Hand[1]])
    print("딜러 카드의 총 합은", Dealer_HandSum, "입니다.")
    #여기서 딜러 논리. 16이하면 뽑고 17이상이면 스테이하는거
    while (Dealer_HandSum < 17):
        Result = 0
        print("딜러가 %d 번째 카드를 뽑습니다." %n)
        print("………")
        New_card=random.sample(Deck_List, 1)
        Dealer_Hand = Dealer_Hand + New_card
        print(New_card)
        Dealer_HandSum = Dealer_HandSum + Card[Dealer_Hand[n-1]]
        print("딜러 카드의 총 합은", Dealer_HandSum, "입니다.")
        n=n+1
        if (Dealer_HandSum > 21):
            print('딜러의 카드 합이 21을 초과했습니다')
            Result = Result + 1
    print("딜러의 차례가 끝났습니다.")
    print()
    Result = Result + 1

if Result == 1:
    if Player_HandSum > Dealer_HandSum:
        print('당신이 승리하였습니다!')
    elif Player_HandSum == Dealer_HandSum:
        print('비겼습니다.')
    elif Player_HandSum < Dealer_HandSum:
        print('당신은 패배하셨습니다...')

if Result == 2:
    print('Bust! 당신이 승리하였습니다!')
        

# 5. 카드값 비교후 승패 결정
#브레이크 구문으로 플레이어 턴 끝내면 딜러랑 카드 비교해서 높은 쪽이 승리
#if구문 사용하면 될것같음
