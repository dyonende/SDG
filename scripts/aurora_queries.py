import sys

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
            if  t.find("developing countr")
            
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
    
print(in_sdg3(sys.argv[1]))                