# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import os
import pyttsx3
import pyttsx3.voice
import time

class textspeaker():

    @staticmethod
    def text_to_speech_ssml(ssml_text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    
        # Set the voice properties to support SSML
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice.name == 'Microsoft Zira Desktop - English (United States)':
                engine.setProperty('voice', voice.id)
                break
    
        engine.say(ssml_text)
        engine.runAndWait()
        
    @staticmethod
    def text_to_speech(text):
        engine = pyttsx3.init(engine='sapi5')
        engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
        engine.say(text)
        engine.runAndWait()
    



ssml_text = '''
Think about a limiting belief that has been holding you back in life.|10|
Imagine how much it weighs on your body.|10|   
What are the consequences of having this belief?|10|
what are you losing?  |10|
What are you missing out on?|10|
Feel how it feels to feel that loss.  |10|
Realize that feeling of pain in your body.|10|
What is this belief costing you financially?  |10|
What does this belief cost you in your own self-esteem, or self-respect, 
... or self-love?|10|
Having this belief, what does it do to your self-confidence?|10|
Does it create doubt or strength to have this belief?|10|
How do you feel about yourself when you live by this belief?|10|
Do you feel powerful or weaker?|10|
How does this belief affect your energy level?|10|
Does it create energy or take energy away?|10|
What do you think of when you think of yourself living by this belief?|10|
What do you say to yourself when you look in the mirror and realize you’ve 
allowed this belief to control you?   |10|
Say it to yourself.  |10|
See it.  |10|
How does your face look when you think about living with this belief and 
the weight of it pulling you down?|10|
Feel how it feels.   |10|
What kind of a role model are you for your children?   |10|
What kind of a role model are you for anybody?|10|
How does it affect you spiritually?|5| your relationship with your creator?|10|
Think of what all the costs are for you physically, financially, 
emotionally, socially, spiritually,...
all the areas of your life.|20|

Take the weight of all of this limitations, all the things you’re 
missing out on, and pull yourself into the future.|10| 

And as you go into the future, step 5 years into the 
future, and make sure you drag with you all of the limiting feelings 
and experiences and limitations that this belief will create for 
another 5 years stacking one top another, like a giant snowball 
getting bigger and bigger and bigger, pushing you further down. |10|

And now step into the future 5 years from now and with you 
bring all the things you’ve missed out on, all the pain, all the 
frustration, all the anger that this belief have generated through time.|15|

All the things you’ve given up on.|5|

Bring all of that with you.|10|

Drag it with you now, 5 years in the future.|10|


Now step in the future, 10 years from now.  |10|
Drag 10 years of disappointment with you.|10|

10 years of one failure building on another.|10|

10 years of all the limitations of this belief, 
all the things you’ve missed out coming with you.|10|

10 years in the future, now look in the mirror and notice how you feel.|10|

Do you feel older or younger?…More alive or less alive?…Does your body 
feel heavier or lighter?|10|

Do you feel stronger or weaker?…What do you say to yourself as you look 
at yourself after living this way for a decade?|10|

10 years.|10|

What did you give up?|10|
What did you give up emotionally?|10|

How much frustration have you experienced for 10 years because of this 
belief?|10|

How many things were you afraid of?…How many things did you not do?
How many things did you give up on?|10|



Step 20 years into the future, now and drag 2 decades, 20 years of pain 
with you, all the way, and feel all the things you missed out on for 20 
years, culminating on your back.|10|

Feel it.|10|

Feel all the things you gave up on, all the things you missed out on, all 
the pain you’ve experienced because of this limiting belief.|10|

Look in the mirror and notice what your face looks like, what your body 
looks like.|10|

Are you healthy or not?…Are you fatter?…Do you feel lighter or heavier?|10|

Stronger or weaker?…More alive or less alive?…More excited or totally 
depressed and disappointed?|10|

Where are you?…What’s happened to you?…What price did you pay for this 
lousy belief?|10|

What did it cost you in your relationships?|10|

What did it cost you in your career?|10|
in your business?|10|

What didn’t you do because of this belief?…What didn’t you try?
What didn’t you go for?|10|

What does it cost you physically? Emotionally?  Spiritually? Financially?|10|

What does it cost your family life?|10|

What do you say to yourself after 20 years of living this way with this
limiting belief?|10|



How do you feel about your life if you’ve lived this way for 20 years?|10|

And decide if you’re willing to live this way.|10|

Are you willing to have this be your destiny?|10|

If this is painful enough that you’re absolutely committed to never living 
this way again, your brain will change your belief.|10|

If not, you better keep working on this until it’s really painful.|10|

Do whatever it takes.|10|

Ask yourself questions. |10|
Feel the pain.|10|

If you’re committed to never having this happen in your life, note this is 
only the shadow of the future as they said.|10|

And that this can be changed by you changing your belief.|10|




Come backwards in time.  Come back to today, and realize that none of this 
has happened yet, fortunately.|10|
Come all the way back to today, and realize none of this has happened yet.|10|

It doesn’t have to happen if you make some changes.|10|

And as you do, you may notice that if you did this, and you really were 
feeling the feelings, you may have been bent over, as you got older, and 
felt more of the weight of those problems.|10|
And as you come back to today, you may find yourself sitting or standing 
more upright…breathing more fully…feeling more alive.|10|

And you might want to shake your body out and interrupt that pattern.|10|
Get out of that state completely. Change your physiology.|10|
Change your state by moving your body around, bounce up and down, move 
around, breathe, and get completely out of that state.|10|

(wow, the author just stopped plaging at this point, lol. need to bring 
in the second half aiming you at your new replacement belief. what a dick 
move. by only doing this step youre only applying pain and giving no 
direction or correction. bad shepherding.)

Now, think of the new belief you want to adopt.|10| This belief creates a whole 
new timeline where the old belief no longer exists and the new belief is 
steering your behavior.|10| Test how you will live differently with this 
belief.|10| How will your interactions change?|10| How will you change?|10|
How will your health change?|10| How will your relationships change?|10|
How will your relationship with the world and universe change?|10| How will 
your thoughts change?|10| And what does that future look like in 5 years?|10|
In 10?|10| How does it look in 20 years?|10| Is it desireable? Does the new 
belief need modification for an even better future?|10| Is this a future you 
feel good about building?|10|

If not, stop here and make the belief better and test it again.|10|

Now that you have a tested belief and a plan for a better future, start 
building it right now.|10| Go inside and experience tomorrow with the 
old belief gone and the new belief already there.|10|
where do you notice the new belief in your behavior, or do you even notice it?|10|
Now jump ahead to next week.|10| Take a moment to look back on the last 
few days and see yourself back at this point where it changed.|10| Now jump 
a year into to future.|10| Look back on the events in your timeline and how the
new belief has changed things. How are you different?|10| How are people 
different to you?|10| How are you different to people?|10| How has this new belief
changed your life in a year?|10| What has improved?|10| What improvements 
were you surprised by?|10| Now turn around and look 5 years into the future.|10| 
before jumping there, how do you think this new belief will change you in 
the next 4 years?|10| Now jump to 5 years in the future.|10| Look all the way 
back to this moment.|10| How has the new belief made things better?|10| How 
are you physically better?|10| How comfortable is your living situation?|10|
How wealthy are you? |10|How has the new belief effected varous aspects of 
your life, improving them?|10| Just as a last check, quickly jump 20 years 
into the future and savor all the wealth, and health, and pleasure this new 
belief brought into your life over the years.|10| Look back 20 years and 
thank yourself for choosing to change in such an important way.|10| And then, 
come back to this moment.|10|

Before you are two timelines and you must choose one.|10| The fundamental 
difference in this timelines is your chosen belief.|10| Because of this the 
old and new belief cannot exist in the same timeline.|10| The new belief has
the one future you just visited.|10|

Make your choice and mentally move into the timeline.|10| Pause for a second to 
let time pass.|10| With each breath you move further into the future of the new 
timeline.|10| With each breath you you move further away from the point where
the new timeline split from the old one.|10|

Now bring yourself to full conscious awareness as quickly as you may
comfortably do so.

'''

q_list = [s.strip() for s in ssml_text.split('|')]

for question in q_list:
    print(question)
    #time.sleep(int(question)) if question.isnumeric() else textspeaker.text_to_speech_ssml(question)
    