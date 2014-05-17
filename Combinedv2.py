#Pokemon Storage
from math import *
from random import *
##import rgine

import sys
path = sys.path[0]
if not path: path = sys.path[1]
def STAB(PokeType,PokeType2,AttType):
    if PokeType==AttType or PokeType2==AttType:
        return 1.5
    else:
        return 1

def BonusCalc(typ,oppType,oppType2):
    bonus=1
    # effect=()
    for i in range(0,len(eval(typ+"Bonus")[typ])):
        if oppType==(eval(typ+"Bonus"))[typ][i][0]:
            bonus*=(eval(typ+"Bonus"))[typ][i][1]
            return bonus
    for i in range(0,len(eval(typ+"Bonus")[typ])):
        if oppType2!="NoType":
            if oppType2==(eval(typ+"Bonus"))[typ][i][0]:
                bonus*=(eval(typ+"Bonus"))[typ][i][1]
                return bonus
    return bonus

##    if bonus==0:
##        effect="had no effect."
##    if bonus==1/2:
##        effect="was not very effective."
##    if bonus==1:
##        effect==None
##    if bonus==2:
##        effect="was super effective!"
##    if bonus==4:
##        effect="was ultra effective!!!!"
##        
##        
##    return([bonus,"Your attack "+effect])
   

           
FirBonus={"Fir":[["Fir",1/2],["Wat",1/2],["Gra",2],["Ice",2],["Bug",2],["Roc",1/2],["Dra",1/2],["Ste",2]]}
NorBonus={"Nor":[["Roc",1/2],["Gho",0],["Ste",1/2]]}
WatBonus={"Wat":[["Fir",2],["Wat",1/2],["Gra",1/2],["Gro",2],["Roc",1/2],["Dra",1/2]]}
EleBonus={"Ele":[["Wat",2],["Ele",1/2],["Gra",1/2],["Gro",0],["Fly",2],["Dra",1/2]]}
GraBonus={"Gra":[["Fir",1/2],["Wat",1/2],["Gra",1/2],["Poi",1/2],["Gro",1/2],["Fly",1/2],["Bug",1/2],["Roc",1/2],["Dra",1/2]]}
IceBonus={"Ice":[["Fir",1/2],["Wat",1/2],["Grass",1/2],["Ice",1/2],["Poi",1/2],["Gro",2],["Fly",2],["Dra",2],["Ste",1/2]]}
FigBonus={"Fig":[["Nor",2],["Poi",1/2],["Fly",1/2],["Psy",1/2],["Roc",2],["Gho",0],["Dar",2],["Ste",2],["Fai",1/2]]}
PoiBonus={"Poi":[["Gra",2],["Poi",1/2],["Gro",1/2],["Roc",1/2],["Gho",1/2],["Ste",0],["Fai",2]]}
GroBonus={"Gro":[["Fir",2],["Ele",2],["Gra",1/2],["Poi",2],["Fly",0],["Bug",1/2],["Roc",2],["Ste",2]]}
FlyBonus={"Fly":[["Ele",1/2],["Gra",2],["Fig",2],["Bug",2],["Roc",1/2],["Ste",1/2]]}
PsycBonus={"Psy":[["Fig",2],["Poi",2],["Psy",1/2],["Dar",0],["Ste",1/2]]}
BugBonus={"Bug":[["Fir",1/2],["Gra",2],["Fig",1/2],["Poi",1/2],["Fly",1/2],["Psy",2],["Gho",1/2],["Dar",2],["Ste",1/2],["Fai",1/2]]}
RocBonus={"Roc":[["Fir",2],["Ice",2],["Poi",1/2],["Fly",2],["Gro",1/2],["Roc",2],["Ste",1/2]]}
GhoBonus={"Gho":[["Nor",0],["Fly",2],["Gho",2],["Dar",2]]}
DraBonus={"Dra":[["Dra",2],["Ste",1/2],["Fai",0]]}
DarBonus={"Dar":[["Fig",1/2],["Psy",2],["Gho",2],["Dar",1/2],["Fai",1/2]]}
SteBonus={"Ste":[["Fir",1/2],["Wat",1/2],["Ele",1/2],["Ice",1/2],["Roc",2],["Ste",1/2],["Fai",2]]}
FaiBonus={"Fai":[["Fir",1/2],["Fig",1/2],["Poi",1/2],["Dra",2],["Dar",2],["Ste",1/2]]}

def PokeName(code):
    return PokeStat[code][0]

def PokeType(code):
    if len(PokeStat[code][1])==1:
        return PokeStat[code][1]
    if len(PokeStat[code][1])==2:
        return PokeStat[code][2][0],PokeStat[number][1][1]
    
def Pokelevel(name):
  
    for i in range (len(UserPoke)):
        print(UserPoke[i][0][0])
        if UserPoke[i][0][0]==name:
            return trunc(UserPoke[i][2][0]/500)
        

def PokeAtkP(code):
    return PokeStat[number][3][1]

def PokeDefP(code):
    return PokeStat[number][3][1]

def PokeXPCalc(level):
    xp=level*500
    atkGain=level/2
    defGain=level/2
    return [xp,atkGain,defGain]

##class Pokemon(_object):
##    def __init__(self,name,typ,level):
##        pass


UserPoke=[[["Charmeleon"],["Fir"],[15100],[64,58],["Fire_Fang","Flamethrower","Slash","Double_Edge"],["Info"],["Charizard",36],[120]]]
opp=[[['Blubasaur'],["Gra","Poi"],[15000],[49,49],["Razor Leaf","Vine_Whip","Tackle","Double_Edge"],["A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon."],["Ivysaur"],[120]]]

