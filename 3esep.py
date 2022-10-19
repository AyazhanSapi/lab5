#Cапи Аяжан
#лаборатория5
#Тізімде қолданылатын функциядарды қолданып, программа жазып шығу. Тізім ретінде әр студент өзінің резюмесін ұсынсын. Және сол тізіммен жұмыс жасасын.
print("резюме")
resume = ["Сәпи Аяжан Полатқызы", "25.04.2001", "Satbayev University-Computer Science", "Английский, Русский, Казахский"]
print(resume)

resume.append("Пунктуальность, стрессоустойчивость")
print(resume) 

info = ["010425601119"]
resume.extend(info)
print("\n", resume)

resume.insert(2, "87475006373")
print('\n', resume)

resume.remove("25.04.2001")
print('\n', resume)

resume.pop()
print('\n', resume)

resume.index("87475006373")
print('\n', resume)

resume.sort()
print('\n', resume)

resume_copy = resume.copy()
print(resume_copy)
print('\n', resume)

resume.clear()
print('\n', resume)
