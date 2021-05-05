#https://aurora-network-global.github.io/sdg-queries/

def in_sdg1(t):
    #Target 1.1
    if  t.find("poverty")>-1:
        if  t.find("eradicat")>-1       or \
            t.find("reduct")>-1         or \
            t.find("end")>-1            or \
            t.find("ending")>-1         or \
            t.find("alleviat")>-1:
            return True
               
    if  t.find("poverty line")>-1       or \
        t.find("poverty indicator")>-1:
        return True
        
    if  t.find("poverty")>-1            or \
        t.find("income")>-1:
        if  t.find("inequalit")>-1:
            return True
            
    if  t.find("poverty")>-1:
        if  t.find("chronic")>-1        or \
            t.find("extreme"):
            return True
            
    #Target 1.2
    if  t.find("poverty")>-1:
        if  t.find("living")>-1         or \
            t.find("life")>-1           or \
            t.find("child")>-1          or \
            t.find("socioeconomic")>-1  or \
            t.find("socio-economic")>-1 or \
            t.find("social welfare")>-1 or\
            t.find("household")>-1      or \
            t.find("income")>-1         or \
            t.find("poverty line")>-1:
            return True
 
    #Target 1.3
    if  t.find("social protection")>-1          or \
        t.find("economic marginalization")>-1   or \
        t.find("economic marginalisation")>-1   or \
        t.find("poor")>-1                       or \
        t.find("vulnerable")>-1:
        if  t.find("poverty")>-1                or \
            t.find("income")>-1:
            return True
            
    #Target 1.4
    if  t.find("access")>-1                 or \
        t.find("right")>-1:
        if  t.find("economic resource")>-1  or \
            t.find("basic service")>-1:
            return True
            
    if t.find("ownership")>-1 and t.find("land")>-1:
        return True
        
    #Target 1.5
    if  t.find("resilien")>-1:
        if  t.find("poverty")>-1    or \
            t.find("the poor")>-1:
            return True
            
    if  t.find("disaster")>-1:
        if  t.find("number of death")>-1 or \
            t.find("economic loss")>-1:
            return True
            
        elif t.find("risk reduction")>-1 and t.find("strateg")>-1:
            return True
            
    #Target 1.a
    if  t.find("poverty")>-1:
        if  t.find("develop")>-1:
            if  t.find("cooperat")>-1   or \
                t.find("assistan")>-1:
                return True
                
            elif t.find("program")>-1   or \
                t.find("polic")>-1:
                return True
                
    if  t.find("government")>-1:  
        if  t.find("spending")>-1:
            if  t.find("education")>-1  or \
                t.find("health")>-1     or \
                t.find("social protection")>-1:
                return True
                
    if  t.find("government")>-1 and t.find("expenditure")>-1:
        if  t.find("education")>-1  or \
            t.find("health")>-1     or \
            t.find("social protection")>-1:
                return True
                
    #Target 1.b
    if  t.find("investment")>-1 and t.find("poverty")>-1:
        return True
        
    if  t.find("government")>-1 and t.find("spending")>-1:
        if  t.find("women")>-1 or \
            t.find("poor and vulnerable")>-1:
            return True
            
    if  t.find("government")>-1 and t.find("expenditure")>-1:
        if  t.find("women")>-1 or \
            t.find("poor and vulnerable")>-1:
            return True
            
    return False
    
def in_sdg2(t):
    #Target 2.1
    if  t.find("hunger")>-1     or \
        t.find("famine")>-1:
        if  t.find("end")>-1        or \
            t.find("ending")>-1     or \
            t.find("eradicat")>-1   or \
            t.find("reduc")>-1      or \
            t.find("alleviat"):
            return True
            
    if  t.find("access")>-1:
        if  t.find("food")>-1 or \
            t.find("nutrition")>-1:
            if  t.find("poor")>-1   or \
                t.find("child")>-1  or \
                t.find("infant")>-1:
                return True
                
    if  t.find("prevalen")>-1   or \
        t.find("hunger")>-1     or \
        t.find("famine")>-1:
        if  t.find("food security")>-1      or \
            t.find("food insecurity")>-1    or \
            t.find("food deprivation")>-1   or \
            t.find("malnutrition")>-1       or \
            t.find("undernutrition")>-1     or \
            t.find("malnourish")>-1         or \
            t.find("undernourish")>-1:
            return True
            
    #Target 2.2
    if  t.find("child")>-1      or \
        t.find("infant")>-1     or \
        t.find("neonate")>-1    or \
        t.find("newborn")>-1    or \
        t.find("baby")>-1       or \
        t.find("babies")>-1:
        if  t.find("hunger")>-1             or \
            t.find("stunting")>-1           or \
            t.find("wasting")>-1            or \
            t.find("nutritional status")>-1 or \
            t.find("malnutrition")>-1       or \
            t.find("undernutrition")>-1     or \
            t.find("malnourish")>-1         or \
            t.find("undernourish")>-1:
            return True
            
    if  t.find("adolescent girl")>-1    or \
        t.find("pregnant women")>-1     or \
        t.find("lactating women")>-1:
        if  t.find("nutrition")>-1:
            if  t.find("need")>-1:
                return True
                
    #Target 2.3
    if  t.find("agriculture")>-1    or \
        t.find("food")>-1:
        if  t.find("producti")>-1:
            if  t.find("scale")>-1      or \
                t.find("smallscale")>-1:
                return True
                
    if  t.find("agriculture")>-1    or \
        t.find("food")>-1:
        if  t.find("sustainab")>-1:
            if  t.find("intensificat")>-1:
                return True
                
    #Target 2.4
    if  t.find("agriculture")>-1:
        if  t.find("sustainab")>-1  or \
            t.find("resilien")>-1:
            return True
            
    if  t.find("food production")>-1:
        if  t.find("sustainab")>-1  or \
            t.find("resilien")>-1:
            return True
    
    if  t.find("future")>-1 and t.find("high")>-1:  
        if  t.find("food demand")>-1:
            return True
            
    #Target 2.5
    if  t.find("genetic diversity")>-1  or \
        t.find("biodiversity")>-1:
        if  t.find("maintain")>-1       or \
            t.find("conserve")>-1:
            if  t.find("seed")>-1                   or \
                t.find("cultivated plant")>-1       or \
                t.find("farmed animal")>-1          or \
                t.find("domesticated animal")>-1:
                return True
                
    #Target 2.a
    if  t.find("agriculture")>-1:
        if  t.find("investment")>-1 or \
            t.find("investing")>-1:
            if  t.find("developing countr")>-1:
                return True
                
    #Target 2.b
    if  t.find("agriculture")>-1:
        if  t.find("world")>-1:
            if  t.find("market")>-1:
                return True
                
    if  t.find("agriculture")>-1:
        if  t.find("trade")>-1  or \
            t.find("import")>-1 or \
            t.find("export")>-1:
            if  t.find("restriction")>-1    or \
                t.find("distort")>-1        or \
                t.find("subsid")>-1:
                return True
                
    if  t.find("agriculture")>1 and t.find("doha development round")>-1:
        return True
        
    if  t.find("producer support estimate")>-1:
        return True
        
    #Target 2.c
    if  t.find("food price")>-1:
        if  t.find("volatil")>-1:
            return True
            
    if  t.find("food")>-1:  
        if  t.find("commodit")>-1:
            if  t.find("market")>-1:
                return True
            
    return False
    
