from tkinter import *
from PIL import ImageTk, Image
import requests

root = Tk()
root.title("Compressed Ore Value Calculator")
icon = PhotoImage(file="Images/Veldspar.png")
root.iconphoto(False, icon)

MarketFrame = LabelFrame(root, padx=5, pady=5)
MarketFrame.grid()

TritPrices = []
PyeritePrices = []
MexallonPrices = []
MegacytePrices = []
IsogenPrices = []
MorphitePrices = []
NocxiumPrices = []
ZydrinePrices = []

loop = "true"
MinimumQuantity = 1

veldspar_img = ImageTk.PhotoImage(Image.open("Images/Veldspar.png"))
arkonor_img = ImageTk.PhotoImage(Image.open("Images/Arkonor.jpg"))
bistot_img = ImageTk.PhotoImage(Image.open("Images/Bistot.jpg"))
crokite_img = ImageTk.PhotoImage(Image.open("Images/Crokite.jpg"))
darkochre_img = ImageTk.PhotoImage(Image.open("Images/DarkOchre.jpg"))
gneiss_img = ImageTk.PhotoImage(Image.open("Images/Gneiss.jpg"))
hedbergite_img = ImageTk.PhotoImage(Image.open("Images/Hedbergite.jpg"))
hemorphite_img = ImageTk.PhotoImage(Image.open("Images/Hemorphite.jpg"))
jaspet_img = ImageTk.PhotoImage(Image.open("Images/Jaspet.jpg"))
kernite_img = ImageTk.PhotoImage(Image.open("Images/Kernite.jpg"))
mercoxit_img = ImageTk.PhotoImage(Image.open("Images/Mercoxit.png"))
omber_img = ImageTk.PhotoImage(Image.open("Images/Omber.jpg"))
plagioclase_img = ImageTk.PhotoImage(Image.open("Images/Plagioclase.png"))
pyroxeres_img = ImageTk.PhotoImage(Image.open("Images/Pyroxeres.png"))
scordite_img = ImageTk.PhotoImage(Image.open("Images/Scordite.png"))
spodumain_img = ImageTk.PhotoImage(Image.open("Images/Spodumain.jpg"))

RefineYieldLabel = Label(root, text="Your refine %", bd=2)
TritaniumLabel = Label(root, text="Tritanium Price", bd=2)
PyeriteLabel = Label(root, text="Pyerite Price", bd=2)
MexallonLabel = Label(root, text="Mexallon Price", bd=2)
IsogenLabel = Label(root, text="Isogen Price", bd=2)
NocxiumLabel = Label(root, text="Nocxium Price", bd=2)
MegacyteLabel = Label(root, text="Megacyte Price", bd=2)
ZydrineLabel = Label(root, text="Zydrine Price", bd=2)
MorphiteLabel = Label(root, text="Morphite Price", bd=2)

RefineYield = Entry(root, width=5, borderwidth=2)
TritaniumPrice = Entry(root, width=10, borderwidth=2)
PyeritePrice = Entry(root, width=10, borderwidth=2)
MexallonPrice = Entry(root, width=10, borderwidth=2)
IsogenPrice = Entry(root, width=10, borderwidth=2)
NocxiumPrice = Entry(root, width=10, borderwidth=2)
MegacytePrice = Entry(root, width=10, borderwidth=2)
ZydrinePrice = Entry(root, width=10, borderwidth=2)
MorphitePrice = Entry(root, width=10, borderwidth=2)

ArkonorLabel = Label(root, text="Arkonor", bd=2)
BistotLabel = Label(root, text="Bistot", bd=2)
CrokiteLabel = Label(root, text="Crokite", bd=2)
DarkOchreLabel = Label(root, text="Dark Ochre", bd=2)
GneissLabel = Label(root, text="Gneiss", bd=2)
HedbergiteLabel = Label(root, text="Hedbergite", bd=2)
HemorphiteLabel = Label(root, text="Hemorphite", bd=2)
JaspetLabel = Label(root, text="Jaspet", bd=2)
KerniteLabel = Label(root, text="Kernite", bd=2)
MercoxitLabel = Label(root, text="Mercoxit", bd=2)
OmberLabel = Label(root, text="Omber", bd=2)
PlagioclaseLabel = Label(root, text="Plagioclase", bd=2)
PyroxeresLabel = Label(root, text="Pyroxeres", bd=2)
ScorditeLabel = Label(root, text="Scordite", bd=2)
SpodumainLabel = Label(root, text="Spodumain", bd=2)
VeldsparLabel = Label(root, text="Veldspar", bd=2)

