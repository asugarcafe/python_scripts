import Dice
import datetime
from CoC_CharacterGenerator_7 import Investigator_7_Fast, SkillList, InvestigatorItem, InvestigatorWeapon, InvestigatorBackpack
from CoC_SoloTools import SoloGameTools as SGT, SoloPlayerJournal, DegreeOfSuccess, DifficultyModifier, Contestant

date_start = '1925-03-24 15:57:06'
start_city = 'Rochester, NY'
#nick_name = 'Fox'
full_name = 'Tyler (Fox) Renard'
profession = 'Journeyman Runrunner'

if profession == '':
    #as skill progresses give a few higher skill points but take away physical 
    career_stages = ['Apprentice', 'Journeyman', 'Master']
    die1 = Dice.Dice(len(career_stages))
    career_stage = career_stages[die1.Roll()-1]
    
    profession_choices = ['Runrunner/Smuggler', 'Detective', 'Priest/Rabbi', 'Grocer', 
                          'Archaeologist', 'Reporter', 'Jazz Musician',
                          'Pharmacist', 'Occultist', 'Physician', 'Pick Pocket',
                          'Burglar', 'Beat Cop', 'Farmer', 'Lawyer', 
                          'Parapsychologist', 'Sailor', 'Soldier', 'Actor',
                          'Stunt Person', 'Taxi/Truck Driver']
    die2 = Dice.Dice(len(profession_choices))
    base_profession = profession_choices[die2.Roll()-1]
    profession = career_stages[die1.Roll()-1] + ' ' + profession_choices[die2.Roll()-1]
    print(profession)


cs = {'STR':60,'CON':40,
      'POW':60,'DEX':60,
      'APP':50,'SIZ':60,
      'INT':70,'EDU':50}
        
inv = Investigator_7_Fast(full_name, list(cs.values()), profession)
#inv.print_character()
#investgator.print_character_skill()#starting skills
#for key, val in sorted(SkillList.get_base_skill_list(inv.DEX, inv.EDU).items()):
#    print('{0}: {1:-2}'.format(key, val))

inv.SKILL_LIST.set_skill('Spot Hidden', 40)
inv.SKILL_LIST.set_skill('Handgun', 40)
inv.SKILL_LIST.set_skill('Listen', 40)
inv.SKILL_LIST.set_skill('Navigate', 50)
inv.SKILL_LIST.set_skill('Pilot', 50)
inv.SKILL_LIST.set_skill('Stealth', 70)
inv.SKILL_LIST.set_skill('Language Other', 50)
inv.SKILL_LIST.set_skill('Fast Talk', 60)
inv.SKILL_LIST.set_skill('Persuade', 60)
inv.SKILL_LIST.set_skill('Swim', 35)

sk = 'Drive Auto' #run runners were the original nascar
inv.SKILL_LIST.set_skill(sk, inv.SKILL_LIST.get_skill(sk)+ 20) 
sk = 'Appraise' #character would be able to assess a contraband items approx value
inv.SKILL_LIST.set_skill(sk, inv.SKILL_LIST.get_skill(sk)+ 20) 
sk = 'Meteorology' #character would be weather-wise due to job
inv.SKILL_LIST.set_skill(sk, inv.SKILL_LIST.get_skill(sk)+ 20) 
sk = 'Forgery' #character would need to make fake docs and licenses
inv.SKILL_LIST.set_skill(sk, inv.SKILL_LIST.get_skill(sk)+ 20) 
#inv.print_character_skill()#skills upon starting the game

def reset_skill_check():
    skill_check = {}
    for key, val in sorted(inv.SKILL_LIST.skills.items()):
        skill_check[key.upper()] = 0
    return skill_check

skill_check_success = reset_skill_check()
with open(full_name + ' - journal.txt', 'w') as f:
    f.write(inv.get_character_sheet(ListSkills=True) + '\n\n')


#----------------------------------------------------
#-------------- Story Flow --------------------------
#----------------------------------------------------

d4 = Dice.Dice(4)
d10 = Dice.Dice(10)
d100 = Dice.Dice(100)
quest_source = 59 #d100.Roll()
#Directly observing some bizarre occurence

inciting_incident = 71 #d100.Roll()
#Heading to work one morning, no-one recognizes you. This is
#disconcerting, but even more so when your family and friends don’t
#recognize you either. 