def in_sdg3(t):
    #Target 3.1
    if  t.find("reduce")>-1 or \
        t.find("end")>-1    or \
        t.find("ending")>-1 or \
        t.find("ratio")>-1:
        if  t.find("maternal")>-1:
            if  t.find("mortality")>-1  or \
                t.find("death")>-1:
                return True
    
    #Target 3.2
    if  t.find("reduce")>-1     or \
        t.find("end")>-1        or \
        t.find("ending")>-1     or \
        t.find("prevent")>-1    or \
        t.find("ratio")>-1:
        if  t.find("neonatal")>-1   or \
            t.find("under-five")>-1 or \
            (t.find("under")>-1 and t.find("5")>-1 and t.find("five"))  or \
            t.find("before fifth")>-1:
                if  t.find("mortality")>-1  or \
                    t.find("death"):
                    return True
                    
    #Target 3.3
    if  t.find("epidemic")>-1   or \
        t.find("pandemic")>-1   or \
        t.find("combat")>-1     or \
        t.find("fight")>-1:
        if  t.find("tuberculos")>-1             or \
            t.find("malaria")>-1                or \
            t.find("hepatit")>-1                or \
            t.find("hiv")>-1                    or \
            t.find("aids")>-1                   or \
            t.find("tropical disease")>-1       or \
            t.find("zika")>-1                   or \
            t.find("zikv")>-1                   or \
            t.find("ebola")>-1                  or \
            t.find("water-borne disease")>-1    or \
            t.find("communicable disease")>-1   or \
            t.find("neglected disease")>-1      or \
            t.find("dengue")>-1                 or \
            t.find("chagas")>-1                 or \
            t.find("trypanosom")>-1             or \
            t.find("covid19")>-1                or \
            t.find("covid-19")>-1               or \
            t.find("2019-ncov")>-1              or \
            t.find("sars-cov-2")>-1             or \
            t.find("sars-cov2")>-1              or \
            t.find("hcov-2019")>-1              or \
            t.find("ncovid-19")>-1              or \
            t.find("severe acute respiratory syndrome")>-1  or \
            t.find("severe acute respiratory syndrome corona virus 2")>-1   or \
            t.find("coronavirus")>-1            or \
            t.find("coronavirus")>-1:
            return True
            
    #Target 3.4
    if  t.find("cardiovascular disease")>-1     or \
        t.find("heart attack")>-1               or \
        t.find("stroke")>-1                     or \
        t.find("myocard infarct")>-1            or \
        t.find("cerebrovascular accident")>-1   or \
        t.find("cva")>-1                        or \
        t.find("cancer")>-1                     or \
        t.find("neoplasm")>-1                   or \
        t.find("tumor")>-1                      or \
        t.find("tumour")>-1                     or \
        t.find("carcinoma")>-1                  or \
        t.find("chronic obstructive pulmonary disease") or \
        t.find("copd")>-1                       or \
        t.find("coad")>-1                       or \
        t.find("lung emphysema")>-1             or \
        (t.find("bronchitis")>-1 and t.find("chornic")>-1)  or \
        t.find("asthma")>-1                     or \
        t.find("diabetes mellitus")>-1          or \
        t.find("diabetes insipidus")>-1:
        if  t.find("premature")>-1:
            if  t.find("mortality")>-1          or \
                t.find("death")>-1:
                return True
        elif t.find("mortality rate")>-1:
            return True
        elif t.find("suicid")>-1:
            return True
            
    #Target 3.5
    if  t.find("abuse")>-1          or \
        t.find("harmful use")>-1    or \
        t.find("addict")>-1:
        if  t.find("substance")>-1  or \
            t.find("drug")>-1       or \
            t.find("alcohol")>-1:
            if  t.find("prevention")>-1 or \
                t.find("treatment"):
                return True
        elif t.find("alcohol")>-1 and t.find("per capita")>-1:
            return True
                
    if  t.find("binge drinken")>-1:
        if  t.find("prevention")>-1 or \
            t.find("treatment")>-1:
            return True
            
    #Target 3.6
    if  (t.find("road")>-1 and t.find("traffic")>-1)    or \
        t.find("drunk driv")>-1:
        if  t.find("injur")>-1      or \
            t.find("death")>-1      or \
            t.find("accident")>-1   or \
            t.find("trauma")>-1:
            return True
            
    #Target 3.7
    if  t.find("access")>-1 or \
        (t.find("national")>-1 and (t.find("strategy")>-1 or t.find("program"))):
        if  t.find("sexual health care")>-1         or \
            t.find("sexual healthcare")>-1          or \
            t.find("reproductive health care")>-1   or \
            t.find("reproductive healthcare")>-1:
            return True
            
    if  t.find("family planning")>-1        or \
        t.find("unintended pregnanc")>-1    or \
        t.find("unwanted pregnanc")>-1      or \
        t.find("unintended motherhood")>-1:
        return True
        
    if  t.find("adolescent")>-1 or \
        t.find("teen")>-1:
        if  t.find("birt rate")>-1  or \
            t.find("pregnan")>-1    or \
            t.find("mother")>-1:
            return True
            
    #Target 3.8
    if  t.find("universal health coverage")>-1  or \
        t.find("essential")>-1:
        if  t.find("healthcare")>-1     or \
            t.find("health care")>-1    or \
            t.find("medicine")>-1       or \
            t.find("vaccine")>-1:
            return True
            
    if t.find("household expenditure")>-1 and t.find("health")>-1:
        return True
        
    #Target 3.9
    if  t.find("mortality")>-1  or \
        t.find("death")>-1      or \
        t.find("illness")>-1:
        if  t.find("poison")>-1     or \
            t.find("contaminat")>-1 or \
            t.find("pollut")>-1:
            if  t.find("air")>-1    or \
                t.find("water")>-1  or \
                t.find("soil")>-1   or \
                t.find("hazardous chemical")>-1:
                return True
        elif t.find("unsafe")>-1    or \
            t.find("inadequate")>-1:
            if  t.find("water")>-1  or \
                t.find("sanitation")>-1:
                return True
        elif t.find("uninten")>-1 and t.find("poison")>-1:
            return True
            
    #Target 3.a
    if  (t.find("tobacco")>-1 and t.find("control")>-1) or \
        (t.find("health")>-1 and t.find("smoking")>-1)  or \
        (t.find("smoking")>-1 and (t.find("cessation")>-1 or t.find("quit")>-1)\
        and (t.find("health")>-1 or t.find("benefit")>-1)):
        return True
        
    if  t.find("tobacco")>-1    or \
        t.find("smoking")>-1:
        if  t.find("age")>-1:
            if  t.find("prevalen")>-1   or \
                t.find("number")>-1:
                return True
                
    #Target 3.b
    if  t.find("research and development")>-1  or \
        t.find("r-d")>-1:
        if  t.find("medicine")>-1   or \
            t.find("vaccin")>-1:
            return True
            
    if  t.find("access")>-1:
        if  t.find("essential")>-1:
            if  t.find("medicine")>-1   or \
                t.find("vaccin")>-1:
                return True
                
    if  t.find("develop")>-1 and t.find("assist")>-1:
        if  t.find("medical research")>-1   or \
            t.find("health sector"):
            return True
            
    #Target 3.c
    if  t.find("developing countr")>-1:
        if  t.find("health")>-1:
            if  t.find("financing")>-1      or \
                t.find("recruit")>-1        or \
                t.find("development")>-1    or \
                t.find("training")>-1:
                return True
                
    if  t.find("health worker")>-1:
        if  t.find("density")>-1    or \
            t.find("distribution")>-1:
            if  t.find("developing countr")>-1: 
                return True
            
    #Target 3.d
    if  t.find("health")>-1:
        if  (t.find("early")>-1 and t.find("warning")>-1)   or \
            (t.find("risk")>-1 and t.find("reduction")>-1)  or \
            (t.find("risk")>-1 and t.find("management")>-1):
            return True
            
    if  t.find("international health regulations")>-1   or \
        t.find("health emergenc")>-1:
        if  t.find("prepar")>-1:
            return True
            
    return False    

def in_sdg4(t):
    #Target 4.1
    if  t.find("quality education")>-1:
        if  t.find("inclusi")>-1    or \
            t.find("equit")>1:
            return True
            
    if  t.find("quality")>-1    or \
        t.find("equitabl")>-1   or \
        t.find("free")>-1       or \
        t.find("affordab")>-1   or \
        t.find("acces")>-1:
        if  t.find("primary education")>-1      or \
            t.find("primary school")>-1         or \
            t.find("secondary education")>-1    or \
            t.find("secondary school")>-1:
            return True
            
    if  t.find("proficiency level")>-1:
        if  t.find("reading")>-1    or \
            t.find("mathematics")>-1:
            return True
            
    #Target 4.2
    if  t.find("quality")>-1    or \
        t.find("equitabl")>-1   or \
        t.find("free")>-1       or \
        t.find("affordab")>-1   or \
        t.find("acces")>-1:
        if  t.find("preschool")>-1              or \
            t.find("pre-school")>-1             or \
            t.find("pre-primary education")>-1  or \
            t.find("pre-primary school")>-1     or \
            t.find("preprimary school")>-1      or \
            t.find("preprimary education")>-1:
            return True
            
    #Target 4.3
    if  t.find("equal")>-1  or \
        t.find("equit")>-1:
        if  t.find("access")>-1:
            if  t.find("tertiary education")>-1 or \
                t.find("university")>-1         or \
                t.find("vocational education"):
                return True
                
    #Target 4.4
    if  t.find("employ")>-1 or \
        t.find("decent")>-1 or \
        t.find("entrepreneur")>-1 or \
        t.find("job")>-1:
        if  t.find("increas")>-1:
            if  t.find("skills")>-1 or \
                t.find("competenc")>-1:
                return True
                
    #Target 4.5
    if  t.find("educat")>-1:
        if  t.find("gender disparit")>-1    or \
            t.find("gender parit")>-1       or \
            t.find("gender inequalit")>-1   or \
            t.find("gender equalit")>-1     or \
            t.find("vulnerable")            or \
            t.find("disabilit")             or \
            t.find("disabled")              or \
            t.find("indigen"):
            return True
            
    if  t.find("equal")>-1:
        if  t.find("educat")>1:
            if  t.find("girl")>-1   or \
                t.find("women")>-1:
                return True
                
    #Target 4.6
    if  t.find("literacy")>-1   or \
        t.find("numeracy")>-1   or \
        t.find("reading skill")>-1   or \
        t.find("writing skill")>-1:
        return True
        
    #Target 4.7
    if  t.find("sustainable development")>-1:
        if  t.find("educat")>-1     or \
            t.find("teach")>-1      or \
            t.find("learn")>-1:
            return True
            
    if  t.find("sustainab")>-1  or \
        t.find("global citizenship")>-1:
        if  t.find("education")>-1:
            if  t.find("program")>-1    or \
                t.find("curricul")>-1   or \
                t.find("policy")>-1     or \
                t.find("policies")>-1:
                return True
                
    #Target 4.a
    if  t.find("school facilit")>-1:
        return True
    
    if  t.find("school")>-1:
        if  t.find("access")>-1:
            if  t.find("electricity")>-1    or \
                t.find("internet")>-1       or \
                t.find("computer")>-1:
                return True
                
    if  t.find("school")>-1:
        if  t.find("drinking water")>-1 or \
            t.find("sanitation")>-1     or \
            t.find("handwashing")>-1    or \
            t.find("hand washing")>-1:
            return True
            
    #Target 4.b
    if  t.find("scholarships")>-1:
        if  (t.find("develop")>-1 and t.find("countr)>-1")) or \
            t.find("least developed countr")>-1             or \
            t.find("small island")>-1:
            return True
        elif t.find("south africa")>-1      or \
            t.find("sub-saharan africa")>-1 or \
            t.find("equatorial africa")>-1  or \
            t.find("west africa")>-1:
            return True
            
    #Target 4.c
    if  t.find("teacher")>-1:
        if  t.find("training")>-1   or \
            t.find("qualified")>-1  or \
            t.find("education")>-1:
            if  (t.find("develop")>-1 and t.find("countr)>-1")) or \
                t.find("least developed countr")>-1             or \
                t.find("small island")>-1:
                return True
                
    return False