ArkonorValue = Label(root, text="Compressed Arkonor:", bd=2)
BistotValue = Label(root, text="Compressed Bistot:", bd=2)
CrokiteValue = Label(root, text="Compressed Crokite:", bd=2)
DarkOchreValue = Label(root, text="Compressed Dark Ochre:", bd=2)
GneissValue = Label(root, text="Compressed Gneiss:", bd=2)
HedbergiteValue = Label(root, text="Compressed Hedbergite:", bd=2)
HemorphiteValue = Label(root, text="Compressed Hemorphite:", bd=2)
JaspetValue = Label(root, text="Compressed Jaspet:", bd=2)
KerniteValue = Label(root, text="Compressed Kernite:", bd=2)
MercoxitValue = Label(root, text="Compressed Mercoxit:", bd=2)
OmberValue = Label(root, text="Compressed Omber:", bd=2)
PlagioclaseValue = Label(root, text="Compressed Plagioclase:", bd=2)
PyroxeresValue = Label(root, text="Compressed Pyroxeres:", bd=2)
ScorditeValue = Label(root, text="Compressed Scordite:", bd=2)
SpodumainValue = Label(root, text="Compressed Spodumain:", bd=2)
VeldsparValue = Label(root, text="Compressed Veldspar:", bd=2)

ArkonorPrice = Entry(root, width=10, borderwidth=2)
BistotPrice = Entry(root, width=10, borderwidth=2)
CrokitePrice = Entry(root, width=10, borderwidth=2)
DarkOchrePrice = Entry(root, width=10, borderwidth=2)
GneissPrice = Entry(root, width=10, borderwidth=2)
HedbergitePrice = Entry(root, width=10, borderwidth=2)
HemorphitePrice = Entry(root, width=10, borderwidth=2)
JaspetPrice = Entry(root, width=10, borderwidth=2)
KernitePrice = Entry(root, width=10, borderwidth=2)
MercoxitPrice = Entry(root, width=10, borderwidth=2)
OmberPrice = Entry(root, width=10, borderwidth=2)
PlagioclasePrice = Entry(root, width=10, borderwidth=2)
PyroxeresPrice = Entry(root, width=10, borderwidth=2)
ScorditePrice = Entry(root, width=10, borderwidth=2)
SpodumainPrice = Entry(root, width=10, borderwidth=2)
VeldsparPrice = Entry(root, width=10, borderwidth=2)

# Inserts a default value into refine yield - user can still erase this value and cause a type error.
if RefineYield.get() == "":
    RefineYield.insert(0, 50)


