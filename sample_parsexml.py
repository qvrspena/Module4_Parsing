# Vhan Randolp Pena

import xml.etree.ElementTree as et
tree = et.parse("sample.xml")

root = tree.getroot()

Job_Title = []
Company_Name = []
Category = []
City = []

for title in root.iter('job_title'):
    Job_Title.append(title.text)

for company in root.iter('company_name'):
    Company_Name.append(company.text)

for cat in root.iter('category'):
    Category.append(cat.text)    

for city_name in root.iter('city'):
    City.append(city_name.text)

print(Job_Title)
print(Company_Name)
print(Category)
print(City)