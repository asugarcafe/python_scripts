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
Think about a limiting belief that has been holding you back in life.
Imagine how much it weighs on your body.   
What are the consequences of having this belief?  
what are you losing?  
What are you missing out on?
Feel how it feels to feel that loss.  
Realize that feeling of pain in your body.
What is this belief costing you financially?  
What does this belief cost you in your own self-esteem, or self-respect, 
or self-love?
Having this belief, what does it do to your self-confidence?
Does it create doubt or strength to have this belief?
How do you feel about yourself when you live by this belief?
Do you feel powerful or weaker?
How does this belief affect your energy level?
Does it create energy or take energy away?
What do you think of when you think of yourself living by this belief?
What do you say to yourself when you look in the mirror and realize you’ve 
allowed this belief to control you?   
Say it to yourself.  
See it.  
How does your face look when you think about living with this belief and 
the weight of it pulling you down?
Feel how it feels.   
What kind of a role model are you for your children?   
What kind of a role model are you for anybody?
How does it affect you spiritually?…your relationship with your creator?
Think of what all the costs are for you physically, financially, 
emotionally, socially, spiritually,
all the areas of your life.

Take the weight of all of these limitations, all the things you’re 
missing out on, and I want you to pull yourself into the future. 

And as you go into the future, I want you to step 5 years into the 
future, and make sure you drag with you all of the limiting feelings 
and experiences and limitations that this belief will create for 
another 5 years stacking one top another, like a giant snowball 
getting bigger and bigger and bigger, pushing you further down. 

And I want you to step into the future 5 years from now and with you 
bring all the things you’ve missed out on, all the pain, all the 
frustration, all the anger that this belief have generated through time.

All the things you’ve given up on.

Bring all of that with you.

Drag it with you now, 5 years in the future.


Now step in the future, 10 years from now.  Drag 10 years of disappointment with you.

10 years of one failure building on another.

10 years of all the limitations of these beliefs, all the things you’ve missed out coming with you.

10 years in the future, now look in the mirror and notice how you feel.

Do you feel older or younger?…More alive or less alive?…Does your body feel heavier or lighter?

Do you feel stronger or weaker?…What do you say to yourself as you look at yourself after living this way for a decade?

10 years.

What did you give up?…What did you give up emotionally?

How much frustration have you experienced for 10 years because of these beliefs?

How many things were you afraid of?…How many things did you not do?…How many things did you give up on?”



Step 20 years into the future, now and drag 2 decades, 20 years of pain with you, all the way, and feel all the things you missed out on for 20 years, culminating on your back.

Feel it.

Feel all the things you gave up on, all the things you missed out on, all the pain you’ve experienced because of these limiting beliefs.

Look in the mirror and notice what your face looks like, what your body looks like.

Are you healthy or not?…Are you fatter?…Do you feel lighter or heavier?

Stronger or weaker?…More alive or less alive?…More excited or totally depressed and disappointed?

Where are you?…What’s happened to you?…What price did you pay for these lousy beliefs?

What did it cost you in your relationships?

What did it cost you in your career?… in your business?

What didn’t you do because of these beliefs?…What didn’t you try?…What didn’t you go for?

What does it cost you physically? Emotionally?  Spiritually? Financially?

What does it cost your family life?

What do you say to yourself after 20 years of living this way with these limiting beliefs?



How do you feel about your life if you’ve lived this way for 20 years?

And decide if you’re willing to live this way.

Are you willing to have this be your destiny?

If this is painful enough that you’re absolutely committed to never living this way again, your brain will change your beliefs.

If not, you better keep working on this until it’s really painful.

Do whatever it takes.

Ask yourself questions. Feel the pain.

If you’re committed to never having this happen in your life, note this is only the shadow of the future as they said.

And that this can be changed by you changing your beliefs.




Come backwards in time.  Come back to today, and realize that none of this has happened yet, fortunately.   Come all the way back to today, and realize none of this has happened yet.

It doesn’t have to happen if you make some changes.

And as you do, you may notice that if you did this, and you really were feeling the feelings, you may have been bent over, as you got older, and felt more of the weight of those problems.   And as you come back to today, you may find yourself sitting or standing more upright…breathing more fully…feeling more alive.

And you might want to shake your body out and interrupt that pattern.   Get out of that state completely.   Change your physiology.  Change your state by moving your body around, bounce up and down, move around, breathe, and get completely out of that state.

(wow, the author just stopped plaging at this point, lol. need to bring 
in the second half aiming you at your new replacement belief. what a dick 
move. by only doing this step youre only applying pain and giving no 
direction or correction.)

Now, think of the new belief you want to adopt. This belief creates a whole 
new timeline where the old belief no longer exists and the new belief is 
steering your behavior. Test how you will live differently with this 
belief. How will your interactions change? How will you change? How will
your health change? How will your relationships change? How will your 
relationship with the world and universe change? How will your thoughts
change? And what does that future look like in 5 years? In 10? How does it 
look in 20 years? Is it desireable? Does the new belief need modification 
for an even better future? Is this a future you feel good about building?

If not, stop here and make the belief better and test it again.

Now that you have a tested belief and a plan for a better future, start 
building it right now. Go inside and experience tomorrow with the 
old belief gone and the new belief already there.
where do you notice the new belief in your behavior, or do you even notice it?
Now jump ahead to next week. Take a moment to look back on the last 
few days and see yourself back at this point where it changed. Now jump 
a year into to future. Look back on the events in your timeline and how the
new belief has changed things. How are you different? How are people 
different to you? How are you different to people? How has this new belief
changed your life in a year? What has improved? What improvements were you 
surprised by? Now turn around and look 5 years into the future. 
before jumping there, how do you think this new belief will change you in 
the next 4 years? Now jump to 5 years in the future. Look all the way back to 
this moment. How has the new belief made things better? How are you physically
better? How comfortable is your living situation? How wealthy are you? 
How has the new belief effected varous aspects of your life, improving 
them? Just as a last check, quickly jump 20 years into the future and 
savor all the wealth, and health, and pleasure this new belief brought into 
your life over the years. Look back 20 years and thank yourself for choosing
to change in such an important way. And then, come back to this moment.

Before you are two timelines and you must choose one. The fundamental 
difference in these timelines is your chosen belief. Because of this the 
old and new beliefs cannot exist in the same timeline. The new belief has
the one future you just visited.

Make your choice and mentally move into the timeline. Pause for a second to 
let time pass. With each breath you move further into the future of the new 
timeline. With each breath you you move further away from the point where
the new timeline split from the old one.

Now bring yourself to full conscious awareness as quickly as you may
comfortably do so.

'''

q_list = [s.strip() for s in ssml_text.split('?')]

for question in q_list:
    print(question)
    #time.sleep(int(question)) if question.isnumeric() else textspeaker.text_to_speech_ssml(question)
    