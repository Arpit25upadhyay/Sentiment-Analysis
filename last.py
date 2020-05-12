# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *

# NLP Packages
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import spacy
nlp = spacy.load('en_core_web_sm')
from textblob import Blobber

 
 # Structure and Layout
window = Tk()
window.title("Sentiment Analysis")
window.geometry("1000x700")
window.config(background='black')

# TAB LAYOUT
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
#tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)


# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text='Sentiment Analysis')
tab_control.add(tab2, text='File Processer')
#tab_control.add(tab3, text="Visualize")
tab_control.add(tab4, text='About')


label1 = Label(tab1, text= 'Sentiment Analysis',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'File Processing',padx=5, pady=5)
label2.grid(column=0, row=0)

#label3 = Label(tab3, text= 'Enter Text to Visualize',padx=5, pady=5)
#label3.grid(column=0, row=0)

label4 = Label(tab4, text= 'Sentiment Analysis using python',padx=5, pady=5)
label4.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

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

# Functions FOR NLP FOR TAB ONE
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

b=Blobber(analyzer=NaiveBayesAnalyzer())
def get_sentiment():
	raw_text = str(raw_entry.get())
	new_text = b(raw_text).sentiment
	#final_text = new_text.sentiment
	p=new_text.p_pos * 100
	n=new_text.p_neg * 100
	result= '\nPolarity:{}, Positive%:{}, Negative%:{}'.format(new_text.classification,p,n)
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


# Clear Text  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_result():
	tab2_display_text.delete('1.0',END)


#function for tab 3 Graph view

#def get_sentiment():
#	raw_text = str(raw_entry.get())
#	new_text = TextBlob(raw_text, analyzer=NaiveBayesAnalyzer())
#	final_text = new_text.sentiment
#	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
#	tab3_display.insert(tk.END,result)


# MAIN NLP TAB

#raw_entry=StringVar()
#entry1=Entry(tab3,textvariable=raw_entry,width=100)
#entry1.grid(row=1,column=2)

# BUTTONS
#button1=Button(tab3,text="Visualize", width=15,command=get_tokens,bg='#03A9F4',fg='#fff')
#button1.grid(row=1,column=3,padx=15,pady=15)

# Display Screen For Result
#tab3_display = ScrolledText(tab3,width=120)
#tab3_display.grid(row=9,column=0, columnspan=4,padx=5,pady=5)




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


def get_file_pos_tags():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = new_text.tags
	result = '\nPOS of Speech : {}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def get_file_sentiment():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
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




# MAIN NLP TAB
l1=Label(tab1,text="Enter Text To Analysis")
l1.grid(row=1,column=0,padx=15,pady=15)


raw_entry=StringVar()
entry1=Entry(tab1,textvariable=raw_entry,width=100)
entry1.grid(row=1,column=2)

# BUTTONS
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

window.mainloop()




