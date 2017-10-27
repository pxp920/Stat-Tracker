from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import re
import csv
import tkinter.font as tkFont
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import tkinter.messagebox

Teamlist = ['Aalborg BK','Aalesunds FK','Aarhus GF','Aberdeen','AC Ajaccio','AC Horsens','Accrington','AD Alcorcón','Adelaide United',
'adidas All-Star ','Admira Wacker','ADO Den Haag','AEK Athens','AFC Eskilstuna','AFC Wimbledon','AIK','AJ Auxerre','Ajax',
'Akhisarspor','Akhmat Grozny','Al Ahli','Al Batin','Al Faisaly','Al Fateh','Al Fayha','Al Hilal','Al Ittihad','Al Nassr',
'Al Qadisiyah','Al Raed','Al Shabab','Al Taawoun','Alanyaspor','Alavés','Albacete Bpie','Albirex Niigata','América',
'América de Cali','Amiens SC','Amkar Perm','Angers SCO','Antalyaspor','Anzhi Makhachkala','Argentina','Argentinos Jrs.',
'Arka Gdynia','Arsenal','Arsenal Primera','Arsenal Tula','AS Monaco','Ascoli ','ASNL','ASSE','Aston Villa','Atalanta','Athletic Club',
'Atlanta United','Atlas','Atlético Huila','Atlético Madrid','Atlético Mineiro','Atlético Tucumán','Atlético-GO','Audax Italiano',
'Aue','Augsburg','Australia','Australia - Women','Austria','Avaí','Avellino ','AZ','Banfield','Bari ','Barnet','Barnsley',
'Basaksehir','Bayern','Belenenses','Belgium','Belgrano','Benevento','Berlin','Besiktas','Beveren','Bielefeld','Birmingham City',
'BK Häcken','Blackburn Rovers','Blackpool','Boavista','Boca Juniors','Bochum','Bohemian FC','Bolivia ','Bologna','Bolton',
'Botafogo','Bourg en Bresse','Bournemouth','Bradford City','Braunschweig','Bray Wanderers','Brazil','Brazil - Women',
'Bremen','Brentford','Brescia ','Brighton','Brisbane Roar','Bristol City','Bristol Rovers','Brøndby IF','BSC Young Boys',
'Bucaramanga','Bulgaria ','Burnley','Bursaspor','Burton Albion','Bury','C. Tokyo','C. United','CA Osasuna','Cádiz CF',
'Cagliari','Cambridge Utd','Cameroon ','Canada','Canada - Women','Cardiff City','Carl Zeiss Jena','Carlisle United',
'Carpi ','Católica','CD Antofagasta','CD Huachipato','CD Leganés','CD Lugo','CD Numancia','CD O\'Higgins','CD Palestino',
'CD Tenerife','Celtic','Central Coast','Cerezo Osaka','Cesena ','CF Reus','Chamois FC','Chapecoense','Charleroi','Charlton Ath'
,'Chaves','Chelsea','Cheltenham Town','Chemnitzer FC','Chesterfield','Chiavari ','Chicago Fire','Chievo Verona','Chile ',
'China PR','China PR - Women','Cittadella ','Clermont Foot','Club Brugge','Colchester','Colombia ','Colón','Colorado Rapids',
'Columbus Crew SC','Concepción','Consa.Sapporo','Córdoba CF','Coritiba','Cork City','Cortuluá','Côte d\'Ivoire ','Coventry City',
'Cracovia','Crawley Town','Cremona ','Crewe Alexandra','Crotone','Cruz Azul','Cruzeiro','Crystal Palace','CSKA Moscow',
'Cultural Leonesa','Curicó Unido','Czech Republic','Daegu FC','Darmstadt','de Chile','Defensa','Denmark','Deportes Temuco',
'Deportes Tolima','Deportivo Cali','Deportivo Pasto','Derby County','Derry City','Dijon FCO','Dinamo Moscow','Djurgårdens IF',
'Doncaster','Dortmund','Dresden','Drogheda United','Duisburg','Dundalk','Dundee FC','Düsseldorf','EA Guingamp','Ecuador ',
'Egypt ','Empoli','England','England - Women','Envigado','ESTAC Troyes','Estoril Praia','Estudiantes','Ettifaq FC','Everton',
'Everton de Viña','Excel Mouscron','Excelsior','Exeter City','FC Barcelona','FC Barcelona "B"','FC Basel','FC Dallas',
'FC Groningen','FC Helsingør','FC København','FC Krasnodar','FC Lausanne-Sport','FC Lorient','FC Lugano','FC Luzern','FC Magdeburg',
'FC Metz','FC Midtjylland','FC Nantes','FC Nordsjælland','FC Porto','FC Rostov','FC Seoul','FC Sion','FC St. Gallen',
'FC Thun','FC Tosno','FC Twente','FC Ufa','FC Ural','FC Utrecht','FC Zürich','FCSM','Fenerbahçe','Feyenoord','Finland ',
'Finn Harps','Fiorentina','FK Austria Wien','FK Haugesund','Fleetwood Town','Fluminense','Foggia ','Forest Green',
'Fortuna Köln','France','France - Women','Frankfurt','Freiburg','Frosinone ','FSV Zwickau','Fulham','Fürth','Galatasaray',
'Galway United','Gamba Osaka','Gangwon FC','Gazélec Ajaccio','Gençlerbirligi','Genoa','Germany','Germany - Women','Getafe CF',
'GIF Sundsvall','Gillingham','Gimnasia','Girona FC','Girondins de Bx','Godoy Cruz','Górnik Zabrze','Göztepe','Granada CF',
'Grasshopper Club','Greece','Grêmio','Grimsby Town','Großaspach','Guadalajara','Guimarães','GwangJu FC','Hallescher FC',
'Halmstads BK','Hamburg','Hamilton','Hammarby IF','Hannover','Hansa Rostock','Havre AC','Hearts','Heidenheim','Hellas Verona',
'Heracles Almelo','Hibernian','HJK Helsinki','Hobro IK','Hoffenheim','Houston Dynamo','Huddersfield','Hull City','Hungary ',
'Huracán','Iceland','IF Elfsborg','IFK Göteborg','IFK Norrköping','IK Sirius','Impact Montréal','Incheon United','Independiente',
'India ','Ingolstadt','Inter','Ipswich','Iquique','Ireland','Italy','Italy - Women','Jagiellonia','Jaguares','Jeju United',
'Jeonbuk Hyundai','Jeonnam Dragons','Johnstone','J-Södra','Júbilo Iwata','Junior','Juventus','KAA Gent','Kaiserslautern',
'Kaizer Chiefs','Kalmar FF','Karabükspor','Karlsruher SC','KAS Eupen','Kashima Antlers','Kashiwa Reysol','Kasimpasa',
'Kawasaki-F','Kayserispor','Kiel','Kilmarnock','Köln','Konyaspor','Korona Kielce','KRC Genk','Kristiansund','KV Kortrijk','KV Mechelen',
'KV Oostende','La Berrichonne','La Equidad','LA Galaxy','La Spezia ','Lanús','LASK Linz','Lazio','Lech Poznan','Lechia Gdansk',
'Leeds United','Legia Warszawa','Leicester City','Leipzig','León','Levante UD','Leverkusen','LIGA NOS','Lillestrøm SK','Limerick FC',
'Lincoln City','Liverpool','Lobos','Lokeren','Lokomotiv Moscow','Lorca FC','LOSC Lille','Luton Town','Lyngby BK','Mainz',
'Málaga CF','Malmö FF','Manchester City','Manchester Utd','Mansfield Town','Marítimo','Medellín','Melbourne City','Mexico',
'Mexico - Women','M\'gladbach','Middlesbrough','Milan','Millonarios','Millwall','Minnesota United','MK Dons','MLS All Stars ',
'Molde FK','Monarcas Morelia','Monterrey','Montpellier HSC','Morecambe','Moreirense','Motherwell','N.A.M.','NAC Breda','Nacional',
'Napoli','Nàstic','Necaxa','Netherlands','Netherlands - Women','New England','New York City FC','New Zealand','New Zealand - Women',
'Newcastle Jets','Newcastle Utd','Newell\'s','Newport County','Nîmes Olympique','Northampton','Northern Ireland','Norway',
'Norway - Women','Norwich','Nott\'m Forest','Notts County','Novara ','Nürnberg','NY Red Bulls','Odds BK','Odense BK',
'OGC Nice','Ohod Club','OL','Oldham Athletic','Olimpo','Olympiacos CFP','OM','Omiya Ardija','Once Caldas','Örebro SK',
'Orlando City','Orlando Pirates','Osmanlispor','Östersunds FK','Oviedo','Oxford United','Pachuca','Paços Ferreira','Palermo ',
'Palmeiras','Panathinaikos','PAOK','Paraguay ','Paranaense','Paris','Paris FC','Parma ','Partick Thistle','Patriotas','Patronato',
'Pats','Pauli','PEC Zwolle','Perth Glory','Peru ','Perugia ','Pescara','Peterborough','Petrolera','Philadelphia','Phoenix',
'Piast Gliwice','Plymouth Argyle','Pogon Szczecin','Pohang Steelers','Poland','Ponte Preta','Port Vale','Portimão','Portland Timbers',
'Portsmouth','Portugal','Preston','Preußen Münster','PSV','Puebla','QPR','Querétaro','Quevilly Rouen','Racing Club','Randers FC',
'Rangers','Rayo Vallecano','RB Salzburg','RC Celta','RC Deportivo','RC Lens','RC Strasbourg','RCD Espanyol','Reading','Real Betis',
'Real Madrid','Real Salt Lake','Real Sociedad','Regensburg','Rio Ave','Rionegro Águilas','River Plate','Rochdale','Roda JC',
'Roma','Romania','Rosario Central','Rosenborg BK','Ross County','Rotherham Utd','Rot-Weiß Erfurt','Royal Antwerp FC','RSC Anderlecht',
'Rubin Kazan','Russia','Sagan Tosu''Salerno ','Sampdoria','San Lorenzo','San Luis','San Martín','Sandecja','Sandefjord','Sandhausen',
'Sangju Sangmu','Santa Fe','Santa Maria','Santos','Santos Laguna','São Paulo','Sarpsborg 08 FF','Sassuolo','Saudi Arabia',
'SC Braga','SC Heerenveen','SC Paderborn','Schalke','Scotland','SCR Altach','Scunthorpe Utd','SD Eibar','SD Huesca','Seattle Sounders',
'Setúbal','Sevilla Atlético','Sevilla FC','Shakhtar Donetsk','Shamrock Rovers','Sheffield Utd','Sheffield Wed','Shimizu S-Pulse',
'S-Hiroshima','Shrewsbury','Silkeborg IF','Sint-Truiden','Sivasspor','SJ Earthquakes','SK Brann','SK Rapid Wien','SK Sturm Graz',
'SKA-Khabarovsk','SKN St. Pölten','SL Benfica','Slask Wroclaw','Sligo Rovers','Slovenia ','SM Caen','Sogndal Fotball','SønderjyskE',
'South Africa ','Southampton','Southend United','Spain','Spain - Women','SPAL','Sparta Praha','Sparta Rotterdam','Spartak Moscow',
'Sport','Sportfreunde Lotte','Sporting','Sporting CP','Sporting KC','Spurs','Stabæk Fotball','Stade Brestois','Stade de Reims',
'Stade Rennais','Standard Liège','Stevenage','Stoke City','Strømsgodset IF','Stuttgart','Sunderland','Suwon Samsung','SV Mattersburg',
'SV Meppen','SV Wehen','Swansea City','Sweden','Sweden - Women','Swindon Town','Switzerland ','Sydney FC','Talleres','Temperley',
'Termalica','Terni ','Tigre','Tigres Dimayor','Tigres','Tijuana','Toluca','Tondela','Torino','Toronto FC','Toulouse FC',
'Tours FC','Trabzonspor','Tromsø IL','Turkey','UD Almería','UD Las Palmas','Udinese','Ulsan Hyundai','Unión','Union Berlin',
'Unión Española','United States','United States - Women','Unterhaching','Urawa Reds','Uruguay ','US Orléans','Valencia CF',
'Valenciennes FC','Vålerenga Fotball','Valladolid CF','Vegalta Sendai','Vélez Sarsfield','Venezia ','Venezuela ','Ventforet Kofu',
'Veracruz','Vercelli ','VfL Osnabrück','VfR Aalen','Victory','Viking FK','Vila das Aves','Villa Maipú','Villarreal CF','Vissel Kobe',
'Vitesse','Vitória','VVV-Venlo','Wales','Walsall','Wanderers','Watford','Werder Bremen II','West Brom','West Ham','Whitecaps FC',
'Wigan Athletic','Willem II','Wisla Kraków','Wisla Plock','Wolfsberger AC','Wolfsburg','Wolves','World XI ','WS Wanderers',
'Würzburg','Wycombe','Yeni Malatyaspor','Yeovil Town','Yokohama','Zaglebie Lubin','Zaragoza','Zenit','Zulte-Waregem']

