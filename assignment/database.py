"""
Employee Portal
    database.py

Stefana Chiritescu
"""

import sqlite3

# connect to database
con = sqlite3.connect("employees.db")
cur = con.cursor()

# creates database and inserts table if it does not exist
try:
    cur.execute(
        "CREATE TABLE Employee(emp_id INTEGER(10) PRIMARY KEY, first_name VARCHAR(45), surname VARCHAR(45), "
        "gender VARCHAR(10), department VARCHAR(100), position VARCHAR(45), date_of_birth VARCHAR(10), start_date "
        "VARCHAR(10), email VARCHAR(60), contact VARCHAR(20), salary INTEGER(12), active BLOB, address VARCHAR(100), "
        "picture BLOB)")
    data = [(6612, "Peter", "Doni", "Male", "Business Development", "Business Development Manager", "06/05/1985",
             "02/03/2017", "peter.doni@gmail.com", "253-862-6859", 70500, True,
             "883 Vanasse Rd,\nKettle Falls,\nWashington (WA),\n99141", "./images/peter.jpg"),
            (7407, "Fiona", "Winterscale", "Female", "Services", "Technical Services Director", "07/25/1996",
             "12/31/2018", "fwinterscale1@fda.gov", "451-237-4922", 119232, False,
             "9736 Pepper Wood Road,\nMilehouse,\nWashington (WA),\n99120", "./images/fiona.jpg"),
            (6913, "Myrtia", "Spybey", "Female", "Marketing", "Marketing Manager", "07/08/1981", "09/23/2001",
             "mspybey2@bbc.co.uk", "476-307-5002", 210151, True,
             "1515 Upham Crossing,\nWaterfall,\nWashington (WA),\n87426", "./images/myrtia.jpg"),
            (8294, "Francisca", "Crone", "Female", "Engineering", "Software Engineering Intern", "11/08/1987",
             "01/12/2011", "fcrone3@yahoo.com", "630-674-9432", 34800, True,
             "19 Ilene Crossing,\nFore,\nWashington (WA),\n18521", "./images/francisca.jpg"),
            (
                3089, "Lorain", "Tropman", "Female", "Business Development", "Sales Specialist", "04/31/1962",
                "06/26/2006",
                "ltropman4@berkeley.edu", "644-458-7480", 276078, True,
                "6371 Dottie Park,\nShrub Oak,\nNew York (NY),\n62342", "./images/lorain.jpg"),
            (2854, "Allegra", "Kastel", "Female", "Training", "Training Assistant", "10/24/1969", "08/29/2018",
             "akastel5@patch.com", "559-126-9571", 112000, True, "014 Upham Center,\nLake Mary,\nNew York (NY),\n47232",
             "./images/allegra.jpg"),
            (1705, "Gracie", "Creedland", "Female", "Legal", "Legal Assistant", "04/02/1994", "03/23/2014",
             "gcreedland6@ezinearticles.com", "495-834-2568", 70500, True,
             "9 Oak Drive,\nSouthfield,\nNew York (NY),\n27577", "./images/gracie.jpg"),
            (5567, "William", "Clemencet", "Male", "Human Resources", "Human Resource Manager", "07/04/1972",
             "05/09/2010", "wclemencet7@uol.com", "753-193-3875", 109203, False,
             "9 Carpenter Place,\nColchester,\nNew York (NY),\n60505", "./images/william.jpg"),
            (2526, "Kian", "Egdell", "Male", "Sales", "Senior Sales Executive", "05/02/1988", "05/23/2010",
             "kegdell8@moonfruit.com", "804-735-0112", 210106, False,
             "7 Mccormick Center,\nColchester,\nWashington (WA),\n75137", "./images/kian.jpg"),
            (9498, "Shayanne", "Barde", "Female", "Marketing", "Markerint Assistant", "06/04/1987", "07/12/2020",
             "sbarde9@xing.com", "862-668-5540", 89040, True, "6058 Spohn Pass,\nShrub Oak,\nWashington (WA),\n65421",
             "./images/shayanne.jpg"),
            (9645, "Audry", "Hedin", "Female", "Product Management", "Product Manager", "01/11/1996", "06/11/2018",
             "ahedina@edublogs.org", "194-589-5442", 118000, True, "799 2nd Court,\nAuburn,\nWashington (WA),\n98621",
             "./images/audry.jpg"),
            (4955, "Adam", "Borrel", "Male", "Product Management", "Product Management Assistant ", "01/08/1971",
             "06/08/2009", "aborrelb@fema.com", "937-916-6302", 40676, False,
             "3618 Blaine Point,\nPlymouth,\nNew York (NY),\n34621", "./images/adam.jpg"),
            (
                3134, "Vivian", "Wegman", "Female", "Business Development", "Marketing Manager", "02/03/1983",
                "31/05/2001",
                "bwegmanc@icq.com", "476-802-3738", 76895, True,
                "77951 Loeprich Lane,\nCharlotte,\nNorth Carolina (NC),\n87524", "./images/vivian.jpg"),
            (5935, "Frederick", "Gounet", "Male", "Support", "Digital Media Officer", "28/09/1971", "23/04/2012",
             "agounetd@bandcamp.com", "488-136-6089", 294010, True, "7 Maywood Way,\nRockville,\nNew York (NY),\n75674",
             "./images/frederick.jpg"),
            (8357, "Candi", "Cowling", "Female", "Engineering", "Architecture Software Engineer", "08/07/1969",
             "11/08/2018", "ccowlinge@gmail.com", "460-944-1756", 190000, True,
             "201 Springs Center,\nNorth Naples,\nNew York (NY),\n45983", "./images/candi.jpg"),
            (1277, "Bevan", "Babington", "Male", "Sales", "Sales Manager", "02/21/1986", "02/20/2011",
             "bbabingtonf@cnet.com", "322-623-6758", 91546, True,
             "6840 Doe Crossing Circle,\nSyracuse,\nWashington (WA),\n23875", "./images/bevan.jpg"),
            (3434, "Carl", "Alliker", "Male", "Services", "General Services Manager", "11/10/1983", "01/06/2018",
             "callikerg@redcross.org", "809-575-9353", 90105, False,
             "5526 Monterey Plaza,\nMonessen,\nWashington (WA),\n76423", "./images/carl.jpg"),
            (4285, "Kenn", "Corten", "Male", "Accounting", "Accounting Manager", "01/04/1983", "01/24/2005",
             "kcortenh@uiuc.edu", "172-506-9062", 120913, True, "3082 Fremont Hill,\nMinco,\nWashington (WA),\n78652",
             "./images/kenn.jpg"),
            (1273, "Ashlee", "McCormack", "Female", "Human Resources", "Human Resource Coordinator", "01/29/1999",
             "12/29/2008", "amccormacki@narod.ru", "623-737-9544", 50956, True,
             "95936 Banding Center,\nGrand Rapids,\nNew York (NY),\n23652", "./images/ashlee.jpg"),
            (
            4911, "Anestassia", "Kiwitz", "Female", "Product Management", "Product Manager", "08/01/1989", "03/12/2003",
            "akiwitzj@edus.com", "801-568-3424", 132000, False,
            "34732 Delaware Trail,\nGrand Rapids,\nMichigan (MI),\n23652", "./images/anestassia.jpg"),
            (5271, "Natasha", "Chatten", "Female", "Marketing", "Marketing Analyst", "05/08/1964", "09/04/2022",
             "gchattenk@sina.com.cn", "494-309-5801", 68000, False,
             "23006 Red Cloud Trail,\nAshtabula,\nNew York (NY),\n67321", "./images/natasha.jpg"),
            (8886, "Orella", "Coryndon", "Female", "Legal", "Legal Assistant Intern", "03/02/1996", "10/21/2001",
             "ocoryndonl@netlog.com", "608-355-9338", 20800, True,
             "89 Blue Bill Park Point,\nNew Brunswick,\nNew Jersey (NJ),\n67321", "./images/orella.jpg"),
            (4714, "Glynda", "Bellini", "Female", "Accounting", "Bookkeeping Assistant", "10/10/1976", "12/11/2014",
             "gbellinim@gmail.com", "282-528-1067", 46637, True,
             "20 Pennsylvania Center,\nCookeville,\nNew Jersey (NJ),\n86231", "./images/glynda.jpg"),
            (1326, "Jamie", "Castledine", "Male", "Training", "Training Co-ordinator", "02/12/1979", "02/01/2014",
             "jcastledinen@fda.gov", "957-792-3139", 70987, True,
             "2 Westridge Point,\nRochester,\nNew York (NY),\n12651", "./images/jamie.jpg"),
            (5561, "Tara", "Burbudge", "Female", "Services", "Building Services Engineer", "02/11/1963", "02/10/2006",
             "tburbudgeo@1und1.de", "819-581-8954", 280000, True,
             "9454 Prairieview ,\nManhattan,\nNew York (NY),\n49892", "./images/tara.jpg"),
            (5035, "Max", "Esmead", "Male", "Engineering", "Senior Quality Engineer", "09/01/1969", "04/17/2022",
             "besmeadp@lulu.com", "770-397-0402", 160300, True,
             "853 Tomscot Crossing,\nRochester,\nMichigan (MI),\n12651", "./images/max.jpg"),
            (
                2071, "Alfy", "Castiblanco", "Male", "Business Development", "Business Development Executive",
                "09/25/1998",
                "05/11/2001", "acastiblancoq@ameblo.jp", "132-347-9567", 70396, False,
                "704 Clemons Place,\nOmaga,\nNew Jersey (NJ),\n75521", "./images/alfy.jpg"),
            (
                7029, "Coleman", "Crispin", "Male", "Business Development", "Financial Analyst", "08/07/1989",
                "06/01/2010",
                "ccrispinr@vimeo.com", "821-153-0230", 86765, False,
                "2828 Susan Avenue,\nManhattan,\nNew York (NY),\n67421", "./images/coleman.jpg"),
            (8014, "Daniel", "Grosvenor", "Male", "Human Resources", "Human Resource Assistant", "03/03/1990",
             "06/10/2022", "dgrosvenors@ucoz.ru", "783-465-2454", 40791, True,
             "276 Northfield Drive,\nPhoenix,\nWashington (WA),\n87325", "./images/daniel.jpg"),
            (1642, "Boris", "Greenley", "Male", "Business Development", "Chief Executive Officer", "09/23/1977",
             "01/02/2000", "bgreenleyt@uol.com", "403-438-3406", 780000, True,
             "675 Vera ,\nManhattan,\nNew York (NY),\n45651", "./images/boris.jpg"),
            (7124, "Cristy", "Edis", "Female", "Human Resources", "Site HR Administrator", "11/05/1964", "01/07/2009",
             "cedisu@wikispaces.com", "133-115-6155", 39058, True,
             "9562 Manufacturers Terrace,\nGreer,\nNew Jersey (NJ),\n66932", "./images/cristy.jpg"),
            (1284, "Suzanne", "Shorto", "Female", "Accounting", "Accounting Assistant Intern", "11/11/1997",
             "11/01/2008", "wshortov@archive.org", "457-247-0427", 30000, True,
             "2112 Sherman Hill,\nWest Osborne,\nNew York (NY),\n45971", "./images/suzanne.jpg"),
            (6178, "Fayina", "Walcot", "Female", "Research and Development", "Payment Adjustment Coordinator",
             "09/01/1996", "06/11/2002", "fwalcotw@hotmail.com", "408-288-2997", 987639, True,
             "66 David Pass,\nBedford,\nNew Jersey (NJ),\n12651", "./images/fayina.jpg"),
            (9577, "Clementine", "Pascow", "Female", "Research and Development", "Health Coach IV", "10/02/1965",
             "07/27/2017", "kpascowx@cnn.com", "163-913-2280", 814871, True,
             "7931 Kensington Place,\nWingdale,\nWashington (WA),\n12651", "./images/clementine.jpg"),
            (9449, "Ondrea", "Eannetta", "Female", "Human Resources", "Human Resources Manager", "04/06/1991",
             "08/24/2010", "oeannettay@timesonline.co.uk", "651-756-5074", 118469, False,
             "46898 Monument Avenue,\nBoston,\nNew York (NY),\n56421", "./images/ondrea.jpg"),
            (7346, "Edward", "Fronks", "Male", "Training", "Training Manager", "02/07/1975", "03/31/2015",
             "cfronksz@nih.gov", "715-596-4599", 181896, True, "36 Maryland Junction,\nDumas,\nNew Jersey (NJ),\n87532",
             "./images/edward.jpg"),
            (1135, "Loren", "Roddick", "Female", "Sales", "Senior Sales Consultant", "02/07/1975", "08/03/2011",
             "lroddick10@gmail.com", "422-168-4277", 67303, True,
             "13 Commercial Point,\nOsseo,\nWashington (WA),\n11995", "./images/loren.jpg"),
            (7021, "Katy", "Triplow", "Female", "Engineering", "Junior Quality Engineer", "01/07/1986", "01/03/2013",
             "ktriplow11@sciencedaily.com", "753-362-1992", 99350, True,
             "4421 Kim Junction,\nBoston,\nNew York (NY),\n66321", "./images/katy.jpg"),
            (3470, "Liva", "Barnshaw", "Female", "Services", "Customer Services", "09/08/1970", "09/07/2006",
             "lbarnshaw12@bloomberg.com", "909-628-6419", 32070, False,
             "9 Eggendart Pass,\nMaintown,\nNew Jersey (NJ),\n76533", "./images/liva.jpg"),
            (5026, "Petronia", "Bates", "Female", "Support", "Admin Support", "09/03/1966", "06/04/2007",
             "pbates13@dropbox.com", "469-903-1367", 51000, True, "59 Columbus Trail,\nBryan,\nNew York (NY),\n46299",
             "./images/petronia.jpg"),
            (9096, "Emmanuel", "Caurah", "Male", "Support", "Support Worker", "12/02/1966", "10/11/2013",
             "ecaurah14@phpbb.com", "442-856-0450", 31000, True,
             "69612 Armistice Park,\nRochester,\nWashington (WA),\n76318", "./images/emmanuel.jpg"),
            (7006, "Rosene", "Kimmerling", "Female", "Engineering", "Structural Analysis Engineer", "16/11/1985",
             "01/31/2012", "rkimmerling15@gmail.com", "454-652-2988", 70000, True,
             "530 Judy Alley,\nManhattan,\nNew York (NY),\n67521", "./images/rosene.jpg"),
            (2045, "Enrique", "Daniels", "Male", "Sales", "Junior Sales Associate", "02/10/1968", "04/12/2002",
             "edantuoni16@stumbleupon.com", "912-698-8290", 35252, True,
             "686 1st Lane,\nJacksonville,\nNew York (NY),\n64211", "./images/enrique.jpg"),
            (8037, "Ailyn", "Cartmer", "Female", "Legal", "Legal Operations Associate", "07/03/1966", "04/08/2022",
             "acartmer17@legal.com", "291-429-4327", 89633, True, "539 Kim Hill,\nPlainview,\nWashington (WA),\n98429",
             "./images/ailyn.jpg"),
            (8437, "Amalie", "Howison", "Female", "Services", "Customer Services", "12/17/1968", "09/18/2002",
             "ahowison18@wunderground.com", "622-320-4373", 59000, True,
             "0338 Sage Center,\nIndianola,\nNew York (NY),\n65311", "./images/amalie.jpg"),
            (9644, "Almira", "Flanagan", "Female", "Business Development", "Financial Manager", "08/09/1991",
             "12/11/2003", "aflanagan19@gmail.com", "531-710-0576", 67940, True,
             "12101 Meadow Ridge Center,\nSpringfield,\nNew Jersey (NJ),\n56543", "./images/almira.jpg"),
            (5529, "Parnell", "Frentz", "Male", "Engineering", "Software Testing Engineer", "17/08/1979", "01/24/2013",
             "pfrentz1a@redcross.com", "221-711-7567", 120631, True,
             "2860 Redwing Hill,\nBoston,\nNew York (NY),\n76632", "./images/parnell.jpg"),
            (8579, "Neil", "Balwin", "Male", "Accounting", "Accounting Assistant", "07/09/1997", "09/02/2020",
             "nbalwin@geocities.co.uk", "625-911-2277", 58236, True,
             "422 Mallory Center,\nManhattan,\nNew York (NY),\n76042", "./images/neil.jpg"),
            (1124, "Torrey", "Vanee", "Male", "Research and Development", "General Manager", "12/08/1964", "05/10/2014",
             "torrey_vanee@wufoo.com", "213-150-9972", 576343, True,
             "516 Redwing Circle,\nAlbermane,\nWashington (WA),\n76312", "./images/torrey.jpg"),
            (3373, "Francine", "McGready", "Female", "Legal", "Legal Secretary", "04/16/1986", "05/16/2018",
             "fmcgready1d@time.com", "448-810-3395", 36300, True,
             "218 Lighthouse Bay Street,\nQueens\nNew York(NY)\n54789", "./images/francine.jpg")]

    cur.executemany("INSERT INTO Employee VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

# prints if database already exists
except:
    print("Employees database has not been created as it already exists.")
