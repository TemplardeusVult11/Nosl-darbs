# text-based piedzīvojumu spēle, kuras darbība norisinās vidusslaikos.

import random
import time
import json
import textwrap
import sys
def ievads():
    print(" Spēles darbība norisinās mītiskā, izdomātā vidusslaiku pasaulē.")
    print(" Tu pēkšņi, attopies, kāda grants ceļa galā. Tu redzi zīmi, kas norāda, ka pa labi ir pilsēta, bet pa kreisi ir norāde uz kuras rakstīts, ka tālāk seko dzīvību apdraudošs, zagļu pārpildīts ceļš.")
    print()

def izveliescelu():
    cels=""
    while cels !="1" and cels !="2":
        cels=input(" Pa kuru ceļu tu dosies tālāk, pa labi vai pa kreisi? (1 vai 2):")
    print(" Tu dodies tālāk pa izvēlēto ceļu")
    time.sleep(2)
    if cels=="1":
        print(" Tu atpazīsti redzamo skatu. Tu esi nonācis mājās!")
    else:
        print(" Pēkšņi, krūmos kaut kas sakustas.")
        print(" No krūmiem izlec zaglis un tev uzbrūk!")
        input(" Ko tu dari?")
        time.sleep(1)
        print(" Zaglis aiz apjukuma, būdams gana cietsirdīgs, tevi nogalina")
        time.sleep(1)
        print(" Spēles beigas...")
        time.sleep(2)
        playAgain=input("Spēlēt vēlreiz? (Jā vai nē)")
        while playAgain=="jā":
            ievads()
            izvele=izveliescelu()
        else:
            print("Paldies par spēlēšanu")
def pilseta():
    print(" Pēc ilgiem ceļiem un neceļiem, tu atrodies dzimtās pilsētas centrā. Kāds no daudzajiem tirgotājiem un cilvēkiem tevi atpazīst.")
    time.sleep(3)
    print(" Kāds tirgonis tev pienāk klāt un brīdi paskatījies un padomājis, tevi uzrunā.")
    time.sleep(1)
    print(" -Vai tu gadījumā neesi no šejienes?")
    time.sleep(2)
    print(" -Jā! Šķiet, ka tevi pazīstu")
    time.sleep(2)
    vards=input(" -Saki, kā tevi sauc?")
    print(f"Tik tiešām! Piedod, ka biju tevi aizmirsis vecais draugs! Paskatieties visi, {vards} ir mājās!")
    time.sleep(2)

def atbilde():
    print("Vai vēlies iedzert krūzi alus, kamēr pastāsti kā ir gājis?")
    print("Jā vai nē?")
    atbilde=input("")
    if atbilde=="jā":
        print("Tad tik ejam")
    if atbilde=="nē":
        print("Pēkšņi, no nekurienes uzrodas pūķis un tevi apēd!")
        print("Spēles beigas")
        playAgain=input("Spēlēt vēlreiz? (Jā vai nē)")
        while playAgain=="jā":
            ievads()
            izvele=izveliescelu()
        else:
            print("Paldies par spēlēšanu")
def alus():
    print("Jūs apsēžaties pie galda vietējā krogā. viss izskatās kā agrāk.")
    print("-dzirdēju, ka tu piedalījies Lielajā Orkijas karā.")
    time.sleep(1)
    loma=["Burvis", "Mācītājs", "Kareivis"]
    tava=random.choice(loma)
    print(f"-Tu esot bijis {tava}")
    time.sleep(1)
    print(" Tu piekrītoši pamāj ar galvu.")
def uzbrukums():
    time.sleep(2)
    print("Pēkšņi, krogā iebrūk vesels bars zagļu.")
    print("-Atdodiet visu, kas jums ir!-kliedz lielākais zaglis.")
    izvele=input("Visi skatās uz tevi pēc palīdzības. Ko tu dari?")
    izdodas=random.randint(1,6)
    if izdodas >= 4:
        print("Es tevi apsveicu! Tu to izdarīji un esi uzvarējis spēli!")
    else:
        print("Zagļi visus apzog un redzot, ko tu mēģini darīt, aiz apjukuma, būdami gana cietsirdīgi, tevi nogalina. Spēles beigas :(")
    
 
#Man tas Json modulis nesanāk, kad importēju, tad visu nostopo. Tikai pedējā dienā pirms iesutīšanas importēju.. tādēļ arī tik vēlu ziņoju. Un mainu pašvērtējumu uz seši vai septiņi :D cerīgi




ievads()
izveliescelu()
pilseta()
atbilde()
alus()
uzbrukums()

        





        
        