def veldspar():
    tritanium = (415 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    VeldsparPrice.delete(0, END)
    VeldsparPrice.insert(0, round(tritanium, 2))


def arkonor():
    tritanium = (22000 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    mexallon = (2500 * float(RefineYield.get()) / 100) * float(MexallonPrice.get())
    megacyte = (320 * float(RefineYield.get()) / 100) * float(MegacytePrice.get())
    ArkonorPrice.delete(0, END)
    ArkonorPrice.insert(0, round((tritanium + mexallon + megacyte), 2))


def bistot():
    pyerite = (12000 * float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    zydrine = (450 * float(RefineYield.get()) / 100) * float(ZydrinePrice.get())
    megacyte = (100 * float(RefineYield.get()) / 100) * float(MegacytePrice.get())
    BistotPrice.delete(0, END)
    BistotPrice.insert(0, round((pyerite + zydrine + megacyte), 2))


def crokite():
    tritanium = (21000 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    nocxium = (760 * float(RefineYield.get()) / 100) * float(NocxiumPrice.get())
    zydrine = (135 * float(RefineYield.get()) / 100) * float(ZydrinePrice.get())
    CrokitePrice.delete(0, END)
    CrokitePrice.insert(0, round((tritanium + zydrine + nocxium), 2))


def darkOchre():
    tritanium = (10000 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    nocxium = (120 * float(RefineYield.get()) / 100) * float(NocxiumPrice.get())
    isogen = (1600 * float(RefineYield.get()) / 100) * float(IsogenPrice.get())
    DarkOchrePrice.delete(0, END)
    DarkOchrePrice.insert(0, round((tritanium + isogen + nocxium), 2))


def gneiss():
    pyerite = (21000 *float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    mexallon = (760 * float(RefineYield.get()) / 100) * float(MexallonPrice.get())
    isogen = (135 * float(RefineYield.get()) / 100) * float(IsogenPrice.get())
    GneissPrice.delete(0, END)
    GneissPrice.insert(0, round((pyerite + mexallon + isogen), 2))


def hedbergite():
    pyerite = (1000 * float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    nocxium = (100 * float(RefineYield.get()) / 100) * float(NocxiumPrice.get())
    isogen = (200 * float(RefineYield.get()) / 100) * float(IsogenPrice.get())
    zydrine = (19 * float(RefineYield.get()) / 100) * float(ZydrinePrice.get())
    HedbergitePrice.delete(0, END)
    HedbergitePrice.insert(0, round((pyerite + nocxium + isogen + zydrine), 2))


def hemorphite():
    tritanium = (2200 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    nocxium = (120 * float(RefineYield.get()) / 100) * float(NocxiumPrice.get())
    zydrine = (15 * float(RefineYield.get()) / 100) * float(ZydrinePrice.get())
    isogen = (100 * float(RefineYield.get()) / 100) * float(IsogenPrice.get())
    HemorphitePrice.delete(0, END)
    HemorphitePrice.insert(0, round((tritanium + nocxium + zydrine + isogen), 2))


def jaspet():
    mexallon = (350 * float(RefineYield.get()) / 100) * float(MexallonPrice.get())
    nocxium = (75 * float(RefineYield.get()) / 100) * float(NocxiumPrice.get())
    zydrine = (8 * float(RefineYield.get()) / 100) * float(ZydrinePrice.get())
    JaspetPrice.delete(0, END)
    JaspetPrice.insert(0, round((mexallon + nocxium + zydrine), 2))



def kernite():
    tritanium = (134 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    mexallon = (267 * float(RefineYield.get()) / 100) * float(MexallonPrice.get())
    isogen = (134 * float(RefineYield.get()) / 100) * float(IsogenPrice.get())
    KernitePrice.delete(0, END)
    KernitePrice.insert(0, round((mexallon + tritanium + isogen), 2))


def mercoxit():
    morphite = (300 * float(RefineYield.get()) / 100) * float(MorphitePrice.get())
    MercoxitPrice.delete(0, END)
    MercoxitPrice.insert(0, round(morphite, 2))


def omber():
    tritanium = (800 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    pyerite = (100 * float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    isogen = (85 * float(RefineYield.get()) / 100) * float(IsogenPrice.get())
    OmberPrice.delete(0, END)
    OmberPrice.insert(0, round((tritanium + pyerite + isogen), 2))


def plagioclase():
    tritanium = (107 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    pyerite = (213 * float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    mexallon = (107 * float(RefineYield.get()) / 100) * float(MexallonPrice.get())
    PlagioclasePrice.delete(0, END)
    PlagioclasePrice.insert(0, round((tritanium + pyerite + mexallon), 2))


def pyroxeres():
    tritanium = (351 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    nocxium = (5 * float(RefineYield.get()) / 100) * float(NocxiumPrice.get())
    pyerite = (25 * float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    mexallon = (50 * float(RefineYield.get()) / 100) * float(MexallonPrice.get())
    PyroxeresPrice.delete(0, END)
    PyroxeresPrice.insert(0, round((tritanium + pyerite + nocxium + mexallon), 2))


def scordite():
    tritanium = (346 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    pyerite = (173 * float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    ScorditePrice.delete(0, END)
    ScorditePrice.insert(0, round((tritanium + pyerite), 2))


def spodumain():
    tritanium = (56000 * float(RefineYield.get()) / 100) * float(TritaniumPrice.get())
    pyerite = (12050 * float(RefineYield.get()) / 100) * float(PyeritePrice.get())
    mexallon = (2100 * float(RefineYield.get()) / 100) * float(MexallonPrice.get())
    isogen = (450 * float(RefineYield.get()) / 100) * float(IsogenPrice.get())
    SpodumainPrice.delete(0, END)
    SpodumainPrice.insert(0, round((tritanium + pyerite + mexallon + isogen), 2))


# Make min quantity equal to the value typed into the price field, or create a seperate column/entry field for that.
# Consider adding tool tips


def marketUpdate():
    TritaniumOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34")
    TritData = TritaniumOrder.json()
    for x in TritData:
        # 30000144 - Perimeter system id
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            TritPrices.append(x['price'])


    PyeriteOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=35")
    PyeriteData = PyeriteOrder.json()

    # MinimumQuantity = int(input('How much pyerite will you need?'))

    for x in PyeriteData:
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            PyeritePrices.append(x['price'])

    MexallonOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=36")
    MexallonData = MexallonOrder.json()

    # MinimumQuantity = int(input('How much mexallon will you need?'))

    for x in MexallonData:
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            MexallonPrices.append(x['price'])

    MegacyteOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=40")
    MegacyteData = MegacyteOrder.json()

    # MinimumQuantity = int(input('How much megacyte will you need?'))

    for x in MegacyteData:
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            MegacytePrices.append(x['price'])

    IsogenOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=37")
    IsogenData = IsogenOrder.json()

    # MinimumQuantity = int(input('How much isogen will you need?'))

    for x in IsogenData:
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            IsogenPrices.append(x['price'])

    NocxiumOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=38")
    NocxiumData = NocxiumOrder.json()

    # MinimumQuantity = int(input('How much nocxium will you need?'))

    for x in NocxiumData:
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            NocxiumPrices.append(x['price'])

    ZydrineOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=39")
    ZydrineData = ZydrineOrder.json()

    # MinimumQuantity = int(input('How much zydrine will you need?'))

    for x in ZydrineData:
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            ZydrinePrices.append(x['price'])

    MorphiteOrder = requests.get("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=11399")
    MorphiteData = MorphiteOrder.json()

    # MinimumQuantity = int(input('How much Morphite will you need?'))

    for x in MorphiteData:
        systemID = x['system_id']
        if systemID == 30000142 and (x['volume_remain'] >= MinimumQuantity):
            MorphitePrices.append(x['price'])

    TritPrices.sort()
    PyeritePrices.sort()
    MexallonPrices.sort()
    MegacytePrices.sort()
    IsogenPrices.sort()
    MorphitePrices.sort()
    NocxiumPrices.sort()
    ZydrinePrices.sort()

    TritaniumPrice.delete(0, END)
    PyeritePrice.delete(0, END)
    MexallonPrice.delete(0, END)
    IsogenPrice.delete(0, END)
    NocxiumPrice.delete(0, END)
    MegacytePrice.delete(0, END)
    ZydrinePrice.delete(0, END)
    MorphitePrice.delete(0, END)

    TritaniumPrice.insert(0, TritPrices[0])
    PyeritePrice.insert(0, PyeritePrices[0])
    MexallonPrice.insert(0, MexallonPrices[0])
    IsogenPrice.insert(0, IsogenPrices[0])
    NocxiumPrice.insert(0, NocxiumPrices[0])
    MegacytePrice.insert(0, MegacytePrices[0])
    ZydrinePrice.insert(0, ZydrinePrices[0])
    MorphitePrice.insert(0, MorphitePrices[0])

# Come back and create an button/label object and have it loop through
# the images and create buttons/labels with less/more responsive code


button_arkonor = Button(root, image=arkonor_img, command=arkonor)
button_bistot = Button(root, image=bistot_img, command=bistot)
button_crokite = Button(root, image=crokite_img, command=crokite)
button_darkochre = Button(root, image=darkochre_img, command=darkOchre)
button_gneiss = Button(root, image=gneiss_img, command=gneiss)
button_hedbergite = Button(root, image=hedbergite_img, command=hedbergite)
button_hemorphite = Button(root, image=hemorphite_img, command=hemorphite)
button_jaspet = Button(root, image=jaspet_img, command=jaspet)

button_kernite = Button(root, image=kernite_img, command=kernite)
button_mercoxit = Button(root, image=mercoxit_img, command=mercoxit)
button_omber = Button(root, image=omber_img, command=omber)
button_plagioclase = Button(root, image=plagioclase_img, command=plagioclase)
button_pyroxeres = Button(root, image=pyroxeres_img, command=pyroxeres)
button_scordite = Button(root, image=scordite_img, command=scordite)
button_spodumain = Button(root, image=spodumain_img, command=spodumain)
button_veldspar = Button(root, image=veldspar_img, command=veldspar)

button_marketupdate = Button(root, text="Update Prices", command=marketUpdate)
button_quit = Button(root, text='Exit', command=root.quit)

RefineYieldLabel.grid(row=8, column=3)
RefineYield.grid(row=8, column=4)

TritaniumLabel.grid(row=0, column=0)
PyeriteLabel.grid(row=1, column=0)
MexallonLabel.grid(row=2, column=0)
IsogenLabel.grid(row=3, column=0)
NocxiumLabel.grid(row=4, column=0)
MegacyteLabel.grid(row=5, column=0)
ZydrineLabel.grid(row=6, column=0)
MorphiteLabel.grid(row=7, column=0)

TritaniumPrice.grid(row=0, column=1)
PyeritePrice.grid(row=1, column=1)
MexallonPrice.grid(row=2, column=1)
IsogenPrice.grid(row=3, column=1)
NocxiumPrice.grid(row=4, column=1)
MegacytePrice.grid(row=5, column=1)
ZydrinePrice.grid(row=6, column=1)
MorphitePrice.grid(row=7, column=1)

ArkonorValue.grid(row=0, column=3)
BistotValue.grid(row=1, column=3)
CrokiteValue.grid(row=2, column=3)
DarkOchreValue.grid(row=3, column=3)
GneissValue.grid(row=4, column=3)
HedbergiteValue.grid(row=5, column=3)
HemorphiteValue.grid(row=6, column=3)
JaspetValue.grid(row=7, column=3)

KerniteValue.grid(row=0, column=5)
MercoxitValue.grid(row=1, column=5)
OmberValue.grid(row=2, column=5)
PlagioclaseValue.grid(row=3, column=5)
PyroxeresValue.grid(row=4, column=5)
ScorditeValue.grid(row=5, column=5)
SpodumainValue.grid(row=6, column=5)
VeldsparValue.grid(row=7, column=5)

KernitePrice.grid(row=0, column=6)
MercoxitPrice.grid(row=1, column=6)
OmberPrice.grid(row=2, column=6)
PlagioclasePrice.grid(row=3, column=6)
PyroxeresPrice.grid(row=4, column=6)
ScorditePrice.grid(row=5, column=6)
SpodumainPrice.grid(row=6, column=6)
VeldsparPrice.grid(row=7, column=6)

ArkonorPrice.grid(row=0, column=4)
BistotPrice.grid(row=1, column=4)
CrokitePrice.grid(row=2, column=4)
DarkOchrePrice.grid(row=3, column=4)
GneissPrice.grid(row=4, column=4)
HedbergitePrice.grid(row=5, column=4)
HemorphitePrice.grid(row=6, column=4)
JaspetPrice.grid(row=7, column=4)


VeldsparLabel.grid(row=9, column=0)
ArkonorLabel.grid(row=9, column=1)
BistotLabel.grid(row=9, column=2)
CrokiteLabel.grid(row=9, column=3)
DarkOchreLabel.grid(row=9, column=4)
GneissLabel.grid(row=9, column=5)
HedbergiteLabel.grid(row=9, column=6)
HemorphiteLabel.grid(row=9, column=7)

JaspetLabel.grid(row=11, column=0)
KerniteLabel.grid(row=11, column=1)
MercoxitLabel.grid(row=11, column=2)
OmberLabel.grid(row=11, column=3)
PlagioclaseLabel.grid(row=11, column=4)
PyroxeresLabel.grid(row=11, column=5)
ScorditeLabel.grid(row=11, column=6)
SpodumainLabel.grid(row=11, column=7)

button_veldspar.grid(row=10, column=0, padx=5)
button_arkonor.grid(row=10, column=1, padx=5)
button_bistot.grid(row=10, column=2, padx=5)
button_crokite.grid(row=10, column=3, padx=5)
button_darkochre.grid(row=10, column=4, padx=5)
button_gneiss.grid(row=10, column=5, padx=5)
button_hedbergite.grid(row=10, column=6, padx=5)
button_hemorphite.grid(row=10, column=7, padx=5)

button_jaspet.grid(row=12, column=0, padx=5)
button_kernite.grid(row=12, column=1, padx=5)
button_mercoxit.grid(row=12, column=2, padx=5)
button_omber.grid(row=12, column=3, padx=5)
button_plagioclase.grid(row=12, column=4, padx=5)
button_pyroxeres.grid(row=12, column=5, padx=5)
button_scordite.grid(row=12, column=6, padx=5)
button_spodumain.grid(row=12, column=7, padx=5)

button_marketupdate.grid(row=8, column=1, padx=10, pady=10)
#button_quit.grid(row=8, column=2, pady=10)


root.mainloop()