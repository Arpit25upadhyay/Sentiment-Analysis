# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import csv

# NLP Packages
from textblob import TextBlob
from textblob import classifiers
from textblob.classifiers import NaiveBayesClassifier
#from textblob.classifiers import DecisionTreeClassifier
import spacy
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
nlp = spacy.load('en_core_web_sm')
 
 # Structure and Layout
window = Tk()
window.title("Sentiment Analysis")
window.geometry("1000x700")
window.config(background='black')

# TAB LAYOUT
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)


# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text='Sentiment Analysis')
tab_control.add(tab2, text='File Processer')
tab_control.add(tab3, text="Machine Learning")
tab_control.add(tab4, text='About')


label1 = Label(tab1, text= 'Sentiment Analysis',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'File Processing',padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text= 'Machine learning Sentiment Analysis',padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text= 'Sentiment Analysis using python',padx=5, pady=5)
label4.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# tab 4 ------------------------------------------------------------------

about_label = Label(tab4,text="Made by:",pady=5,padx=5)
about_label.grid(column=1,row=1)
about_label = Label(tab4,text="Arpit Upadhyay",pady=5,padx=5)
about_label.grid(column=1,row=2)
about_label = Label(tab4,text="Nishi Sharma",pady=5,padx=5)
about_label.grid(column=1,row=3)
about_label = Label(tab4,text="Aryan Chaudhary",pady=5,padx=5)
about_label.grid(column=1,row=4)
about_label = Label(tab4,text="Divya Jain",pady=5,padx=5)
about_label.grid(column=1,row=5)

# Functions FOR NLP FOR TAB ONE --------------------------------------------
def get_tokens():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	final_text = list(str(new_text.words).split(" "))
	result = '\nTokens:{}'.format(final_text)
	tab1_display.insert(tk.END,result)

def get_pos_tags():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	final_text = new_text.tags
	result = '\nPOS of Speech : {}'.format(final_text)
	tab1_display.insert(tk.END,result)


def get_sentiment():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text,analyzer=NaiveBayesAnalyzer())
	final_text = new_text.sentiment
	p=final_text.p_pos * 100
	n=final_text.p_neg * 100
	result= '\nPolarity:{}, Positive%:{}, Negative%:{}'.format(final_text.classification,p,n)
	tab1_display.insert(tk.END,result)

def get_entities():
	raw_text = str(raw_entry.get())
	docx = nlp(raw_text)
	final_text = [(entity.text,entity.label_) for entity in docx.ents ]
	result = '\nEntities:{}'.format(final_text)
	tab1_display.insert(tk.END,result)



# Clear entry widget
def clear_entry_text():
	entry1.delete(0,END)

def clear_display_result():
	tab1_display.delete('1.0',END)
	
# MAIN NLP TAB 1------------------------------------------------
l1=Label(tab1,text="Enter Text To Analysis")
l1.grid(row=1,column=0,padx=15,pady=15)


raw_entry=StringVar()
entry1=Entry(tab1,textvariable=raw_entry,width=100)
entry1.grid(row=1,column=2)

# BUTTONS for tab1--------------------------------------
button1=Button(tab1,text="Tokenize", width=15,command=get_tokens,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=15,pady=15)


button2=Button(tab1,text="POS Tags", width=15,command=get_pos_tags,bg='#BB86FC')
button2.grid(row=4,column=2,padx=15,pady=15)


button3=Button(tab1,text="Sentiment", width=15,command=get_sentiment,bg='#f44336',fg='#fff')
button3.grid(row=4,column=3,padx=15,pady=15)


button4=Button(tab1,text="Entities", width=15,command=get_entities,bg='#80d8ff')
button4.grid(row=5,column=0,padx=15,pady=15)


button5=Button(tab1,text="Reset", width=15,command=clear_entry_text,bg="#b9f6ca")
button5.grid(row=5,column=2,padx=15,pady=15)

button6=Button(tab1,text="Clear Result", width=15,command=clear_display_result)
button6.grid(row=5,column=3,padx=15,pady=15)

# Display Screen For Result
tab1_display = ScrolledText(tab1,width=100)
tab1_display.grid(row=8,column=0, columnspan=4,padx=5,pady=5)

# Allows you to edit
tab1_display.config(state=NORMAL)

#-----------------------------------------------------------------------------
#function for tab 2
# Clear Text file  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_result():
	tab2_display_text.delete('1.0',END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
	file1 = tk.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)

def get_file_tokens():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = list(str(new_text.words).split(" "))
	result = '\nTokens:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

def get_file_sentiment():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
	tab2_display_text.insert(tk.END,result)

