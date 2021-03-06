'''
동시성을 활용한 알라딘 웹 크롤링
'''

from bs4 import BeautifulSoup
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        suop = BeautifulSoup(html, 'html.parser')
        names = suop.find_all("a", "bo3")
        for name in names:
            title = name.find("b")
            if title is not None:
                print(title.text)


async def main():
    BASE_URL = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&"
    urls = [
        # 페이지 번호에 따라 데이터를 가져오도록 작성함
        f"{BASE_URL}page={i}&Stockstatus=1&PublishDay=84&CID=3057&SearchOption=" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        # *는 리스트를 해체해 줌
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())


'''
<result>
유시민의 경제학 카페
하워드 막스 투자와 마켓 사이클의 법칙
앞으로 3년 경제전쟁의 미래
프로테스탄트 윤리와 자본주의 정신
노예의 길
변화는 어떻게 일어나는가
장하준의 경제학 강의 (반양장)
복잡계 세상에서의 투자
업스트림
인구 미래 공존
한 권으로 끝내는 코인 투자의 정석
새로운 시대의 부, 디지털 자산이 온다
모방과 창조
수험생을 위한 기초 경제수학 특강
화폐전쟁 4 : 전국시대
화폐전쟁 2 : 금권 천하
화폐전쟁 3 : 금융 하이 프런티어
100년 만의 세계경제 붕괴 위기와 리플혁명
왜 지금 교육 경제학인가
디지털 테라포밍
50대 사건으로 보는 돈의 역사
뉴 맵
최배근 대한민국 대전환 100년의 조건
블랙 스완
미시경제학
트렌드 코리아 2022
돈의 흐름에 올라타라
앞으로 100년 : 인류의 미래를 위한 100장의 지도
NFT 레볼루션
존 메이너드 케인스
돈의 속성 (150쇄 기념 에디션)
돈의 심리학
부의 인문학
사경인의 친절한 투자 과외
부의 시나리오
경매하는 직장인
경제금융용어 700선
누가 한국 경제를 파괴하는가
경제기사 궁금증 300문 300답
돈의 역사는 되풀이된다
2030 축의 전환
은행이 멈추는 날
세계미래보고서 2022 : 메타 사피엔스가 온다
42가지 사건으로 보는 투기의 세계사
돈 버는 NFT 처음부터 제대로 만들고 판매하기
금리와 환율 알고 갑시다
부동산 트렌드 2022
앞으로 10년 빅테크 수업
요즘 애들
EBS 다큐프라임 자본주의
생각하지 않는 사람들 (10주년 개정증보판)
경영학 콘서트
경제학연습 : 미시편
경제학연습 : 거시편
인플레이션
블록체인 무엇인가?
공정한 보상
코린이를 위한 코인의 모든 것
머물고 싶은 동네가 뜬다
도시의 승리
만화로 보는 맨큐의 경제학 1~7 세트 - 전7권
모르면 호구 되는 경제상식
2050 수소에너지
위기의 시대, 돈의 미래
세계미래보고서 2035-2055
안티프래질
경제학 콘서트 2
자본론 1 - 상
진보와 빈곤
돈의 감각
파이썬 증권 데이터 분석
비트코인은 강했다
자본주의와 자유
플랫폼 경제와 공짜 점심
금융시장의 포식자들
친절한 트렌드 뒷담화 2022
모든 것의 가격
투자 시프트
달러는 왜 비트코인을 싫어하는가
만화로 배우는 블록체인
블록체인 혁명 (증보판)
투자자의 인문학 서재
나쁜 사마리아인들 (10주년 특별판)
피지털 커먼즈
경제지표 정독법
한국인을 읽는다
금의 미래
미국의 사회주의 선언
공정거래법의 이론과 실제
일본전산 이야기
부의 골든타임
진보와 빈곤
부의 미래, 누가 주도할 것인가
모두 거짓말을 한다
자본주의 대전환
투자의 신세계
나의 첫 금리 공부
작은 것이 아름답다
금융시장의 기술적 분석
존 롤스 정의론
존리의 금융문맹 탈출
디지털 신세계 메타버스를 선점하라
생각에 관한 생각
위드 코로나 2022년 경제전망
넛지
비트코인, 지혜의 족보
이코노미스트 2022 세계대전망
미래의 부
살면서 한번은 경제학 공부
팬데믹 머니
반도체 제국의 미래
메타버스 새로운 기회
빅테크 미래보고서 2025
2022 트렌드 노트
부의 대이동
부자의 그릇
시장을 뒤흔든 100명의 거인들
실직 도시
2022 한국이 열광할 세계 트렌드
거대한 가속
라이프 트렌드 2022 : Better Normal Life
최진기의 경제상식 오늘부터 1일
국부론 -상
경제 상식사전
불평등한 선진국
나의 첫 금융 수업
제대로 배우는 비트코인과 블록체인
레이어드 머니 돈이 진화한다
코로노믹스
폴 크루그먼의 지리경제학
만화로 읽는 피케티의 21세기 자본
재테크는 모르지만 부자로 키우고 싶어
왜 우리는 불평등한가
주주 자본주의의 배신
부자, 관상, 기술
돈의 불장난
휴대폰 인류의 블록체인 디파이 혁명
메린이를 위한 메타버스의 모든 것
새로운 금융이 온다
자본주의
사상으로서의 근대경제학
초과 수익을 찾아서 2/e
기후위기와 비즈니스의 미래
반도체 대전 2030
돈과 인생을 움직이는 머니 머츄어리티
커넥터스
그들이 말하지 않는 23가지
내일의 부 1 : 알파편
7대 이슈로 보는 돈의 역사 2
버블 : 부의 대전환
경제학 오디세이
유한계급론
금융 오디세이
넥스트 머니
어려웠던 경제기사가 술술 읽힙니다
명쾌하고 야무진 최신 경제 용어 해설
아세안 슈퍼앱 전쟁
나는 금리로 경제를 읽는다 (리커버)
2030 극한 경제 시나리오
2020 자본시장법 강의
투자은행과 사모펀드
90년생이 온다
클라우스 슈밥의 제4차 산업혁명
유한계급론
세계 경제가 만만해지는 책
거대한 전환
바젤3 모멘트
인플레이션 이야기
축적의 시간
불평등의 대가
정해진 미래
비트코인과 블록체인, 가상자산의 실체 2/e
나는 세계 일주로 자본주의를 만났다
내러티브 경제학
현명한 투자자의 인문학
블록체인 트렌드 2022-2023
뉴미디어 트렌드 2022
자유경제 톡톡
부의 시그널
행운에 속지 마라
국부론 -하
2022 트렌드 모니터
클라우스 슈밥의 위대한 리셋
앞으로 10년 부의 거대 물결이 온다
경제학 콘서트
뉴타입의 시대
행동경제학
2022 피할 수 없는 부채 위기
외계어 없이 이해하는 암호화폐
물어보기 부끄러워 묻지 못한 금융상식
경제사상가 이건희
오늘 배워 내일 써먹는 경제상식
한국의 눈물, 한국도 일본처럼 투자할 곳이 완전히 사라진다
죽은 경제학자의 살아있는 아이디어
댄 애리얼리 부의 감각
페이크
일반인을 위한 한국은행의 알기쉬운 경제이야기
화폐전쟁 1 : 달러의 종말
주린이도 술술 읽는 친절한 경제책
파이낸셜 모델링 바이블
자본주의의 미래
애덤 스미스 국부론
디레버리징
신 대공황
스킨 인 더 게임 Skin in the Game
문 앞의 야만인들
돈의 흐름이 보이는 회계 이야기
세속의 철학자들
부의 대전환 코인전쟁
혼돈의 시대, 경제의 미래
상식 밖의 경제학
돈 좀 굴려봅시다
지금 애덤 스미스를 다시 읽는다
자본주의 어디서 와서 어디로 가는가
한 번 보고 바로 써먹는 경제용어 460
화폐혁명
돈의 감정
금리의 역사
일차원적 인간
일러스트로 바로 이해하는 가장 쉬운 행동경제학
세계경제사
혁신의 시작
도덕경제학
담대한 전환 대한민국 산업미래전략 2030
좋은 기업 나쁜 주식 이상한 대주주
'''