PokeStat={1:[['Bulbasaur'],["Gra","Poi"],[],[49,49],["Razor_Leaf","Vine_Whip","Tackle","Double_Edge"],["A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon."],["Ivysaur",16]],

          2:[["Ivysaur"],["Gra","Poi"],[],[62,63],["Vine_Whip","Razor_Leaf","Mega_Drain","Poison Powder"],["When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower's coming bloom."],["Venasaur",32]],
          3:[["Venusaur"],["Gra","Poi"],[],[82,83],["Razor_Leaf","Giga_Drain","Solar_Beam","Double_Edge"],["By spreading the broad petals of its flower and catching the sun's rays, it fills its body with power."],["Final Stage of evolution"]],
          4:[["Charmander"],["Fir"],[],[52,43],["Scratch","Ember","Fire_Punch","Tackle"],["Info"],["Charmeleon",16]],
          5:[["Charmeleon"],["Fir"],[],[64,58],["Fire_Fang","Flamethrower","Slash","Double_Edge"],["Info"],["Charizard",36]],
          6:[["Charizard"],["Fir","Fly"],[],[84,78],["Fire_Blast", "Wing_Attack", "Flamethrower","Double_Edge"],["Info"],["Final Stage of evolution"]],
          7:[["Squirtle"],["Wat"],[],[48,65],["Tackle", "Bubble", "Water_Gun","Bite"],["Info"],["Wartortle",16]],
          8:[["Wartortle"],["Wat"],[0],[63,80],["Slam", "Water_Gun", "Bubblebeam","Crunch"],["Info"],["Blastoise",36]],
          9:[["Blastoise"],["Wat"],[0],[83,100],["Hydro_Pump","Ice_Beam","Crunch","Bubblebeam"],["Info"],["Final Stage of evolution"]],
          10:[["Caterpie"],["Bug"],[0],[30,35],["Tackle","String_Shot","Splash","Fury_Cutter"],["Info"],["Metapod",7]],
          11:[["Metapod"],["Bug"],[0],[25,50],[],["Tackle","String_Shot","Harden","Splash"],["Butterfree",10]],
          12:[["Butterfree"],["Bug","Fly"],[0],[45,50],["Psybeam","Gust","Confusion","Silver_Wind"],["Info"],["Final Stage of Evolution"]],
          13:[["Weedle"],["Bug","Poi"],[0],[35,30],["Tackle","String Shot","Splash","Poison Sting"],["info"],["Kakuna",7]],
          14:[["Kakuna"],["Bug","Poi"],[],[25,50],["Tackle","String_Shot","Poison_Sting","Harden"],["Beedrill",10]],
          15:[["Beedrill"],["Bug","Poi"],[],[90,40],["Poison_Jab","Silver_Wind","Fury_Attack","Headbutt"],["Final Stage of Evolution"]],
          16:[["Pidgey"],["Fly","Nor"],[],[45,40],["Tackle","Gust","Quick_Attack","Wing_Attack"],["Pidgeotto",18]],
          17:[["Pidgeotto"],["Fly","Nor"],[],[60,55],["Wing Attack","Quick_Attack","Peck","Secret_Power"],["Pidgeot",36]],
          18:[["Pidgeot"],["Fly","Nor"],[],[80,75],["Drill_Peck","Wing_Attack","Secret_Power","Hyper_Beam"],["Final Stage of Evolution"]],
          19:[["Rattata"],["Nor"],[],[56,35],["Bite","Hyper Fang","Tackle","Quick Attack"],["Raticate",20]],
          20:[["Raticate"],["Nor"],[],[81,60],["Super_Fang","Hyper_Fang","Secret_Power","Quick_Attack"],["Final Stage of Evolution"]],
          21:[["Spearow"],["Nor","Fly"],[],[60,30],["Peck","Wing_Attack","Quick_Attack","Aerial Ace"],["Fearow",20]],
          22:[["Fearow"],["Nor","Fly"],[],[90,65],["Drill_Peck","Pluck","Quick_Attack"],["Final Stage of Evolution"]],
          23:[["Ekans"],["Poi"],[],[60,44],["Wrap","Poison_Sting","Bite","Acid"],["Arbok",22]],
          24:[["Arbok"],["Poi"],[],[85,69],["Poison_Fang","Poison_Sting","Wrap","Mud_Bomb"],["Final Stage of Evolution"]],
          25:[["Pikachu"],["Ele"],[],[55,40],["Thundershock","Shock_Wave","Quick_Attack","Slam"],["Raichu","Thunder_Stone"]],
          26:[["Raichu"],["Ele"],[],[90,55],["Thunderbolt","Shock_Wave","Slam","Facade"],["Final Stage of Evolution"]],
          27:[["Sandshrew"],["Gro"],[],[75,85],["Dig","Scratch","Mud_Slap","Tackle"],["Sandslash",22]],
          28:[["Sandslash"],["Gro"],[],[100,110],["Dig","Slash","Facade","Quick_Attack"],["Final Stage of Evolution"]],
          29:[["NidoranF"],["Poi","Gro"],[],[47,52],["Poison_Sting","Quick_Attack","Double _Kick","Fury_Swipes"],["Nidorina",16]],
          30:[["Nidorina"],["Poi","Gro"],[],[62,67],["Poison_Fang","Poison_Sting","Double_Kick","Horn Attack"],["Nidoqueen"]],
          31:[["Nidoqueen"],["Poi","Gro"],[],[92,87],["Double Kick","Earthquake","Poison_Sting","Stomp"],["Final Stage of Evolution","Moon_Stone"]],
          32:[["NidoranM"],["Poi","Gro"],[],[57,40],["Poison_Sting","Horn_Attack","Tackle","Dig"],["Nidorino",16]],
          33:[["Nidorino"],["Poi","Gro"],[],[72,57],["Double_Kick","Horn_Attack","Dig","Take_Down"],["Nidoking","Moon_Stone"]],
          34:[["Nidoking"],["Poi","Gro"],[],[102,77],["Earthquake","Megahorn","Horn_Attack","Mega_Kick"],["Clefable"]],
          35:[["Clefairy"],["Fai"],[],[45,48],["Doubleslap","Pound","Quick_Attack","Sing"],["Clefable","Moon_Stone"]],
          36:[["Clefable"],["Fai"],[],[70,73],["Doubleslap","Secret_Power","Facade","Sing"],["Final Stage of Evolution"]],
          37:[["Vulpix"],["Fir"],[],[41,40],["Ember","Confuse_Ray","Quick_Attack","Leer"],["Ninetales","Fire_Stone"]],
          38:[["Ninetales"],["Fir"],[],[76,75],["Flamethrower","Confuse_Ray","Screech","Fire_Spin"],["Final Stage of Evolution"]],
          39:[["Jigglypuff"],["Nor","Fai"],["Sing","Pound","Doubleslap","Secret_Power"],[45,20],[],["Wigglytuff","Moon_Stone"]],
          40:[["Wigglytuff"],["Nor","Fai"],[],[70,45],["Sing","Doubleslap","Facade","Double_Team"],["Final Stage of Evolution"]],
          41:[["Zubat"],["Poi","Fly"],[],[45,35],["Confuse_Ray","Wing Attack","Leech_Life","Tackle"],["Golbat",22]],
          42:[["Golbat"],["Poi","Fly"],[],[80,70],["Confuse_Ray","Air_Cutter","Wing_Attack","Poison_Fang"],["Final "
                                                                                                            "Stage of Evolution"]],
          43:[["Oddish"],["Gra","Poi"],[],[50,55],["Sleep_Powder","Poisonpowder","Absorb","Pound"],["Gloom",21]],
          44:[["Gloom"],["Gra","Poi"],[],[65,70],["Sleep_Powder","Mega_Drain","Absorb","Slam"],["Vineplume","Leaf_Stone"]],
          45:[["Vineplume"],["Gra","Poi"],[],[80,85],["Giga_Drain","Acid","Slam","Sleep_Powder"],["Final Stage of Evolution"]],
          46:[["Paras"],["Gra","Bug"],[],[70,55],["Scratch","Fury_Cutter","Tackle","Leech_Life"],["Parasect",24]],
          47:[["Parasect"],["Gra","Bug"],[],[95,80],["Fury_Cutter","Signal_Beam","Cut","Slash"],["Final Stage of Evolution"]],
          48:[["Venonat"],["Poi","Bug"],[],[55,50],["Poisonpowder","Tackle","Acid","Confusion"],["Venomoth",31]],
          49:[["Venomoth"],["Poi","Bug"],[],[65,60],["Wing_Attack","Silver_Wind","Acid","Signal_Beam"],["Final Stage of Evolution"]],
          50:[["Diglett"],["Gro"],[],[55,25],["Dig","Scratch","Leer","Quick_Attack"],["Dugtrio",26]],
          51:[["Dugtrio"],["Gro"],[],[80,50],["Dig","Slash","Slam","Earth_Power"],["Final Stage of Evolution"]],
          52:[["Meowth"],["Nor"],[],[45,35],[],["Scratch","Quick_Attack","Growl","Pay_Day"],["Persian",28]],
          53:[["Persian"],["Nor"],[],[70,60],["Slash","Secret_Power","Pay_Day","Screech"],["Final Stage of Evolution"]],
          54:[["Psyduck"],["Wat"],[],[52,48],["Confusion","Water_Gun","Scratch","Confuse_Ray"],["Golduck",33]],
          55:[["Golduck"],["Wat"],[],[82,78],["Confusion","Bubblebeam","Slash","Brine"],["Final Stage of Evolution"]],
          56:[["Mankey"],["Fig"],[],[80,35],["Low_Kick","Scratch","Thrash","Karate_Chop"],["Primeape",28]],
          57:[["Primeape"],["Fig"],[],[105,60],["Cross_Chop","Brick_Break","Scratch","Leer"],["Final Stage of Evolution"]],
          58:[["Growlithe"],["Fir"],[],[70,45],["Ember","Quick_Attack","Flame_Wheel","Growl"],["Arcanine","Fire_Stone"]],
          59:[["Arcanine"],["Fir"],[],[110,80],["Flame_Wheel","Flamethrower","Extremespeed","Screech"],["Final Stage of Evolution"]],
          60:[["Poliwag"],["Wat"],[],[50,40],["Bubble","Water_Gun","Hypnosis","Pound"],["Poliwhirl",25]],
          61:[["Poliwhirl"],["Wat"],[],[65,65],["Bubblebeam","Water_Gun","Hypnosis","Slam"],["Poliwrath","Water_Stone"]],
          62:[["Poliwrath"],["Wat","Fig"],[],[95,95],["Surf","Mega_Punch","Water_Gun","Hypnosis"],["Final Stage of Evolution"]],
          63:[["Abra"],["Psy"],[],[20,15],["Confusion","Teleport","Scratch","Psywave"],["Kadabra",16]],
          64:[["Kadabra"],["Psy"],[],[35,30],["Confusion","Psybeam","Psywave","Thundershock"],["Alakazam",32]],
          65:[["Alakazam"],["Psy"],[],[50,45],["Psychic","Psybeam","Thunderbolt","Calm Mind"],["Final Stage of Evolution"]],
          66:[["Machop"],["Fig"],[],[80,50],["Karate_Chop","Low_Kick","Comet_Punch","Body_Slam"],["Machoke",28]],
          67:[["Machoke"],["Fig"],[],[100,70],["Karate_Chop","Body_Slam","Mach_Punch","Fire_Punch"],["Machamp",40]],
          68:[["Machamp"],["Fig"],[],[130,80],["Cross_Chop","Seismic_Toss","Fire_Punch","Thunder_Punch"],["Final Stage of Evolution"]],
          69:[["Bellsprout"],["Gra","Poi"],[],[75,35],["Vine_Whip","Absorb","Wrap","Bind"],["Weepinbell",21]],
          70:[["Weepinbell"],["Gra","Poi"],[],[90,50],["Vine_Whip","Razor_Leaf","Sleep_Powder","Acid"],["Victreebel","Leaf_Stone"]],
          71:[["Victreebel"],["Gra","Poi"],[],[105,65],["Razor_Leaf","Acid","Sludge","Solarbeam"],["Final Stage of Evolution"]],
          72:[["Tentacool"],["Wat","Poi"],[],[40,35],["Acid","Water_Gun","Constrict","Wrap"],["Tentacruel",30]],
          73:[["Tentacruel"],["Wat","Poi"],[],[70,65],["Acid","Bubblebeam","Sludge","Constrict"],["Final Stage of Evolution"]],
          74:[["Geodude"],["Roc","Gro"],[],[80,100],["Rock_Throw","Magnitude","Tackle","Rollout"],["Graveler",25]],
          75:[["Graveler"],["Roc","Gro"],[],[95,115],["Rock_Throw","Magnitude","Slam","Harden"],["Golem",35]],
          76:[["Golem"],["Roc","Gro"],[],[120,130],["Earth_Power","Rock Slide","Dig","Rollout"],["Final Stage of Evolution"]],
          77:[["Ponyta"],["Fir"],[],[85,55],["Ember","Fire_Spin","Stomp","Quick Attack"],["Final Stage of Evolution",40]],
          78:[["Rapidash"],["Fir"],[],[100,70],["Stomp","Fire_Spin","Flame_Wheel","Extremespeed"],["Final Stage of Evolution"]],
          79:[["Slowpoke"],["Wat","Psy"],[],[65,65],["Confusion","Water_Gun","Tail_Whip","Bubble"],["Slowbro",37]],
          80:[["Slowbro"],["Wat","Psy"],[],[75,110],["Confusion","Water_Gun","Bubble","Confuse_Ray"],["Final Stage of "
                                                                                                      "Evolution"]],
          81:[["Magnemite"],["Ele","Ste"],[],[35,70],["Thundershock","Tackle","Thunder_Wave","Sonicboom"],["Magneton",30]],
          82:[["Magneton"],["Ele","Ste"],[],[60,95],["Thunderbolt","Sonicboom","Mirror_Shot","Magnet_Bomb"],["Final Stage of Evolution"]],
          83:[["Farfetch'd"],["Fly","Nor"],[],[65,55],["Wing_Attack","Quick_Attack","Cut","False_Swipe"],["Final Stage of Evolution"]],
          84:[["Dodou"],["Fly","Nor"],[],[110,70],["Peck","Fury_Attack","Stomp","Quick_Attack"],["Dodrio",31]],
          85:[["Dodrio"],["Fly","Nor"],[],[110,70],['Drill_Peck','Peck','Extremespeed','Stomp'],["Final Stage of Evolution"]],
          86:[["Seel"],["Wat","Ice"],[],[45,55],["Aurora_Beam",'Water_Gun','Body_Slam','Powder_Snow'],["Dewgong",34]],
          87:[["Dewgong"],["Wat","Ice"],[],[70,80],["Surf","Ice_Beam","Body_Slam","Aqua_Tail"],["Final Stage of Evolution"]],
          88:[["Grimer"],["Poi"],[],[80,50],["Tackle","Poison_Gas","Mud_Slap","Sludge"],["Muk",38]],
          89:[["Muk"],["Poi"],[],[105,75],["Sludge","Sludge_Bomb","Pound","Toxic"],["Final Stage of Evolution"]],
          90:[["Shellder"],["Wat","Ice"],[],[65,100],["Aurora_Beam","Water_Gun","Withdraw","Tackle"],["Cloyster","Water_Stone"]],
          91:[["Cloyster"],["Wat","Ice"],[],[95,180],["Water_Gun","Aurora_Beam","Ice_Beam","Spike_Cannon"],["Final Stage of Evolution"]],
          92:[["Gastly"],["Gho","Poi"],[],[35,30],["Lick","Hypnosis","Night_Shade","Confuse_Ray"],["Haunter",25]],
          93:[["Haunter"],["Gho","Poi"],[],[50,45],["Hypnosis","Poison_Gas","Shadow_Ball","Sucker_Punch"],["Gengar",40]],
          94:[["Gengar"],["Gho","Poi"],[],[65,60],["Hypnosis","Sludge_Bomb","Shadow_Ball","Sucker_Punch"],["Final Stage of Evolution"]],
          95:[["Onix"],["Roc","Gro"],[],[45,160],["Bind","Rock_Throw","Slam","Rock_Tomb"],["Final Stage of Evolution"]],
          96:[["Drowzee"],["Psy"],[],[48,45],["Confusion","Hypnosis","Pound","Body_Slam"],["Hypno"]],
          97:[["Hypno"],["Psy"],[],[73,70],["Psychic","Headbutt","Zen_Headbutt","Psybeam"],["Final Stage of Evolution"]],
          98:[["Krabby"],["Psy"],[],[105,90],["Water_Gun","Vicegrip","Cut","Bubble"],["Kingler",28]],
          99:[["Kingler"],["Psy"],[],[130,115],["Bubblebeam","Crabhammer","Vicegrip","Metal_Claw"],["Final Stage of Evolution"]],
          100:[["Voltorb"],["Ele"],[],[50,70],["Sonicboom","Explosion","Spark","Rollout"],["Electrode",30]],
          101:[["Electrode"],["Ele"],[],[50,70],["Explosion","Spark","Thunderbolt","Charge_Beam"],["Final Stage of Evolution"]],
          102:[["Exeggcute"],["Ele"],[],[40,80],["Uproar","Bullet_Seed","Sleep_Powder","Confusion"],["Exeggutor","Leaf_Stone"]],
          103:[["Exeggutor"],["Ele"],[],[95,85],["Hypnosis","Confusion","Psychic","Razor_Leaf"],["Final Stage of Evolution"]],
          104:[["Cubone"],["Ground"],[],[50,95],["Headbutt","Bone_Club","Bonemerang","False_Swipe"],["Marowak",28]],
          105:[["Marowak"],["Ground"],[],[80,110],["Bonemerang","Headbutt","Thrash","Dig"],["Final Stage of Evolution"]],
          106:[["Hitmonlee"],["Fig"],[],[120,53],["Double_Kick","Rolling_Kick","Jump_Kick","Brick_Break"],["Final Stage of Evolution"]],
          107:[["Hitmonchan"],["Fig"],[],[105,79],["Ice_Punch","Mach_Punch","Thunderpunch","Fire_Punch"],["Final Stage of Evolution"]],
          108:[["Lickitung"],["Nor"],[],[55,75],["Rollout","Lick","Secret_Power","Wrap"],["Final Stage of Evolution"]],
          109:[["Koffing"],["Poi"],[],[65,95],["Poison_Gas","Smog","Sludge","Assurance"],["Weezing",34]],
          110:[["Weezing"],["Poi"],[],[90,120],["Sludge","Poison_Gas","Smog","Smokescreen"],["Final Stage of Evolution"]],
          111:[["Rhyhorn"],["Gro","Roc"],["Horn_Attack","Rock_Throw","Take_Down","Rock_Blast"],[85,90],[],["Rhydon",42]],
          112:[["Rhydon"],["Gro","Roc"],[],[130,120],["Stone_Edge","Megahorn","Rock_Blast","Stomp"],["Final Stage of Evolution"]],
          113:[["Chansey"],["Nor"],[],[5,5],["Pound","Softboiled","Doubleslap","Sing"],["Final Stage of Evolution"]],
          114:[["Tangla"],["Gra"],[],[55,115],["Ancientpower","Vine Whip","Absorb","Pound"],["Final Stage of Evolution"]],
          115:[["Kangaskhan"],["Nor"],[],[95,80],["Comet_Punch","Fake_Out","Bite","Mega_Punch"],["Final Stage of "
                                                                                                 "Evolution"]],
          116:[["Horsea"],["Wat"],[],[40,70],["Water_Gun","Bubble","Pound","Twister"],["Final Stage of Evolution",32]],
          117:[["Seadra"],["Wat"],["Bubblebeam","Dragon_Rage","Leer","Water_Gun"],[65,95],[],["Final Stage of Evolution"]],
          118:[["Goldeen"],["Wat"],[],[67,60],["Bubble","Pound","Horn_Attack","Water_Gun"],["Final Stage of Evolution",33]],
          119:[["Seaking"],["Wat"],[],[92,65],["Drill_Peck","Horn_Attack","Surf","Bubble"],["Final Stage of Evolution"]],
          120:[["Staryu"],["Wat","Psy"],[],[45,55],["Water_Gun","Rapid_Spin","Bubble","Slam",],["Starmie","Water_Stone"]],
          121:[["Starmie"],["Wat","Psy"],[],[75,85],["Rapid_Spin","Surf","Aurora_Beam","Confusion"],["Final Stage of Evolution"]],
          122:[["Mr.Mime"],["Fai","Psy"],[],[45,65],["Confusion","Pound","Doubleslap","Psychic"],["Final Stage of Evolution"]],
          123:[["Scyther"],["Bug","Fly"],[],[45,65],["Slash","Fury_Cutter","False_Swipe","Wing_Attack"],["Final Stage of Evolution"]],
          124:[["Jynx"],["Psy","Ice"],[],[50,35],["Confusion","Ice_Punch","Lovely_Kiss","Powder_Snow"],["Final Stage of Evolution"]],
          125:[["Elecabuzz"],["Ele"],[],[83,57],["Thunderpunch","Quick_Attack","Take_Down","Shock_Wave"],["Final Stage of Evolution"]],
          126:[["Magmar"],["Fir"],[],[95,57],["Fire_Punch","Smog","Ember","Mega_Punch"],["Final Stage of Evolution"]],
          127:[["Pinsir"],["Bug"],[],[120,100],["Vicegrip","Bind","Brick_Break","Cut"],["Final Stage of Evolution"]],
          128:[["Tauros"],["Nor"],[],[100,95],["Stomp","Take_Down","Mud_Shot","Horn_Attack"],["Final Stage of Evolution"]],
          129:[["Magikarp"],["Wat"],[],[10,55],["Splash","Tackle","Splash","Splash"],["Gyarados",20]],
          130:[["Gyarados"],["Wat","Fly"],[],[155,109],["Waterfall","Thrash",'Aerial_Ace',"Water_Pulse"],["Final Stage of Evolution"]],
          131:[["Lapras"],["Wat","Ice"],[],[85,80],["Ice_Beam","Surf","Water_Gun","Confuse_Ray"],["Final Stage of Evolution"]],
          132:[["Ditto"],["Nor"],[],[48,48],["Pound","Tackle","Slam","Secret_Power"],["Final Stage of Evolution"]],
          133:[["Eevee"],["Nor"],[],[55,50],["Quick_Attack","Secret_Power","Iron_Tail","Tackle"],[["Vaporeon","Water_Stone"],["Flareon","Fire_Stone"],["Jolteon","Thunder_Stone"]]],
          134:[["Vaporeon"],["Wat"],[],[65,60],["Aurora_Beam","Water_Gun","Aqua_Tail","Bubblebeam"],["Final Stage of Evolution"]],
          135:[["Jolteon"],["Ele"],[],[65,60],["Thundershock","Quick Attack","Shock Wave","Thunder Fang"],["Final Stage of Evolution"]],
          136:[["Flareon"],["Fir"],[],[130,60],["Ember","Quick_Attack","Flame_Wheel","Fire_Spin"],["Final Stage of Evolution"]],
          137:[["Porygon"],["Nor"],[],[60,70],["Confusion","Signal_Beam","Tackle","Rapid_Spin"],["Final Stage of Evolution"]],
          138:[["Omanyte"],["Roc","Wat"],[],[40,100],["Rock_Blast","Water_Gun","Rock_Throw","Bubble"],["Omastar",40]],
          139:[["Omastar"],["Roc","Wat"],[],[60,125],["Brine","Mud_Shot","Rock_Blast","Ancientpower"],["Final Stage of Evolution"]],
          140:[["Kabuto"],["Roc","Wat"],[],[80,90],["Rock_Blast","Water_Gun","Scratch","Leech Life",],["Kabutops",40]],
          141:[["Kabutops"],["Roc","Wat"],[],[115,105],["Slash","Rock_Slide","Water_Gun","False_Swipe"],["Final Stage of Evolution"]],
          142:[["Aerodactyl"],["Roc","Fly"],[],[105,65],["Rock_Slide","Air_Cutter","Aerial_Ace","Crunch"],["Final Stage of Evolution"]],
          143:[["Snorlax"],["Nor"],[],[110,65],["Rest","Body_Slam","Rollout","Crunch"],["Final Stage of Evolution"]],
          144:[["Articuno"],["Fly","Ice"],[],[85,100],["Ice_Beam","Sky_Attack","Blizzard","Confuse_Ray"],["Final Stage of Evolution"]],
          145:[["Zapdos"],["Fly","Ele"],[],[90,85],[],["Zap_Cannon","Thunderbolt","Drill_Peck","Discharge"]],
          146:[["Moltres"],["Fly","Fir"],[],[100,90],["Flamethrower","Sky_Attack","Solarbeam","Heat_Wave"],["Final Stage of Evolution"]],
          147:[["Dratini"],["Dra"],[],[64,45],["Wrap","Thunder_Wave","Twister","Dragon_Rage"],["Dragonair",30]],
          148:[["Dragonair"],["Dra"],[],[84,65],["Dragon Rage","Aqua Tail","Twister","Constrict"],["Dragonite",55]],
          149:[["Dragonite"],["Dra","Fly"],[],[134,95],["Dragon_Rage","Dragon_Claw","Hyper_Beam","Aqua Tail"],["Final "
                                                                                                               "Stage "
                                                                                                               "of Evolution"]],
          150:[["Mewtwo"],["Psy"],[],[110,90],["Psychic","Swift","Psycho_Cut","Aura_Sphere"],["Final Stage of Evolution"]],
          151:[["Mew"],["Fsy"],[],[100,100],["Psychic","Pyscho_Cut","Thunder","Ice_Beam"],["Final Stage of Evolution"]]}
