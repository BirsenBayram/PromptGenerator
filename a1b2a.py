#%%
#Avatarin nasil gortunsun istersin
#Hangi hayvan seni yansitiyor
import random
def SubPrompt(gender, CAnimalC, CAvatarC, CustAccList, CustPetList, CustHobbiesList):
    SubPrompt1 = 'Create a happy {gender} {animal}'
    SubPrompt2 = 'Create a happy {gender} {avatar}'
    SubPrompt3 = 'Create a happy {gender} monster like from Monster Inc. movie'

    GenderDict = {
                    'kadin': 'female', 
                    'erkek': 'male'
                    }
    AnimalDict = {
        'kedi': 'cat', 
        'köpek': 'dog'
        }
    AvatarDict = {
        'robot': 'robot',
        'süperkahraman': 'super hero'
        }
    
    RAnimal = random.choice(CAnimalC)
    EAnimal = AnimalDict.get(RAnimal)

    RAvatar = random.choice(CAvatarC)
    EAvatar = AvatarDict.get(RAvatar)

    CustGender = GenderDict.get(gender)

    SubPrompt1 = SubPrompt1.replace('{gender}', CustGender).replace('{animal}', EAnimal)
    SubPrompt2 = SubPrompt2.replace('{gender}', CustGender).replace('{avatar}', EAvatar)
    SubPrompt3 = SubPrompt3.replace('{gender}', CustGender)

#Aksesuar
    AccessouriesDict = {
                            'Gunes gozlugu':'wearing sunglasses',
                            'sapka':'wearing hat',
                            'bere':'wearing beanie',
                            'bel cantasi':'wearing waist bag'
                        }
    
    if len(CustAccList)==0:
        SubPrompt1 = SubPrompt1
        SubPrompt2 = SubPrompt2
        SubPrompt3 = SubPrompt3
    elif len(CustAccList)==1:
        if CustAccList[0] == 'Gunes gozlugu':
            SubPrompt1 = SubPrompt1 + 'wearing sunglasses'
            SubPrompt2 = SubPrompt2 + 'wearing sunglasses'
            SubPrompt3 = SubPrompt3 + 'wearing sunglasses.'
        elif CustAccList[0] == 'sapka':
            SubPrompt1 = SubPrompt1 + 'wearing hat'
            SubPrompt2 = SubPrompt2 + 'wearing hat'
            SubPrompt3 = SubPrompt3 + 'wearing hat'
        elif CustAccList[0] == 'bere':
            SubPrompt1 = SubPrompt1 + 'wearing beanie'
            SubPrompt2 = SubPrompt2 + 'wearing beanie'
            SubPrompt3 = SubPrompt3 + 'wearing beanie'
        else:
            SubPrompt1 = SubPrompt1 + 'wearing waist bag'
            SubPrompt2 = SubPrompt2 + 'wearing waist bag'
            SubPrompt3 = SubPrompt3 + 'wearing waist bag'
    elif len(CustAccList)==2:
        SubPrompt1 = f"{SubPrompt1} {AccessouriesDict.get(CustAccList[0], '')}"
        SubPrompt2 = f"{SubPrompt2} {AccessouriesDict.get(CustAccList[0], '')}"
        SubPrompt3 = f"{SubPrompt3} {AccessouriesDict.get(CustAccList[1], '')}"
    elif len(CustAccList)==3:
        SubPrompt1 = f"{SubPrompt1} {AccessouriesDict.get(CustAccList[0], '')}"
        SubPrompt2 = f"{SubPrompt2} {AccessouriesDict.get(CustAccList[1], '')}"
        SubPrompt3 = f"{SubPrompt3} {AccessouriesDict.get(CustAccList[2], '')}"
    else:
        selected_acc = random.choice(CustAccList)
        SubPrompt1 = f"{SubPrompt1} {AccessouriesDict.get(selected_acc, '')}"
        CustAccList.remove(selected_acc)

        selected_acc = random.choice(CustAccList)
        SubPrompt2 = f"{SubPrompt2} {AccessouriesDict.get(selected_acc, '')}"
        CustAccList.remove(selected_acc)

        selected_acc = random.choice(CustAccList)
        SubPrompt3 = f"{SubPrompt3} {AccessouriesDict.get(selected_acc, '')}"