journal = SoloPlayerJournal('Personal Diary of ' + full_name)
entry_date = datetime.datetime(1925, 3, 20, 6, 13)
entry_text = ('This morning started like any other. After waking I shaved and dressed and took the trolley to the docks. But instead of being greeted by the members of my crew they acted as though I were suspicious and asked me my business. At first, I thought they were having a jape and continued towards the warehouse offices. But, the men Ive known, and mostly trusted, for the past two years bullied up on me and told me to heel-toe back where I came from. After a few minutes of hot talk they still weren''t breaking the game so I pressed them that the jape wasnt funny anymore and we had work to do. I had to hold myself back from breaking Champs''s finger (especially because he''d break mine back,) when he poked it into my chest, told me he didn''t know me, never met me, and said to high-tail it or I''d get his shoe-polish on my teeth. Rather than risk breaking up the crew over a few split lips and hurting everyones feelings I backed off and went to the nosh to get a cup of joe and the breakfast I normally took after reviewing the days numbers. I needed to figure out what their game was.' +
'\nAt the diner, Daisy the waitress seemed to be playing at the same game when I ordered the usual. She cheerily replied "And what would be the usual for you, Darlin?". This took me back because I''d been ordering the same hash and egg plate every day for the last nine months. When I asked what Daisy was playing at I started to get a sinking feeling. Daisy just stared back at me with an empty expression. Daisy was easy on the eyes but not bright enough to hold to a jape this long without breaking. Sighing, I ordered a coffee and the hash and egg plate. As Daisy turned to give the order to the cook I sunk back into the booth. Something was definitely wrong.' +
'\nAfter finishing my breakfast, I went to the washroom to clean up, take my morning duece, and check my face in the mirror to make sure I am who I am.')

journal.add_entry(entry_date, entry_text)
#print(len(journal.events))


#created NPC Milo, second in command of my smuggling crew, just in case I need him later        
cs = {'STR':60, 'CON':45,
      'POW':80, 'DEX':60,
      'APP':50, 'SIZ':60,
      'INT':40, 'EDU':35}
milo = Investigator_7_Fast('Milo (Champ) Walker', list(cs.values()), 'Disgraced Boxer')
milo.SKILL_LIST.set_skill('Brawl', 50)
milo.SKILL_LIST.set_skill('Dodge', 50)
milo.SKILL_LIST.set_skill('Handgun', 60) #38 revolver dmg 1d10

# after looking in the washroom mirror
next_direction = SGT.get_next_story_direction()
nd = 'Dice Roll - Roll Against Dice Roll Table p26'
roll = 94 #d100.Roll() # 94 = Something Happens - Random Event Table
roll = 50 #d100.Roll() # A con-man has set up a table in the main street and is selling some truly bizarre items. He seems in a hurry to get rid of them as quickly as possible. 

entry_date = datetime.datetime(1925, 3, 20, 7, 30)
entry_text = ('After a quick once-over in the washroom, I saw that my face hadn''t changed and realized this morning''s game was either fun taken too far, or Champ was taking over my crew and told the boys I was dead to them. I decided I was going to go back to the crew and press the issue.' + 
'\n[Story Direction - Something Happens: A con-man has set up a table in the main street and is selling some truly bizarre items. He seems in a hurry to get rid of them as quickly as possible.]I exited the diner and surveyed the street. Across the street I spotted what looked like a three-card monte grifter. I crossed to watch his game. Upon closer inspection I saw that he was selling wares. Looking over his table I noted these weren''t the usual items a burglar or thief (which he had to be,) would sell on the open street. His wares seemed to be religious in nature, though not of any religion of which I was familiar. They seemed acient and of primitive craftsmanship. The seller, seemed nervous and in a hurry to move the wares. He even offered to cut his price by half when I showed interest in clay and wood model of what looked like the viking boats I''d learned about while visiting an exhibit at the museum of science. Though not usual interested in such things, I was dating a bird at the time who loved museums and dragged me all over the city to every show she could find. Not usually a history buff, as a man who spends a lot of time at sea, I found the viking''s seamanship admirable.' +
'\nI counter offered a dollar lower for the clay and wood model, and he only hesitated a moment before taking my 2 dollars and wishing me good luck')

journal.add_entry(entry_date, entry_text)

# Fox puts the boat in his pocket and decides to head back to the docks to spy on his crew and plan his next move
# Fox's goal at this point is to figure out if the gang is tryin to out him and if so, put a little discipline in place
next_direction = SGT.get_next_story_direction()
#print(next_direction)
nd = 'Development - Roll against Development Table p22.'
roll = 23 #d100.Roll() # Roll on the verbs table
roll = 76 #d100.Roll()/10 # 300-399
roll = 47 #d100.Roll()/10 # 300 + 47 = 347 obscure
entry_date = datetime.datetime(1925, 3, 20, 7, 45)
entry_text = 'I knew the dock pretty well and figured I''d climb on top of the warehouse to spy on my crew. That would give me a vantage point enough to see most of their movements and hear their conversations.'
journal.add_entry(entry_date, entry_text)

