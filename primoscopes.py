import csv


#Assigned value 'no_sign_in' to all blank 0 Signed In entries (Some zero signed in entries are type=guest leave those)
#Assigned value 'undefined' to all blank User Group entries with non-zero Signed In entries
VISITINGSCHOLAR = ['visitscholar', 'visitingscholar', 'vistfacstaff']
EMERITUS = ['emeritifac', 'emeritus', 'emeritusfaculty', 'facultyemeriti']
CALS_WALKIN = ['walkin', 'calswalkin']
FRIENDS_OF = ['fol', 'folsustaining', 'friendsofthelibrary', '36']
GRADUATE = ['graduate', 'graduatedisted', 'graduatestudent', 'student_graduate', 'g', '6', '20']
RETIRED = ['retiree', 'retiredfaculty', 'r']
ALUMNI = ['alu', 'alumni', 'csualumni', 'csulbalumni', 'csunalumni', 'patronsalumni', 'community/alumni', '27']
FACULTY = ['faculty', 'adjunctfaculty', 'contractfaculty', 'csufaculty', 'parttimefacultylecturers', 'f', '1']
TEST_GROUP = ['gin', 'bursartestgroup', 'patrontest', 'sageuser']
UNDERGRADUATE = ['amp', 'student', 'student(ug)', 'undergraduate', 'u', '0']
TA_GA = ['ta/ga', '14']
INTERNAL_LIBRARY_OPERATIONS = ['desk', 'ill', 'inhouse', 'internalstaff', 'libassociate', 'libinternaluse', 'library', 'librarydepartment', 'libstaff', 'special(internal library use)', 'mbari', 'sutro', '7']
PUBLIC_COMMUNITY = ['community', 'community borrower', 'courtesy', 'courtesy borrower', 'commborrower', 'com_borw', 'nau', 'generalpublic', 'guestpass', 'public', 'public access computer user', 'publicborrower', 'publicpcuser', 'p', '72', '18', '22']
COMMUNITY_COLL = ['mtsac', 'cuestacol', 'ccstudent', 'cr']
HIGH_SCHOOL = ['hs', 'high school students']
EXT_ED = ['extendededucation', 'e']
MERGED_STAFF = ['staff', 'staffiii', 'auxilliarystaff', 's', '2']
UNDEFINED = ['999', 'undefined']

csv_file = "clean_data.csv"
with open(csv_file, 'w') as csvfile:
    with open('2017-2019_xlsx.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        writer = csv.DictWriter(csvfile, fieldnames=csv_reader.fieldnames)
        writer.writeheader()

        for row in csv_reader:
            if (row["User Group"] in VISITINGSCHOLAR):
                row["User Group"] = "visitscholar"
            elif (row["User Group"] in EMERITUS):
                row["User Group"] = "emeritus"
            elif (row["User Group"] in CALS_WALKIN):
                row["User Group"] = "cals_walkin"
            elif (row["User Group"] in FRIENDS_OF):
                row["User Group"] = "friends_of"
            elif (row["User Group"] in GRADUATE):
                row["User Group"] = "graduate"
            elif (row["User Group"] in RETIRED):
                row["User Group"] = "retired"
            elif (row["User Group"] in ALUMNI):
                row["User Group"] = "alumni"
            elif (row["User Group"] in FACULTY):
                row["User Group"] = "faculty"
            elif (row["User Group"] in TEST_GROUP):
                row["User Group"] = "test_group"
            elif (row["User Group"] in UNDERGRADUATE):
                row["User Group"] = "undergraduate"
            elif (row["User Group"] in TA_GA):
                row["User Group"] = "ta_ga"
            elif (row["User Group"] in INTERNAL_LIBRARY_OPERATIONS):
                row["User Group"] = "internal_library_operations"
            elif (row["User Group"] in PUBLIC_COMMUNITY):
                row["User Group"] = "public_community"
            elif (row["User Group"] in COMMUNITY_COLL):
                row["User Group"] = "community_coll"
            elif (row["User Group"] in HIGH_SCHOOL):
                row["User Group"] = "high_school"
            elif (row["User Group"] in EXT_ED):
                row["User Group"] = "ext_ed"
            elif (row["User Group"] in EXT_ED):
                row["User Group"] = "ext_ed"
            elif (row["User Group"] in MERGED_STAFF):
                row["User Group"] = "merged_staff"
            elif (row["User Group"] in UNDEFINED):
                row["User Group"] = "undefined"  
            elif ((row["User Group"] is None or row["User Group"].strip() == '') and row['Signed In'] == '0'):
                row["User Group"] = "no_sign_in" 
            elif ((row["User Group"] is None or row["User Group"].strip() == '') and row['Signed In'] != '0'):
                row["User Group"] = "undefined"              
            writer.writerow(row)

  

