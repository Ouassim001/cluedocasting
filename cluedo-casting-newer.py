vraagmoet1 = input("ben je ouder dan 30?\n ")
vraagmoet2 = input("heb je ervaring met acteren?\n ")


vraag1kolo = input("heb je een militaire achtergrond?\n ").lower()
vraag2kolo = input("kan je met wapens omgaan?\n ").lower()
vraag3kolo = input("ben je een man?\n ").lower()

vraag1domi = input("vind je feestjes niks?\n ").lower()
vraag2domi = input("ben je geheimzinnig?\n ").lower()
vraag3domi = input("ben je een man?\n ").lower()

vraag1prof = input("zou je een archeoloog kunnen spelen?\n ").lower()
vraag2prof = input("hou je van reizen?\n ").lower()
vraag3prof = input("ben je een man?\n ").lower

vraag1wit = input("zou je handig zijn in de keuken?\n ").lower()
vraag2wit = input("zou je een soort werk van de rest van je leven volhouden?\n ").lower()
vraag3wit = input("ben je een vrouw?\n ").lower()

vraag1rosa = input("zou je een actrice of een model kunnen zijn?\n ").lower()
vraag2rosa = input("ben je een vrouw?\n ").lower()
vraag3rosa = input("heb je veel emotie die je niet binnen kan houden?\n ").lower()

vraag1blue = input("hou je van feestjes?\n ").lower()
vraag2blue = input("zou je wraak willen nemen als iemand wat van je af zou pakken?\n ").lower()
vraag3blue = input("ben je een vrouw?\n ").lower

if vraag1kolo and vraag2kolo and vraag3kolo == "ja":
    print("Je mag op auditie voor de rol van Kolonel van Geelen") 
    
elif vraag1domi and vraag2domi and vraag3domi == "ja":
    print("Je mag op auditie voor de rol van Dominee Groenewoud")


elif vraag1prof and vraag2prof and vraag2prof == "ja":
    print("Je mag op auditie voor de rol van Professor Pimpel")

elif vraag1wit and vraag2wit and vraag3wit == "ja":
    print("Je mag op auditie voor de rol van Mevrouw de Wit")

elif vraag1rosa and vraag2rosa and vraag3rosa == "ja":
    print("Je mag op auditie voor de rol van Rosa Roodhart")

elif vraag1blue and vraag2blue and vraag3blue == "ja":
    print("Je mag op auditie voor de rol van Mevrouw Blaauw van Draet")
else:
    print("Je mag helaas niet op auditie.")
