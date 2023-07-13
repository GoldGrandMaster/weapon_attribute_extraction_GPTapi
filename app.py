# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey
extraction_prompt = "\nThis is weapon description. Extract the attributes [Weapon Name, Type/Category, Power/Force, Range/Effective Range, Accuracy/Precision, Reliability/Durability, Fire Rate/Cyclic Rate, Caliber/Projectile Size, Magazine Capacity, Barrel Length, Weight, Overall Length, Operating System/Action, Stock/Buttstock, Grip/Handle, Sights/Optics, Muzzle Device/Flash Suppressor, Safety Mechanism, Trigger Type, Fire Selector Modes (Single, Burst, Full Auto), Magazine Type (Detachable, Fixed), Recoil Management System, Firing Mechanism (Semi-Automatic, Automatic), Country/Manufacturer, Year of Introduction, Usage/Role (Assault, Sniper, Shotgun, etc.), Materials (Metal, Polymer, Wood), Folding/Adjustable Stock, Picatinny/Accessory Rail, Sling Attachment Points, Bayonet Compatibility, Suppressor/Suppressor-ready, Reload Mechanism (Bolt, Pump, Lever, etc.), Feed System (Box Magazine, Drum Magazine), Rate of Fire, Penetration Capability, Stopping Power, Modularity/Customization Options, Disassembly/Assembly Process, Grip Texture/Patterning, Ambidextrous Features, Sighting System (Iron Sights, Red Dot, Scope), Rail Systems (M-Lok, KeyMod), Ergonomics/Handling, Aesthetics/Design, Field Stripping/Cleaning, Fire Control Group/Trigger Assembly, Gas System (Direct Impingement, Piston), Barrel Profile (Heavy, Light, Fluted), Magazine Release Mechanism, Ejection Port Position (Left, Right), Bolt Carrier Group Design, Muzzle Velocity, Special Features/Innovations, Discreet Carry Options]  from this description. write the result like this [attribute1 name : ... after next line attribute2 name : ... after next line]"
# App framework
st.title('Weapon Atrributes Extraction')
prompt = st.text_input('Plug in your weapon description here')

# Prompt templates
title_tempalte = PromptTemplate(
    input_variables = ['topic'],
    template='{topic}' + extraction_prompt
)


# LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_tempalte, verbose=True, output_key='title')

# show stuff to the screen if there's a prompt
if prompt:
    title = title_chain.run(prompt)

    st.write(title)