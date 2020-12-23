import requests
import bs4


class covid_korea:
    def __init__(self):
        pass

    def total_cases(self):
        print("total_cases")
        
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
        
    def new_daily_cases(self):
        print("new_daily_cases")

        website = "http://ncov.mohw.go.kr/en/bdBoardList.do?brdId=16&brdGubun=162&dataGubun=&ncvContSeq=&contSeq=&board_id= "
        result = requests.get(website)
        soup = bs4.BeautifulSoup(result.text, "lxml")
        cases = soup.select('.number')

        print("Total: " + str(cases[0].text))
        print("Seoul: " + str(cases[8].text))
        print("Gyeonggi-do: " + str(cases[72].text))
        print("Incheon: " + str(cases[32].text))
        print("Sejong: " + str(cases[64].text))
        print("Gangwon-do: " + str(cases[80].text))
        print("Chungcheongbuk-do: " + str(cases[88].text))
        print("Chungcheongnam-do: " + str(cases[2].text))
        print("Daejeon: " + str(cases[48].text))
        print("Gyeongsangbuk-do: " + str(cases[120].text))
        print("Gyeongsangnam-do: " + str(cases[128].text))
        print("Busan: " + str(cases[16].text))
        print("Ulsan: " + str(cases[56].text))
        print("Daegu: " + str(cases[24].text))
        print("Jeollabuk-do: " + str(cases[104].text))
        print("Jeollanam-do: " + str(cases[112].text))
        print("Gwangju: " + str(cases[40].text))
        print("Jeju: " + str(cases[96].text))
        
    def gwangju_travel_path(self):
        print("gwangju_travel_path")

        website = "https://www.gwangju.go.kr/c19/guRoutePrvntList.do"
        result = requests.get(website)
        soup = bs4.BeautifulSoup(result.text, "lxml")
        cases = soup.select(".tb_default")
   
        def remove(string):
            return "".join(string.split())
   
        a=0
   
        for i in cases[0]:
            if a == 7:
                print(i.text)
            a += 1

            
    def gwangju_prevention_area(self):
           print("gwangju_prevention_area")
   
           website = "https://www.gwangju.go.kr/c19/routPrevention.
           result = requests.get(website)
           soup = bs4.BeautifulSoup(result.text, "lxml")
           cases = soup.select(".tb_default")
 
           a=0
   
           today = date.today()
           d = today.strftime("%m-%d")
 
           def remove(string):
               return "".join(string.split())
   
           for i in cases[0]:
               if a == 7:

                   print(i.text)
   
               a += 1