def in_sdg5(t):
   #Target 5.1
    if  t.find("discrimination")>-1:
        if  t.find("sexual")>-1 or \
            t.find("gender")>-1 or \
            t.find("women")>-1  or \
            t.find("female")>-1 or \
            t.find("girl")>-1:
            return True
            
    if  t.find("law")>-1         or \
        t.find("legislation")>-1 or \
        t.find("legal")>-1:
        if  t.find("equality")>-1:
            if  t.find("sexual")>-1 or \
                t.find("gender")>-1 or \
                t.find("women")>-1  or \
                t.find("female")>-1 or \
                t.find("girl")>-1:
                return True
                
    #Target 5.2
    if  t.find("violence")>-1:
        if  t.find("sexual")>-1         or \
            t.find("physical")>-1       or \
            t.find("phsychological")>-1:
            if  t.find("gender")>-1 or \
                t.find("women")>-1  or \
                t.find("female")>-1 or \
                t.find("girl")>-1:
                return True
                
    if  t.find("human trafficking")>-1:
        return True
        
    #Target 5.3
    if  t.find("genital mutilation")>-1 or \
        t.find("genital cutting")>-1:
        if  t.find("gender")>-1 or \
            t.find("women")>-1  or \
            t.find("female")>-1 or \
            t.find("girl")>-1:
            return True
                
    if  t.find("female circumcision")>-1 or \
        t.find("child marriage")>-1:
        return True
        
    if  t.find("forced marriage")>-1 or \
        t.find("early marriage")>-1:
        if  t.find("women")>-1  or \
            t.find("female")>-1 or \
            t.find("girl")>-1:
            return True
            
    #Target 5.4
    if  t.find("women")>-1  or \
        t.find("female")>-1 or \
        t.find("girl")>-1   or \
        t.find("gender")>-1:
        if  t.find("domestic work")>-1  or \
            t.find("household")>-1 or \
            t.find("household work")>-1 or \
            t.find("unpaid care")>-1 or \
            t.find("unpaid work")>-1 or \
            t.find("shared responsibility")>-1:
            return True
    
    #Target 5.5
    if  t.find("women")>-1  or \
        t.find("female")>-1 or \
        t.find("girl")>-1   or \
        t.find("gender")>-1:
        if  t.find("participati")>-1  or \
            t.find("opportuni")>-1:
            if  t.find("leadership")>-1:
                return True
        if  t.find("seat")>-1       or \
            t.find("numbert")>-1:
            if  t.find("parliament")>-1 or \
                t.find("government")>-1:
                return True
            elif t.find("manager")>-1:
                return True
        if  t.find("glass ceiling")>-1:
            return True
            
    #Target 5.6
    if  t.find("reproductive rights")>-1:
        return True
        
    if  t.find("access")>-1:
        if  t.find("sexual health care")>-1 or \
            t.find("sexual healthcare")>-1  or \
            t.find("reproductive healthcare")>-1   or \
            t.find("reproductive health care")>-1   or \
            t.find("sexual information")>-1 or \
            t.find("sexual education")>-1   or \
            t.find("reproductive information")>-1   or \
            t.find("reproductive education")>-1:
            return True
            
    if  t.find("own")>-1    or \
        t.find("informed")>-1:
        if  t.find("decision")>-1:
            if  t.find("contracepti")>-1    or \
                t.find("reproducti")>-1     or \
                t.find("family planning")>-1    or \
                t.find("parenting plan")>-1 or \
                t.find("abortion")>-1:
                return True
                
    #Target 5.a
    if  t.find("women's property rights")>-1:
        return True
        
    if  t.find("gender")>-1 or \
        t.find("women")>-1  or \
        t.find("female")>-1 or  \
        t.find("girl")>-1:     
        if  t.find("property")>-1   or \
            t.find("ownership")>-1  or \
            t.find("right")>-1      or \
            t.find("control")>-1:
            if  t.find("land")>-1   or  \
                t.find("natural resource")>-1   or \
                t.find("economic resource")>-1:
                return True
                
        elif t.find("landowner")>-1 or \
            t.find("land owner")>-1:
                return True
                
    #Target 5.b
    if  t.find("technolog")>-1:
        if  t.find("empower")>-1:
            if  t.find("women")>-1  or \
                t.find("female")>-1 or \
                t.find("girl")>-1:
                return True
                
    #Target 5.c
    if  t.find("empower")>-1    or \
        t.find("discrimination")    or \
        t.find("equalit")>-1    or \
        t.find("inequalit")>-1  or \
        t.find("disparity")>-1  or \
        t.find("indisparity")>-1   or \
        t.find("diversity")>-1:
        if  t.find("gender")>-1 or \
            t.find("women")>-1  or \
            t.find("female")>-1 or \
            t.find("girl")>-1:
            if  t.find("policy")>-1 or \
                t.find("policies")>-1   or \
                t.find("legislation")>-1    or \
                t.find("law")>-1:
                return True
                
    if  t.find("women's rights")>-1 or \
        t.find("governance and gender")>-1  or \
        t.find("thirds wave feminism")>-1   or \
        t.find("sexism")>-1:
        if  t.find("policy")>-1 or \
            t.find("policies")>-1   or \
            t.find("legislation")>-1    or \
            t.find("law")>-1:
            return True
            
    return False

def in_sdg6(t):
    #Target 6.1
    if  t.find("drinking")>-1:
        if  t.find("water")>-1:
            if  t.find("access")>-1 or \
                t.find("afford")>-1 or \
                t.find("safe")>-1   or \
                t.find("secur")>-1:
                return True
                
    #Target 6.2
    if  t.find("sanitation")>-1 or \
        t.find("toilet")>-1:
        if  t.find("access")>-1:
            return True
    
    if  t.find("sanitation management")>-1  or \
        t.find("managed sanitation")>-1:
        return True
        
    if  t.find("end")>-1:
        if  t.find("open defecation")>-1    or \
            t.find("open defaecation")>-1:
            return True
            
    if  t.find("hand washing")>-1   or \
        t.find("handwashing")>-1:
        if  t.find("facilit")>-1:
            return True
            
    if  t.find("sewerage")>-1:
        if  t.find("develop")>-1 and t.find("countr")>-1:
            return True
            
    #Target 6.3
    if  t.find("reduc")>-1:
        if  t.find("water")>-1:
            if  t.find("pollution")>-1  or \
                t.find("contamination")>-1:
                return True
                
    if  t.find("increase")>-1:
        if  t.find("water")>-1:
            if  t.find("safe reus")>-1  or \
                t.find("recycl")>1:
                return True
                
    if  t.find("wastewater")>-1     or \
        t.find("waste water")>-1    or \
        t.find("sewage")>-1:
        if  t.find("manage")>-1 or \
            t.find("treat")>-1  or \
            t.find("untreat")>-1:
            return True
            
    if  t.find("good")>-1   or \
        t.find("poor")>-1   or \
        t.find("improve")>-1:
        if  t.find("water quality")>-1:
            return True
            
    #Target 6.4
    if  t.find("efficient")>-1:
        if  t.find("water")>-1  or \
            t.find("freshwater")>-1:
            if  t.find("use")>-1    or \
                t.find("supply")>-1 or \
                t.find("availab")>-1:
                return True
                
    if  t.find("water scarc")>-1    or \
        t.find("water short")>-1:
        return True
        
    #Target 6.5
    if  t.find("water")>-1:
        if  t.find("cooperation")>-1    or \
            (t.find("resource")>-1 and t.find("manage")>-1):
            return True
            
    if  t.find("address")>-1    or \
        t.find("coping")>-1     or \
        t.find("polic")>-1:
        if  t.find("water scarc")>-1    or \
            t.find("water short")>-1:
            return True
            
    #Target 6.6
    if  t.find("water")>-1:
        if  t.find("ecosystem")>-1:
            return True
            
    #Target 6.a
    if  t.find("water")>-1  or \
        t.find("sanitation")>-1:
        if  t.find("development")>-1:
            if  t.find("assist")>-1     or \
                t.find("support")>-1    or \
                t.find("program"):
                return True
                
    #Target 6.b
    if  t.find("water")>-1  or \
        t.find("sanitation")>-1:
        if  t.find("local")>-1:
            if  t.find("communit")>-1   or \
                t.find("administrat")>-1:
                return True
            
    return False 
    
def in_sdg7(t):
    #Target 7.1
    if  t.find("access")>-1:
        if  t.find("affordable")>-1 or \
            t.find("reliable")>-1   or \
            t.find("modern")>-1:
            if  t.find("energy")>-1 or \
                t.find("electricity")>-1:
                return True
                
    #Target 7.2
    if  t.find("share")>-1      or \
        t.find("increas")>-1    or \
        t.find("promot")>-1:
        if  t.find("renewable")>-1      or \
            t.find("alternative")>-1    or \
            t.find("clean")>-1:
            if  t.find("energy")>-1 or \
                t.find("fuel")>-1:
                return True
        elif t.find("energy")>-1:
            if  t.find("conversion")>-1 or \
                t.find("transition")>-1:
                return True
        elif t.find("biofuel")>-1   or \
            t.find("biogas")>-1     or \
            t.find("heat pump")>-1  or \
            t.find("hybrid power")>-1   or \
            t.find("solar enery")>-1    or \
            t.find("solar power")>-1    or \
            t.find("wind energy")>-1    or \
            t.find("wind farm")>-1      or \
            t.find("wind power")>-1     or \
            t.find("wind turbine")>-1:
            return True
            
    #Target 7.3
    if  t.find("improv")>-1:
        if  t.find("energy")>-1:
            if  t.find("efficiency")>-1:
                return True
                
    if  t.find("reduc")>-1:
        if  t.find("energy consumption")>-1:
            return True
            
    if  t.find("energy intensity")>-1   or \
        t.find("energy consumption")>-1:
        if  t.find("primary")>-1    or \
            t.find("gdp")>-1:
            return True
            
    #Target 7.a
    if  t.find("energy")>-1:
        if  t.find("international")>-1:
            if  t.find("cooperation")>-1:
                return True
                
    #Target 7.b
    if  t.find("modern")>-1 or \
        t.find("sustainable")>-1:
        if  t.find("energy")>-1:
            if  t.find("least developed countr")>-1 or \
                t.find("small island")>-1   or \
                (t.find("develop")>-1 and t.find("countr")>-1):
                return True
                
    return False
    
