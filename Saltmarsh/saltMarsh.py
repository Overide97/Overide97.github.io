import random
import numpy

races = ['Human', 'Elf', 'Half_Elf',
         'Gnome', 'Halfling', 'Half_Orc',
         'Dragonborn', 'Tiefling', 'Other']

jobs = ['Fisher', 'Sailor', 'Laborer', 
        'Smuggler', 'Miner', 'Mercenary',
        'Academic', 'Adventurer', 'Aristocrat',
        'Artisan/Guild Member', 'Entertainer','Exile/Hermit/Refugee', 
        'Explorer/Wanderer', 'Farmer/Herder', 'Hunter/Trapper', 
        'Merchant', 'Politician/Bureaucrat', 'Priest']

classes = ['Paladin', 'Cleric', 'Rogue',
           'Fighter', 'Barbarian', 'Druid',
           'Warlock', 'Sorcerer', 'Wizard',
           'Bard', 'Ranger']

DwarfJobs = ['Miner', 'Stonemason', 'Blacksmith', 
             'Carpenter', 'Architect', 'Dungeoneer']

study=['Historian', 'Alchemist', 'Mathematician',
       'Physician', 'Linguist', 'Engineer',
       'Psycologist', 'Lawyer', 'Archeologist',
       'Biologist', 'Bardologist']

guilds = ['Alchemist and Apothecaries', 'Armorers, locksmiths and finesmiths',
          'Brewers, Distillers and vintners', 'Calligraphers, scribes and scriveners',
          'Carpenters, roofers and plasterers', 
          'Cartographers, surveyors and chart-makers', 'Cobblers and shoemakers', 
          'Cooks and bakers', 'Glassblowers and glaziers',
          'Jewlers and gemcutters', 'Leatherworkers, skinners and tanners', 
          'Masons and stonecutters', 'Painters, limners and sign-makers',
          'Potters and tile-makers', 'Shipwrights and sailmakers',
          'Smiths and metal-forgers', 'Tinkers, pewterers and casters',
          'Wagon-makers and wheelwrights', 'Weavers and dyers',
          'Woodcarvers, coopers and bowyers']

### Soldier is not included, as they have a town guard.

#religion = ['Valkur', 'Umberlee']

genders = ['Male', "Female", 'Non-Binary']

#The major ethnicities and minorities of faerun are intended for the region 
#of Salt Marsh.

################################################################################
################ Human Ethnicities of the Forgotten Realms #####################
################################################################################

MajorEthnicities = ['Illuskan', 'Tethyrian', 'Chondathan', 
                    'Minority']

Minority_location = ['Faerun', 'KaraTur', 'Maztica']

Faerun_Minorities = ['Northlander', 'Ffolk', 'Abbalayar', 
                     'Netherese', 'Arkaiun', 'Bedine', 
                     'Mulan', 'Rashemi', 'Damaran',
                     'Ramuvian', 'Calishite', 'Chult', 
                     'Lantana', 'Halruaan', 'Dupari', 
                     'Imaskari', 'Nars', 'Gurs',
                     'Shaarans', 'Sossrin', 'Tashalan', 
                     'Tuiga', 'Turami', 'Vaasans']

KaraTur_Minorities = ['Issacortae', 'Koryoan', 'Kozakuran', 
                      'Kuong', 'Shou', 'Wanese', 
                      'Wu_Haltai', 'Bavanese', 'Bertanese', 
                      'Bawani', 'Nubani', 'Pazruki',
                      'Purang', 'ulutiun']

Maztica_Minorities = ['Azuposi', 'Green Folk', 'Metahel', 
                      'Nahopaca', 'Nexalans', 'North Ones', 
                      'Payit', 'Itza']

################################################################################
########################### Elven SubRaces #####################################
################################################################################

################################################################################
#ElvenEthnicities = ['Ar\'Tel\'Quessir', 'Teu\'Tel\'Quessir', 
                    #'Ruar\'Tel\'Quessir', 'Or\'Tel\'Quessir', 
                    #'Grugach', 'Drow', 
                    #'Alu\'Tel\'Quessir', 'Aril\'Tel\'Quessir',
                    #'Ly\'Tel\'Quessir']
################################################################################

ElvenEthnicities = ['ArTelQuessir', 'TeuTelQuessir', 
                    'RuarTelQuessir', 'OrTelQuessir', 
                    'Grugach', 'Drow', 
                    'AluTelQuessir', 'ArilTelQuessir',
                    'LyTelQuessir']

################################################################################
########################## Gnomish Subraces ####################################
################################################################################

GnomeEthnicities = ['Forstneblin', 'Steinneblin', 'Svirfneblin'] 

################################################################################
######################### Halfling Subraces ####################################
################################################################################

HalflingEthnicities = ['Anadian', 'Ghostwise', 
                       'Lightfoot', 'Strongheart']

################################################################################
############################# Orc Subraces #####################################
################################################################################

OrcEthnicities = ['Mountain', 'Grey', 'Orog']

