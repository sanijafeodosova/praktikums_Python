""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
vards=str(input("Ievadiet savu vārdu! "))
if vards=="Sanija":
    print("Labdien,", vards,"pimrdienā!")
else:
    print("Uz redzēšanos!")