climb_roll = 2 #d100.Roll()
climb_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Climb'), climb_roll)
skill_check_success['CLIMB'] = skill_check_success['CLIMB'] + 1

stealth_roll = 51 #d100.Roll()
stealth_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Stealth'), stealth_roll)
skill_check_success['STEALTH'] = skill_check_success['STEALTH'] + 1


entry_date = datetime.datetime(1925, 3, 20, 7, 47)
entry_text = ('After a few short minutes [CLIMB skill roll = 2: Success] I found myself peering down [STEALTH skill roll = 51: Success] on them as they loaded the trade cargo onto the smaller faster boat we use for jobs where we might have to outrun harbor police. We''re smugglers so we always make a point to hid our cargo but the crew was making extra effort, under Champ''s hushed but urgent orders to OBSCURE the labelling on the crates they were covering. This piqued my interest because we usually reuse crates labelled as food stuffs. I wondered why Champ would have ordered the labels changed and why the cargo needed more than our usual, very thorough, camouflaging.' + 
'\nThen one of the younger guys asked Champ, "Why hasn''t Fox come by yet this morning? Do you think it had to do with that cop pretending to be him?" Champ shushed him harshly and retorted, "The boss can handle himself just fine. That cop didn''t know nothing and he got nothing. If Fox can''t get here by the time we leave I''ll check in on him this evening. This is a special job for big money and the boss would kick our asses for not making the run. When he gets his cut he''ll forgive us for doing the job without his okay."')
journal.add_entry(entry_date, entry_text)
#This is terrifying +5 Mythos Points and a Sanity Roll 2/1d4 + 1 to Fox
inv.MYTHOS_POINTS = inv.MYTHOS_POINTS + 5
san_roll = 9 #d100.Roll()
san_dos = SGT.get_DegreeOfSuccess(inv.INT, 9)
#inv.SANITY_POINT = inv.SANITY_POINT - 2

entry_date = datetime.datetime(1925, 3, 20, 7, 48)
entry_text = 'My mind reeled [MYTHOS_POINTS + 5, SANITY_POINT -2] at the undeniable truth that these men, my cohorts, my friends, truly didnt recognize me. This was no joke, I was truly a different person to them! It was only through will that I didn''t cry out.'
journal.add_entry(entry_date, entry_text)

stealth_roll = 19 #d100.Roll()
stealth_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Stealth'), stealth_roll)
#print(stealth_dos)
skill_check_success['STEALTH'] = skill_check_success['STEALTH'] + 1

downtime_interrupt_roll = 41 #d100.Roll() #undisturbed
downtime_interrupt_roll = 95 #d100.Roll() #disturbed Perform a dice roll

inv.MYTHOS_POINTS = inv.MYTHOS_POINTS - 2
entry_date = datetime.datetime(1925, 3, 20, 7, 52)
entry_text = ('After a few minutes [DOWNTIME, chosen] I regained my composure [MYTHOS_POINTS - 2] and retreated to a place on the roof where no one from the ground could see me.' +
             '\nI would have liked to stay there longer [DOWNTIME, chosen, interrupted by next phone call] but something compelled me to get to my office.')
journal.add_entry(entry_date, entry_text)

#follow up on 95 disturbance
disturbed_roll = 94 #d100.Roll() # Something happens: Random Event Table
random_event_roll = 8 # d100.Roll() #A nearby telephone rings. You feel an impulse to pick it up. You do, but at the other end all you hear is faint talking, as if the other person is many many miles away. It is whispering numbers…. coordinates?

#Fox has to get near a phone for this, I assume he decided to climb down the building and sneak into his office through the window
climb_roll = 25 #d100.Roll()
#going to assume he has a high degree of success possible: he knows the building and he just made the climb up
climb_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Climb'), climb_roll, int(DifficultyModifier.Likely))
#print(climb_dos)
skill_check_success['CLIMB'] = skill_check_success['CLIMB'] + 1

stealth_roll = 51 #d100.Roll()
stealth_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Stealth'), stealth_roll, int(DifficultyModifier.Likely))
#print(stealth_dos)
skill_check_success['STEALTH'] = skill_check_success['STEALTH'] + 1

init_roll = 42 #d100.Roll()
init_dos = SGT.get_DegreeOfSuccess(inv.DEX, init_roll, int(DifficultyModifier.Possible))
#print(init_dos)

does_milo_hear_roll = 77 #d100.Roll()
does_milo_hear_dos = SGT.get_DegreeOfSuccess(milo.SKILL_LIST.get_skill('Listen'), does_milo_hear_roll, int(DifficultyModifier.Possible))
#print(does_milo_hear_the_phone_ring_dos)