def in_sdg8(t):
    #Target 8.1
    if  t.find("economic")>-1:
        if  t.find("growth")>-1:
            if  t.find("per capita")>-1 or \
                t.find("sustain")>-1:
                return True
            if  t.find("least developed countr")>-1 or \
                t.find("small island")>-1   or \
                (t.find("develop")>-1 and t.find("countr")>-1):
                return True
                
    if  t.find("growth")>-1:
        if  t.find("gross domestic product")>-1 or \
            t.find("gdp")>-1:
            return True
            
    #Target 8.2
    if  t.find("economic productivity")>-1:
        return True
        
    if  t.find("economic")>-1:
        if  t.find("productivity")>-1:
            if  t.find("diversif")>-1   or \
                t.find("upgrad")>-1     or \
                t.find("innovat")>-1:
                return True
                
    #Target 8.3
    if  t.find("decent job")>-1     or \
        t.find("decent work")>-1    or \
        t.find("job creat")>-1      or \
        t.find("quality job")>-1:
        return True
        
    if  t.find("develop")>-1:
        if  (t.find("producer")>-1 and t.find("activit")>-1)    or \
            t.find("labor produc")>-1   or \
            t.find("entrepreneurship")>-1:
            return True
            
    if  t.find("informal")>-1:
        if  t.find("employment")>-1:
            return True
            
    #Target 8.4
    if  t.find("resource efficiency")>-1:
        return True
    
    if  t.find("material")>-1:
        if  t.find("footprint")>-1:
            return True
            
    if  t.find("domestic")>-1:
        if  t.find("material")>-1:
            if  t.find("consumption")>-1:
                return True
                
    #Target 8.5
    if  t.find("full employment")>-1    or \
        t.find("equal pay")>-1:
        if  t.find("work")>-1:
            return True
            
    if  t.find("hourly earning")>-1:
        return True
        
    if  t.find("equal")>-1  or \
        t.find("inequal")>-1:
        if  t.find("pay")>-1:
            if  t.find("work")>-1:
                return True
                
    if  t.find("wage")>-1:
        if  t.find("gap")>-1    or \
            t.find("differen")>-1:
            return True
            
    if  t.find("unemployment rate")>-1:
        if  t.find("sex")>-1    or \
            t.find("gender")>-1 or \
            t.find("age")>-1    or \
            t.find("disability")>-1:
            return True
            
    #Target 8.6
    if  t.find("youth")>-1  or \
        t.find("young people")>-1:
        if  t.find("employ")>-1 or \
            t.find("unemploy"):
            return True
            
    #Target 8.7
    if  (t.find("force")>-1 and t.find("labo")>-1)  or \
        t.find("modern slavery")>-1 or \
        (t.find("human")>-1 and t.find("traffick")>-1)   or \
        (t.find("child")>-1 and t.find("labo")>-1)  or \
        (t.find("child")>-1 and t.find("slavery")>-1)  or \
        (t.find("child")>-1 and t.find("traffick")>-1)  or \
        (t.find("child")>-1 and t.find("work")>-1):
        return True
        
    #Target 8.8
    if  t.find("labour right")>-1   or \
        t.find("labor right")>-1:
        return True
        
    if  t.find("safe")>-1   or \
        t.find("secure")>-1:
        if  t.find("work")>-1 and t.find("environment")>-1:
            return True
            
    if  t.find("occupational injur")>-1:
        if  t.find("rate")>-1   or \
            t.find("frequency")>-1:
            return True
            
    if  t.find("international label organization")>-1:
        return True
        
    #Target 8.9
    if  t.find("sustaina")>-1:
        if  t.find("toursim")>-1:
            return True
            
    if  t.find("gdp")>-1    or \
        t.find("gross domestic product")>-1:
        if  t.find("tourism")>-1:
            return True
            
    if  t.find("job")>-1:
        if  t.find("tourism")>-1:
            return True
            
    #Target 8.10
    if  t.find("micro-financ")>-1   or \
        t.find("microfinanc")>-1:
        return True
        
    if  t.find("access")>-1:
        if  t.find("financial service")>-1  or \
            t.find("banking")>-1            or \
            t.find("insurance")>-1:
            return True
            
    #Target 8.a
    if  t.find("least developed countr")>-1 or \
        t.find("small island")>-1   or \
        (t.find("develop")>-1 and t.find("countr")>-1):
        if  t.find("trad")>-1:
            if  t.find("support")>-1    or \
                t.find("assist")>-1     or \
                t.find("aid")>-1:
                return True
                
    if  t.find("aid for trade")>-1:
        return True
        
    #Target 8.b
    if  t.find("global jobs pact")>-1:
        return True
        
    if  t.find("strateg")>-1    or \
        t.find("polic")>-1:
        if  t.find("youth")>-1  or \
            t.find("young people")>-1:
            if  t.find("employ'")>-1    or \
                t.find("unemploy")>-1:
                return True
                
    if  t.find("gdp")>-1    or \
        t.find("gross domestic product")>-1:
        if  t.find("social protection")>-1  or \
            t.find("employment program")>-1:
            return True     

    return False
    
def in_sdg9(t):
    #Target 9.1
    if  t.find("quality")>-1    or \
        t.find("reliab")>-1     or \
        t.find("sustainab")>-1  or \
        t.find("resilient")>-1:
        return True
        
    if  t.find("economic development")>-1   or \
        t.find("human wellbeing")>-1:
        if  t.find("afford")>-1 or \
            t.find("equitable")>-1:
            return True
            
    if  t.find("rural")>-1:
        if  t.find("population")>-1:
            if  t.find("road")>-1:
                return True
                
    if  t.find("passenger")>-1  or \
        t.find("freight")>-1:
        if  t.find("transport")>-1:
            if  t.find("volume")>-1:
                return True
                
    #Target 9.2
    if  t.find("inclusi")>-1    or \
        t.find("sustainab")>-1:
        if  t.find("industr")>-1:
            return True
            
    if  t.find("share")>-1:
        if  t.find("employment")>-1 or \
            t.find("gdp")>-1        or \
            t.find("gross domestic product")>-1:
            if  t.find("industr")>-1:
                return True
                
    if  t.find("manufacturing")>-1:
        if  t.find("value")>-1:
            if  t.find("employment")>-1 or \
                t.find("gdp")>-1        or \
                t.find("gross domestic product")>-1:
                return True
                
    if  t.find("manufacturing employment")>-1:
        return True
        
    #Target 9.3
    if  t.find("small scale industry")>-1   or \
        t.find("small enterprise")>-1       or \
        t.find("small entrepren")>-1        or \
        t.find("microenterprise")>-1        or \
        t.find("micro-enterprise")>-1:
        if  t.find("financ")>-1             or \
            t.find("credit")>-1             or \
            t.find("microcredit")>-1        or \
            t.find("micro-credit")>-1       or \
            t.find("micro-financ")>-1       or \
            t.find("microfinanc")>-1        or \
            t.find("loan")>-1:
            return True
        if  t.find("share")>-1              or \
            t.find("proportion")>-1:
            return True
            
    #Target 9.4
    if  t.find("upgrade")>-1    or \
        t.find("retrofit")>-1:
        if  t.find("infrastructure")>-1 or \
            t.find("industr")>-1:
            if  t.find("sustainab")>-1:
                return True
                
    if  t.find("increas")>-1:
        if  t.find("resource")>-1:
            if  t.find("efficien")>-1:
                return True
                
    if  t.find("clean")>-1  or \
        t.find("environmentally sound")>-1:
        if  t.find("technolog")>-1  or \
            t.find("industr")>-1:
            return True
          
    if  t.find("co2 emmision")>-1:
        if  t.find("per unit")>-1:
            return True
            
    #Target 9.5
    if  t.find("enhance")>-1    or \
        t.find("upgrad")>-1     or \
        t.find("encourag")>-1:
        if  t.find("research")>-1   or \
            t.find("r-d")>-1        or \
            t.find("research and development")>-1   or \
            t.find("innovation")>-1 or \
            (t.find("technol")>-1 and t.find("capabilit")>-1):
            if  (t.find("develop")>-1 and t.find("countr")>-1)  or \
                t.find("least developed countr")>-1:
                return True
                
    if  t.find("enhance")>-1    or \
        t.find("encourag")>-1:
        if  t.find("innovation")>-1:
            return True
            
    if  t.find("research and development")>-1   or \
        t.find("r-d")>-1:
        if  t.find("spending")>-1       or \
            t.find("expenditure")>-1    or \
            t.find("gdp")>-1            or \
            t.find("gross domestic product")>-1:
            return True
            
    if  t.find("researcher")>-1:
        if  t.find("per million inhabitant")>-1:
            return True
            
    #Target 9.a
    if  t.find("sustainab")>-1  or \
        t.find("resilien")>-1:
        if  t.find("infrastructure")>-1:
            if  t.find("develop")>-1:
                if  (t.find("develop")>-1 and t.find("countr")>-1)  or \
                    t.find("least developed countr")>-1 or \
                    t.find("small island")>-1   or \
                    t.find("africa")>-1:
                    return True
                    
    #Target 9.b
    if  t.find("support")>-1    or \
        t.find("assist")>-1     or \
        t.find("aid")>-1:
        if  t.find("research")>-1   or \
            t.find("r-d")>-1        or \
            t.find("research and development")>-1   or \
            t.find("innovation")>-1 or \
            (t.find("technol")>-1 and t.find("capabilit")>-1):
            if  (t.find("develop")>-1 and t.find("countr")>-1):
                return True
                
    if  t.find("technology transfer")>-1:
        if (t.find("develop")>-1 and t.find("countr")>-1)   or \
            t.find("least developed countr")>-1:
            return True
            
    if  t.find("medium-tech")>-1    or \
        t.find("high-tech")>-1:
        if  t.find("industr")>-1:
            if  t.find("value")>-1:
                return True
                
    #Target 9.c
    if  t.find("access")>-1:
        if  t.find("ict")>-1    or \
            t.find("information")>-1    or \
            t.find("communication")>-1  or \
            t.find("internet")>-1       or \
            t.find("mobile")>-1         or \
            t.find("wireless")>-1:
            if (t.find("develop")>-1 and t.find("countr")>-1)   or \
                t.find("small island")>-1   or \
                t.find("least developed countr")>-1:
                return True
                
    if  t.find("proportion")>-1:
        if  t.find("population")>-1:
            if  t.find("mobile")>-1:
                if  t.find("network")>-1    or \
                    t.find("technolog")>-1:
                    return True
    
    return False
    
