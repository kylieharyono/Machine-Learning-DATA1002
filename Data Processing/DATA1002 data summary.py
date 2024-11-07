#opening file
import os
import csv

print("1. life expectancy at birth \n2. infant mortality rate \n3. medical doctors \n4. under-five mortality rate")
num = input("enter the corresponding number: ")

csv1 = open('C:\\Users\\Kylie\\Desktop\\DATA1002\\1_life_exp_at_birth.csv')
csv2 = open('C:\\Users\\Kylie\\Desktop\\DATA1002\\2_infant_mortality_rate.csv')
csv3 = open('C:\\Users\\Kylie\\Desktop\\DATA1002\\3_medical_doctors.csv')
csv4 = open('C:\\Users\\Kylie\\Desktop\\DATA1002\\4_under_five_mortality_rate.csv')

header = True
dictionary = {}

#life exp at birth
if num == "1":
  for line in csv1:
    if header:
      header = False
    else:
      elements = line.split(",")
      country = str(elements[0])
      year = elements[1]
      lifeexp = elements[4]
      if (country in dictionary) == False:
        dictionary[country] = lifeexp

  for key in sorted(dictionary):
      print(key, ":", dictionary[key])




#infant mortality rate
if num == "2":
  for line in csv2:
    if header:
      header = False
    else:
      elements = line.split(",")
      country = str(elements[0])
      year = elements[1]
      inf_mort_rate = elements[4]
      if (country in dictionary) == False:
        dictionary[country] = inf_mort_rate

  for key in sorted(dictionary):
      print(key, ":", dictionary[key])



#medical doctors
if num == "3":
  for line in csv3:
    if header:
      header = False
    else:
      elements = line.split(",")
      country = str(elements[0])
      year = elements[1]
      meddoc = elements[4]
      if (country in dictionary) == False:
        dictionary[country] = meddoc

  for key in sorted(dictionary):
      print(key, ":", dictionary[key])


#under five mortality rate
if num == "4":
  for line in csv4:
    if header:
      header = False
    else:
      elements = line.split(",")
      country = str(elements[0])
      year = elements[1]
      underfive = elements[4]
      if (country in dictionary) == False:
        dictionary[country] = underfive

  for key in sorted(dictionary):
      print(key, ":", dictionary[key])