int_roll = 37 #d100.Roll() # do I remember the coordinates
int_dos = SGT.get_DegreeOfSuccess(inv.INT, int_roll, int(DifficultyModifier.Likely))
#print(int_dos)

coords1_loc = 'Club Island. A small island East of Manitoulin Iland in Lake Huron'

stealth_roll = 4 #d100.Roll()
stealth_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Stealth'), stealth_roll, int(DifficultyModifier.Likely))
#print(stealth_dos)
skill_check_success['STEALTH'] = skill_check_success['STEALTH'] + 1

climb_roll = 48 #d100.Roll()
#going to assume he has a high degree of success possible: he knows the building and he just made the climb up
climb_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Climb'), climb_roll, int(DifficultyModifier.Likely))
#print(climb_dos)

jump_roll = 66 #d100.Roll()
jump_dos = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Jump'), jump_roll, int(DifficultyModifier.Possible))
#print(jump_dos)

fall_damage = 1 #d10.Roll()
inv.HIT_POINT = inv.HIT_POINT - fall_damage

does_milo_hear_roll = 98 #d100.Roll()
does_milo_hear_dos = SGT.get_DegreeOfSuccess(milo.SKILL_LIST.get_skill('Listen'), does_milo_hear_roll, int(DifficultyModifier.Possible))
#print(does_milo_hear_dos)

entry_date = datetime.datetime(1925, 3, 20, 7, 58)
entry_text = ('Still shaken, I climbed down the side of the building and snuck into my office through the window [CLIMB : 25 (success), STEALTH 51 (success)] hoping for a moment to rest and steady my mind. But, just as I tried to catch my breath, the phone rang. [Initiative roll against DEX: 42] The adrenaline must have sharpened my reflexes because I pullet of off the cradle half-way through the first ring. I didnt do so because I wanted to answer the call but I knew if my crew outside heard it ringing someone would come up to the office. [Champ rolls to LISTEN: 77 (fail)]' + 
'\nI held the receiver to my ear and listened. I could barely hear the speaker at the other end. He was whispering numbers, the same six numbers over an over. I hesitated to put the phone back on the reciever for fear that the caller would ring again. After his fourth repetition I had the numbers committed to memory [INT roll (Likely): 37 (success)] and wondered if they my be latitude and longitude coordinates. Whispering, I tried to get the caller to tell me their name or what the numbers were, but they only repeated those same numbers over and over. I assumed those were the corrdinates my crew was heading to. I grabbed a map covering all the Great Lakes out of my desk and stuffed it into my coat and made for the wind to sneak back onto the roof. There, I intenede to wait for my crew to pull out with the says smuggling work so I could take the slow boat and check the corrdinates.' + 
'\nI was quiet [STEALTH roll: 4 (extreme success)] and thorough, but as I attempted to climb [CLIMB roll: 48 failure] back on the roof I slipped and fell 10 feet. Though I tried to land with a roll [JUMP: 66 (failure)] I ended up injuring my ankle [Fall damage 1d10: 1]. Luckily I fell on the opposite side of the building from where my crew were to they wouldnt have heard. [Milo LISTEN roll: 98 (failure)]'
'\nI then watched from a safe distance until my crew sped away. Once I was certain they were out of site, I entered the warehouse and went to my office to get the keys to The Large Marge, our slower but powerful tugboat. I pulled out of the Braddock Bay and steered towards Buffalo.')
journal.add_entry(entry_date, entry_text)

#Successful skill rolls this session:
#CLIMB : 2
#STEALTH : 4
current_stealth = 70 #inv.SKILL_LIST.get_skill('Stealth')
sleath1_adv_check = 11 #d100.Roll() #failure, no skill boost in Stealth

current_climb = 20 #inv.SKILL_LIST.get_skill('Climb')
climb_adv_check = 25 #d100.Roll() #success, rol 1d10 for score addition

climb_skill_increase = 8 #d10.Roll()
inv.SKILL_LIST.set_skill('Climb', inv.SKILL_LIST.get_skill('Climb')+climb_skill_increase) 

inv.MYTHOS_POINTS = 0
skill_check_success = reset_skill_check()
inv.HIT_POINT = 12

trip_distance = 625
tugboat_mph = 15
travel_hours = trip_distance/tugboat_mph # 2 days, 6 hours travel time
#next_direction = SGT.get_next_story_direction() #Development
roll = 11 #d100.Roll() # meet a friendly NPC. roll on NPC table
roll = 13 #d100.Roll() # NPC occupation: Dilletante
roll = 37 #d100.Roll() # NPC gender: female
roll = 46 #d100.Roll() # NPC modifier: talkative 
interaction_modifier = 30 # friendly
roll = 87 #d100.Roll() # +30 exchange outcome very positive 