def in_sdg10(t):
    #Target 10.1
    if  t.find("income")>-1:
        if  t.find("growth")>-1:
            if  t.find("poorest")>-1        or \
                t.find("disadvantaged")>-1  or \
                t.find("marginali")>-1:
                return True
                
    if  t.find("income")>-1:
        if  t.find("equal")>-1      or \
            t.find("inequal")>-1    or \
            t.find("distribution")>-1:
            if  t.find("poorest")>-1        or \
                t.find("disadvantaged")>-1  or \
                t.find("marginali")>-1:
                return True
                
    if  t.find("growth rate")>-1:
        if  t.find("income")>-1     or \
            t.find("per capita")>-1 or \
            t.find("household expenditure")>-1:
            return True
            
    #Target 10.2
    if  t.find("social")>-1 or \
        t.find("socioeconomic")>-1  or \
        t.find("economic")>-1       or \
        t.find("politic")>-1:
        if  t.find("inclusion")>-1  or \
            t.find("exclusion")>-1:
            return True
            
    #Taret 10.3
    if  t.find("legislati")>-1  or \
        t.find("law")>-1        or \
        t.find("polic")>-1      or \
        t.find("action")>-1     or \
        t.find("practice")>-1:
        if  t.find("reduc")>-1:
            if  t.find("equality")>-1   or \
                t.find("inequalit")>-1:            
                return True
        if  t.find("distriminat")>-1:
            return True
        if  t.find("opportun")>-1:
            if  t.find("equal")>-1:
                return True
                
    #Target 10.4
    if  t.find("legislati")>-1  or \
        t.find("law")>-1        or \
        t.find("polic")>-1      or \
        t.find("action")>-1     or \
        t.find("practice")>-1:
        if  t.find("fiscal")>-1 or \
            t.find("wage")>-1   or \
            t.find("social protection")>-1:
            if  t.find("equality")>-1:
                return True
                
    if  t.find("labour")>-1 or \
        t.find("labor")>-1  or \
        t.find("wage")>-1   or \
        t.find("social protection")>-1:
        if  t.find("gdp")>-1    or \
            t.find("gross domestic product")>-1:
            return True
            
    #Target 10.5
    if  t.find("regulat")>-1    or \
        t.find("monitor")>-1:
        if  t.find("global")>-1:
            if  t.find("financial market")>-1   or \
                t.find("financial institution")>-1:
                return True
    
    if  t.find("financial soundness")>-1:
        if  t.find("indicator")>-1:
            return True
                
   #Target 10.6
    if  t.find("representation")>-1  or \
        t.find("voice")>-1  or \
        t.find("voting right")>-1:
        if  t.find("international")>-1:
            if  t.find("developing countr")>-1:
                return True
                
    #Target 10.7
    if  t.find("migration polic")>-1:
        return True
        
    #Target 10.a
    if  t.find("wto")>-1    or \
        t.find("world trade organization")>-1   or \
        t.find("world trade organisation")>-1:
        if (t.find("develop")>-1 and t.find("countr")>-1)   or \
            t.find("least developed countr")>-1 or \
            t.find("small island")>-1:
            return True
            
    if  t.find("import")>-1 or \
        t.find("trad")>-1:
        if  t.find("tarif")>-1:
            if (t.find("develop")>-1 and t.find("countr")>-1)   or \
                t.find("least developed countr")>-1 or \
                t.find("small island")>-1:
                return True
                
    #Target 10.b
    if  t.find("development")>-1:
        if  t.find("assist")>-1 or \
            t.find("support")>-1    or \
            t.find("program")>-1:
            if (t.find("develop")>-1 and t.find("countr")>-1)   or \
                t.find("least developed countr")>-1 or \
                t.find("small island")>-1:
                if  t.find("financial")>-1  or \
                    t.find("donor")>-1:
                    return True
                    
    #Target 10.c
    if  t.find("remittance")>-1:
        if  t.find("migrant")>-1    or \
            t.find("emigrant")>-1   or \
            t.find("immigrant")>-1:
            return True
            
    return False
    
def in_sdg11(t):
    #Target 11.1
    if  t.find("safe")>-1   or \
        t.find("affordab")>-1   or \
        t.find("adequat")>-1:
        if  t.find("housing")>-1:
            return True
            
    if  t.find("upgrade")>-1    or \
        t.find("improv")>-1:
        if  t.find("slum")>-1:
            return True
            
    if  t.find("population")>-1:
        if  t.find("living")>-1:
            if  t.find("slum")>-1:
                return True
                
    #Target 11.2
    if  t.find("sustainab")>-1:
        if  t.find("transport")>-1:
            return True
            
    if  t.find("access")>-1:
        if  t.find("safe")>-1   or \
            t.find("affordab")>-1   or \
            t.find("public")>-1 or \
            t.find("urban")>-1:
            if  t.find("transport")>-1:
                return True
                
    if  t.find("improv")>-1:
        if  t.find("road safety")>-1:
            return True
            
    #Target 11.3
    if  t.find("sustainab")>-1  or \
        t.find("inclusi")>-1:
        if  t.find("urbanisation")>-1   or \
            t.find("urbanization")>-1   or \
            t.find("settlement")>-1     or \
            t.find("city")>-1           or \
            t.find("cities")>-1:
            return True
            
    if  t.find("land")>-1:
        if  t.find("consumption")>-1:
            if  t.find("population")>-1:
                if  t.find("growth")>-1:
                    return True
                    
    if  t.find("urban")>-1      or \
        t.find("city")>-1:
        if  t.find("planning")>-1   or \
            t.find("management")>-1:
            if  t.find("participat")>-1:
                return True
                
    #Target 11.4
    if  t.find("conservat")>-1  or \
        t.find("preservat")>-1  or \
        t.find("protect")>-1    or \
        t.find("safeguard")>-1:
        if  t.find("heritage")>-1:
            return True
            
    #Target 11.5
    if  t.find("disaster")>-1:
        if  t.find("number")>-1:
            if  t.find("death")>-1  or \
                t.find("missing person")>-1 or \
                t.find("human loss")>-1:
                return True
                
        if  t.find("economic loss")>-1  or \
            t.find("gdp")>-1            or \
            t.find("gross domestic product")>-1 or \
            t.find("infrastructure")>-1 or \
            t.find("basic service")>-1:
            return True
            
    #Target 11.6
    if  t.find("city")>-1       or \
        t.find("cities")>-1     or \
        t.find("urban")>-1      or \
        t.find("municipalit")>-1:
        if  t.find("air quality")>-1    or \
            t.find("smog")>-1           or \
            t.find("waste management")>-1   or \
            t.find("solid waste")>-1    or \
            t.find("pm10")>-1           or \
            t.find("pm2.5")>-1:
            return True
            
    #Target 11.7
    if  t.find("safe")>-1   or \
        t.find("inclusive")>-1  or \
        t.find("access")>-1:
        if  t.find("green")>-1  or \
            t.find("public")>-1:
            if  t.find("space")>-1:
                return True
                
    if  t.find("city")>-1       or \
        t.find("cities")>-1     or \
        t.find("urban")>-1      or \
        t.find("municipalit")>-1:
        if  t.find("green")>-1  or \
            t.find("public")>-1:
            if  t.find("space")>-1:
                return True
        if  t.find("victim")>-1:
            if  t.find("physical")>-1   or \
                t.find("sexual")>-1:
                if  t.find("harass")>-1:
                    return True
                    
    #Target 11.a
    if  t.find("city")>-1       or \
        t.find("cities")>-1     or \
        t.find("urban")>-1      or \
        t.find("national")>-1      or \
        t.find("regional")>-1:
        if  t.find("development")>-1:
            if  t.find("plan")>-1:
                return True
                
    if  t.find("urban planning")>-1     or \
        t.find("city planning")>-1      or \
        t.find("urban design")>-1      or \
        t.find("urban development")>-1      or \
        t.find("urban growth")>-1      or \
        t.find("urban renewal")>-1      or \
        t.find("urbanization")>-1:
        return True
        
    #Target 11.b
    if  t.find("reduc")>-1:
        if  t.find("disaster")>-1:
            if  t.find("risk")>-1:
                return True
    
    if  t.find("sendai framework")>-1:
        return True
        
    #Target 11.c
    if  (t.find("develop")>-1 and t.find("countr")>-1)  or \
        t.find("least developed countr")>-1 or \
        t.find("small island")>-1:
        if  t.find("building")>-1:
            return True
            
    return False
    
def in_sdg12(t):
    #Target 12.1
    if  t.find("sustainab")>-1:
        if  t.find("consum")>-1 or \
            t.find("product")>-1:
            return True
            
    #Target 12.2
    if  t.find("sustainab")>-1:
        if  t.find("natural resource")>-1:
            return True
            
    if  t.find("sustainab")>-1  or \
        t.find("efficien")>-1:
        if  t.find("natural resource")>-1:
            return True
            
    if  t.find("material")>-1   or \
        t.find("carbon")>-1     or \
        t.find("water")>-1:
        if  t.find("footprint")>-1:
            return True
        
    if  t.find("material")>-1:
        if  t.find("consumption")>-1:
            if  t.find("domestic")>-1   or \
                t.find("household")>-1:
                return True
                
    #Target 12.3
    if  t.find("food")>-1:
        if  t.find("wast")>-1   or \
            t.find("loss")>-1   or \
            t.find("spoil")>-1:
            return True
            
    if  t.find("postharvest loss")>-1   or \
        t.find("post-harvest loss")>-1:
        return True
        
    #Target 12.4
    if  t.find("life cycle analysis")>-1    or \
        t.find("life cycle assesment")>-1:
        return True
        
    if  t.find("life cycle")>-1:
        if  t.find("hazardous")>-1  or \
            t.find("toxic")>-1:
            if  t.find("chemical")>-1   or \
                t.find("waste")>-1:
                return True
                
    if  t.find("per capita")>-1:
        if  t.find("hazardous")>-1  or \
            t.find("toxic")>-1:
            if  t.find("chemical")>-1   or \
                t.find("waste")>-1:
                return True
                
    #Target 12.5
    if  t.find("prevent")>-1    or \
        t.find("reduc")>-1:
        if  t.find("chemical")>-1   or \
            t.find("waste")>-1:
            if  t.find("recycl")>-1 or \
                t.find("reuse")>-1  or \
                t.find("reusing")>-1    or \
                t.find("air")>-1    or \
                t.find("water")>-1  or \
                t.find("soil")>-1:
                return True
                
    if  t.find("national")>-1:
        if  t.find("recycling rate")>-1:
            return True
            
    if  t.find("tons")>-1:
        if  t.find("material")>-1:
            if  t.find("recycle")>-1:
                return True
                
    #Target 12.6
    if  t.find("sustainab")>-1:
        if  t.find("practice")>-1   or \
            t.find("information")>-1    or \
            t.find("report")>-1:
            if  t.find("compan")>-1 or \
                t.find("firm")>-1   or \
                t.find("corporate")>-1  or \
                t.find("business")>-1:
                return True
                
    #Target 12.7
    if  t.find("sustainab")>-1:
        if  t.find("procurement")>-1    or \
            t.find("buying")>-1:
            if  t.find("policy")>-1 or \
                t.find("policies")>-1   or \
                t.find("priorit")>-1    or \
                t.find("action")>-1:
                return True
                
    #Target 12.8
    if  t.find("sustainab")>-1  or \
        t.find("global citizenship")>-1:
        if  t.find("information")>-1    or \
            t.find("awareness")>-1:
            return True
            
        if  t.find("education")>-1:
            if  t.find("program")>-1    or \
                t.find("curricul")>-1   or \
                t.find("policy")>-1     or \
                t.find("policies")>-1:
                return True
                
    #Target 12.a
    if  t.find("sustainab")>-1:
        if  t.find("consum")  >-1   or \
            t.find("product")>-1:
            if  (t.find("develop")>-1 and t.find("countr")>-1)  or \
                t.find("least developed countr")>-1 or \
                t.find("small island")>-1:
                return True
                
    #Target 12.b
    if  t.find("sustainab")>-1:
        if  t.find("tourism")>-1:
            return True
            
    #Target 12.c
    if  t.find("subsid")>-1 or \
        t.find("tax")>-1:
        if  t.find("fossil-fuel")>-1    or \
            t.find("coal")>-1           or \
            t.find("petrol")>-1:
            return True
            
    return False
    
