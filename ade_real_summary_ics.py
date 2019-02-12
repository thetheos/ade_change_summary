from icalendar import Calendar, Event
import copy

"""
#Convert Dic Q2
convert_dic = {'LEPL1202-Q2 A': 'Physique II', 'LEPL1502_Q2.2 Labo V34': 'PROJET II Labo V34', 'LEPL1105-Q2 A+B': 'Analyse II', 'LEPL1301-Q2 A': 'Chimie et chimie physique I', 'LEPL1502_Q2 A': 'Projet II', 'LEPL1502-Q2 A+B': 'Projet II', 'LEPL1105_Q2 A': 'Analyse II', 'LEPL1104-Q2 A+B': 'Methode Numerique', 'LEPL1202_Q2 A': 'Physique II', 'LEPL1104_Q2 A': 'Methode Numerique', 'LEPL1803-Q2 A+B': 'Economie', 'LEPL1301_Q2 A': 'Chimie et chimie physique I', 'LEPL1502=O': 'Projet II', 'LEPL1102': 'LEPL1102', 'LEPL1803_Q2 A': 'Economie', 'Interro': 'Interro', 'LEPL1301-Q2 S1 et S10 A+B': 'LEPL1301-Q2 S1 et S10 A+B', 'Remise de rapport de projet 11 Q2': 'Remise de rapport de projet 11 Q2', 'LEPL1202-Q2 S13 A+B': 'Physique II', 'C.A.11 Q2': 'C.A.11 Q2', 'LEPL1502_Q2 Labo A': 'Projet II Labo A'}
"""

def modify_cal(cal, convert_dic):
    """
    Create a new icalendar with concern of the convertion dictionnary
    """
    new_cal = Calendar()
    for elm in cal.walk():
        if elm.name == "VEVENT":
            event = elm
            event["summary"] = convert_dic[str(elm.get("summary"))] 
            new_cal.add_component(event)
    return new_cal


def create_dic(cal):
    """
    Create a convert dic. Key: the summary displayed on ade, Value (to input) the value you want to assign
    """
    convert_dic = {}
    for elm in new_cal.walk():
        if elm.name == "VEVENT":
            if elm.get("summary") not in convert_dic:
                name = input("What name for: {} ? \n (Press enter to leave as it is)".format(str(elm.get("summary"))))
                if name == "":
                    convert_dic[str(elm.get("summary"))] = str(elm.get("summary"))
                else:
                    convert_dic[str(elm.get("summary"))] = name
    return convert_dic


"""

f = open("adeQ2.ics", "r")
cal = Calendar.from_ical(f.read())
new_cal = copy.deepcopy(cal)


convert_dic = {}
Different_title = []
create_dic(new_cal)
new_cal = modify_cal(new_cal, convert_dic)
new_f = open("output.ics", "wb")
new_f.write(new_cal.to_ical())
new_f.close()
f.close()
print(new_cal)

"""

in_cal_file_path = input("Enter the input calendar path (.ics): \n")
try:
    in_cal = open(in_cal_file_path, "r")
except:
    print("Something went wrong when openin the file")
cal = Calendar.from_ical(in_cal.read())
in_cal.close()
new_cal = copy.deepcopy(cal)
conversion_dic = create_dic(new_cal)
out_cal = modify_cal(new_cal, conversion_dic)
out_file = open("output.ics", "wb")
out_file.write(new_cal.to_ical())
out_file.close()
print("Successfully saved in current directory as output.ics")