#birlikte yasadigin hayvan
#CustPetList = ['kedi','kopek','kus','balik','tarantula','iguana']
    PetDict = {
                'kedi':'with cat',
                'kopek':'with dog',
                'kus':'with bird',
                'balik':'with fish',
                'tarantula':'with tarantula',
                'iguana':'with iguana'
               }
    if len(CustPetList) == 0:
        SubPrompt1 = SubPrompt1
        SubPrompt2 = SubPrompt2
        SubPrompt3 = SubPrompt3
    elif len(CustPetList) == 1:
        if CustPetList[0] == 'kedi':
            SubPrompt1 = SubPrompt1 + 'with cat'
            SubPrompt2 = SubPrompt2 + 'with cat'
            SubPrompt3 = SubPrompt3 + 'with cat'
        elif CustPetList[0] == 'kopek':
            SubPrompt1 = SubPrompt1 + 'with dog'
            SubPrompt2 = SubPrompt2 + 'with dog'
            SubPrompt3 = SubPrompt3 + 'with dog'
        elif CustPetList[0] == 'kus':
            SubPrompt1 = SubPrompt1 + 'with bird'
            SubPrompt2 = SubPrompt2 + 'with bird'
            SubPrompt3 = SubPrompt3 + 'with bird'
        elif CustPetList[0] == 'balik':
            SubPrompt1 = SubPrompt1 + 'with fish'
            SubPrompt2 = SubPrompt2 + 'with fish'
            SubPrompt3 = SubPrompt3 + 'with fish'
        elif CustPetList[0] == 'tarantula':
            SubPrompt1 = SubPrompt1 + 'with tarantula'
            SubPrompt2 = SubPrompt2 + 'with tarantula'
            SubPrompt3 = SubPrompt3 + 'with tarantula'
        else:
            SubPrompt1 = SubPrompt1 + 'with iguana'
            SubPrompt2 = SubPrompt2 + 'with iguana'
            SubPrompt3 = SubPrompt3 + 'with iguana'
    elif len(CustPetList) ==  2:
        SubPrompt1 = f"{SubPrompt1} {PetDict.get(CustPetList[0], '')}"
        SubPrompt2 = f"{SubPrompt2} {PetDict.get(CustPetList[0], '')}"
        SubPrompt3 = f"{SubPrompt3} {PetDict.get(CustPetList[1], '')}"
    elif len(CustPetList) ==  3:
        SubPrompt1 = f"{SubPrompt1} {PetDict.get(CustPetList[0], '')}"
        SubPrompt2 = f"{SubPrompt2} {PetDict.get(CustPetList[1], '')}"
        SubPrompt3 = f"{SubPrompt3} {PetDict.get(CustPetList[2], '')}"
    else:
        selected_pet = random.choice(CustPetList)
        SubPrompt1 = f"{SubPrompt1} {PetDict.get(selected_pet, '')}"
        CustPetList.remove(selected_pet)

        selected_pet = random.choice(CustPetList)
        SubPrompt2 = f"{SubPrompt2} {PetDict.get(selected_pet, '')}"
        CustPetList.remove(selected_pet)

        selected_pet = random.choice(CustPetList)
        SubPrompt3 = f"{SubPrompt3} {PetDict.get(selected_pet, '')}"