def in_sdg13(t):
    #Target 13.0
    if  t.find("climate")>-1:
        if  t.find("anthropogenic")>-1      or \
            t.find("action")>-1             or \
            t.find("adapt")>-1              or \
            t.find("biodiversity")>-1       or \
            t.find("carbon")>-1             or \
            t.find("change")>-1             or \
            t.find("crisis")>-1             or \
            t.find("deforestati")>-1        or \
            t.find("desertificati")>-1      or \
            t.find("ecolo")>-1              or \
            t.find("environment")>-1        or \
            t.find("ghg")>-1                or \
            t.find("global change")>-1      or \
            t.find("greenhouse gas")>-1     or \
            t.find("hazard")>-1             or \
            t.find("reforestati")>-1        or \
            t.find("variabilit")>-1         or \
            t.find("warming")>-1            or \
            t.find("water stress")>-1:
            return True
        if  t.find("paris")>-1:
            if  t.find("agreement")>-1      or \
                t.find("cop21")>-1:
                return True
        if  t.find("kyoto")>-1:
            if  t.find("protocol")>-1:
                return True
                
    if  t.find("climate action")>-1         or \
        t.find("climate effect")>-1         or \
        t.find("climate model")>-1          or \
        t.find("climate variability")>-1          or \
        t.find("climate variation")>-1          or \
        t.find("climate-driven")>-1          or \
        t.find("climatology")>-1          or \
        t.find("eco-innovation")>-1          or \
        t.find("environmental change")>-1          or \
        t.find("environmental impact")>-1          or \
        t.find("global climate")>-1          or \
        t.find("global warming")>-1          or \
        t.find("green-house effect")>-1          or \
        t.find("greenhouse effect")>-1          or \
        t.find("greenhouse gas")>-1:
        return True
        
    if  t.find("sea level")>-1:
        if  t.find("chang")>-1  or \
            t.find("rising")>-1:
            return True
            
    #Target 13.1
    if  t.find("climat")>-1 or \
        t.find("natural disaster")>-1:
        if  t.find("resilien")>-1:
            return True
            
    if  t.find("reduc")>-1:
        if  t.find("disaster")>-1:
            if  t.find("risk")>-1:
                return True
                
    if  t.find("disaster")>-1:
        if  t.find("number")>-1:
            if  t.find("death")>-1  or \
                t.find("people")>-1:
                return True
                
        if  t.find("missing person")>-1 or \
            t.find("human loss")>-1:
            return True
            
    #Target 13.2
    if  t.find("climat")>-1:
        if  t.find("polic")>-1  or \
            t.find("strateg")>-1    or \
            t.find("plan")>-1       or \
            t.find("plans")>-1      or \
            t.find("planning")>-1:
            return True
            
    #Target 13.3
    if  t.find("climate")>-1:
        if  t.find("information")>-1    or \
            t.find("awareness")>-1      or \
            t.find("educat")>-1         or \
            t.find("teach")>-1          or \
            t.find("learn")>-1:
            return True
            
    #Target 13.a
    if  t.find("climate")>-1:
        if  t.find("fund")>-1   or \
            t.find("funds")>-1  or \
            t.find("funding")>-1    or \
            t.find("money")>-1  or \
            t.find("dollar")>-1 or \
            t.find("commitment")>-1 or \
            t.find("capitali")>-1:
            return True
            
    if  t.find("unfcc")>-1  or \
        t.find("united nations framework convention for climate change")>-1:
        return True       
            
    #Target 13.b
    if  t.find("climate")>-1:
        if  t.find("assist")>-1     or \
            t.find("support")>-1    or \
            t.find("aid")>-1        or \
            t.find("program")>-1    or \
            t.find("development")>-1    or \
            t.find("capacity")>-1:
            if  (t.find("develop")>-1 and t.find("countr")>-1)  or \
                t.find("least developed countr")>-1 or \
                t.find("small island")>-1:
                return True
                
    return False
    
def in_sdg14(t):
    #Target 14.1
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("pollut")>-1 or \
            t.find("debris")>-1  or \
            t.find("eutrophication")>-1 or \
            t.find("contamination")>-1  or \
            t.find("waste")>-1          or \
            t.find("plastic")>-1:
            return True
            
    #Target 14.2
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("ecosystem")>-1  or \
            t.find("biodivers")>-1  or \
            t.find("protection")>-1 or \
            t.find("environmental")>-1  or \
            t.find("degradation")>-1:
            return True
            
    #Target 14.3
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("acidi")>-1  or \
            t.find("ph ")>-1:
            return True
            
    #Target 14.4
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("overfish")>-1   or \
            t.find("fisheries")>-1  or \
            t.find("fishery")>-1    or \
            t.find("fish stock")>-1 or \
            t.find("fishing")>-1:
            return True
            
    #Targe 14.5
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("protected")>-1  or \
            t.find("conserv")>-1:
            if  t.find("area")>-1:
                return True
                
    #Target 14.6
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("fish stock")>-1:
            return True
            
    #Target 14.7
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("least developed countr")>-1 or \
            t.find("small island")>-1   or \
            (t.find("develop")>-1 and t.find("countr")>-1):
            return True
        if  t.find("sustainab")>-1:
            if  t.find("fish")>-1   or \
                t.find("aquaculture")>-1    or \
                t.find("tourism")>-1:
                return True
                
    #Target 14.a
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("research")>-1:
            if  t.find("develop")>-1    or \
                t.find("budget")>-1     or \
                t.find("spending")>-1:
                return True
                
        if  t.find("knowledge")>-1:
            if  t.find("develop")>-1    or \
                t.find("increase")>-1:
                return True
                
        if  t.find("transfer")>-1:
            if  t.find("technology")>-1:
                return True
                
    #Target 14.b
    if  t.find("small-scale")>-1:
        if  t.find("fish")>-1:
            return True
            
    #Target 14.c
    if  t.find("ocean")>-1  or \
        t.find("marine")>-1 or \
        t.find("coast")>-1  or \
        t.find("sea")>-1    or \
        t.find("coral reef")>-1:
        if  t.find("sustainab")>-1  or \
            t.find("preserv")>-1    or \
            t.find("conserv")>-1    or \
            t.find("protect")>-1:
            if  t.find("jurisdiction")>-1   or \
                t.find("legal")>-1          or \
                t.find("law")>-1:
                return True
                
    if  t.find("sustainab")>-1  or \
        t.find("preserv")>-1    or \
        t.find("conserv")>-1    or \
        t.find("protect")>-1:
        if  t.find("unclos")>-1 or \
            t.find("un convention on the law of the sea")>-1    or \
            t.find("united nations convention on the law of the sea")>-1:
            return True
            
    return False
    