print(PokeStat[10][4][0])
attack={
        
        "Bug_Bite":[["Bug"],[[60],[100],[20]],[None]],
        "Hard_Roller":[["Bug"],[[55],[95],[25]],[None]],
        "X-Scissor":[["Bug"],[[80],[100],[15]],[None]],
        "Leech_Life ":[["Bug"],[[20],[100],[15]],["LifeDrain",1/2]],
        "Pin_Missile":[["Bug"],[[[25],[85],[20]]],["Multi"]],
        "Fury_Cutter":[["Bug"],[[40],[95],[20]],["TempPowInc"]],
        "String_Shot":[["Bug"],[[25],[95],[40]],[None]],
        "Megahorn":[["Bug"],[[120],[85],[10]],[None]],
        "Silver_Wind":[["Bug"],[[60],[100],[5]],["AllRaise",1/10]],
        "Signal_Beam":[["Bug"],[[75],[100],[15]],["Confuse",1/10]],
        "Bug_Buzz":[["Bug"],[[90],[100],[10]],["OpAtkDec",1/10]],

        "Crunch":[["Dar"],[[80],[100],[15]],["OpDefDec",1/5]],
        "Dark_Pulse":[["Dar"],[[60],[100],[20]],["Flinch",1/5]],
        "Beat_Up":[["Dar"],[[50],[90],[20]],[None]],
        "Fake_Out":[["Dar"],[[40],[100],[10]],["Flinch",1]],
        "Payback":[["Dar"],[[50],[100],[10]],[None]],
        "Persuit":[["Dar"],[[60],[100],[20]],[None]],
        "Sucker_Punch":[["Dar"],[[80],[100],[5]],[None]],
        "Assurance":[["Dar"],[[60],[100],[10]],[None]],
        "Bite":[["Dar"],[[60],[100],[25]],["Flinch",3/10]],

        "Draco_Meteor":[["Dra"],[[130],[90],[5]],[None]],
        "Dragon_Rage":[["Dra"],[[50],[100],[10]],["SetDamage",40]],
        "Dragon_Tail":[["Dra"],[[60],[90],[10]],["Swap"]],
        "Dragon Claw":[["Dra"],[[80],[100],[15]],[None]],
        "Outrage":[["Dra"],[[120],[100],[10]],[None]],
        "Dragon_Breath":[["Dra"],[[60],[100],[20]],["Para",3/10]],
        "Dragon_Pulse":[["Dra"],[[85],[100],[10]],[None]],
        "Dragon_Rush ":[["Dra"],[[100],[75],[10]],["Flinch",1/5]],
        "Twister":[["Dra"],[[50],[90],[20]],[None]],
        "Beat_Up":[["Dra"],[[40],[100],[20]],["Flinch",1/5]],
        "Discharge":[["Ele"],[[80],[100],[15]],["Para",3/10]],
        "Electro_Ball":[["Ele"],[[60],[100],[20]],[None]],
        "Zap_Cannon":[["Ele"],[[120],[50],[5]],["Para",1]],

        "Thunder":[["Ele"],[[110],[70],[10]],["Para",3/10]],
        "Electro_Web":[["Ele"],[[55],[95],[15]],[None]],
        "Thunder_Wave":[["Ele"],[[0],[100],[20]],["Para",1]],
        "Bolt_Strike":[["Ele"],[[130],[85],[5]],["Para",2/5]],
        "ThunderShock":[["Ele"],[[40],[100],[30]],["Para",1/10]],
        "Shock_Wave":[["Ele"],[[65],[95],[15]],[["Para",1/10],["Flinch",1/10]]],
        "Thunder Fang":[["Ele"],[[90],[100],[15]],[None]],
        "Spark":[["Ele"],[[65],[100],[20]],["Para",3/10]],
        "Charge Beam":[["Ele"],[[50],[90],[10]],["AtkInc",7/10]],
        "Thunderpunch":[["Ele"],[[75],[100],[15]],["Para",1/10]],
        "Volt_Tackle":[["Ele"],[[120],[100],[15]],["Para",1/10],["Rec",1/4]],

        "Triple_Kick":[["Fig"],[[40],[90],[10]],[None]],
        "Seismic_Toss":[["Fig"],[[0],[100],[20]],["LevelDamage"]],
        "Cross_Chop":[["Fig"],[[100],[80],[5]],["HighCrit"]],
        "Rolling_Kick":[["Fig"],[[60],[85],[15]],["Para",3/10]],
        "Jump_Kick":[["Fig"],[[40],[90],[10]],["Rec",1/3]],
        "Aura_Sphere":[["Fig"],[[80],[100],[20]],[None]],
        "Mach_Punch":[["Fig"],[[40],[100],[30]],[None]],
        "Dynamic_Punch":[["Fig"],[[100],[50],[5]],["Confuse",1]],
        "Hammer_Arm":[["Fig"],[[100],[90],[10]],[None]],
        "Focus_Punch":[["Fig"],[[60],[100],[10]],[None]],
        "Revenge":[["Fig"],[[40],[90],[10]],[None]],
        "Drain_Punch":[["Fig"],[[75],[100],[10]],["LifeDrain",1/2]],
        "Sky_Uppercut":[["Fig"],[[85],[90],[15]],["Reach"]],
        "Superpower":[["Fig"],[[120],[100],[5]],[["AtkDec",1/3],["DefDec",1/3]]],
        "Force_Palm":[["Fig"],[[60],[100],[10]],["Para",3/10]],
        "Brick_Break":[["Fig"],[[75],[100],[15]],[None]],
        "Sacred_Sword":[["Fig"],[[90],[100],[20]],[None]],
        "Karate_Chop":[["Fig"],[[50],[100],[25]],["HighCrit"]],

        "Fire_Fang":[["Fir"],[[65],[95],[15]],[["Flinch",1/10],["Burn",1/10]]],
        "Flare_Blitz":[["Fir"],[[120],[100],[15]],[["Rec",1/4],["Burn",1/10]]],
        "Incinerate":[["Fir"],[[60],[100],[15]],[None]],
        "Flame_Wheel":[["Fir"],[[60],[100],[25]],["Burn",1/10]],
        "Flamethrower":[["Fir"],[[90],[100],[15]],["Burn",1/10]],
        "Flame_Burst":[["Fir"],[[70],[100],[15]],[None]],
        "Fire_Blast":[["Fir"],[[110],[85],[5]],["Burn",1/10]],
        "Eruption":[["Fir"],[[150],[100],[5]],[None]],
        "Lava_Plume":[["Fir"],[[80],[100],[15]],["Burn",3/10]],
        "Fire_Punch":[["Fir"],[[75],[100],[15]],["Burn",1/10]],
        "Sacred_Fire":[["Fir"],[[100],[90],[10]],[None]],
        "Overheat":[["Fir"],[[40],[95],[5]],["Burn",1/2]],
        "Blue_Flare":[["Fir"],[[130],[85],[5]],["Burn",1/5]],
        "Heat_Wave":[["Fir"],[[95],[90],[10]],["Burn",1/10]],
        "Fire_Spin":[["Fir"],[[35],[85],[15]],["Trap"]],

        "Air_Cutter":[["Fly"],[[60],[95],[25]],["HighCrit"]],
        "Acrobatics":[["Fly"],[[55],[100],[15]],[None]],
        "Gust":[["Fly"],[[40],[100],[35]],[None]],
        "Bounce":[["Fly"],[[85],[85],[5]],["Para",3/10],["Charge"]],
        "Pluck":[["Fly"],[[60],[100],[20]],[None]],
        "Brave_Bird":[["Fly"],[[120],[100],[15]],["Rec",1/4]],
        "Peck":[["Fly"],[[35],[100],[35]],[None]],
        "Wing_Attack":[["Fly"],[[60],[100],[35]],[None]],
        "Sky_Attack":[["Fly"],[[140],[90],[5]],["Charge"]],
        "Drill_Peck":[["Fly"],[[80],[100],[20]],[None]],
        "Fly":[["Fly"],[[90],[95],[15]],["Charge"]],
        "Air_Slash":[["Fly"],[[75],[95],[20]],["Flinch",3/10]],
        "Aeroblast":[["Fly"],[[100],[95],[5]],[None]],
        "Aerial_Ace":[["Fly"],[[60],[100],[20]],["HighCrit"]],

        "Hypnosis":[["Gho"],[[0],[60],[20]],["Sleep",1]],
        "Confuse_Ray":[["Gho"],[[0],[100],[10]],["Confuse",1]],
        "Shadow_Punch":[["Gho"],[[60],[100],[20]],[None]],
        "Shadow_Ball":[["Gho"],[[80],[100],[15]],["OpDefDec"]],
        "Night_Shade":[["Gho"],[[0],[100],[15]],["LevelDamage"]],
        "Ominous_Wind":[["Gho"],[[60],[100],[5]],["AllRaise",1/10]],
        "Lick":[["Gho"],[[30],[100],[30]],["Para",3/10]],
        "Astonish":[["Gho"],[[30],[100],[15]],["Flinch",3/10]],
        "Shadow_Sneak":[["Gho"],[[40],[100],[30]],[None]],
        "Evil_Eye":[["Gho"],[[80],[100],[20]],[None]],

        "Bullet_Seed":[["Gra"],[[20],[100],[30]],["Multi"]],
        "Solarbeam":[["Gra"],[[120],[100],[10]],["Charge"]],
        "Petal_Dance":[["Gra"],[[120],[100],[10]],[None]],
        "Stun_Spore":[["Gra"],[[0],[75],[30]],["Para",1]],
        "Poisonpowder":[["Gra"],[[0],[75],[35]],["Pois",1]],
        "Mega_Drain":[["Gra"],[[40],[100],[15]],["LifeDrain",1/2]],
        "Grass_Knot":[["Gra"],[[60],[100],[20]],[None]],
        "Leech_Seed":[["Gra"],[[0],[90],[10]],["DoTDrain"]],
        "Frenzy_Plant":[["Gra"],[[150],[90],[6]],["Charge"]],
        "Absorb":[["Gra"],[[20],[100],[25]],["LifeDrain",1/2]],
        "Leaf_Storm":[["Gra"],[[130],[90],[5]],["AtkDec"]],
        "Power_Whip":[["Gra"],[[120],[85],[5]],[None]],
        "Giga_Drain":[["Gra"],[[75],[100],[10]],["LifeDrain",1/2]],
        "Needle_Arm":[["Gra"],[[60],[100],[15]],["Flinch",3/10]],
        "Seed_Bomb":[["Gra"],[[80],[100],[15]],[None]],
        "Leaf_Blade":[["Gra"],[[90],[100],[15]],["HighCrit"]],
        "Vine_Whip":[["Gra"],[[45],[100],[25]],[None]],
        "Razor_Leaf":[["Gra"],[[55],[95],[25]],["HighCrit"]],
        "Magical_Leaf":[["Gra"],[[60],[100],[20]],[None]],
        "Sleep_Powder":[["Gra"],[[0],[75],[15]],["Sleep",1]],

        "Magnitude":[["Gro"],[[60],[100],[30]],[None]],
        "Mud_Shot":[["Gro"],[[55],[95],[15]],[None]],
        "Sand_Attack":[["Gro"],[[0],[100],[15]],["OpAccDec"]],
        "Sand_Tomb":[["Gro"],[[60],[100],[20]],["Trap"]],
        "Bone_Rush":[["Gro"],[[25],[90],[10]],["Multi"]],
        "Bone_Club":[["Gro"],[[65],[85],[20]],["Flinch",1/10]],
        "Bonemerang":[["Gro"],[[50],[90],[10]],["Multi",2]],
        "Earthquake":[["Gro"],[[100],[100],[10]],[None]],
        "Earth_Power":[["Gro"],[[90],[100],[10]],[None]],
        "Dig":[["Gro"],[[80],[100],[10]],[None]],
        "Mud_Bomb":[["Gro"],[[65],[85],[10]],[None]],

        "Ice_Punch":[["Ice"],[[75],[100],[15]],["Freeze",1/10]],
        "Avalanche":[["Ice"],[[60],[100],[10]],[None]],
        "Ice_Shard":[["Ice"],[[40],[100],[30]],[None]],
        "Icicle_Spear":[["Ice"],[[25],[100],[30]],["Multi"]],
        "Ice_Fang":[["Ice"],[[65],[95],[15]],[["Flinch",1/10],["Freeze",1/10]]],
        "Icy_Wind":[["Ice"],[[55],[95],[15]],[None]],
        "Powder_Snow":[["Ice"],[[40],[100],[25]],["Freeze",1/10]],
        "Blizzard":[["Ice"],[[110],[70],[5]],["Freeze",1/10]],
        "Aurora_Beam":[["Ice"],[[65],[100],[20]],[None]],
        "Ice_Beam":[["Ice"],[[90],[100],[10]],["Freeze",1/10]],

        "Slam":[["Nor"],[[80],[75],[20]],[None]],
        "Explosion":[["Nor"],[[250],[100],[5]],["Nuke"]],
        "Wrap":[["Nor"],[[15],[90],[20]],["Trap"]],
        "Razor_Wind":[["Nor"],[[80],[100],[10]],["HighCrit"]],
        "Headbutt":[["Nor"],[[70],[100],[15]],["Flinching",1/3]],
        "Horn_Drill":[["Nor"],[[0],[0],[5]],["VariableInstakill"]],
        "Bind":[["Nor"],[[15],[85],[20]],["Trap"]],
        "Growl":[["Nor"],[[0],[100],[40]],["OpAtkDec"]],
        "Facade":[["Nor"],[[70],[100],[20]],["DoubleGain"]],
        "Sing":[["Nor"],[[0],[55],[15]],["Sleep",1]],
        "Softboiled":[["Nor"],[[0],[0],[10]],["HealthGain"]],
        "Rage":[["Nor"],[[20],[100],[20]],["AtkInc"]],
        "Retaliation":[["Nor"],[[70],[100],[5]],[None]],
        "Skull_Bash":[["Nor"],[[130],[100],[10]],["Charge","DefInc"]],
        "Last_Resort":[["Nor"],[[140],[100],[5]],["LastMove"]],
        "Egg_Bomb":[["Nor"],[[100],[75],[10]],[None]],
        "Leer":[["Nor"],[[0],[100],[30]],["OpDefDec"]],
        "Fury_Attack":[["Nor"],[[15],[85],[20]],["Multi"]],
        "Body_Slam":[["Nor"],[[85],[100],[15]],["Para",3/10]],
        "Crush_Claw":[["Nor"],[[75],[95],[10]],["OpDefDec",1/2]],
        "Take_Down":[["Nor"],[[90],[85],[20]],["Rec",1/4]],
        "Double_Slap":[["Nor"],[[15],[85],[10]],["Multi"]],
        "Double_Hit":[["Nor"],[[35],[90],[10]],["DoubleHit"]],
        "Secret_Power":[["Nor"],[[70],[100],[20]],[None]],
        "Fury_Swipes":[["Nor"],[[18],[80],[15]],["Multi"]],
        "Slash":[["Nor"],[[70],[100],[20]],["HighCrit"]],
        "Swords_Dance":[["Nor"],[[40],[10],[30]],["AtkInc"]],
        "Tackle":[["Nor"],[[50],[100],[35]],[None]],
        "Extremespeed":[["Nor"],[[80],[100],[5]],[None]],
        "Tail_Whip":[["Nor"],[[0],[100],[30]],["OpDefDec"]],
        "Pound":[["Nor"],[[120],[100],[15]],[None]],
        "Double_Edge":[["Nor"],[[40],[10],[30]],["Rec",1/3]],
        "Rock_Climb":[["Nor"],[[90],[85],[20]],["Confuse",1/5]],
        "Dizzy_Punch":[["Nor"],[[70],[100],[10]],["Confuse",1/5]],
        "Hyper_Beam":[["Nor"],[[150],[90],[5]],["Charge"]],
        "Screech":[["Nor"],[[0],[85],[40]],["OpDefDec"]],
        "Scratch":[["Nor"],[[40],[100],[35]],[None]],
        "Smokescreen":[["Nor"],[[0],[100],[20]],["OpAccDec"]],
        "Giga_Impact":[["Nor"],[[150],[90],[5]],["Charge"]],
        "False_Swipe":[["Nor"],[[40],[100],[40]],["NoKill"]],
        "Pay_Day":[["Nor"],[[40],[100],[20]],["Payday"]],
        "Hyper_Voice":[["Nor"],[[90],[100],[10]],[None]],
        "Supersonic":[["Nor"],[[0],[55],[20]],["Confuse",1]],
        "Guillotine":[["Nor"],[[0],[0],[5]],["Nuke"]],
        "Mega_Kick":[["Nor"],[[120],[75],[5]],[None]],
        "Comet_Punch":[["Nor"],[[90],[100],[10]],[None]],
        "Swift":[["Nor"],[[60],[100],[20]],[None]],
        "Lovely_Kiss":[["Nor"],[[0],[75],[10]],["Sleep",1]],
        "Mega_Punch":[["Nor"],[[18],[85],[15]],["Multi"]],
        "Sonicboom":[["Nor"],[[0],[90],[20]],["SetDamage",20]],
        "Rapid_Spin":[["Nor"],[[20],[100],[40]],[None]],
        "Rest":[["Nor"],[[0],[0],[10]],["Rest"]],
        "Vicegrip":[["Nor"],[[55],[100],[30]],[None]],
        "Yawn":[["Nor"],[[0],[0],[10]],["Sleep"]],
        "Hyper_Fang":[["Nor"],[[80],[90],[15]],["Flinch",1/10]],
        "Vicegrip":[["Nor"],[[55],[100],[30]],[None]],
        "Sweet_Kiss":[["Nor"],[[0],[75],[10]],["Confuse",1]],
        "Spike_Cannon":[["Nor"],[[20],[100],[15]],["Multi"]],
        "Horn_Attack":[["Nor"],[[65],[100],[25]],[None]],
        "Thrash":[["Nor"],[[120],[100],[10]],[None]],
        "Cut":[["Nor"],[[50],[95],[30]],[None]],
        "Harden":[["Nor"],[[0],[0],[30]],["DefInc"]],
        "Super_Fang":[["Nor"],[[0],[90],[10]],["HalfLife"]],

        "Clear_Smog":[["Poi"],[[50],[100],[15]],[None]],
        "Poison_Jab":[["Poi"],[[80],[100],[20]],["Poison",3/10]],
        "Poison_Tail":[["Poi"],[[50],[100],[25]],[["Poison",1/10],["HighCrit"]]],
        "Sludge_Bomb":[["Poi"],[[90],[100],[10]],["Poison",3/10]],
        "Toxic":[["Poi"],[[0],[90],[10]],["BadPoison"]],
        "Acid":[["Poi"],[[40],[100],[30]],["OpDefDec",1/10]],
        "Poison_Gas":[["Poi"],[[0],[90],[40]],["Poison",1]],
        "Poison_Sting":[["Poi"],[[15],[100],[35]],["Poison",3/10]],
        "Smog":[["Poi"],[[30],[70],[20]],["Poison",2/5]],
        "Sludge":[["Poi"],[[65],[100],[20]],["Poison",3/10]],
        "Poison_Fang":[["Poi"],[[50],[100],[15]],["Poison",3/10]],
        "Gunk_Shot":[["Poi"],[[120],[80],[5]],["Poison",3/10]],

        "Calm_Mind":[["Psy"],[[0],[0],[20]],["AtkInc","DefInc"]],
        "Luster_Purge":[["Psy"],[[70],[100],[5]],["OpDefDec",1/2]],
        "Teleport":[["Psy"],[[0],[0],[20]],["Swap"]],
        "Psywave":[["Psy"],[[0],[80],[15]],["LevelDamage"]],
        "Psybeam":[["Psy"],[[65],[100],[20]],["Confuse",1/10]],
        "Psychic":[["Psy"],[[90],[100],[10]],["OpDefDec",1/10]],
        "Zen_Headbutt":[["Psy"],[[80],[90],[15]],["Flinch",1/5]],
        "Psycho_Cut":[["Psy"],[[70],[100],[20]],["HighCrit"]],
        "Extrasensory":[["Psy"],[[80],[100],[20]],["Flinch",1/10]],
        "Confusion":[["Psy"],[[50],[100],[25]],["Confuse",1/10]],
        "Hidden_Power":[["Psy"],[[60],[100],[15]],[None]],
        "Synchro_Noise":[["Psy"],[[50],[100],[15]],[None]],

        "Rock_Slide":[["Roc"],[[75],[90],[10]],["Flinch",3/10]],
        "Stone_Edge":[["Roc"],[[100],[80],[5]],["HighCrit"]],
        "Rollout":[["Roc"],[[30],[90],[20]],["IoCAtk"]],
        "Rock_Blast":[["Roc"],[[25],[90],[10]],["Multi"]],
        "Ancientpower":[["Roc"],[[60],[100],[5]],["AllRaise",1/10]],
        "Rock_Wrecker":[["Roc"],[[150],[90],[5]],["Charge"]],
        "Head_Smash":[["Roc"],[[150],[80],[5]],["Rec",1/2]],
        "Rock_Throw":[["Roc"],[[50],[90],[15]],[None]],

        "Steel_Wing":[["Roc"],[[70],[90],[25]],["DefInc"]],
        "Meteor_Mash":[["Roc"],[[90],[90],[10]],["AtkInc",1/10]],
        "Metal_Burst":[["Roc"],[[0],[100],[10]],["OppAtkDamage",1.5]],
        "Magnet_Bomb":[["Roc"],[[60],[100],[20]],[None]],
        "Iron_Tail":[["Roc"],[[100],[75],[15]],["OpDefDec",1/10]],
        "Metal_Claw":[["Roc"],[[50],[95],[35]],["AtkInc",1/10]],
        "Mirror_Shot":[["Roc"],[[65],[85],[10]],[None]],
        "Iron_Head":[["Roc"],[[80],[100],[15]],[None]],
        "Flash_Cannon":[["Roc"],[[50],[100],[10]],[None]],

        "Surf":[["Wat"],[[90],[100],[15]],[None]],
        "Splash":[["Wat"],[[0],[0],[40]],[None]],
        "Aqua_Jet":[["Wat"],[[40],[100],[20]],[None]],
        "Crabhammer":[["Wat"],[[100],[90],[10]],["HighCrit"]],
        "Aqua_Tail":[["Wat"],[[90],[90],[10]],[None]],
        "Bubblebeam":[["Wat"],[[65],[100],[20]],[None]],
        "Muddy_Water":[["Wat"],[[90],[85],[10]],["OpAccDec",3/10]],
        "Brine":[["Wat"],[[65],[100],[10]],[None]],
        "Water_Pulse":[["Wat"],[[60],[100],[20]],["Confuse",1/5]],
        "Waterfall":[["Wat"],[[80],[100],[15]],["Flihch",1/5]],
        "Water_Gun":[["Wat"],[[40],[100],[25]],[None]],
        "Bubble":[["Wat"],[[40],[100],[30]],[None]],
        "Hydro_Pump":[["Wat"],[[110],[80],[10]],[None]],
}