my38 = InvestigatorWeapon('.38 Long Colt', '1d10', '15m',.75, 1, 6)
inv.BACKPACK.add_item(my38)

cs = {'STR':50, 'CON':50,
      'POW':50, 'DEX':50,
      'APP':70, 'SIZ':60,
      'INT':50, 'EDU':80}
zoe = Investigator_7_Fast('Zoe (Princess) Platt', list(cs.values()), 'Dilletante (Conservationist)')
zoe.SKILL_LIST.set_skill('Brawl', 25)
zoe.SKILL_LIST.set_skill('Dodge', 25)
zoe.SKILL_LIST.set_skill('Natural World', 50) #
zoe.SKILL_LIST.set_skill('Zoology', 50) #
zoe.SKILL_LIST.set_skill('Biology', 60) #
zoe.SKILL_LIST.set_skill('Science', 60) #
zoe.SKILL_LIST.set_skill('Botany', 70) #

roll = 99 #d100.Roll() # FAIL!! Try to persuade me to find something on the island, tell her its treasure. +30 exchange outcome very positive 
roll_success = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Persuade'), roll + interaction_modifier, int(DifficultyModifier.Possible))


roll = 68 #d100.Roll() # Push the roll. Subtract the friendly modifier. If fail she calls out a bodyguard I didnt see Try to persuade me to find something on the island, tell her Im actually looking for a lost friend and could use someone who knows the island. 
roll_success = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Persuade'), roll, int(DifficultyModifier.Possible))
#print(roll_success)

#she yells to her bodyguard
cs = {'STR':65, 'CON':50,
      'POW':50, 'DEX':65,
      'APP':50, 'SIZ':65,
      'INT':60, 'EDU':60}
mo = Investigator_7_Fast('Mohammad (Mo) Hill', list(cs.values()), 'Retired Soldier')
mo.SKILL_LIST.set_skill('Brawl', 45)
mo.SKILL_LIST.set_skill('Rifle', 50)
mo.SKILL_LIST.set_skill('Pilot', 30) # for the boat they had to use to get there
mo.SKILL_LIST.set_skill('Intimidate', 50) #first skill a bodyguard needs to learn

roll = 96# d100.Roll() # How does Mo approach me: Indifferent
interaction_modifier = 0

#mo tells me to keep my distance and there wont be any trouble
roll = 27 #d100.Roll() # Mo rolls intimidate to make sure I understand
roll_success = SGT.get_DegreeOfSuccess(mo.SKILL_LIST.get_skill('Intimidate'), roll, int(DifficultyModifier.Possible))
#mo intimidates me so I keep my distance. I tell them both Im sorry to bother them

entry_date = datetime.datetime(1925, 3, 23, 13, 58)
entry_text = ('Large Marge is a slow boat so it took the better part of 3 days to get to the coordinates in Lake Huron. An hour or so after noon I pulled into the small bay on Club Island. Club Island was a common rumrunner drop point due to the bay giving shipmen relief from choppy water while transferring contraband. Sadly, there was no dock so I dropped anchor far enough out that a lower tide would beach Marge. I pocketed the .38 Long I keep hidden under the gauge board on Marge and rowed the dinghy to the North beach.' 
'\n[Story direction: Development - meet a friendly NPC (female, dilletante, talkative)]As I stepped onto shore I heard a woman call out to me. I didnt see her at first but then she came out of the treeline. She remarked that she didnt think anyone else was expected to be on the island and asked if I was from the conservancy. She was talkative and barely let me get in a word edge-wise before shed convinced herself that I had been sent here to help her out for some reason and that she was cataloging new plants and needed my help loading samples onto her boat, though she was ancheored on the East side of the island.'
'\nI should have laid back and let her talk. She was easy on the eyes and assumed without question that I was here to aid her. But for the last two days Id been trying to figure out why my crew didnt recognize me and who gave them the one-off smuggling job for good money. Id assumed the answers were on this island and I was in a hurry to find them. Normally, Im a pretty smooth talker but the lack of sleep, and stress of the situation got the better of me. I stopped her talking abruptly and said, "Lady, Im not here form any conservancy, but I could use yourhelp if you know the island. Ive got word theres a treasure on this island and Id be willing to sahre if youd show me around and help me find it." [PERSUADE 99 failure] Whether she got mad at my calousness or just interrupting her endless talking she leaned back rebuffed and stated at me like Id just spit in her drink.'
'\nRealizing Id made a miscue I took a breath and tried to use my manners. "Listen, Im sorry, theres no treasure. I was just trying to get you to help me. Im looking for some one whos missing and I believe they might be on the island." I didnt tell her the missing person was me. "Would you help me look for them?" [PURSUADE PUSH 68 failure] I can usually sweet-talk my way past the toughest customs officials or into the laciest of panties but I just fell flat this time. She screamed at the top of lungs "MO!" and looked to the treeline. A half second later a gorilla of a human wearing a turban came out of the treeline at a brisk trot and stood between myself and the woman. He got very quiet and still and just leaned forward at me and, almost whispering, poked a hole in my already shaken result with one word, "scram." [Mo IMTIMIDATE 27 success] I jumped back and threw my hands up. The pretty laday and her monkey Moe werent going to be of any help. For a second I thought of flashing the gun to let the giant mook I didnt appreciate the threat. But, I thought better of it and just apologized to both of them. "Listen, Im sorry. Im looking for someone very important to me and I think they might be on this island. Im going be looking around. If we happen to meet again please dont think it was on purpose." Then I headed East along the shore a quarter mile before heading North into the treeline.')
journal.add_entry(entry_date, entry_text)