#hobilerin nelerdir
#CustHobbiesList = ['kitap okumak', 'gezmek', 'yuzmek', 'kayak', 'yemek yapmak', 'muzik dinlemek']    

    HobbiesDict = {
        'kitap okumak':'there is a book on its hand',
        'gezmek':'its hobby is travelling',
        'yuzmek':'its hobby is swimming',
        'kayak':'its hobby is skiing',
        'yemek yapmak': 'its hobby is cooking',
        'muzik dinlemek':'its hobby is listening music'
                }

    if len(CustHobbiesList) == 0:
        SubPrompt1 = SubPrompt1
        SubPrompt2 = SubPrompt2
        SubPrompt3 = SubPrompt3
    elif len(CustHobbiesList) == 1:
        if CustPetList[0] == 'kitap okumak':
            SubPrompt1 = SubPrompt1 + 'there is a book on its hand'
            SubPrompt2 = SubPrompt2 + 'there is a book on its hand'
            SubPrompt3 = SubPrompt3 + 'there is a book on its hand'
        elif CustHobbiesList[0] == 'gezmek':
            SubPrompt1 = SubPrompt1 + 'its hobby is travelling'
            SubPrompt2 = SubPrompt2 + 'its hobby is travelling'
            SubPrompt3 = SubPrompt3 + 'its hobby is travelling'
        elif CustHobbiesList[0] == 'yuzmek':
            SubPrompt1 = SubPrompt1 + 'its hobby is swimming'
            SubPrompt2 = SubPrompt2 + 'its hobby is swimming'
            SubPrompt3 = SubPrompt3 + 'its hobby is swimming'
        elif CustHobbiesList[0] == 'kayak':
            SubPrompt1 = SubPrompt1 + 'its hobby is skiing'
            SubPrompt2 = SubPrompt2 + 'its hobby is skiing'
            SubPrompt3 = SubPrompt3 + 'its hobby is skiing'
        elif CustHobbiesList[0] == 'yemek yapmak':
            SubPrompt1 = SubPrompt1 + 'its hobby is cooking'
            SubPrompt2 = SubPrompt2 + 'its hobby is cooking'
            SubPrompt3 = SubPrompt3 + 'its hobby is cooking'
        else:
            SubPrompt1 = SubPrompt1 + 'its hobby is listening music'
            SubPrompt2 = SubPrompt2 + 'its hobby is listening music'
            SubPrompt3 = SubPrompt3 + 'its hobby is listening music'
    elif len(CustHobbiesList) ==  2:
        SubPrompt1 = f"{SubPrompt1} {HobbiesDict.get(CustHobbiesList[0], '')}"
        SubPrompt2 = f"{SubPrompt2} {HobbiesDict.get(CustHobbiesList[0], '')}"
        SubPrompt3 = f"{SubPrompt3} {HobbiesDict.get(CustHobbiesList[1], '')}"
    elif len(CustHobbiesList) ==  3:
        SubPrompt1 = f"{SubPrompt1} {HobbiesDict.get(CustHobbiesList[0], '')}"
        SubPrompt2 = f"{SubPrompt2} {HobbiesDict.get(CustHobbiesList[1], '')}"
        SubPrompt3 = f"{SubPrompt3} {HobbiesDict.get(CustHobbiesList[2], '')}"
    else:
        selected_hobby = random.choice(CustHobbiesList)
        SubPrompt1 = f"{SubPrompt1} {HobbiesDict.get(selected_hobby, '')}"
        CustHobbiesList.remove(selected_hobby)

        selected_hobby = random.choice(CustHobbiesList)
        SubPrompt2 = f"{SubPrompt2} {HobbiesDict.get(selected_hobby, '')}"
        CustHobbiesList.remove(selected_hobby)

        selected_hobby = random.choice(CustHobbiesList)
        SubPrompt3 = f"{SubPrompt3} {HobbiesDict.get(selected_hobby, '')}"


    print(SubPrompt1)
    print(SubPrompt2)
    print(SubPrompt3)



# %%
CustHobbiesList = ['kitap okumak', 'gezmek', 'yuzmek', 'kayak', 'yemek yapmak', 'muzik dinlemek']
CustAccList = ['Gunes gozlugu', 'sapka','bel cantasi']
CustPetList = ['kedi','kopek','kus','balik','tarantula','iguana']
#AccessouriesSub(CustAccList)
gender = 'kadin'
CAnimalC = ['kedi', 'köpek']
CAvatarC = ['robot', 'süperkahraman']
SubPrompt(gender, CAnimalC, CAvatarC, CustAccList, CustPetList, CustHobbiesList)
# %%
