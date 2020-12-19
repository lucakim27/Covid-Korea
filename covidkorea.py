import requests
import bs4


class covid_korea:
    def __init__(self):
        pass

    def total_cases(self):
        website = "http://ncov.mohw.go.kr/en/bdBoardList.do?brdId=16&brdGubun=162&dataGubun=&ncvContSeq=&contSeq=&board_id= "
        result = requests.get(website)
        soup = bs4.BeautifulSoup(result.text, "lxml")
        cases = soup.select('.num')

        print("Total: " + str(cases[18].text))
        print("Seoul: " + str(cases[0].text))
        print("Gyeonggi-do: " + str(cases[8].text))
        print("Incheon: " + str(cases[3].text))
        print("Sejong: " + str(cases[7].text))
        print("Gangwon-do: " + str(cases[9].text))
        print("Chungcheongbuk-do: " + str(cases[10].text))
        print("Chungcheongnam-do: " + str(cases[11].text))
        print("Daejeon: " + str(cases[5].text))
        print("Gyeongsangbuk-do: " + str(cases[14].text))
        print("Gyeongsangnam-do: " + str(cases[15].text))
        print("Busan: " + str(cases[1].text))
        print("Ulsan: " + str(cases[6].text))
        print("Daegu: " + str(cases[2].text))
        print("Jeollabuk-do: " + str(cases[12].text))
        print("Jeollanam-do: " + str(cases[13].text))
        print("Gwangju: " + str(cases[4].text))
        print("Jeju: " + str(cases[16].text))