# next, 
#next_direction = SGT.get_next_story_direction() #Discovery - Roll against Discovery Table p 23
roll = 39 #d100.Roll() # Discovery: 39 - You observe/are caught up in someoccurrence directly relating to what you are investigating
roll = 10 # d100.Roll() #Discovery: 10 (Roll against CON) - 1-5: Str / 6-10: Con / 11-15: Dex / 16-20: Int / 21-25: Pow / 26-30:Anthropology /31-35: Charm / 36-40: Disguise / 41-45: Fast Talk / 46-50: History / 51-55: Intimidate / 56-60: Law / 61-65: Navigate / 66-70:Occult / 71-75: Persuade / 76-80:Psychology / 81-85: Spot Hidden /86-90: Science / 91-95: Sleight ofHand / 96-100: Track
roll = 51 #d100.Roll() #CON roll - failure
roll_success = SGT.get_DegreeOfSuccess(inv.CON, roll)
#print(roll_success)

entry_date = datetime.datetime(1925, 3, 23, 14, 10)
entry_text = ('I found myself having to hike up a small bluff. At the top, I was so winded, I thought I spotted something moving in the trees but it was just a trick of a mind short of oxygen [Story Direction: Discovery. Roll against CON to see if I discover it: 51 (failure)] After I caught my breath I continued North.')
journal.add_entry(entry_date, entry_text)

#next_direction = SGT.get_next_story_direction() #Dice Roll - Roll Against Dice Roll Table p26
#print(next_direction)
roll = 2 #d100.Roll() # Dice Roll: 2 - You hear something
roll = 30 #d100.Roll() #Auditory Effects: I hear screaming
roll = 100 #d100.Roll() #Auditory Effects: I hear screaming FROM EVERYWHERE!
roll = 48 #d100.Roll() #50/50 Terrifying vs Petrifying: 48 "only" terrifying
inv.MYTHOS_POINTS = inv.MYTHOS_POINTS + 5 # MP 5
roll = 36# d100.Roll() #SAN roll: 36 SAN - 2/1d4+1
roll_success = SGT.get_DegreeOfSuccess(inv.SAN, roll)
inv.SAN = inv.SAN - 2

entry_date = datetime.datetime(1925, 3, 23, 14, 15)
entry_text = ('[Dice Roll - You hear something (I hear screaming FROM EVERYWHERE!) MYTHOS + 5, SAN 36 success. SAN - 2] A few minutes later, I heard loud, violent, frightened screaming! But, not from a specific direction. It came from all around me! I nearly froze with fear! For a moment I lost my guts and ran back along the path Id followed. But since I heard the screaming there as well I just got low, tried to cover my ears from the din and watch for what my be causing such a terrible distress. I pulled out the .38 Long but had no idea where to point it so I kept it hidden under my coat! The screaming seemed louder than a normal human seemed capable of, and while the screaming might be feminine I didnt think it soulnded like the nature buff, (or her gorilla,) that Id met down at the bay.')
journal.add_entry(entry_date, entry_text)

#next_direction = SGT.get_next_story_direction() #Danger - Roll against Danger Table p25, then the Verbs Table p40.
#print(next_direction)
roll = 26 #d100.Roll() # Danger: 2 - Out of nowhere, you are assaulted by an unknown thug.
roll = 52 #d100.Roll() # Verbs 200-299
roll = 77 #d100.Roll() # Verbs 277: hamper
cs = {'STR':65, 'CON':45,
      'POW':80, 'DEX':60,
      'APP':60, 'SIZ':60,
      'INT':50, 'EDU':45}
