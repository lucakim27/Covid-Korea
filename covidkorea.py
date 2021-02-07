import requests
import bs4

class covid_korea:
    def __init__(self):
        
        website = "http://ncov.mohw.go.kr/en/bdBoardList.do?brdId=16&brdGubun=162&dataGubun=&ncvContSeq=&contSeq=&board_id= "
        result = requests.get(website)
        soup = bs4.BeautifulSoup(result.text, "lxml")
        cases1 = soup.select('.num')
        cases2 = soup.select('.number')

        print("Left: Total, Right: Daily")
        print("Source: http://ncov.mohw.go.kr/en")

        print("Total: " + str(cases1[18].text) + "(" + str(cases2[0].text) + ")")
        print("Seoul: " + str(cases1[0].text) + " (" + str(cases2[8].text) + ")")
        print("Gyeonggi-do: " + str(cases1[8].text) + " (" + str(cases2[72].text) + ")")
        print("Incheon: " + str(cases1[3].text) + " (" + str(cases2[32].text) + ")")
        print("Sejong: " + str(cases1[7].text) + " (" + str(cases2[64].text) + ")")
        print("Gangwon-do: " + str(cases1[9].text) + " (" + str(cases2[80].text) + ")")
        print("Chungcheongbuk-do: " + str(cases1[10].text) + " (" + str(cases2[88].text) + ")")
        print("Chungcheongnam-do: " + str(cases1[11].text) + " (" + str(cases2[2].text) + ")")
        print("Daejeon: " + str(cases1[5].text) + " (" + str(cases2[48].text) + ")")
        print("Gyeongsangbuk-do: " + str(cases1[14].text) + " (" + str(cases2[120].text) + ")")
        print("Gyeongsangnam-do: " + str(cases1[15].text) + " (" + str(cases2[128].text) + ")")
        print("Busan: " + str(cases1[1].text) + " (" + str(cases2[16].text) + ")")
        print("Ulsan: " + str(cases1[6].text) + " (" + str(cases2[56].text) + ")")
        print("Daegu: " + str(cases1[2].text) + " (" + str(cases2[24].text) + ")")
        print("Jeollabuk-do: " + str(cases1[12].text) + " (" + str(cases2[104].text) + ")")
        print("Jeollanam-do: " + str(cases1[13].text) + " (" + str(cases2[112].text) + ")")
        print("Gwangju: " + str(cases1[4].text) + " (" + str(cases2[40].text) + ")")
        print("Jeju: " + str(cases1[16].text) + " (" + str(cases2[96].text) + ")")
