"""
A Python script to clean up pathway abundance input data. 

Takes in .csv imported dataset with:
 >pathway names unchanged from paprica output
 >float values of relative abundance 
 
"""
#-------------------------
## Hinako Terauchi
## Apr 20, 2021
#-------------------------

def compile_regEx_paprica():
    """
    Compiles the regEx needed to parse out paprica-based pathway string.
    
    ## Eventually figure out the better way to do this
    - want: be able to search if any regEx matches a string input
        > then spit out the regex that it matched with 
        > go into re.search() statements accordingly
        > keep in mind some order matters. 
        > I have list below but dict is prob more versatile
        > check the bookmarked pages
            > especially about Aho–Corasick algorithm
    """
    
    import re
    
    # Define a list to store the results to return:
    regEx_list = []
    
    # compiling regex:

    # in case of 'to':
    p_to_source = re.compile("\S+?(?=\.+to)")
    p_to_target = re.compile("(?<=\.to.)\S+")
    # append to list:
    regEx_list.append(p_to_source)
    regEx_list.append(p_to_target)

    # target has 'and':
    p_and_firstT = re.compile("\S+(?=\.and\.)")
    p_and_secondT = re.compile("(?<=\.and\.)\S+")    
    # append to list:
    regEx_list.append(p_and_firstT)
    regEx_list.append(p_and_secondT)

    # sourse: just get the metabolite:
    s_no_ion = re.compile("\S+(?=\.\w+ion)")
    # append to list:
    regEx_list.append(s_no_ion)

    # replacing biosynthesis only's:
    t_no_synth4sub = re.compile("\.\w+synthesis\S*")
    # append to list:
    regEx_list.append(t_no_synth4sub)

    # getting rid of roman numerals:
    p_no_IV = re.compile("\.[IV]*$")
    # append to list:
    regEx_list.append(p_no_IV)

    # getting before & after 'from':
    t_from = re.compile("\S+(?=\.\S*from\.\S*)")
    s_from = re.compile("(?<=from\.)\S+")
    # append to list:
    regEx_list.append(t_from)
    regEx_list.append(s_from)

    return regEx_list 

#--------------------------------------
    
def parse_paprica_paths(data):
    """
    Parses out the pathway names in paprica format
    and outputs a dataframe with nodes and edge weight
    
    *currently includes the re.compile()
    since I can't figure out a better way
    """
    
    import re
    
    # compile all the regEx:
    ## in case of 'to':
    p_to_source = re.compile("\S+?(?=\.+to)")
    p_to_target = re.compile("(?<=\.to.)\S+")
    ## target has 'and':
    p_and_firstT = re.compile("\S+(?=\.and\.)")
    p_and_secondT = re.compile("(?<=\.and\.)\S+")
    ## sourse: just get the metabolite:
    s_no_ion = re.compile("\S+(?=\.\w+ion)")
    ## replacing biosynthesis only's:
    t_no_synth4sub = re.compile("\.\w+synthesis\S*")
    ## getting rid of roman numerals:
    p_no_IV = re.compile("\.[IV]*$")
    ## getting before & after 'from':
    t_from = re.compile("\S+(?=\.\S*from\.\S*)")
    s_from = re.compile("(?<=from\.)\S+")

    # Define an empty dataframe formatted for networkx:
    dfInput4nx = pd.DataFrame(columns=["source","target","weight"])
    
    # go thru the pathway names and parse them:
    ### ! very brute force X( !
    
    for rowNum in range(len(data)):
        path=data["pathways"][rowNum]
        print(rowNum,path)
        weight = data["amount"][rowNum]

        # if path has roman numerals or period attached:
        if re.search(p_no_IV,path):
            path=re.sub(p_no_IV,"",path)

        # if 'to' format:
        if re.search("\.to\.", path):
            source = re.search(p_to_source,path).group()
            # if source has -ion attached:
            if re.search(s_no_ion,source):
                source = re.search(s_no_ion,source).group()

            target = re.search(p_to_target,path).group()

            # if resulting target more than 1:
            if re.search("and",target):
                #print(target)
                #print(re.search(p_and_firstT,target))
                target1=re.search(p_and_firstT,target).group()
                target2=re.search(p_and_secondT,target).group()

                dfInput4nx= dfInput4nx.append({"source":source, "target":target1, "weight":weight},ignore_index=True)
                dfInput4nx= dfInput4nx.append({"source":source, "target":target2, "weight":weight},ignore_index=True)

            # if target is just 1:
            else:
                # adding all the info to the df:
                dfInput4nx= dfInput4nx.append({"source":source, "target":target, "weight":weight},ignore_index=True)

        # if it has 'synthesis' but no 'to':
        if re.search(t_no_synth4sub,path):
            source = "unknown"+str(rowNum)
            target = re.sub(t_no_synth4sub,"",path)
            dfInput4nx=dfInput4nx.append({"source":source, "target":target, "weight":weight},ignore_index=True)

        # if it's 'from' format:
        if re.search("from",path):
            source = re.search(s_from,path).group()

            target = re.search(t_from,path).group()
            # if target has -ion attached:
            if re.search(s_no_ion,target):
                target = re.search(s_no_ion,target).group()

            dfInput4nx =dfInput4nx.append({"source":source, "target":target, "weight":weight}, ignore_index=True)
            
            
    return dfInput4nx

#------------------------------------------

    
    