def Damage(Level,BaseP,SpAtk,SpDef,r,STAB,Weakness,CH):
    DamageDelt=(trunc(((trunc(trunc((((trunc((trunc(((Level*2)/5)+2))*BaseP*SpAtk/50)/77))+2)*CH*r/100)))*STAB)*Weakness))
    return DamageDelt

##print(Damage((trunc(UserPoke[0][2][0]/500)),\
##             attack[UserPoke[0][4][0]][1][0][0],\
##             (trunc(PokeStat[1][3][0]+(UserPoke[0][2][0]/500)*1/2)),\
##             (trunc(PokeStat[1][3][1]+(opp[2][0]/500)*1/2)),\
##             randint(85,100),\
##             (STAB(PokeStat[1][3][0],PokeStat[1][3][1],attack[UserPoke[0][4][0]][0])),\
##             BonusCalc((attack[UserPoke[0][4][0]][0][0]),opp[1][0],opp[1][-1]),\
##             1))



##StartUserPokeHP=UserPoke[0][-1][0]
##CurrUserPokeHP=StartUserPokeHP
##
##StartOppPokeHP=opp[0][-1][0]
##CurrOppPokeHP=StartOppPokeHP
##
##for i in range(0,len(UserPoke)):
##    print("Your Pokemon: \n",UserPoke[i][0][0]+",",CurrUserPokeHP,"/",StartUserPokeHP)
##
##for i in range(0,len(opp)):
##    print(opp[0][0][0],":",CurrOppPokeHP,"/",StartOppPokeHP)
##
##print("Your Attacks:\n")
##for i in range(4):
##    print(i+1,UserPoke[0][4][i])
##
##userattackchoice=input("Enter the attack# you want")
##userattack=(UserPoke[0][4][int(userattackchoice)-1])
##
                                                            