thug1 = Investigator_7_Fast('Unknown Thug s', list(cs.values()), 'Enforcer')
thug1.SKILL_LIST.set_skill('Brawl', 50)
thug1.SKILL_LIST.set_skill('Handgun', 50)
thug38 = InvestigatorWeapon('.38 revolver', '1d10', '', .75, 1, 6)
thug1.BACKPACK.add_item(thug38)

#thug1.print_character()

## opposing skill roll for intiative
#cont_1 = Contestant('Fox', inv.DEX) #, 'bonus')
#cont_2 = Contestant('Thug 1', thug1.DEX) #, 'penalty')
#winner = SGT.opposed_skill_roll(cont_1, cont_2)
## Fox rolled 100. Failure.
## Thug 1 rolled 19. HardSuccess.
## Victor: Thug 1print(winner)

roll = 85 #d100.Roll() #Spot check, did he see my gun and draw his
roll_success = SGT.get_DegreeOfSuccess(thug1.SKILL_LIST.get_skill('Spot Hidden'), roll)
# He did not spot my gun, so he did not pull his

roll = 69# d100.Roll() #Brawl 69 + likelySuccess modifer: RegularSuccess, Thug attempts to stab me, when I dont even know he was there
roll_success = SGT.get_DegreeOfSuccess(thug1.SKILL_LIST.get_skill('Brawl'), roll, int(DifficultyModifier.Likely))
#print(roll_success)

roll = 1#d4.Roll() first forgiving roll in three rounds!
roll2 = 1#d4.Roll() #thugs added damage roll, second forgiving roll in three rounds!
inv.HIT_POINT = inv.HIT_POINT - (roll + roll2)

roll = 83#d100.Roll() #Handgun: 83 (failure) FUCK!. I attempt to shoot him, adding likely modifier because he's so close
roll_success = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Handgun'), roll, int(DifficultyModifier.Likely))

roll = 50 #d100.Roll() #Brawl 69 + likelySuccess modifer: RegularSuccess, Thug attempts to stab me again
roll_success = SGT.get_DegreeOfSuccess(thug1.SKILL_LIST.get_skill('Brawl'), roll, int(DifficultyModifier.Likely))

roll = 4 #d4.Roll() #fook
roll2 = 4 #d4.Roll() #thugs added damage roll,
inv.HIT_POINT = inv.HIT_POINT - (roll + roll2)
# fuck fuck fuck, I am bleeding out
roll = 8 #d100.Roll() #CON roll 8 ExtremeSuccess: because I took over half my helath in damage
roll_success = SGT.get_DegreeOfSuccess(inv.CON, roll)

#I stay conscious and active enough for one more shot
roll = 56 #d100.Roll() #Handgun: 56 regular success. I attempt to shoot him again, adding likely modifier because he's so close
roll_success = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('Handgun'), roll, int(DifficultyModifier.Likely))

roll = 6#d10.Roll() good shot!
thug1.HIT_POINT = thug1.HIT_POINT - roll

#now the thug needs to make a CON roll
roll = 57#d100.Roll() #CON roll : because he took over half his helath in damage
roll_success = SGT.get_DegreeOfSuccess(thug1.CON, roll)
#the thug slumps over, either dead or unconscious

inv.BACKPACK.drop_item('.38 Long Colt')
my38 = InvestigatorWeapon('.38 Long Colt', '1d10', '15m', .75, 1, 4)
inv.BACKPACK.add_item(my38) #just readding the gun with 2 less bullets

#check mythos and sanity
inv.MYTHOS_POINTS = inv.MYTHOS_POINTS + 5 # MP 5
roll = 65 #d100.Roll() #SAN roll: 36 SAN - 2/1d4+1, fuck that was close
roll_success = SGT.get_DegreeOfSuccess(inv.SAN, roll)
inv.SAN = inv.SAN - 2


#attempt some first aid first, or at least to plug up my holes
roll = 86 #d100.Roll() #First Aid: 86 failure
roll_success = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('First Aid'), roll, int(DifficultyModifier.Likely))

#push first aid roll and risk injuring myself one more hit point
roll = 90 #d100.Roll() #First Aid: 90 failure FUCK!
roll_success = SGT.get_DegreeOfSuccess(inv.SKILL_LIST.get_skill('First Aid'), roll, int(DifficultyModifier.Likely))
inv.HIT_POINT = inv.HIT_POINT - 1

roll = 92 #d100.Roll() #CON roll because I lost half my HP again - 92
roll_success = SGT.get_DegreeOfSuccess(inv.CON, roll)
#I pass out