NameList = ['Panos','David']


class AutocompleteEntry(Entry):
    def __init__(self, Teamlist, *args, **kwargs):

        Entry.__init__(self, *args, **kwargs,font="Helvetica 8 bold")
        self.Teamlist = Teamlist
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.lb_up = True

                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*',re.IGNORECASE)
        return [w for w in self.Teamlist if re.match(pattern, w)]


class AutocompleteEntryNames(Entry):
    def __init__(self, NameList, *args, **kwargs):

        Entry.__init__(self, *args, **kwargs,font="Helvetica 8 bold")
        self.NameList = NameList
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.lb_up = True

                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)
    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*',re.IGNORECASE)
        return [w for w in self.NameList if re.match(pattern, w)]


def show_entry_fields():
   print("%s vs %s: %s:%s" % (e1.get(), e2.get(), e3.get(), e4.get()))


def save_data():
    list = [e1.get(),e5.get(),e3.get(),e2.get(),e6.get(),e4.get()]
    try:
        with open("C:/Users/Panagiotis.Pantazis/Documents/Python Scripts/Stat Tracker/ScoreTracking.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(list)
            tk.messagebox.showinfo("Saving Prompt", "Successfully Saved Result")
    except:
        tk.messagebox.showinfo("Saving Prompt", "Failed To Save Result")


def calculategoals():
    # Read Tracker
    df = pd.read_csv("C:/Users/Panagiotis.Pantazis/Documents/Python Scripts/Stat Tracker/ScoreTracking.csv", header=0,encoding='ANSI')

    # Create base 1 index
    df['Index'] = range(1, len(df) + 1)

    # Create new columns
    df['Player A Wins'] = np.where(df['Player A Goals'] > df['Player B Goals'], 1, 0)
    df['Player B Wins'] = np.where(df['Player B Goals'] > df['Player A Goals'], 1, 0)
    df['Game Ends in Draw'] = np.where(df['Player A Goals'] == df['Player B Goals'], 1, 0)

    # Create cumulative sum columns
    Columns = ['Player A Goals', 'Player B Goals']
    for each in Columns:
        df['Cumulative' + each] = df[each].cumsum(axis=0)

    # Plot Cumulative Goals
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    ax.plot(df['Index'], df['CumulativePlayer A Goals'], label="Player A Cumulative Goals")
    ax.plot(df['Index'], df['CumulativePlayer B Goals'], label="Player B Cumulative Goals")
    plt.xlabel("Games Played")
    plt.ylabel("Goals Scored")
    loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    ax.legend(prop={'size': 8})
    plt.show()


def calculatwins():
    df = pd.read_csv("C:/Users/Panagiotis.Pantazis/Documents/Python Scripts/Stat Tracker/ScoreTracking.csv", header=0,
                     encoding='ANSI')

    # Create base 1 index
    df['Index'] = range(1, len(df) + 1)

    # Create new columns
    df['Player A Wins'] = np.where(df['Player A Goals'] > df['Player B Goals'], 1, 0)
    df['Player B Wins'] = np.where(df['Player B Goals'] > df['Player A Goals'], 1, 0)
    df['Game Ends in Draw'] = np.where(df['Player A Goals'] == df['Player B Goals'], 1, 0)

    # Create cumulative sum columns
    Columns = ['Player A Goals', 'Player B Goals']
    for each in Columns:
        df['Cumulative' + each] = df[each].cumsum(axis=0)

    Columns = ['Player A Wins', 'Player B Wins', 'Game Ends in Draw']
    for each in Columns:
        df['Cumulative' + each] = df[each].cumsum(axis=0)

    f, ax = plt.subplots(1, figsize=(10, 5))

    # Set bar width at 1
    bar_width = 1

    # positions of the left bar-boundaries
    bar_l = [i for i in range(len(df['Index']))]

    # positions of the x-axis ticks (center of the bars as bar labels)
    tick_pos = [i for i in bar_l]

    totals = [i + j + k for i, j, k in
              zip(df['CumulativePlayer A Wins'], df['CumulativePlayer B Wins'], df['CumulativeGame Ends in Draw'])]
    pre_rel = [i / j * 100 for i, j in zip(df['CumulativePlayer A Wins'], totals)]
    mid_rel = [i / j * 100 for i, j in zip(df['CumulativePlayer B Wins'], totals)]
    post_rel = [i / j * 100 for i, j in zip(df['CumulativeGame Ends in Draw'], totals)]

    # Create a bar chart in position bar_1
    ax1 = ax.bar(bar_l,
                 # using pre_rel data
                 pre_rel,
                 # labeled
                 label='Player A Wins',
                 # with alpha
                 alpha=0.9,
                 # with color
                 color='#191970',
                 # with bar width
                 width=bar_width,
                 # with border color
                 edgecolor='white'
                 )

    # Create a bar chart in position bar_1
    ax2 = ax.bar(bar_l,
                 # using mid_rel data
                 mid_rel,
                 # with pre_rel
                 bottom=pre_rel,
                 # labeled
                 label='Player B Wins',
                 # with alpha
                 alpha=0.9,
                 # with color
                 color='#b22222',
                 # with bar width
                 width=bar_width,
                 # with border color
                 edgecolor='white'
                 )

    # Create a bar chart in position bar_1
    ax3 = ax.bar(bar_l,
                 # using post_rel data
                 post_rel,
                 # with pre_rel and mid_rel on bottom
                 bottom=[i + j for i, j in zip(pre_rel, mid_rel)],
                 # labeled
                 label='Draws',
                 # with alpha
                 alpha=0.9,
                 # with color
                 color='#708090',
                 # with bar width
                 width=bar_width,
                 # with border color
                 edgecolor='white'
                 )

    for i, (r1, r2, r3) in enumerate(zip(ax1, ax2, ax3)):
        h1 = r1.get_height()
        h2 = r2.get_height()
        h3 = r3.get_height()
        ax1values = round((i + 1) * h1 / 100)
        ax2values = round((i + 1) * h2 / 100)
        ax3values = round((i + 1) * h3 / 100)
        if ax1values != 0:
            plt.text(r1.get_x() + r1.get_width() / 2.
                     , h1 / 2.
                     , "%d" % ax1values
                     , ha="center"
                     , va="center"
                     , color="white"
                     , fontsize=12
                     , fontweight="bold")
        if ax2values != 0:
            plt.text(r2.get_x() + r2.get_width() / 2.
                     , h1 + h2 / 2.
                     , "%d" % ax2values
                     , ha="center"
                     , va="center"
                     , color="white"
                     , fontsize=12
                     , fontweight="bold")
        if ax3values != 0:
            plt.text(r3.get_x() + r3.get_width() / 2.
                     , h1 + h2 + h3 / 2.
                     , "%d" % ax3values
                     , ha="center"
                     , va="center"
                     , color="white"
                     , fontsize=12
                     , fontweight="bold")

    # Set the ticks to be first names
    plt.xticks(tick_pos, df['Index'])
    ax.set_ylabel("Percentage")
    ax.set_xlabel("Games Played")

    plt.legend(bbox_to_anchor=(0.05, 1.02, 1, .2), loc="lower left", ncol=3)

    plt.show()


def validate(string):
    regex = re.compile(r"(\+|\-)?[0-9,]*$")
    result = regex.match(string)
    return (string == ""
            or (string.count('+') <= 1
                and string.count('-') <= 1
                and string.count(',') <= 1
                and result is not None
                and result.group(0) != ""))


def on_validate(P):
    return validate(P)


def raise_frame(frame):
    frame.tkraise()

def userlist():
    df = pd.read_csv("C:/Users/Panagiotis.Pantazis/Documents/Python Scripts/Stat Tracker/ScoreTracking.csv")


if __name__ == '__main__':
    master = tk.Tk()
    f1 = Frame(master)
    f2 = Frame(master)

    for frame in (f1, f2):
        frame.grid(row=0, column=0, sticky='news')

    tkFont.Font(family="Helvetica", size=8)

    background_image = tk.PhotoImage(file="C:/Users/Panagiotis.Pantazis/Documents/Python Scripts/Stat Tracker/SoccerPitch2.png")
    background_label = tk.Label(f1, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(f1, text="Player A Name", font="Helvetica 8 bold italic").grid(row=1, column=1, padx=5, pady=(5,2))
    Label(f1, text="Player A Team", font="Helvetica 8 bold italic").grid(row=2, column=1, padx=5, pady=2)
    Label(f1, text="Player A Goals", font="Helvetica 8 bold italic").grid(row=3, column=1, padx=5, pady=2)

    Label(f1, text="Player B Name", font="Helvetica 8 bold italic").grid(row=1, column=3, padx=5, pady=(5,2))
    Label(f1, text="Player B Team", font="Helvetica 8 bold italic").grid(row=2, column=3, padx=5, pady=2)
    Label(f1, text="Player B Goals", font="Helvetica 8 bold italic").grid(row=3, column=3, padx=5, pady=2)

    e1 = AutocompleteEntry(Teamlist, f1)
    e2 = AutocompleteEntry(Teamlist, f1)

    e3 = Entry(f1, validate="key", font="Helvetica 8 bold")
    e3.insert(END, '0')
    vcmd = (e3.register(on_validate), '%P')
    e3.config(validatecommand=vcmd)

    e4 = Entry(f1, validate="key", font="Helvetica 8 bold")
    e4.insert(END, '0')
    vcmd = (e4.register(on_validate), '%P')
    e4.config(validatecommand=vcmd)

    e5 = AutocompleteEntryNames(NameList, f1)
    e6 = AutocompleteEntryNames(NameList, f1)

    e1.grid(row=2, column=2, padx=5, pady=2)
    e2.grid(row=2, column=4, padx=5, pady=2)
    e3.grid(row=3, column=2, padx=5, pady=2)
    e4.grid(row=3, column=4, padx=5, pady=2)
    e5.grid(row=1, column=2, padx=5, pady=(5,2))
    e6.grid(row=1, column=4, padx=5, pady=(5,2))

    Button(f1, text='Exit', command=master.quit).grid(row=5, column=1, sticky=N, pady=(5,2))
    Button(f1, text='Save Score', command=save_data).grid(row=5, column=4, sticky=N, pady=(5,2))
    Button(f1, text='Goal History', command=calculategoals).grid(row=7, column=1, sticky=N, pady=(2,2))
    Button(f1, text='Win History', command=calculatwins).grid(row=7, column=4, sticky=N, pady=(2,2))

    Button(f1, text='Go to frame 2', command=lambda: raise_frame(f2)).grid(row=8, column=1, sticky=N, pady=(5,2))
    Label(f1, text='FRAME 1').grid(row=8, column=2, sticky=N, pady=(5,2))

    Label(f2,text='Welcome to Stat Tracker BETA\nSelect your user below and start recording your FIFA stats').pack(pady=10)


    Label(f2, text='Select User').pack(pady=10)
    variable = StringVar(f2)
    variable.set("Panos")  # default value
    list = ["Panos", "David"]
    w = OptionMenu(f2, variable, *list)
    w.pack()




    raise_frame(f1)

    master.mainloop()