class Pokemon(object):
    def __init__(self):
        pass
        

    def load(self, identifer, xp):
        self.level = xp/500
        self.ID=identifer
        self.SpAtk=PokeStat[identifer][3][0]+(self.level/2)
        self.SpDef=PokeStat[identifer][3][1]+(self.level/2)
        self.type1=PokeStat[identifer][1][0]
        self.type2=PokeStat[identifer][1][-1]
        self.hp=self.level*4
        self.skill=PokeStat[self.ID][4][:]
##        self.image = pygame.image.load(path+"/resources/pokemon/ordered_images/%d.png"%self.ID).convert_alpha()
        
      
    def getID(self):
        return self.ID
    
    def getName(self):
        return Pokestat[self.ID][0]

    def getHP(self):
        return self.hp

    def getSkill(self, skillno):
        return self.skill[skillno]

    def getSkillP(self,skillno):
       
        return attack[self.getSkill(skillno)][1][0][0]
    
    def getSkillT(self,skillno):
        return attack[self.getSkill(skillno)][0][0]

    def getSkillA(self,skillno):
        return attack[self.getSkill(skillno)][1][1][0]
        

    def attack(self, other, skillno):
        accCheckv=self.getSkillA(skillno)
        accCheck=randint(0,100)
        if accCheck<=accCheckv:
            damage = Damage(self.level,
                            self.getSkillP(skillno),
                            self.SpAtk,
                            self.SpDef,
                            randint(85,100),
                            STAB(self.type1,self.type2,self.getSkillT(skillno)),
                            BonusCalc(self.getSkillT(skillno),other.type1,other.type2),
                            1)
            if not self.getSkillP(skillno): damage = 0
            other.hp -= damage
            return damage
        elif accCheck>=accCheckv:
            return 0

    def getProperties(self):
        return {} # all properties

    def render(self):   # basic image -> no anim.
        return self.image
    
    def get_hp_percentage(self):
        return self.hp//self.level*4

##print(userattack)
##print((Damage((trunc(UserPoke[0][2][0]/500)),\
##             (attack[userattack][1][0][0]),\
##             (trunc(PokeStat[1][3][0]+(UserPoke[0][2][0]/500)*1/2)),\
##             (trunc(PokeStat[1][3][1]+(opp[0][3][0]/500)*1/2)),\
##             100,\
##             (STAB(PokeStat[1][3][0],PokeStat[1][3][1],attack[UserPoke[0][4][0]][0])),\
##             BonusCalc((attack[userattack][0][0]),opp[0][1][0],opp[0][1][-1]),\
##             1)))

a = Pokemon()
a.load(10, 2500)
b = Pokemon()
b.load(15, 4000)
print(a.hp, b.hp)
print(a.attack(b, 2))
print(a.hp, b.hp)
print(b.attack(a, 0))
print(a.hp, b.hp)