def get_file_pos_tags():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = new_text.tags
	result = '\nPOS of Speech : {}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def get_file_entities():
	raw_text = displayed_file.get('1.0',tk.END)
	docx = nlp(raw_text)
	final_text = [(entity.text,entity.label_) for entity in docx.ents ]
	result = '\nEntities:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def summary():
	raw_text = displayed_file.get('1.0',tk.END)
	docx = nlp(raw_text)
	final_text = [ (token.text,token.shape_,token.lemma_,token.pos_) for token in docx ]
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)




# FILE READING  AND PROCESSING TAB
l1=Label(tab2,text="Open File To Process")
l1.grid(row=1,column=2,padx=15)


displayed_file = ScrolledText(tab2,height=8,width=100)# Initial was Text(tab2)
displayed_file.grid(row=2,column=1, columnspan=3,padx=5,pady=3)


# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File", width=15,command=openfiles,bg='#c5cae9')
b0.grid(row=3,column=1,padx=15,pady=15)

b1=Button(tab2,text="Reset ", width=15,command=clear_text_file,bg="#b9f6ca")
b1.grid(row=3,column=2,padx=10,pady=15)

b1a=Button(tab2,text="Summary", width=15,command=summary,bg='blue',fg='#fff')
b1a.grid(row=3,column=3,padx=15,pady=15)

b2=Button(tab2,text="Tokenize", width=15,command=get_file_tokens,bg='#03A9F4',fg='#fff')
b2.grid(row=4,column=1,padx=15,pady=15)


b3=Button(tab2,text="POS Tags", width=15,command=get_file_pos_tags,bg='#BB86FC')
b3.grid(row=4,column=2,padx=10,pady=15)


b4=Button(tab2,text="Sentiment", width=15,command=get_file_sentiment,bg='#f44336',fg='#fff')
b4.grid(row=4,column=3,padx=15,pady=15)


b5=Button(tab2,text="Entities", width=15,command=get_file_entities,bg='#80d8ff')
b5.grid(row=5,column=1,padx=15,pady=15)


b6=Button(tab2,text="Clear Result", width=15,command=clear_result)
b6.grid(row=5,column=2,padx=10,pady=15)

b7=Button(tab2,text="Close", width=15,command=window.destroy)
b7.grid(row=5,column=3,padx=15,pady=15)

# Display Screen

# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2,height=14,width=100)
tab2_display_text.grid(row=7,column=1, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

#-------------------------------------------------------------------
#function for tab 3 MACHINE LEARNING

#--------------------------------------------------------------------
#training Naive bayes
#with open('E:/av.csv', newline='') as f:
#    reader = csv.reader(f)
#    data = list(reader)
#---------------------------------------------------------------------------------------------------
T= [
    ('I love this sandwich.', 'pos'),
    ('this is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('this is my best work.', 'pos'),
    ("what an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('he is my sworn enemy!', 'neg'),
    ('my boss is horrible.', 'neg'),
    ('If this new iPhone sounds like itll suck after tomorrows announcement then the jokes on me for saving up to get it', 'neg'),
    ('I love Apple despite the fact that Im constantly dissing the iPhone Really looking forward to tomorrows event', 'pos'),
     ('iPhones Everything you need to know Apples event of the year which is being held on September has ma ', 'pos'), ('Apple is expected to announce the iPhoneS atPM tomorrow  Translation At PM tomorrow the Internet will lose its shit', 'pos'), ('I dropped my iPhone in the beer cooler on the beach yesterday so I gotta get a new one tomorrow', 'neg'), ('Christmas in September Apples keynote on the upcoming iPhone is today atam Pacific', 'pos'), ('All the latest Sheffield Wednesday news on iPhone and iPad SWFC', 'pos'), ('Analyst suggests this may be the last big iPhone launch  with via AppleEvent', 'pos'), ('Tech Tuesday Apple launches new iPhone with Force Touch newiphone', 'pos'), ('I cant wait I need a new phone And since Samsung has abandoned the UK market Ill be ordering an iPhone this Friday', 'pos'), ('If Apple is upgrading the camera on the iPhones models I seriously may upgradeamp my phone isnt evenyr old yet photographyproblems', 'pos'), ('In Wednesdays FirstFT  long reign the Queen iPhone unveiling and more Sign up at ', 'pos'), ('its gonna at least be a new iPhone event  Its that time of year ago The next iPhone comes out onor around Septth', 'pos'), ('Will I be getting a new iPhone this year No But my two older kids will So Im kind of curious about today ', 'pos'), ('So yeah back to the iEvent today If Apple doesnt do lowcost iPhoneC replacement model akaC then we may see peak iPhone within mo', 'pos'), ('unique mark patterns made by the oil of the fingertip on the glass of the iPhone screen when using different apps ', 'pos'), ('Swanage  An Apple IPhone has been handed in  Swanage Town Hall Office Please come in and speak to us if you think it may be yours', 'pos'), ('Business Insider RUMOUR Siri may always be ready to respond to your voice on the next iPhone AAPL Apple t ', 'pos'), ('I really hope Apple weighs a cup of nuts on the iPhoneSth Generation iPhone', 'pos'), ('This thest year Ive not been to excited about the new iPhone announcement but Im stoked for the new Apple TV amp their streaming service', 'pos'), ('would you PLEASE let us know when the iPhones will be available for purchase Hoping before theth of September Thanks', 'pos'), ('The new IPhone is expected to be unveiled today atpm As well as a potential Apple TV Watch it here AppleEvent ', 'pos'), ('So iPhoneth generation has models Plus andS If I can wait it out Ill get the', 'pos'), (' seats for an Apple product announcement iPhone is just upgrade AppleSiri TV may be big I wonder whos playing TayTay Billy J', 'neg'), ('Cracked myst iPhone ever and Im so pissed  Anyone know where I can get it fixed ASAP besides Apple', 'neg'), ('Cant wait to see the new iPhone tomorrow And final can update my apple watch to OS', 'pos'), ('I expect to see news about aGB iPhone when I wake up tomorrow', 'pos'), ('The iPhoneS the greatest thing to ever exist since the iPhone CROWD GOES WILD  ', 'pos'), ('its your last chance to take advantage of Gazelles best price guarantee on iPhone tradeins ', 'pos'), ('Definitely watching the iPhone event today to see what Ill be upgrading to in February', 'pos'), ('Color take on the head doodles from WonderWoman Wednesday From a while back  only have the iPhone photo though ', 'pos'), ('I do love my iPhoneplus but I am definitely not a fan of the fact that I just accidentally sat on it and it is now another shape', 'neg'), ('Few more hours to iPhones launch and im still using theth generation _', 'pos'), ('Myth Grade Art Teacher had her iPhone stolen from the classroom someone took the SIM card out so she couldnt track it', 'neg'), ('Get the popcorn or coffee in my case ready folks hour till the new iPhone event Tuning in from Asheville NC ', 'pos'), ('Im eligible for an upgrade next Monday Hopefully the new iPhone drops next Friday so I can go straight to Verizon after work', 'pos'), ('Minutes aways for the unvieling of iphonesplus or is it going to be Iphone ', 'pos'), ('apple A look at the evolution of Apples iPhone Apple will unveil the new iPhone on Wednesday The next iPho ', 'pos'), ('I turn soon amp a friend went missing on a Tuesday nite the other who has his iPhone doesnt know how to use it amp I wasnt even there', 'neg'), (' Ah bizarrely I see it on my iPhone but not on laptop with Safari which only hasst tabs  Weird', 'pos'), ('If youre an iPhone user like myself new phone and more to be revealed in the next minutes Watch it live here ', 'pos'), ('Im so excited to see the new iPhone release even though it may be following a trend xD', 'pos'), ('Cool filter called the blinding sun amp iPhonec Lol  Gediminas Tower ', 'pos'), ('Well Ill be watching on ath gen of iphone even it wont get ios update  AppleEvent', 'pos'), ('Why would you waste a good iPod like thisidiotsIDIOTS ', 'neg'), ('I crushed akm run with a pace of with Nike + iPod  makeitcount  nikeplus september  ', 'pos'), ('can next Friday please get here any faster I need the rest of Illinois on my iPod', 'pos'), ('I will have it by tomorrow Im on my iPod now haha When you free', 'pos'), (' come join mark on his charity live stream to help fight Depression and Bipolar   you may even an ipod eggplant', 'pos'), ('Memorised the journey to Lucys tomorrow in case my iPod and iPhone run out of charge on route haha', 'pos'), ('Lmao just turned on my ipod forst time inevs amp this is the last photo ', 'pos'), ('I have the Moonlight Sonatard movement in my iPod and I listen to it when I need to relax', 'pos'), ('I have faith that tonight I may win an iPod which would mean the world to me and I would treasure it qith my life', 'pos'), ('still cant get my IPODrd gen shuffle to change songs cos of the USB NOT RECOGNIZED ERROR shit Does this mean I need new USB CABLE', 'neg'), ('Hey my birthday is this coming Thursday and I dont necessarily want an Ipod but a happy birthday would suffice haha EGGPLANT', 'pos'), ('EGGPLANT LETS GO new winner of the iPod and may we reach out goal Hazzah and Mark are you going to pax south', 'pos'), ('The stream is so long I wanna go to sleep but I want a IPodnd hardest decision in my life', 'pos'), ('EGGPLANT i want a ipod ', 'pos'), ('Apple has a recall on allst generation iPod Nanos And will give you ath generation iPod Nano if you return thest generation one', 'pos'), ('h im going to make a twitter to use on my ipod at schoolwork tomorrow bc this fucks up my notifs', 'neg'), ('I should be getting into bed I am however instead looking through my iPod for songs I might want to pole to  I may be addicted', 'pos'), ('I have to deal with this ipod so rest in pieces my emo snowflake fuckers Heres to our tomorrow Thank you for living to see today', 'neg'), ('Let you know what kind of day its going to best song up on my IPod is Do It Now By Mos DefYB  Leggo', 'pos'), ('Still head over heels in love with myth generation iPod Curated to the hilt ipod Apple oldtech personalmediadevices', 'pos'), ('I may have a yo ipod classic ive never encountered a problem w it unlike my sisters whose newer models seem to crash quite easily', 'pos'), ('BTW is the guy who gave me an iPod last year on which my son st set me up on Twitter Myst tweet was', 'pos'), ('off on holiday tomorrow downloading apps for ipod for the plane anyone know any good free ones', 'pos'), ('I still have my original newfangled iPod Maybe Ill bring it to the game on Monday', 'pos'), ('I may have a playlist on my iPod devoted entirely to songs about trains I may also be a total geek', 'pos'), ('Hey please RT running GNR on Sunday anyone got suggestions for good running songs  Need to update the iPod', 'pos'), ('Finally gonna buy my own camera tomorrow  Im so excited Ill be able to take pictures with something else than my old ipod', 'pos'), ('Loading some sick new music onto my iPod for the BillikenK tomorrow', 'pos'), ('st day back at work after a terrible week off and Ive forgotten my ipod security pass and lunch mondaydaze cancelmonday', 'neg'), ('Dont forget to collect the bills and win free ipod nanoth generation amp CK vouchers of total bills  we ', 'pos'), ('Sitting in my office window open sun shining in listening to my ipod wondering exactly what the catch is with this job', 'pos'), ('Does anyone know how to get around a disabledth gen ipod WITHOUT putting it into recovery mode', 'neg'), ('ipod iPod nano may be the worst ATM skimmer ever created  Just when you thought the click wheel iPODNANO', 'neg'), (' gud thing about losing my phone is that it made me use my iPod which has all the songs I used listen to inrd year', 'pos'), ('I drenched the old iPod nanoth gen in isopropanol and it actually worked The screen will never look the same but totally worth it', 'pos'), ('Cant believe I left my charger at Tias I have just under until tomorrow so in living on my IPod You can only contact me via Twitter', 'neg'), ('Found my old iPod from liketh grade and am now realizing I listened to some hood tunes for just a kid', 'pos'), ('tbt when i got my ipod stolen inth grade and i was only upset bc i thought whoever stole it was gonna leak the lesbian porn i had on it', 'neg'), ('Im not taking my iPod to school tomorrow because I want to have a battery when I go to my concert', 'pos'), ('Mys is out of data till theth and cant connect to wifi anymore I have an iPod now', 'neg'), ('just synced saturdays live set on my ipod time to pick up fragments of my memories together and cry on the train', 'neg'), (' Thats why my ProgIndieHeavy Rockfilled iPod has One Directionsrd andth albums on it I am Not kidding', 'pos'), ('yall i got my ipod taken inrd period because i forgot to turn my volume down and i got a notif about army selca day', 'neg'), ('I used to absolutely love the music to Silent Hill Even had it on my ipod ', 'pos'),
    ('i went through my old iPod nano and I still listen to the same music I did inth gradechili peppers green day the killers blink omfg', 'pos'), ('Found an ancient ipod nano I may have to keep it', 'pos'), ('Gonna try to run laps tomorrow atleast it should be easy I just cant talk to ppl Just gotta listen to my iPod and keep runnin', 'pos'), ('st song on the iPod upon leaving GB is Good Life by One Republic amp upon leaving an amazing weekend w amp her fam it truly is', 'pos'), ('Also my fucking iPod got stolen at snipes amp the only thing I cant let go of is the music Take thest gen iPod just want my Jamz back', 'neg'), ('idk I just wanted to make convo since my phone is kinda ruined because pool and Im using like ard generation iPod lol so', 'neg'), ('miss you tay I was just looking thru my ipod amp I have vids of you singing back in SAT prep lol', 'pos'), ('Sometimes youre just better off dead theres a gun in your hand thats pointing to your head Wednesdays iPod selection', 'neg'), ('I have loads to tell you guys that will make yall super proud but Im using my iPod now and its super laggy so Ill tell later or tomorrow', 'pos'), ('havent listened all morning WED is an IPod day besides dont want to hear about Astros choke job', 'neg'), ('Another nail in the coffin to Jayz failure Tidal as Cash Money sues form over Lil Wankers album ', 'neg'), ('FF  not just for the drinks but for JayZs problems problems that we may just ponder about at some point in our lives', 'pos'), ('Sitting at a curb staring at the White House Listening to jayzthats a fine Friday', 'pos'), ('Dear ppl who attribute vocal fry trend to Britney amp Kim K have you ever heard JayZ talk ', 'neg'), ('Im crushed Its a hoax JayZ and Beyonce arent trying to buy rights to the Confederate flag via ', 'neg'), ('For those who may not know JayZ wrote the verses for Still DRE but hes never disrespected Dre or ever spoken about ghostwriting', 'pos'), ('Decemberth only cause I used the beginning in my JayZ speech for class ', 'pos'), ('Was hoping this would escalate to be something like Nas vs JayZ but Meek got KOed in thend round lol', 'pos'), ('NEW Video Casey Veggies Talks First Meeting With JayZ At Years Old Working Hard to Inspire the Youth Dec', 'pos'), ('Meek drooped like a Jayz album thend amprd time you hear it You will understand it and Fall in love with it', 'pos'), ('JayZ stole his wholend verse from Problems from Bun B in the UGK song Touched Come on yall listen to old hip hop', 'neg'), ('Roadblock In the immortal words of JayZ Whatever deity may guide my life dear lord dont let me die tonight ', 'pos'), ('CRAZY IN LOVE by BEYONCE FEAT JAYZ was no in the UK charts on August ', 'pos'), ('Would be crazy if Dr Dre Eminem JayZ all show up at OVOFest tomorrow Tonight its OVO', 'pos'), ('JayZ stole Bigs actual words damn near dast bars on I just wanna love you give it to me  ', 'neg'), ('My following may not be as big as JayZs but I got a solid supportive growing following Thanks for the love TeamMYU', 'pos'), ('thest dance at my wedding will actually just be a duet of Diamonds From Sierra LeoneRemix with my husband as JayZ and myself as Kanye', 'pos'), ('Aye now Meek may surprise us You know when JayZ dropped Takeover they thought it was over for Nas And then Ether', 'pos'), ('May the best of your today be the worse off your tomorrow  JayZ', 'pos'), ('WEHO is leading the pack for a THE CARTERS Lil Wayne Beyonce and JayZ ride Thursday atpm Grab a bike', 'pos'), ('Imagine if Ether had dropped in the social media age We may not have the same respect we do for Jayz today', 'pos'), ('I know its old but The Beatles JayZ Danger Mouse  cmon Classic mix  ', 'pos'), ('I grew up to this songdidnt knew thend verse is about beyonceuntil nowJAYZ  Lost One ft Chrisette Michele ', 'pos'), ('The sun earth the Lakers JayZ Oprah and whoppers ', 'pos'), ('Prince confirmed that he and JayZ will release an album September PaisleyPark  Minneapolis', 'pos'), ('St James Park randomly playing the instrumental for Myst Song by JayZ at half time  Decent', 'pos'), ('people celebrity Tidal is a Satanic Illuminati Plan to make more  JayZ Beyonce  ', 'neg'), ('Personally handing JayZ jerseys may be the highlight of my New York existence First time Ive been star struck', 'pos'), ('JayZ and Beyonce came to Taylorsth but not Kim and Kanyes wedding Imma let Taylor finish but she had the best birthday of all time', 'pos'), ('FridayFun JayZs got that Friday feeling   Have you', 'pos'), ('Who Belong In therd spot for top of all time JayZ Nas or Eminem', 'pos'), ('Make a lasting impression on the first day of class tomorrow walk in with a boom box blaring Public Service Announcement by JayZ', 'pos'), ('Enjoying how the JayZ vs Abdel Halim Hafez lawsuit forces serious newspapers to put Big Pimpin in headlines ', 'pos'), ('JayZ make time for Bey The President make time for thest lady So where are you so busy at again', 'neg'), ('theres no middle ground with her though Her Jayz insights used to veer off into therd testicle range', 'neg'), ('Just to see a bitch that looks like JayZ Got me fucked up on theth level of hell', 'neg'), ('Sept  Good JayZ drops the best rap album of the decade The Blueprint  Bad World Trade Center gets destroyed   MindBlown', 'pos'), ('Dreamed I was and I spent the night making out with JayZ at a Lower East Side rooftop party until the sun came up', 'pos'), ('My nigga sat down with JayZs right hand man on a rooftop in the city Im rootin for youngin Straight up', 'pos'), ('The best part of living in New York is the nightlife Thend best part is knowing that JayZ and Beyonce share the same weather as me', 'pos'), ('Today was a JayZ type of the day Who knows what tomorrow will bring', 'pos'), ('Whats stopping JayZ Puffy Cent Lil Wayne from doing the same if they havent already  ', 'neg'), ('Although you may know this better than I do since youre from California lol Im not knocking JayZ view in black culture I say', 'pos'), ('We make a million of beats cause our stories is deep And fuck tomorrow as long as the night before was sweet  JayZ', 'pos'), ('Only looking forward to Kanyes performance at the VMAs tomorrow Heard hes bringing out Rih Bey Jayz amp Paul McCarthy', 'pos'), ('I was certainly not expecting to bring and JayZ to the Ville  I may have dropped a tear or two  Greatest show ever', 'pos'), ('If Kanye became President folk that wrote off the masonicilluminati symbols in he and JayZs musicvids as meaningless may think again', 'pos'), ('Today duringth it was dead silent in the library amp all of a sudden my iPad started blasting JayZs voice saying Motherfucker I got this', 'pos'), ('Also the correct Top is Eminem JayZPac The Notorious BIG and Ice Cube in that order with Big Pun as theth man', 'pos'), ('JayZ sat in that Interview like a God showing that he was truly ahead of his time while the other niggas flirting with Foxy Brown', 'pos'), ('I knew Jayz was getting old but I forgot about Eminem He looks something ', 'pos'), ('Not really and Im a huge JayZ fan But when Marchth come around Biggie all day everyday', 'pos'), ('happy bday to the amazing Beyday big love to you JayZ and Blue Ivy may ur family continue to amaze this world loves x', 'pos'), ('The gamest album song he say he rap like EazyE then Nas then cent then dr Dre then JayZ then EazyE again then like his dead bro', 'pos'), ('The day Jayz comes to SA Ill be thest person to cue  at the computicket  I love that man', 'pos'), ('I think you should get as guest against Colbertsst show   He starts with Jeb Bush really baddecisions', 'neg'), (' baddecisions You make me not want to watch your shows by having Jeb BUSH asst show guest NOCOLBERT', 'neg'), ('Jeb Bushs ad blitz begins Septth in the early primary states No poll movement by October Donors might squirm', 'neg'), ('Eric Cantor who evidently wants Jeb Bush to lose the nomination will endorse Jeb Bush on Thursday ', 'neg'), ('Hey Jeb Bush first thing you need to remember is that youre actually running in a primarynd primary voters are nuts', 'neg'), ('Hillary upset Biden may run Jeb Bush upset Trump is leading in the polls both had family in the WH both feeling entitled to be next', 'neg'), ('We need to terminate this horrible deal with Iran on the veryst day in office but JEB BUSH REFUSES End of discussion ', 'neg'), ('Will Ted Cruz Jeb Bush and all the top ten who swore to support the GOP primary winnerdo it   Looks like they may end with TRUMP HA', 'neg'), ('The ONE GOOD thing Trump may do in the LONG RUN is Take OUT Jeb Bush Trump is targeting Jeb as his Main threat', 'neg'), ('Jeb Bush dug himself a deep hole with his Act of Love commentIf he was + yesterday he will be tomorrow', 'neg'), ('OMG A Trump supporter on CNN just suggested that Jeb Bush may have low testosterone which is why hes low energy', 'neg'), ('Jeb Bush is an utter failure Should drop out now as he is inth place', 'neg'), ('What I dont get is why donors would fill Jeb Bushs coffers  There is a frightening division in the Republican Party that may end in loss', 'neg'), ('John Kasich may is just Jeb Bush from the a different state Hes a mealy mouthed squish  ', 'neg'), (' Jeb Bush appears to be afraid of something  Probably the truth and Trump may be able to help him out', 'neg'), ('Turns out that annointing Jeb Bush the default establishment candidate may have been premature you dont say ', 'neg'), ('Tunein to tomorrow Im sitting down with GOP presidential candidate Jeb Bush', 'pos'), ('Donald Trump may criticize Jeb Bush all he wishes but he isnt able to call Jeb Bush nor his supporters racist like the Donald is', 'neg'), ('Jeb Bush may have got himself into a bit of a mess The presidential candidate who will appear on the first  ', 'neg'), ('haha Jeb Bush is such a bore the guy in the background of this vid could totally not give a shit about this dirtbag ', 'neg'),
    (' hell with Jeb bush with Spanish speaking We dont tell Mexico speak English And Im half Hispanic Englishst N the USA', 'neg'),
    ('WASHINGTON Reuters  Jeb Bush said on Thursday he would back fellow Republican presidential hopeful Donald T ', 'pos'), ('If Jeb Bush wins by some far chance the flood gate will be really opened and ourst language will be spanish', 'neg'), ('Jeb Bush should speak English only as it encourages ESL we should be honoring this country  not making it into ard world one', 'neg'), ('Jeb Bush probably knows and hed probably get us into ard Iraq invasion  Knows lots of little facts learns nothing', 'neg'), ('  I cant believe Im defending Jeb Bush but here goesst No official language here in the United States of America', 'neg'), ('and destroy Jeb Bush while Im at it Though these same priorities may be reversed for all I know', 'neg'), ('when you talk about Ben Carson please show him not Jeb Bush like you did on your Thurs Show', 'neg'), ('Just minutes after Jeb Bush bashed Donald Trump in his stump speech on Thursday Bush was questioned by a frustrated voter on what he', 'neg'), ('Jeb Bush pretending hes a co front runner but hes inth place and Carly Fioriana bragging how shes innd place in states Losers', 'neg'), ('Cmon If anybody needs your harsh advice  it would be your friend Jeb Bush does a heck of a lot better', 'neg'), ('The force was not with him when Jeb Bush tried to get social on ForceFriday  marketing millennials', 'neg'), ('A day after taking steps to warm relations with Hispanics Donald J Trump may have taken a step backward when he suggested that Jeb Bush', 'neg'), ('Jeb Bush attacking Donald Trump in Spanish seems like thend act of a Greek tragedy where your efforts to avoid the prophecy make it happen', 'neg'), ('Former Florida Gov Jeb Bush said Thursday that his chief opponent frontrunner Donald Trump is trying to insult his way to the White', 'neg'), ('Jeb Bush may have lots of cash and great political organization but dont compare him to Romney  He doesnt have the moxie needed today', 'neg'), ('All the Beverly Hillbilly Cast Granny Hillary Jeb bush jethro boehner eli may   banker Barak', 'neg'), ('No idea sorry Just kno pundits say Trump will prob lose popularity later as he has little policy Poss Jeb Bush may get Rep Nom', 'neg'), (' Why no mention that Jeb Bush sat on the board of the fraudsters fake company Nice try dumbass', 'neg'), ('ha ha ha Jeb Bush said he didnt need the base to win and he was going to prove it But single digitth place in NH may be result', 'neg'), ('Hey Jeb Bush are these examples of acts of love also Wake up dude they want bring their craphole country to USA ', 'neg'), ('Jeb Bush releasing tax reform plan tomorrow Trump will say it is stupid Bush a moron His plan Make America great amp put on top again', 'neg'), ('Four Hard Questions to Ask About Jeb Bushs Tax Plan Jeb Bushs tax plan is coming out Wednesday Expect the usual soaring language ', 'neg'), ('Refusing to own a gun may cost Jeb Bush dearly Crime is out of control in America Bush going unarmed will ma ', 'neg'), ('Obama gives Joe Biden blessing for bid gt If a second Clinton mail server turns up he may get the nomination ', 'pos'), ('Cmon Joe Biden You really dont want to be President Stop thinking with your ego and start thinking about the party and the people', 'neg'), ('Politico Republicans Giddy Over Possible Biden Candidacy Speculation that Vice President Joe Biden may make  ', 'pos'), ('The continued attacks on thend Amendment will continue if America is foolish enough to ever elect Joe Biden for POTUS Obamasrd term', 'neg'), ('Joe Biden for Presient Really He may be a nice guy but the man is a buffoon', 'neg'), ('Dear journalists please quit with the Joe Biden stories amp speculation Hes not even ourrd choice Sincerely Democrats everywhere', 'neg'), ('Anyway  peace I support both Hillary and Bernie and will support Joe Biden should he run He may indeed ', 'pos'), ('Bennet later dodged a question about the possibility of a Joe Biden runth down eh UR all hypocrites', 'neg'), ('TOP REASONS JOE BIDEN SHOULD RUN FOR PRESIDENT Jimmy Fallon may invite him on his show to play something with pingpong balls', 'pos'), ('st Clinton is the worst debaternd have you ever heard Joe Biden open his mouth Hes a clown', 'neg'), ('Why Joe Biden May Be the Best Hope for Small Businesses ', 'pos'), ('Happy Friday Heres Joe Biden making a cameo on a episode of Where in the World is Carmen Sandiego ', 'pos'), ('Starting to hope Joe Biden enters the race It may just be time for an alternative A debate between Joe and Trump would be epic', 'pos'), ('With Joe Biden campaign fun about to begin via Election', 'pos'), ('Joe Biden may join Bernie Sanders in the Democrat primary I thought the Democrats were opposed to fossil fools ~ Emily Zanotti', 'neg'), ('Take a good look at Bernie Saunders hes giving Hillary a run for her money Joe Biden may join the race And theyre off', 'pos'), ('Why Joe Biden may well be a great candidate for SMBsif hell run of course ', 'pos'), ('Only with Progressive Liberal Lovest people like Bernie Sanders amp Joe Biden can America stay steady Mature of Love Forward first', 'pos'), ('P AFLCIO Pres Dick Trumka to march with Joe Biden in Labor Day paradePeople can read into thatwhat they want Hes a good friend', 'pos'), ('I think Joe Biden will announce hes running for president on Colbert next Thursday', 'pos'), ('Great piece on Joe Biden and allimportant Florida Wish I knew the folks in the condominiums he visits DraftBiden ', 'pos'),
('my phone does not run on latest IOS which may account for problem the other day  time it was replaced', 'neg'),
('Not sure how to start your publication on iOS Well be live helping with ask me anything sessions today and Friday ', 'pos'),
('Parkrun app for iOS downloaded Where have you been before Great app easier access of info amp ready for Saturdays run ', 'pos'),
('Today launches with apps for iOS and Android devices in the US and UK here is what you need to know ', 'pos'),
('Got a project you want to work on Need help with Swift Need an excuse to hang with iOS devs on a Sat Hang with us ', 'pos'),
('Met with iOS Developer today We may have a go', 'pos'), ('CrossSkyHigh is going IOS saturday For now try this indiedev ', 'pos'),
('Whats the best way to get audio recordings from ard party app off of an iOS device Jailbreaking isnt an option', 'pos'),
('Five Great Free Apps and Games for iOS  Augustth Edition  Its that time of the week again News LCHBuzz', 'pos'), 
('See news through the eyes of real people amp be your own reporter with Fresco for iOS coming Septemberth ', 'pos'),
('Siri knows all about Apples iOS event on theth GiveUsAHint ', 'pos'), ('Whos ready for Build Tomorrow Might be the last build till it come to iOS ', 'pos'),
('As Ive been on FB for many years I have a few hundred photo albums but only thest appear in the IOS app Is that right', 'pos'),
('try beat mp it may be on android i have it on ios and its fairly decent', 'pos'),
('Even though there are other differences in the IOS features this still may make people lean a little more towards Apple', 'pos'),
    ('Tom Holland is a terrible spiderman.','pos'),
    ('a terrible Javert (Russell Crowe) ruined Les Miserables for me...','pos'),
    ('The Dark Knight Rises is the greatest superhero movie ever!','neg'),
    ('Fantastic Four should have never been made.','pos'),
    ('Wes Anderson is my favorite director!','neg'),
    ('Captain America 2 is pretty awesome.','neg'),
    ('Let\s pretend "Batman and Robin" never happened..','pos'),
    ('Superman was never an interesting character.','pos'),
('Fantastic Mr Fox is an awesome film!','neg'),
('Dragonball Evolution is simply terrible!!','pos'),
('the beer was good.', 'pos'),
('I do not enjoy my job', 'neg'),
("I ain't feeling dandy today.", 'neg'),
("I feel amazing!", 'pos'),
('Gary is a friend of mine.', 'pos'),
("I can't believe I'm doing this.", 'neg'),
('I am bad boy','neg')
]

#----------------------------------------------------------------------------------------------------------------
cl = NaiveBayesClassifier(T)
#dt = DecisionTreeClassifier(T)


# Clear Text file  with position 1.0
def clear_text():
	entry1.delete(0,END)

# Clear Result of Functions
def clear_res():
	tab3_display.delete('1.0',END)

def get_sentiment_nb():
    raw_text = str(raw_entry.get())
    blob = TextBlob(raw_text, classifier=cl)
    a= blob.classify()
    result = '\nPolarity:{}'.format(a)
    tab3_display.insert(tk.END,result)

#def get_sentiment_dt():
#    raw_text = str(raw_entry.get())
#    blob = TextBlob(raw_text, classifier=dt)
#    a= blob.classify()
#    result = '\nPolarity:{}'.format(a)
#    tab3_display.insert(tk.END,result)

# MAIN NLP TAB 3
l1=Label(tab3,text="Enter Text To Analysis")
l1.grid(row=1,column=0,padx=15,pady=15)


raw_entry=StringVar()
entry1=Entry(tab3,textvariable=raw_entry,width=100)
entry1.grid(row=1,column=2)


#BUTTONS for tab 3
button1=Button(tab3,text="Naive Bayes", width=15,command=get_sentiment_nb,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=15,pady=15)

button2=Button(tab3,text="Reset", width=15,command=clear_text,bg='#BB86FC')
button2.grid(row=4,column=2,padx=15,pady=15)


button3=Button(tab3,text="Clear Result", width=15,command=clear_res,bg='#f44336',fg='#fff')
button3.grid(row=4,column=3,padx=15,pady=15)

#button4=Button(tab3,text="Reset", width=15,command=clear_text,bg='#80d8ff')
#button4.grid(row=1,column=3,padx=15,pady=15)


# Display Screen For Result tab 3
tab3_display = ScrolledText(tab3,width=120)
tab3_display.grid(row=8,column=0, columnspan=4,padx=5,pady=5)

# Allows you to edit
tab3_display.config(state=NORMAL)





window.mainloop()