#CON roll to see who wakes up first
#cont_1 = Contestant('Fox', inv.CON) #, 'bonus')
#cont_2 = Contestant('Thug 1', thug1.CON) #, 'penalty')
#winner = SGT.opposed_skill_roll(cont_1, cont_2)

#Fox rolled 45. Failure.
#Thug 1 rolled 84. Failure.
#No victor.

##push
#Fox rolled 87. Failure.
#Thug 1 rolled 58. Failure.
#No victor.

##push again, really?
#Fox rolled 40. RegularSuccess.
#Thug 1 rolled 20. HardSuccess.
#Victor: Thug 1

## omfg Thug 1 woke up first, killed me, and crawled out into the woods

entry_date = datetime.datetime(1925, 3, 23, 14, 18)
entry_text = ('[Final Entry]'
'\n[Story Direction - Danger: 2 - Out of nowhere, you are assaulted by an unknown thug. Thug 1 (attacks with switchblade 1d4)] [Roll for initiative:Fox rolled 100. Failure. Thug 1 rolled 19. HardSuccess. Victor: Thug 1] [Thug 1 check to see if he saw my gun: 85 failure] [Thug 1 BRAWL with LikelySuccess modifier: 69 (-20) success damage 1, thug 1 addtl damage roll 1. Fox HIT_POINTS - 2] [Fox attemtps to shoot using HANDGUN skill check with LikelySuccess 82 (-20) failure dammit!] [[Thug 1 BRAWL: 50 success, damage 4 addtl damage 8 dammit again!] [Fox makes CON roll to see if he passes out because he lost more than half his hit points: 8 HardSuccess] [Foxes shoots HANDGUN again with LikelySuccess Modifier: 56(-20) id10 damage: 6] [Thug 1 makes CON roll to see if he passes out: 57 failure. Thug 1 passes out][Fox rolls FIRST AID to see if he can get back a hit point: 86 failure][Fox pushes FIRST AID roll and risks doing more damage: 90 failure fuck!!! Fox Hitpoint = 1][Fox rolls agains CON to see if he passes out (just lost half his hitpoints again): 90 failure. Fox passes out][Roll for initiative to see who makes up first: #Fox rolled 45. Failure.#Thug 1 rolled 84. Failure.#No victor.][##push the init roll#Fox rolled 87. Failure.#Thug 1 rolled 58. Failure.#No victor.][##push again, really?#Fox rolled 40. RegularSuccess.#Thug 1 rolled 20. HardSuccess.#Victor: Thug 1][Thug 1 wakes up first. Makes certain Fox is dead by stabbing him in the chest and crawls away][Fox lurches awake for one last moment of consciousness and writes a final line in his journal]'
'\n\n[scrawled in blood] this is some bullshit')
journal.add_entry(entry_date, entry_text)
journal.title = 'Journal of ' + inv.NAME + ' (Found next to his remains on Club Island)'
inv.HIT_POINT = 0


#thug1.print_character()






#--------------------------------------------------
#-----Quick ref--------------------
#--------------------------------------------------

#basic rolling against skill
#roll = 27 #d100.Roll() # Mo rolls intimidate to make sure I understand
#roll_success = SGT.get_DegreeOfSuccess(mo.SKILL_LIST.get_skill('Intimidate'), roll, int(DifficultyModifier.Possible))


## get next direction    
#next_direction = SGT.get_next_story_direction()

## check if your downtime is disturbed, add Mythos points as modifier 
#disturbance_check = SGT.get_downtime_disturbance(investgator.MYTHOS_POINTS)

## opposing skill roll
#ben = Contestant('Ben', 50, 'bonus')
#dave = Contestant('Dave', 50) #, 'penalty')
#winner = SGT.opposed_skill_roll(ben, dave)

#SGT.get_table_pages()

#--------------------------------------------------
#-----Write the current journal--------------------
#--------------------------------------------------
with open(full_name + ' - journal.txt', 'a') as f:
    f.write(journal.title + '\n')
    for entry in journal.events:
        f.write('{0}\n{1}\n\n'.format(entry[0], entry[1]))
        
        
    f.write(inv.get_character_sheet(ListSkills=True))
    f.write('\n\nSuccessful skill rolls this session:'.format(entry[0], entry[1]))
    for k, v in skill_check_success.items(): 
        if v > 0:
            f.write('\n{0} : {1}'.format(k, v))

    f.write('\n\nInventory')
    for v in inv.BACKPACK.items: 
        f.write('\n{0}'.format(v.print_item()))

#--------------------------------------------------
#-----print the current character state------------
#--------------------------------------------------
inv.print_character()