def in_sdg15(t):
    #Target 15.1
    if  t.find("sustainab")>-1  or \
        t.find("conserv")>-1    or \
        t.find("restor")>-1:
        if  t.find("ecosyst")>-1    or \
            t.find("terrestrial")>-1    or \
            t.find("freshwater")>-1 or \
            t.find("inland")>-1     or \
            t.find("forest")>-1     or \
            t.find("environment")>-1    or \
            t.find("soil")>-1       or \
            t.find("land")>-1:
            if  (t.find("ocean")>-1  or \
                t.find("marine")>-1 or \
                t.find("coast")>-1  or \
                t.find("sea")>-1    or \
                t.find("reef")>-1)==False:
                return True
                
    #Target 15.2
    if  t.find("sustainab")>-1:
        if  t.find("management")>-1:
            if  t.find("forest")>-1:
                return True
                
    if  t.find("halt")>-1   or \
        t.find("combat")>-1 or \
        t.find("reduc")>-1:
        if  t.find("deforest")>-1:
            return True
           
    if  t.find("restor")>-1:
        if  t.find("degraded forest")>-1:
            return True
            
    if  t.find("increas")>-1:
        if  t.find("reforest")>-1   or \
            t.find("afforest")>-1:
            return True
            
    #Target 15.3
    if  t.find("halt")>-1   or \
        t.find("combat")>-1 or \
        t.find("reduc")>-1:
        if  t.find("desertification")>-1:
            return True
            
    if  t.find("restor")>-1:
        if  t.find("degraded land")>-1  or \
            t.find("degraded dryland")>-1 or \
            t.find("degraded soil")>-1:
            return True
            
    if  t.find("proportion")>-1     or \
        t.find("percentage")>-1:
        if  t.find("degraded")>-1:
            if  t.find("land")>-1   or \
                t.find("soil")>-1:
                return True
                
    #Target 15.4
    if  t.find("mountain")>-1   or \
        t.find("alpine")>-1:
        if  t.find("ecosystem")>-1  or \
            t.find("biodiversity")>-1:
            return True
            
    if  t.find("mountain green cover index")>-1:
        return True
        
    #Target 15.5
    if  t.find("halt")>-1   or \
        t.find("combat")>-1 or \
        t.find("reduc")>-1:
        if  t.find("degrad")>-1 or \
            t.find("loss")>-1   or \
            t.find("destruction")>-1    or \
            t.find("fragmentation")>-1:
            if  t.find("habitat")>-1    or \
                t.find("land")>-1       or \
                t.find("forest")>-1:
                    return True
                    
    if  t.find("halt")>-1   or \
        t.find("combat")>-1 or \
        t.find("reduc")>-1:
        if  t.find("loss")>-1:
            if  t.find("biodiversity")>-1:
                return True
                
    #Target 15.6
    if  t.find("gene")>-1:
        if  t.find("resource")>-1:
            if  t.find("sharing")>-1:
                return True
                
    #Target 15.7
    if  t.find("poaching")>-1   or \
        t.find("trafficking")>-1:
        if  t.find("species")>-1    or \
            t.find("flora")>-1      or \
            t.find("fauna")>-1      or \
            t.find("wildlife")>-1:
            if  (t.find("ocean")>-1  or \
                t.find("marine")>-1 or \
                t.find("coast")>-1  or \
                t.find("sea")>-1    or \
                t.find("reef")>-1)==False:
                return True
                
    #Target 15.8
    if  t.find("invas")>-1:
        if  t.find("alien")>-1  or \
            t.find("nonnative")>-1  or \
            t.find("non-native")>-1 or \
            t.find("nonindigenous")>-1  or \
            t.find("non-indigenous")>-1:
            if  t.find("species")>-1    or \
                t.find("animal")>-1:
                if  (t.find("ocean")>-1  or \
                    t.find("marine")>-1 or \
                    t.find("coast")>-1  or \
                    t.find("sea")>-1    or \
                    t.find("reef")>-1)==False:
                    return True
                    
    if  t.find("protect")>-1:
        if  t.find("threaten")>-1   or \
            t.find("endanger")>-1:
            if  t.find("species")>-1    or \
                t.find("animal")>-1     or \
                t.find("plant")>-1:
                if  (t.find("ocean")>-1  or \
                    t.find("marine")>-1 or \
                    t.find("coast")>-1  or \
                    t.find("sea")>-1    or \
                    t.find("reef")>-1)==False:
                    return True
                    
    if  t.find("prevent")>-1:
        if  t.find("extinct")>-1:
            if  t.find("threaten")>-1   or \
                t.find("endanger")>-1:
                if  t.find("species")>-1    or \
                    t.find("animal")>-1     or \
                    t.find("plant")>-1:
                    if  (t.find("ocean")>-1  or \
                        t.find("marine")>-1 or \
                        t.find("coast")>-1  or \
                        t.find("sea")>-1    or \
                        t.find("reef")>-1)==False:
                        return True
                        
    #Target 15.9
    if  (t.find("ecosystem")>-1 and t.find("biodiversity")>-1) or \
        t.find("species diversity")>-1:
        if  t.find("polic")>-1  or \
            t.find("strateg")>-1  or \
            t.find("plan")>-1:
            if  (t.find("ocean")>-1  or \
                t.find("marine")>-1 or \
                t.find("coast")>-1  or \
                t.find("sea")>-1    or \
                t.find("reef")>-1)==False:
                return True
                
    if  t.find("aichi biodiversity target")>-1  or \
        t.find("strategic plan for biodiversity")>-1:
        return True
        
    #Target 15.a
    if  t.find("ecosystem")>-1:
        if  t.find("biodiversity")>-1:
            if  t.find("financ")>-1:
                return True
        
            if  t.find("develop")>-1:
                if  t.find("assist")>-1 or \
                    t.find("support")>-1    or \
                    t.find("aid")>-1    or \
                    t.find("program")>-1:
                    return True
            if  t.find("spending")>-1   or \
                t.find("expenditure")>-1    or \
                t.find("gdp")>-1        or \
                t.find("gross domestic product")>-1:
                return True
                
    #Target 15.b
    if  t.find("ecosystem")>-1:
        if  t.find("biodiversity")>-1:
            if  t.find("forest")>-1:
                return True
             
    return False
    
def in_sdg16(t):
    #Target 16.1
    if  t.find("reduc")>-1:
        if  t.find("violence")>-1   or \
            t.find("homocide")>-1:
            return True
            
    if  t.find("victim")>-1:
        if  t.find("homocide")>-1:
            if  t.find("number")>-1 or \
                t.find("per capita")>-1 or \
                t.find("population")>-1:
                return True
                
    if  t.find("conflict")>-1:
        if  t.find("death")>-1:
            if  t.find("number")>-1 or \
                t.find("per capita")>-1 or \
                t.find("population")>-1:
                return True
                
    if  t.find("physical")>-1   or \
        t.find("psychological")>-1  or \
        t.find("sexual")>-1:
        if  t.find("violen")>-1:
            if  t.find("number")>-1 or \
                t.find("per capita")>-1 or \
                t.find("population")>-1:
                return True
                
    if  t.find("safe")>-1:
        if  t.find("walking")>-1:
            if  t.find("number")>-1 or \
                t.find("per capita")>-1 or \
                t.find("population")>-1:
                return True
            
    #Target 16.2
    if  t.find("end")>-1    or \
        t.find("reduc")>-1:
        if  t.find("abus")>-1   or \
            t.find("exploit")>-1    or \
            t.find("traffick")>-1   or \
            t.find("violen")>-1     or \
            t.find("tortur")>-1     or \
            t.find("neglect")>-1:
            if  t.find("child")>-1:
                return True
                
    if  t.find("caregiver")>-1:
        if  t.find("abus")>-1   or \
            t.find("exploit")>-1    or \
            t.find("traffick")>-1   or \
            t.find("violen")>-1     or \
            t.find("tortur")>-1     or \
            t.find("neglect")>-1:
            if  t.find("child")>-1:
                return True
                
    if  t.find("victim")>-1:
        if  t.find("human traffick")>-1:
            return True
            
    if  t.find("sexual")>-1:
        if  t.find("violen")>-1:
            if  t.find("young")>-1:
                if  t.find("number")>-1 or \
                    t.find("per capita")>-1 or \
                    t.find("population")>-1:
                    return True
                    
    if  t.find("children's right")>-1:
        return True
        
    #Target 16.3
    if  t.find("rule of law")>-1:
        return True
        
    if  t.find("access")>-1:
        if  t.find("justice")>-1:
            return True
           
    if  t.find("victim")>-1:
        if  t.find("report")>-1:
            return True
            
    #Target 16.4
    if  t.find("organised crime")>-1    or \
        t.find("orgnanized crime")>-1:
        return True
       
    if  t.find("illegal")>-1    or \
        t.find("illicit")>-1:
        if  t.find("financ")>-1 or \
            t.find("arms")>-1:
            return True
            
    if  t.find("recover")>-1    or \
        t.find("return")>-1:
        if  t.find("stolen")>-1:
            return True
            
    if  t.find("money")>-1:
        if  t.find("launder")>-1:
            return True
            
    #Target 16.5
    if  t.find("corruption")>-1 or \
        t.find("bribe")>-1      or \
        t.find("miscarriage of justice")>-1:
        return True
        
    #Target 16.6
    if  t.find("effective")>-1  or \
        t.find("accountable")>-1    or \
        t.find("transparant")>-1:
        if  t.find("institution")>-1:
            return True
            
    if  t.find("satisf")>-1 or \
        t.find("experience")>-1:
        if  t.find("public service")>-1:
            return True
            
    #Target 16.7
    if  t.find("decision making")>-1:
        if  t.find("responsive")>-1     or \
            t.find("inclusive")>-1      or \
            t.find("participat")>-1     or \
            t.find("represent")>-1:
            return True
            
    if  t.find("inclusive societ")>-1:
        return True
        
    if  t.find("people")>-1 or \
        t.find("women")>-1  or \
        t.find("men")>-1:
        if  t.find("participat")>-1 or \
            t.find("position")>-1:
            if  t.find("institution")>-1        or \
                t.find("government")>-1         or \
                t.find("municipal")>-1          or \
                t.find("judiciary")>-1          or \
                t.find("public service")>-1     or \
                t.find("legislature")>-1        or \
                t.find("parliament")>-1:
                return True
                
    #Target 16.8
    if  t.find("participat")>-1 or \
        t.find("representation")>-1 or \
        t.find("voice")>-1      or \
        t.find("voting right")>-1:
        if  t.find("international")>-1  or \
            t.find("global")>-1:
            if  t.find("develop")>-1:
                if  t.find("countr")>-1:
                    return True
                    
    if  t.find("nongovernmental organisation")>-1   or \
        t.find("nongovernmental organization")>-1   or \
        t.find("non-governmental organisation")>-1  or \
        t.find("non-governmental organization")>-1  or \
        t.find("ngo")>-1:
        if  t.find("develop")>-1:
            if  t.find("countr")>-1:
                return True
                
    #Target 16.9
    if  t.find("legal identity")>-1:
        return True
        
    if  t.find("birth")>-1:
        if  t.find("regist")>-1:
            if  t.find("authorit")>-1   or \
                t.find("municipal")>-1:
                return True
                               
    #Target 16.10
    if  t.find("public")>-1:
        if  t.find("access")>-1:
            if  t.find("information")>-1:
                return True
                
    if  t.find("fundamental freedom")>-1:
        return True
        
    if  t.find("free")>-1:
        if  t.find("speech")>-1 or \
            t.find("press")>-1:
            return True
            
    if  t.find("case")>-1:
        if  t.find("kill")>-1   or \
            t.find("murder")>-1 or \
            t.find("attack")>-1 or \
            t.find("kidnap")>-1 or \
            t.find("disappear")>-1  or \
            t.find("arbitrary detention")>-1    or \
            t.find("tortur")>-1:
            if  t.find("journalist")>-1 or \
                t.find("media personnel")>-1    or \
                t.find("trade union")>-1    or \
                t.find("lawyer")>-1 or \
                t.find("advocates")>-1:
                return True
                
    #Target 16.a
    if  t.find("institution")>-1:
        if  t.find("prevent")>-1    or \
            t.find("combat")>-1:
            if  t.find("violence")>-1   or \
                t.find("terrorism")>-1  or \
                t.find("crime")>-1:
                return True
                
        if  t.find("human right")>-1    or \
            t.find("civil right")>-1    or \
            t.find("child right")>-1:
            return True
            
    #Target 16.b
    if  t.find("discriminat")>-1:
        if  t.find("policy")>-1 or \
            t.find("policies")>-1   or \
            t.find("legislation")>-1    or \
            t.find("law")>-1:
            return True
            
    return False
    