################################################################################
############################ Tiefling Subraces #################################
################################################################################

TieflingEthnicities = ['Asmodeus', 'Baalzebul', 'Dispater', 
                       'Fierna', 'Glasya', 'Levistus', 
                       'Mammon', 'Mephistopheles', 'Zariel']

################################################################################
########################### DragonBorn Subraces ################################
################################################################################

DragonEthnicities = ['Scarlet', 'rust', 'Gold', 'Brass', 
                     'Bronze', 'Copper-Green', 'Black', 'Blue', 
                     'True Brass', 'True Bronze', 'Copper', 'True Gold', 
                     'Green', 'Red', 'Silver', 'White']

################################################################################
########################### Dwarf Ethnicities ##################################
################################################################################

DwarfEthnicities = ['Inugaakalikurit', 'Ae', 'Duergar', 
                    'Barak', 'Urdunnir', 'Vos']

for num in range(4800):
  num = num + 1

  race = random.choices(races, weights=[70, 4, 1, 2, 
                                        15, 5, 1, 1, 
                                        1], k=1)  
################################################################################
  if race[0] =='Human':
    age = random.randint(15, 35)
    if age == 35:
      age = random.randint(35, 53)
      if age == 53:
        age= random.randint(53, 70)
        if age == 70:
          age = random.randint(70, 110)
    job = random.choices(jobs, weights=[50, 12, 11, 3, 
                                        5, 5, 1, 1, 
                                        1, 1, 1, 1, 
                                        1, 1, 1, 3, 
                                        1, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(MajorEthnicities, weights=[45, 25, 25, 5], k=4)
    if ethnicity[0] == 'Minority':
      ethnicity = random.choices(Minority_location, weights=[90, 5, 5], k=3)
      if ethnicity[0] == 'Faerun':
        ethnicity = random.choices(Faerun_Minorities, weights=[40, 30, 9, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1], 
                                                               k=24)
      if ethnicity[0] == 'KaraTur':
        ethnicity[0] = random.choice(KaraTur_Minorities)  
      if ethnicity[0] == 'Maztica':
        ethnicity[0] = random.choice(Maztica_Minorities)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "', '" + job[0] + "', " + str(age) + ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Elf':
    age = random.randint(110, 175)
    if age == 175:
      age = random.randint(175, 263)
      if age == 263:
        age = random.randint(263, 350)
        if age == 350:
          age = random.randint(350, 750)
    job = random.choices(jobs, weights=[1, 2, 1, 5, 
                                        1, 5, 5, 8, 
                                        1, 25, 6, 1, 
                                        3, 1, 10, 22, 
                                        2, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(ElvenEthnicities, weights=[20,30,1,
                                                          1,35,10,
                                                          1,1,1,], k=9)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "', '" + job[0] + "', " + str(age) + ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Half_Elf':
    age = random.randint(20, 62)
    if age == 62:
      age = random.randint(62, 93)
      if age == 93:
        age = random.randint(93, 125)
        if age == 125:
          age = random.randint(125, 185)
    job = random.choices(jobs, weights=[50, 12, 11, 3, 
                                        5, 5, 1, 1, 
                                        1, 1, 1, 1, 
                                        1, 1, 1, 3, 
                                        1, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(MajorEthnicities, weights=[45, 25, 25, 5], k=4)
    if ethnicity[0] == 'Minority':
      ethnicity = random.choices(Minority_location, weights=[90, 5, 5], k=3)
      if ethnicity[0] == 'Faerun':
        ethnicity = random.choices(Faerun_Minorities, weights=[40, 30, 9, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1], k=24)
      if ethnicity[0] == 'KaraTur':
        ethnicity = random.choice(KaraTur_Minorities)
      if ethnicity[0] == 'Maztica':
        ethnicity = random.choice(Maztica_Minorities)
    Ethnicity2 = random.choices(ElvenEthnicities, weights=[20,30,1,
                                                          1,35,10,
                                                          1,1,1,], k=9)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "/" + Ethnicity2[0] + "', '" + job[0] + "', " + str(age) + 
          ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Gnome':
    age = random.randint(40, 100)
    if age == 100:
      age = random.randint(100, 150)
      if age == 150:
        age = random.randint(150, 200)
        if age == 200:
          age = random.randint(200, 500)
    job = random.choices(jobs, weights=[1, 1, 1, 1, 
                                        1, 1, 30, 5, 
                                        1, 25, 1, 1, 
                                        1, 1, 1, 23, 7, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(GnomeEthnicities, weights=[5, 70, 25], k=3)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "', '" + job[0] + "', " + str(age) + ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Halfling':
    age = random.randint(20, 50)
    if age == 50:
      age = random.randint(50, 75)
      if age == 75:
        age = random.randint(75, 100)
        if age == 100:
          age = random.randint(100, 200)
    job = random.choices(jobs, weights=[2, 2, 2, 1, 
                                        1, 1, 1, 1, 
                                        1, 1, 1, 1, 
                                        1, 62, 19, 1, 
                                        1, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(HalflingEthnicities, weights=[1, 4, 75, 20], k=4)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "', '" + job[0] + "', " + str(age) + ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Half_Orc':
    age = random.randint(14, 30)
    if age == 30:
      age = random.randint(30, 45)
      if age == 45:
        age = random.randint(45, 60)
        if age == 60:
          age = random.randint(60, 80)
    job = random.choices(jobs, weights=[50, 12, 11, 3, 
                                        5, 5, 1, 1, 
                                        1, 1, 1, 1, 
                                        1, 1, 1, 3, 
                                        1, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(MajorEthnicities, weights=[45, 25, 25, 5], k=4)
    if ethnicity[0] == 'Minority':
      ethnicity = random.choices(Minority_location, weights=[90, 5, 5], k=3)
      if ethnicity[0] == 'Faerun':
        ethnicity = random.choices(Faerun_Minorities, weights=[40, 30, 9, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1], k=24)
      if ethnicity[0] == 'KaraTur':
        ethnicity = random.choice(KaraTur_Minorities)  
      if ethnicity[0] == 'Maztica':
        ethnicity = random.choice(Maztica_Minorities)
    Ethnicity2 = random.choices(OrcEthnicities, weights=[75, 20, 5], k=3)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "/" + Ethnicity2[0] + "', '" + job[0] + "', " + str(age) + 
          ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Dragonborn':
    age = random.randint(15, 35)
    if age == 35:
      age = random.randint(35, 53)
      if age == 53:
        age= random.randint(53, 70)
        if age == 70:
          age = random.randint(70, 110)
    job = random.choices(jobs, weights=[1, 12, 1, 3, 
                                        5, 5, 1, 50, 
                                        1, 1, 1, 1, 
                                        11, 1, 1, 3, 
                                        1, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(DragonEthnicities, weights=[15, 10, 10, 10,
                                                           10, 10, 2, 2,
                                                           3, 3, 3, 3, 
                                                           2, 2, 3, 2], k=16)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "', '" + job[0] + "', " + str(age) + ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Tiefling':
    age = random.randint(15, 61)
    if age == 61:
      age = random.randint(61, 150)
    job = random.choices(jobs, weights=[1, 12, 1, 3, 
                                        5, 5, 1, 50, 
                                        1, 1, 1, 1, 
                                        11, 1, 1, 3, 
                                        1, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    ethnicity = random.choices(MajorEthnicities, weights=[45, 25, 25, 5], k=4)
    if ethnicity[0] == 'Minority':
      ethnicity = random.choices(Minority_location, weights=[90, 5, 5], k=3)
      if ethnicity[0] == 'Faerun':
        ethnicity = random.choices(Faerun_Minorities, weights=[40, 30, 9, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1, 
                                                               1, 1, 1, 1], 
                                                               k=24)
      if ethnicity[0] == 'KaraTur':
        ethnicity = random.choice(KaraTur_Minorities)  
      if ethnicity[0] == 'Maztica':
        ethnicity = random.choice(Maztica_Minorities)
    Ethnicity2 = random.choices(TieflingEthnicities, weights=[90, 1, 1,
                                                              1, 1, 1,
                                                              1, 1, 1], k=9)
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', '" + ethnicity[0] + 
          "/" + Ethnicity2[0] + "', '" + job[0] + "', " + str(age) + 
          ", '" + gender[0] + "'),")
################################################################################
  if race[0] == 'Other':
    age = 'NULL'
    job = random.choices(jobs, weights=[1, 7, 1, 1, 
                                        20, 1, 20, 1, 
                                        1, 1, 1, 20, 
                                        1, 1, 20, 1, 
                                        1, 1], k=18)
    if job[0] == 'Adventurer':
      job[0] = random.choice(classes)
    elif job[0] == 'Artisan/Guild Member':
      job[0] = random.choice(guilds)
    elif job[0] == 'Academic':
      job[0] = random.choice(study)
    else:
      job[0] = job[0]
    gender = random.choices(genders, weights=[48, 48, 4], k=3)
    print("(" + str(num) + ", '" + race[0] + "', " + "'" + job[0] +
           "', " + str(age) + ", '" + gender[0] + "'),")

for num in range(200):

  num = num + 4801
  age = random.randint(40, 125)
  if age == 125:
    age = random.randint(125, 188)
    if age == 188:
      age = random.randint(188, 250)
      if age ==  250:
        age = random.randint(250, 450)
  job = random.choices(DwarfJobs, weights=[75, 5, 5,
                                           5, 5, 5], k=6)
  ethnicity = random.choices(DwarfEthnicities, weights=[10,10,1,
                                                        77,1,1], k=6)
  gender = random.choices(genders, weights=[48, 48, 4], k=3) 
  print("(" + str(num) + ", '" + 'Dwarf' + "', '" + ethnicity[0] + 
        "', '" + job[0] + "', " + str(age) + ", '" + gender[0] + "')")