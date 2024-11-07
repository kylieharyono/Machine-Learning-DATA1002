import codecs
import csv
types_of_encoding = ["utf8", "cp1252"]

with open("integrated data (2015).csv", "w", newline="", encoding="utf8") as file:
  writer = csv.writer(file)

  headers = "Country,"
  dic = {}
  templist = []
  elements = []

  #life expectancy data
  with open("C:\\Users\\Kylie\\Downloads\\life1.csv", errors ='replace') as file1:
      header = True

      for row in file1:
        elements = row.split(",")
        country = elements[0]
        year = elements[1]
        lifeexp = elements[-4]
        adultmort = elements[-3]
        infantdeath = elements[-2]
        population = elements[-1]
        if header:
          header = False
          headers += "Life Expectancy,Adult Mortality,Infant Deaths,Population,"
        elif (year == "2015"):
          templist = ["","","","",""]
          templist[0] = country
          templist[1] = lifeexp
          templist[2] = adultmort
          templist[3] = infantdeath
          templist[4] = population.rstrip("\n")
          dic[country] = templist



  #health
  with open("C:\\Users\\Kylie\\Downloads\\health (combined).csv", errors ='replace') as file2:
      header = True

      for row in file2:
        elements = row.split(",")
        country = elements[0]
        year = elements[1]
        lifeexpbirth = elements[-4]
        infantmort = elements[-3]
        meddoc = elements[-2]
        under5mort = elements[-1]
        if header:
          header = False
          headers = headers + ("Life Expectancy at Birth,Infant Mortality Rate,Medical Doctors,Under-5 Mortality Rate,")
        elif (year == "2015"):
          if country not in dic:
            dic[country] = [country,"","","",""]
          templist = ["","","",""]
          templist[0] = lifeexpbirth
          templist[1] = infantmort
          templist[2] = meddoc
          templist[3] = under5mort.rstrip("\n")
          dic[country] += templist
          


  #economic status
  with open("C:\\Users\\Kylie\\Downloads\\Economic status.csv", errors ='replace') as file3:
      header = True

      for row in file3:
        elements = row.split(",")
        country = elements[0]
        GDP = elements[-3]
        GDPpercap = elements[-2]
        healthexp = elements[-1]
        if header:
          header = False
          headers = headers + ("GDP (billions of US$),GDP per Capita (US$),Current Health Expenditure (% of GDP),")
        else:
          if (country in dic) == False:
            dic[country] = [country, "","","","","","","",""]
          templist = ["","",""]
          templist[0] = GDP
          templist[1] = GDPpercap
          templist[2] = healthexp.rstrip("\n")
          dic[country] += templist
          


  #death causes
  with open("C:\\Users\\Kylie\\Downloads\\1_sorted_20220327 annual-number-of-deaths-by-cause copy.csv", errors ='replace') as file4:
      header = True

      for row in file4:
        elements = row.split(",")
        country = elements[0]
        year = elements[2]
        meningitis = elements[3]
        neoplasms = elements[4]
        hotsubstances = elements[5]
        malaria = elements[6]
        drowning = elements[7]
        interviolence = elements[8]
        hivaids = elements[9]
        drugs = elements[10]
        tuberc = elements[11]
        roadinj = elements[12]
        maternaldis = elements[13]
        lowrespinfections = elements[14]
        neonataldis = elements[15]
        alcohol = elements[16]
        nature = elements[17]
        diarrheal = elements[18]
        if header:
          header = False
          headers = headers + "Death by Meningitis," + "Death by Neoplasms," + "'Death by Fire, Heat, and Hot Substances'," + "Death by Malaria," + "Death by Drowning," + "Death by Interpersonal Violence," + "Death by HIV/AIDS," + "Death by Drug Use," + "Death by Tuberculosis," + "Death by Road Injuries," + "Death by Maternal Disorders," + "Death by Lower Respiratory Infections," + "Death by Neonatal Disorders," + "Death by Alcohol Use", "Death by Forces of Nature," "Death by Diarrheal Diseases"
        elif (year == "2015"):
          if country not in dic:
            dic[country] = [country, "","","","","","","","","","",""]
          templist = ["","","","","","","","","","","","","","","",""]
          templist[0] = meningitis
          templist[1] = neoplasms
          templist[2] = hotsubstances
          templist[3] = malaria
          templist[4] = drowning
          templist[5] = interviolence
          templist[6] = hivaids
          templist[7] = drugs
          templist[8] = tuberc
          templist[9] = roadinj
          templist[10] = maternaldis
          templist[11] = lowrespinfections
          templist[12] = neonataldis
          templist[13] = alcohol
          templist[14] = nature
          templist[15] = diarrheal.rstrip("\n")
          

          dic[country] += templist
          

      

  writer.writerow(headers)
  for key in dic:
    writer.writerow(dic[key])
    