def in_sdg17(t):
    #Target 17.1
    if  t.find("tax")>-1    or \
        t.find("revenue")>-1:
        if  t.find("collect")>-1:
            if  t.find("government")>-1 or \
                t.find("domestic")>-1:
                return True
                
    if  t.find("tax")>-1    or \
        t.find("expenditure")>-1    or \
        t.find("revenue")>-1:
        if  t.find("government")>-1 or \
            t.find("domestic")>-1:
            if  t.find("gpd")>-1    or \
                t.find("gross domestic product")>-1:
                return True
                
    if  t.find("tax")>-1:
        if  t.find("budget")>-1:
            if  t.find("domestic")>-1:
                return True
                
    #Target 17.2
    if  t.find("develop")>-1:
        if  t.find("assist")>-1 or \
            t.find("support")>-1    or \
            t.find("aid")>-1    or \
            t.find("program")>-1:
            if  t.find("least developed countr")>-1 or \
                t.find("small island")>-1           or \
                (t.find("develop")>-1 and t.find("countr")>-1):
                return True
            
            if  t.find("commitment")>-1 or \
                t.find(" oda")>-1       or \
                t.find("official development assistance")>-1    or \
                t.find(" gni")>-1       or \
                t.find("gross national income")>-1:
                return True
                
    #Target 17.3
    if  t.find("financial resource")>-1:
         if  t.find("least developed countr")>-1 or \
            t.find("small island")>-1           or \
            (t.find("develop")>-1 and t.find("countr")>-1):
            return True
            
    if  t.find("budget")>-1:
        if  t.find("foreign")>-1:
            if  t.find("invest")>-1:
                return True
                
    if  t.find("budget")>-1:
        if  t.find("develop")>-1:
            if  t.find("assist")>-1 or \
                t.find("support")>-1    or \
                t.find("aid")>-1    or \
                t.find("program")>-1:
                return True
                
    if  t.find("budget")>-1:
        if  t.find("south-south")>-1:
            return True
            
    if  t.find("remittance")>-1:
        if  t.find("gpd")>-1    or \
            t.find("gross domestic product")>-1:
            return True
            
    #Target 17.4
    if  t.find("debt")>-1:
         if  t.find("least developed countr")>-1 or \
            t.find("small island")>-1           or \
            (t.find("develop")>-1 and t.find("countr")>-1):
            return True
            
    if  t.find("debt")>-1:
        if  t.find("servic")>-1 or \
            t.find("manag")>-1:
            if  t.find("export")>-1:
                return True
                
    #Target 17.5
    if  t.find("investment")>-1:
        if  t.find("least developed countr")>-1 or \
            t.find("small island")>-1           or \
            (t.find("develop")>-1 and t.find("countr")>-1):
            return True
            
    #Target 17.6
    if  t.find("international")>-1  or \
        t.find("regional")>-1       or \
        t.find("north-south")>-1    or \
        t.find("agreement")>-1      or \
        t.find("south-south")>-1:
        if  t.find("cooperation")>-1:
            if  t.find("science")>-1    or \
                t.find("technology")>-1 or \
                t.find("innovation")>-1:
                return True
    
    if  t.find("subscription")>-1:
        if  t.find("internet")>-1:
            return True
            
    #Target 17.7
    if  t.find("development")>-1    or \
        t.find("transfer")>-1       or \
        t.find("dissemination")>-1  or \
        t.find("diffusion")>-1:
        if  t.find("environment")>-1:
            if  t.find("sound")>-1:
                if  t.find("technolog")>-1:
                    return True
                    
    if  t.find("least developed countr")>-1 or \
        t.find("small island")>-1           or \
        (t.find("develop")>-1 and t.find("countr")>-1):
        if  t.find("environment")>-1:
            if  t.find("sound")>-1:
                if  t.find("technolog")>-1:
                    return True
    
    #Target 17.8
    if  t.find("least developed countr")>-1 or \
        t.find("small island")>-1           or \
        (t.find("develop")>-1 and t.find("countr")>-1):
        if  t.find("capacity")>-1:
            if  t.find("science")>-1    or \
                t.find("technology")>-1 or \
                t.find("innovation")>-1:
                return True
                
    #Target 17.9
    if  t.find("implement")>-1:
        if  t.find("sdg")>-1    or \
            t.find("global development goal")>-1:
            return True
            
    if  t.find("financ")>-1 or \
        t.find("technic")>-1    or \
        t.find("assist")>-1     or \
        t.find("support")>-1    or \
        t.find("aid")>-1:
        if  t.find("least developed countr")>-1 or \
            t.find("small island")>-1           or \
            (t.find("develop")>-1 and t.find("countr")>-1):
            return True
            
    #Target 17.10
    if  t.find("universal")>-1  or \
        t.find("rule based")>-1 or \
        t.find("open")>-1       or \
        t.find("non-discriminat")>-1    or \
        t.find("equit")>-1      or \
        t.find("multilateral")>-1:
        if  t.find("trade")>-1  or \
            t.find("trading")>-1    or \
            t.find("wto")>-1        or \
            t.find("world trade organization")>-1   or \
            t.find("doha development")>-1:
            return True
            
    if  t.find("tariff")>-1:
        if  t.find("average")>-1:
            return True
            
    #Target 17.11
    if  t.find("least developed countr")>-1 or \
        t.find("small island")>-1           or \
        (t.find("develop")>-1 and t.find("countr")>-1):
        if  t.find("global")>-1     or \
            t.find("world")>-1      or \
            t.find("increase")>-1   or \
            t.find("share")>-1:
            if  t.find("export")>-1:
                return True
                
    #Target 17.12
    if  t.find("duty")>-1   or \
        t.find("duties")>-1 or \
        t.find("quotum")>-1 or \
        t.find("quota")>-1:
        if  t.find("free")>-1:
            return True
            
    if  t.find("tariff")>-1:
        if  t.find("least developed countr")>-1 or \
            t.find("small island")>-1           or \
            (t.find("develop")>-1 and t.find("countr")>-1):
            return True
            
    #Target 17.13
    if  t.find("macroeconom")>-1    or \
        t.find("macro-econom")>-1:
        if  t.find("stability")>-1:
            return True
            
    #Target 17.14
    if  t.find("policy")>-1 or \
        t.find("policies")>-1:
        if  t.find("cohoren")>-1    or \
            t.find("coordinat")>-1  or \
            t.find("framework")>-1  or \
            t.find("instrument")>-1:
            if  t.find("sdg")>-1    or \
                t.find("sustainable development")>-1:
                return True
                
    if  t.find("policy")>-1 or \
        t.find("policies")>-1:
        if  t.find("sustainab")>-1:
            if  t.find("sdg")>-1    or \
                t.find("sustainable development")>-1:
                return True
                
    #Target 17.15
    if  t.find("implement")>-1  or \
        t.find("establish")>-1:
        if  t.find("policy")>-1 or \
            t.find("policies")>-1:
            if  t.find("sdg")>-1    or \
                t.find("sustainable development")>-1:
                return True
                
    if  t.find("implement")>-1  or \
        t.find("establish")>-1:
        if  t.find("policy")>-1 or \
            t.find("policies")>-1:
            if  t.find("poverty")>-1:
                if  t.find("eradicat")>-1   or \
                    t.find("reduc")>-1      or \
                    t.find("end")>-1        or \
                    t.find("alleviat")>-1:
                    return True
                    
    if  t.find("cooperation")>-1:
        if  t.find("development")>-1:
            if  t.find("framework")>-1:
                return True
                    
            if  t.find("plan")>-1:
                if  t.find("tool")>-1:
                    return True
                    
    #Target 17.16
    if  t.find("sdg")>-1    or \
        t.find("sustainable development")>-1:
        if  t.find("partner")>-1    or \
            t.find("cooperat")>-1:
            return True
            
        if  t.find("multi-stakeholder")>-1:
            return True
            
    #Target 17.17
    if  t.find("partnership")>-1:
        if  t.find("public")>-1 or \
            t.find("civil societ")>-1:
            return True
            
    #Target 17.18
    if  t.find("least developed countr")>-1 or \
        t.find("small island")>-1           or \
        (t.find("develop")>-1 and t.find("countr")>-1):
        if  t.find("data")>-1   or \
            t.find("statistic")>-1:
            return True
            
    if  t.find("sustainable development")>-1:
        if  t.find("indicator")>-1:
            return True
            
    if  t.find("fundamental principles of official statistics")>-1:
        if  t.find("statistics")>-1:
            if  t.find("legislation")>-1:
                return True
                
    if  t.find("national")>-1:
        if  t.find("plan")>-1:
            if  t.find("statistics")>-1:
                return True
                
    #Target 17.19
    if  t.find("sdg")>-1    or \
        t.find("sustainable development")>-1:
        if  t.find("progress")>-1   or \
            t.find("measurement")>-1    or \
            t.find("measuring")>-1  or \
            t.find("monitor")>-1:
            return True
            
    if  t.find("least developed countr")>-1 or \
        t.find("small island")>-1           or \
        (t.find("develop")>-1 and t.find("countr")>-1):
        if  t.find("data")>-1   or \
            t.find("statistics")>-1:
            if  t.find("capacity")>-1   or \
                t.find("strenghten")>-1 or \
                t.find("budget")>-1     or \
                t.find("money")>-1      or \
                t.find("dollar")>-1     or \
                t.find("resource")>-1:
                return True
                
    if  t.find("population census")>-1  or \
        t.find("housing census")>-1     or \
        t.find("birth registration")>-1 or \
        t.find("death registration")>-1:
        return True
        
    return False
    

    
        
                