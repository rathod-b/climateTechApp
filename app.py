# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_cytoscape as cyto

# Load file with all countries, only once
def loadData():    
    ## Read main data file
    x = pd.read_csv('assets//input_1.csv',index_col=0)
    return x

# Create DF with selected countries, All not in Filt.
# Return list of countries and DF with all climate tech for the selection
# On first run this is provided an 'All'
def filterInputDF(x, filt='All'):
    
    if filt == []:
        print('Received empty country filter, doing nothing.')
        allTechDF = ''
        countries = ''
    elif 'All' not in filt:
        # Dealing with a list of countries
        # Based on input just create a list of countries, then remove duplicates and run after that
        
        fullList1 = []
        fullList2 = []
        fullList3 = []
        fullList4 = []
        mainList = []
        key = 0
        if 'LDCs' in filt:
            fullList1 = filt + LDCs
            fullList1.remove('LDCs')
            key = 1
            print(filt, LDCs, fullList1)
        if 'SIDS' in filt:
            filt.remove('SIDS')
            fullList2 = filt + SIDS
            key = 1
        if 'Africa' in filt:
            filt.remove('Africa')
            fullList3 = filt + Afr
            key = 1
        if 'G77' in filt:
            filt.remove('G77')
            fullList4 = filt + G77
            key = 1
        
        if key:
            # Append all lists into 1, then find unique values.
            mainList = fullList1 + fullList2 + fullList3 + fullList4
            mainList = list(dict.fromkeys(mainList))
        else:
            mainList = filt

        print('Filtering dataset for countries: {}'.format(', '.join(mainList)))

        DFs = []
        for c in mainList:
            x1 = x.loc[x['Country']==c]
            DFs.append(x1)
        allTechDF = pd.concat(DFs)
        countries = mainList
    else:
        # 'All' in filt.
        allTechDF = x
        countries = allTechDF['Country'].unique()
    
    return allTechDF, countries

def createFilterLists(countries):
    LDCs = ['Afghanistan','Angola','Bangladesh','Benin','Bhutan','Burkina Faso','Burundi',\
        'Cambodia','Central African Republic','Chad','Comoros','Congo DRC','Djibouti',\
        'Eritrea','Ethiopia','Gambia','Guinea','Guinea-Bissau','Haiti','Kiribati',\
        'Lao People’s Democratic Republic','Lesotho','Liberia','Madagascar','Malawi',\
        'Mali','Mauritania','Mozambique','Myanmar','Nepal','Niger','Rwanda',\
        'Sao Tome and Principe','Senegal','Sierra Leone','Solomon Islands','Somalia',\
        'South Sudan','Sudan','Timor-Leste','Togo','Tuvalu','Uganda','United Republic of Tanzania','Yemen','Zambia']

    SIDS = ['Antigua and Barbuda','Guyana','Singapore','Bahamas','Haiti ','StKitts and Nevis','Bahrain','Jamaica','StLucia',\
            'Barbados','Kiribati','StVincent and the Grenadines','Belize','Maldives','Seychelles','Cabo Verde','Marshall Islands',\
            'Solomon Islands','Comoros','Federated States of Micronesia','Suriname','Cuba','Mauritius','Timor-Leste ','Dominica',\
            'Nauru','Tonga','Dominican Republic','Palau','Trinidad and Tobago','Fiji','Papua New Guinea','Tuvalu','Grenada',\
            'Samoa','Vanuatu','Guinea-Bissau','Sao Tome and Principe']

    Afr = ['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon','Cabo Verde','Central African Republic',\
           'Chad','Comoros','Congo','Congo DRC','Cote d’Ivoire','Djibouti','Equatorial Guinea','Egypt',\
           'Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau. Kenya','the Kingdom of Lesotho','Liberia',\
           'Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria',\
           'Rwanda','Saharawi Arab Democratic Republic','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia',\
           'South Africa','South Sudan','Sudan','Kingdom of Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']

    G77 = ['Afghanistan','Algeria','Angola','Antigua and Barbuda','Argentina','Azerbaijan','Bahamas','Bahrain','Bangladesh',\
           'Barbados','Belize','Benin','Bhutan','Bolivia','Botswana','Brazil','Brunei Darussalam',\
           'Burkina Faso','Burundi','Cabo Verde','Cambodia','Cameroon','Central African Republic','Chad','Chile','China',\
           'Colombia','Comoros','Congo','Costa Rica','Côte d\'Ivoire','Cuba','Democratic People\'s Republic of Korea',\
           'Congo DRC','Djibouti','Dominica','DominicanRepublic','Ecuador','Egypt','El Salvador',\
           'Equatorial Guinea','Eritrea','Eswatini','Ethiopia','Fiji','Gabon','Gambia','Ghana','Grenada','Guatemala','Guinea',\
           'Guinea-Bissau','Guyana','Haiti','Honduras','India','Indonesia','Iran','Iraq','Jamaica','Jordan',\
           'Kenya','Kiribati','Kuwait','Laos','Lebanon','Lesotho','Liberia','Libya','Madagascar',\
           'Malawi','Malaysia','Maldives','Mali','Marshall Islands','Mauritania','Mauritius','Micronesia (Federated States of)',\
           'Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Nicaragua','Niger','Nigeria','Oman','Pakistan',\
           'Panama','Papua New Guinea','Paraguay','Peru','Philippines','Qatar','Rwanda','Saint Kitts and Nevis','Saint Lucia',\
           'Saint Vincent and the Grenadines','Samoa','Sao Tome and Principe','Saudi Arabia','Senegal','Seychelles','Sierra Leone',\
           'Singapore','Solomon Islands','Somalia','South Africa','South Sudan','Sri Lanka','State of Palestine','Sudan',\
           'Suriname','Syrian Arab Republic','Tajikistan','Thailand','Timor-Leste','Togo','Tonga','Trinidad and Tobago','Tunisia',\
           'Turkmenistan','Uganda','United Arab Emirates','United Republic of Tanzania','Uruguay','Vanuatu',\
           'Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']
    
    for c in LDCs:
        if c not in countries:
            print('Removing LDC ', c)
            LDCs.remove(c)
    print('\n')
    for d in SIDS:
        if d not in countries:
            print('Removing SIDS ', d)
            if d in SIDS:
                SIDS.remove(d)
            else:
                print(d)
    print('\n')
    for e in Afr:
        if e not in countries:
            print('Removing African country ', e)
            Afr.remove(e)
    print('\n')
    for f in G77:
        if f not in countries:
            print('Removing G77 ', f)
            G77.remove(f)
    
    return LDCs, SIDS, Afr, G77

def handleUndef(allTechDF,countries):
    # How many undefined values exist in this filtered set of data?
    # Lets filter them out
    undefCount = allTechDF.loc[allTechDF['INDC technology']=='UNDEFINED'].shape[0]
    print('# of rows with undefined INDC technology is ', undefCount)
    # Create separate DFs for undefined technologies and defined technologies
    countryDF = allTechDF.loc[allTechDF['INDC technology']!='UNDEFINED']
    undefDF = allTechDF.loc[allTechDF['INDC technology']=='UNDEFINED']
    
    return undefDF,countryDF

def determineRelationships(countryDF, countries):
    # Create a DF that holds all unique technology combinations by country, their occurence count, and countries that deploy
    # that pair
    keyList = []
    tech1 = []
    tech2 = []
    country = []
    frequency = []

    for c in countries:

        # filter by each country
        tempDF = countryDF.loc[countryDF['Country']==c]

        # pick their technology needs
        techNeeds = list(tempDF['INDC technology'])

        for r in range(len(techNeeds)):
            if r != len(techNeeds)-1:
                key = str(techNeeds[r]+'&&'+str(techNeeds[r+1]))
                if key not in keyList:
                    # New combination, add to lists
                    keyList.append(key)
                    tech1.append(tempDF.iloc[r,3])
                    tech2.append(tempDF.iloc[r+1,3])
                    frequency.append(1)
                    country.append(c)
                else:
                    # Key exists so get its index and add 1 to frequency.
                    ind = keyList.index(key)
                    frequency[ind] += 1
                    print('Found a duplicate at index {} for country {}'.format(r,c))

    ## Create a pandas DF with compiled information.
    d = {'T1':tech1,'T2':tech2,'key':keyList,'Freq':frequency,'Country':country}
    techDF = pd.DataFrame(d)
#     techDF.to_csv('techDF.csv')
    
    return techDF

# Count the occurence of each technology in the filtered DF.
def techCountFunc(uniqueTech,cTechnologies):
    tech = []
    count = []
    for t in uniqueTech:
        tech.append(t)
        count.append(cTechnologies.count(t))
    dat = {'tech':tech,'count':count}
    techCount = pd.DataFrame(dat)
    return techCount

def getCount(node,x):
    try:
        return x.loc[x['tech']==node,'count']
    except:
        print('Had trouble getting count for this node: ', node)
        return 1

def createCyto(techDF,techCount,uniqueTech):
    
    edges = techDF['key'].tolist()

    nodes = set()

    cy_edges = []
    cy_nodes = []

    count = -1
    for network_edge in edges:
        count += 1

        source, target = network_edge.split("&&")[0], network_edge.split("&&")[1]

        if source not in nodes:
            nCount = getCount(source,techCount)
            nHeight = nCount*1.1
            nWidth = nCount*1.1
            if source in uniqueTech:
                nodes.add(source)
                cy_nodes.append({
                    "data":{
                        "id": source,
                        "label": source,
                        'ht':nHeight+12,
                        'wd':nWidth+12
                    }
                })
            else:
                print(source)
                nodes.add(source)
                cy_nodes.append({
                    "data":{
                        "id": source,
                        "label": source,
                        'ht':nHeight+12,
                        'wd':nWidth+12
                    }
                })

        if target not in nodes:
            nCount = getCount(target,techCount)
            nHeight = nCount*1.1
            nWidth = nCount*1.1
            if target in uniqueTech:
                nodes.add(target)
                cy_nodes.append({
                    "data":{
                        "id": target,
                        "label": target,
                        'ht':nHeight+12,
                        'wd':nWidth+12
                    }
                })
            else:
                print(target)
                nodes.add(target)
                cy_nodes.append({
                    "data":{
                        "id": target,
                        "label": target,
                        'ht':nHeight+12,
                        'wd':nWidth+12
                    }
                })

        freq = techDF.iloc[count,3]
        cy_edges.append({
            'data': {
                'source': source,
                'target': target,
                'weight':freq
            }
        })
    
    return cy_edges, cy_nodes

def createDropdownVals(countries):
    
    listAll = []
    for c in countries:
        tD = dict()
        tD['label']=c
        tD['value']=c
        listAll.append(tD)
    
    allDict = dict()
    allDict['label'] = 'All'
    allDict['value'] = 'All'
    listAll.append(allDict)
    
    ldcDict = dict()
    ldcDict['label'] = 'LDCs'
    ldcDict['value'] = 'LDCs'
    listAll.append(ldcDict)
    
    afrDict = dict()
    afrDict['label'] = 'Africa'
    afrDict['value'] = 'Africa'
    listAll.append(afrDict)
    
    sidsDict = dict()
    sidsDict['label'] = 'SIDS'
    sidsDict['value'] = 'SIDS'
    listAll.append(sidsDict)
    
    g77Dict = dict()
    g77Dict['label'] = 'G77'
    g77Dict['value'] = 'G77'
    listAll.append(g77Dict)
    
    return listAll

def createDropdownVals_tech(uniqueTech):
    
    listAllTech = []
    for t in uniqueTech:
        tD = dict()
        tD['label']=t
        tD['value']=t
        listAllTech.append(tD)
    
    allDict = dict()
    allDict['label'] = 'All'
    allDict['value'] = 'All'
    listAllTech.append(allDict)
    
    return listAllTech

# Initialize
def init():
    inputDF = loadData()
    allTechDF, countries = filterInputDF(inputDF, filt='All')
    LDCs, SIDS, Afr, G77 = createFilterLists(countries)
    undefDF,countryDF = handleUndef(allTechDF,countries)
    techDF = determineRelationships(countryDF, countries)
    # Some processing of series
    listAll = createDropdownVals(countries)
    
    uniqueTech = countryDF['INDC technology'].unique()
    listAllTech = createDropdownVals_tech(uniqueTech)
    
    return inputDF, LDCs, SIDS, Afr, G77, undefDF, countryDF, techDF, listAll, listAllTech

def sortTechCounts(techCount,ascendTF=True):

    # Sort
    sortedTechDf = techCount.sort_values(by='count',ascending=ascendTF)
    sortedTechDfDict = sortedTechDf.to_dict('records')
    
    return sortedTechDfDict

def getInnovation(techCount):
    indToDrop = []
    for r in range(techCount.shape[0]):
        if '*' not in techCount.iloc[r,0]:
            indToDrop.append(r)
    innovation = techCount.drop(index=indToDrop).to_dict('records')
    return innovation

def getUndefinedCategories(undefDF):
    # Create lists for holding values.
    undefCat = []
    undefCtr = []

    # Create a DF with just categories and country names
    for cat in undefDF['Category'].unique():
        # Add category value in the list
        undefCat.append(cat)
        # Add country in the list
        x = list(set(undefDF.loc[undefDF['Category']==cat,'Country'].values.tolist()))
        ctrToAdd = ', '.join(x)
        undefCtr.append(ctrToAdd)
    data = {'Category': undefCat, 'Countries':undefCtr}
    undCats = pd.DataFrame(data)
    undCatsDict = undCats.to_dict('records')
    
    return undCats, undCatsDict

def getUndefinedSectors(undefDF):
    undefSct = []
    undefCtr = []

    # Remove any rows where INDC sector is 0 as these values were NaN before.
    undefDF_1 = undefDF.loc[undefDF['INDC Sector']!='0']

    # For all leftover values, get the values and their countries.
    for sect in undefDF_1['INDC Sector'].unique():
        undefSct.append(sect)
        y = list(set(undefDF_1.loc[undefDF_1['INDC Sector']==sect,'Country'].values.tolist()))
        ctrToAdd = ', '.join(y)
        undefCtr.append(ctrToAdd)
    data = {'Sector':undefSct, 'Countries':undefCtr}
    undSect = pd.DataFrame(data)
    undSectDict = undSect.to_dict('rows')
    
    return undSect, undSectDict

def expandSelection(t):

    ctrs = []

    if 'LDCs' in t:
        ctrs = ctrs + LDCs
    if 'SIDS' in t:
        ctrs = ctrs + SIDS
    if 'Africa' in t:
        ctrs = ctrs + Afr
    if 'G77' in t:
        ctrs = ctrs + G77
    ctrs = ctrs + t
    
    return list(set(ctrs))

# ************************* App begins here ********************************* #
inputDF, LDCs, SIDS, Afr, G77, undefDF, countryDF, techDF, listAll, listAllTech = init()

app = dash.Dash(__name__)
app.title = "NDC Technology Needs Landscape"

default_stylesheet = [
    {
        "selector": 'node',
        'style': {
            'background-color':'white',
            'border-color': 'black',
            "border-width": 1,
            "border-opacity": 1,
            "opacity": 1,
            'width':'data(wd)',
            'height':'data(ht)',
            'label': 'data(label)',
            'text-wrap':'wrap',
            'text-max-width':'125px'
        }
    },
    {
        "selector": 'edge',
        'style': {
            "opacity": 0.75,
            'width':0.25
        }
    },
]

app.layout = html.Div(className = 'app-container', children=[
    
    html.Div(className='app-markdown',children=[
        dcc.Markdown('''
        # Climate Technology Landscape
                
        This application is the result of a collaborative effort by graduate students at the School for Environment and Sustainability, University of Michigan and the Climate Technology Centre & Network. The app illustrates the climate technology needs, trends, and gaps of non-Annex I countries of the Paris Agreement’s Nationally Determined Contribution (NDC) Plans submitted after January 1st, 2016. The countries included are all Least Developed Countries (LDCs), Small Island Developing States (SIDs), Africa, with the inclusion of some G77 (Group of 77) countries, excluding China. Climate technology needs to help countries reduce their greenhouse gas emissions (GHGs) such as wind, solar, hydropower, and more. Climate technologies also include ‘soft’ technologies such as energy-efficient strategies, practices, and awareness campaigns. 
        For more information on this project, please visit the *[Capstone Project Site.](https://sites.google.com/umich.edu/ctcnmsproj/home)*
        
        ## How to use this dashboard?
        The application is divided into two sections: Visualization and Download by Technology.
        
        ### Visualization
        The drop-down menu is a multi-value element. This element allows allows a user to select one or more countries and/or country categories (i.e. SIDS, LDCs, Africa) and view:
        - Climate technology interactions for countries/regions selected using the dropdown menu.
        - Download the unconditional and conditional technology needs and TNA prioritizations for selected values (as CSV).
        - View technologies considered innovative by CTCN’s Technology Taxonomy as a list.
        - View (I)NDC Sectors and Categories where contributions are high level and need further elaboration or the CTCN Technology Taxonomy does not have a suitable category for country contribution, labeled as “Undefined”.
        - View a list of prioritized climate technologies and how often they occur.
        - Download a list of technology connections and the strength of these connections (as CSV).
        
        ### Interactivity
        The visual element in this section is interactive in the following ways:
        - Zoom: user is able to zoom in/out to desired sections.
        - Hover actions: when a user hovers on a (node) climate technology, they can see the climate technology update above the visual.
        - View adjacencies: a user can select a specific node to highlight other nodes that are connected to the selection.
        - Drag: a user can drag and drop nodes to improve the visual layout to their liking.

        
        ''')
    ]),
    
    html.Div(className = 'app-country-selector',children=[
        dcc.Dropdown(
            id = 'selectForFig',
            options = listAll,
            value = 'Senegal',
            multi=True
        )
    ]),
    
    html.Div(className='cyto-figure', children=[
        cyto.Cytoscape(
            id='techFig',
            elements = [],
            layout={
                'name': 'grid',
                'nodeDimensionsIncludeLabels': True
            },
            style={
                'background-color': 'white',
                'height': '85vh',
                'width': '100%'
            },
            stylesheet = []
        )
    ]),
    
    html.Div([
        html.H5(id='cytoscape-mouseoverNodeData-output', children=['Hover on a node to view details'])
    ]),
    
    html.Div(className='app-buttons', children=[
        html.Div(className='app-button',children=[
            html.Button("Climate Technologies CSV Download", id="getNDCByCountries"),
            dcc.Download(id="download-getNDCByCountries"),
        ]),
        
        html.Div(className='app-button',children=[
            html.Button("Undefined Technologies CSV Download", id="getUndefRows"),
            dcc.Download(id="download-getUndefRows"),
        ]),
        
        html.Div(className='app-button',children=[
            html.Button("Download Technology Connections", id="getTechDF"),
            dcc.Download(id="download-getTechDF"),
        ]) 
    ]),
    
    html.Details([
        html.Summary('Innovative technologies:'),
        html.Div(children=[
            # items
            dash_table.DataTable(
                id='Innovation',
                columns=[
                    {'name': 'tech', 'id': 'tech'},
                    {'name': 'count', 'id': 'count'}
            ],
            style_as_list_view=True,
            style_cell={
                'padding': '5px',
                'textAlign':'left',
                'font-size':'15px'
            },
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold',
                'textAlign':'left',
                'font-size':'18px'
            },
            export_format = 'csv')
        ])
    ]),
    
    html.Details([
        html.Summary('Countries with undefined categories:'),
        html.Div(children=[
            dash_table.DataTable(
                id='undefCat',
                columns=[
                    {'name': 'Category', 'id': 'Category'},
                    {'name': 'Countries', 'id': 'Countries'}
            ],
            style_as_list_view=True,
            style_cell={
                'padding': '5px',
                'textAlign':'left',
                'font-size':'15px'
            },
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold',
                'textAlign':'left',
                'font-size':'18px'
            },
            export_format = 'csv')
        ])
    ]),
    
    html.Details([
        html.Summary('Countries with undefined sectors'),
        html.Div(children=[
            dash_table.DataTable(
                id='undefSect',
                columns=[
                    {'name': 'Sector', 'id': 'Sector'},
                    {'name': 'Countries', 'id': 'Countries'}
            ],
            style_as_list_view=True,
            style_cell={
                'padding': '5px',
                'textAlign':'left',
                'font-size':'15px'
            },
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold',
                'textAlign':'left',
                'font-size':'18px'
            },
            export_format = 'csv')
        ])
    ]),
        
    html.Details([
        html.Summary('Climate technology highlights counts'),
        # second column of second row
        html.Div(children=[
            # items
            dash_table.DataTable(
                id='technologyCounts',
                columns=[
                {'name': 'tech', 'id': 'tech'},
                {'name': 'count', 'id': 'count'}
            ],
            style_as_list_view=True,
            style_cell={
                'padding': '5px',
                'textAlign':'left',
                'font-size':'15px'
            },
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold',
                'textAlign':'left',
                'font-size':'18px'
            },
            export_format = 'csv')
        ])
    ]),
    
    html.Div(className='app-markdown',children=[
        dcc.Markdown('''
        ## Download information by technology
        
        The drop-down menu is a multi-value element. This element allows a user to select one or more climate technologies and download a CSV file containing mentions of selected technology by all countries.        
        ''')
    ]),
    
    html.Div(children=[
        # items
        dcc.Dropdown(
            id = 'selectForTech',
            options = listAllTech,
            value = 'All',
            multi=True
        ),
        html.Button("Download by Climate Technologies (CSV)", id="getCountriesByTech"),
        dcc.Download(id="download-getCountriesByTech")
    ])
])

# Callback to update the figure.
@app.callback(
    Output('techFig', 'elements'),
    Output('Innovation','data'),
    Output('technologyCounts','data'),
    Output('undefCat','data'),
    Output('undefSect','data'),
    Input('selectForFig', 'value'))
def update_figure(selected_value):
    if selected_value == [] or selected_value == None:
        fig = []
        print('Encountered selected_value of {}.'.format(selected_value))
    else:
        if type(selected_value)==str:
            sVal = []
            sVal.append(selected_value)
        else:
            sVal = selected_value
        print(sVal)
        # This function takes care of 'All' being selected or not
        allTechDF, countries = filterInputDF(inputDF, sVal)
        undefDF,countryDF = handleUndef(allTechDF,countries)
        techDF = determineRelationships(countryDF, countries)
        
        uniqueTech = countryDF['INDC technology'].unique()
        cTechnologies = list(countryDF['INDC technology'])
        
        techCount = techCountFunc(uniqueTech,cTechnologies)
        cy_edges, cy_nodes = createCyto(techDF, techCount, uniqueTech)
        fig = cy_nodes + cy_edges
        
        # View innovative technologies
        innovation = getInnovation(techCount)
        
        # Data table return
        sortedTechDfDict = sortTechCounts(techCount,ascendTF=False)
        
        undCats, undCatsDict = getUndefinedCategories(undefDF)
        undSect, undSectDict = getUndefinedSectors(undefDF)
        
    return fig, innovation, sortedTechDfDict, undCatsDict, undSectDict

# Thanks to https://github.com/plotly/dash-cytoscape/blob/master/usage-stylesheet.py from https://github.com/plotly/dash-cytoscape
@app.callback(Output('techFig', 'stylesheet'),
              [Input('techFig', 'tapNode')])
def generate_stylesheet(node):
    
    if not node:
        return default_stylesheet

    stylesheet = [
        {
            "selector": 'node',
            'style': {
                'background-color':'white',
                'border-color': 'black',
                "border-width": 1,
                "border-opacity": 1,
                "opacity": 1,
                'width':'data(wd)',
                'height':'data(ht)',
                'label': 'data(label)',
                'text-wrap':'wrap',
                'text-max-width':'125px'
            }
        },
        {
            "selector": 'edge',
            'style': {
                "opacity": 0.75,
                'width':0.25
            }
        },
        {
            "selector": 'node[id = "{}"]'.format(node['data']['id']),
            "style": {
                'background-color': '#00274C',
                "border-color": "#00274C",
                "border-width": 2,
                "border-opacity": 1,
                "opacity": 1,
                'width':45,
                'height':45
            }
        }
    ]

    for edge in node['edgesData']:
        if edge['source'] == node['data']['id']:
            stylesheet.append({
                "selector": 'node[id = "{}"]'.format(edge['target']),
                "style": {
                    'background-color': '#00274C',
                    'opacity': 1,
                    'width':15,
                    'height':15
                }
            })
            stylesheet.append({
                "selector": 'edge[id= "{}"]'.format(edge['id']),
                "style": {
                    "line-color": '#FFCB05',
                    'opacity': 1,
                    'width':'data(freq)'
                }
            })

        if edge['target'] == node['data']['id']:
            stylesheet.append({
                "selector": 'node[id = "{}"]'.format(edge['source']),
                "style": {
                    'background-color': '#00274C',
                    'opacity': 1,
                    'width':15,
                    'height':15
                }
            })
            stylesheet.append({
                "selector": 'edge[id= "{}"]'.format(edge['id']),
                "style": {
                    "line-color": '#FFCB05',
                    'opacity': 1,
                    'width':'data(freq)'
                }
            })

    return stylesheet

# Show information on hover.
@app.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
              Input('techFig', 'mouseoverNodeData'))
def displayTapNodeData(data):
    if data:
        return "Technology: " + data['label']
    
# Callback to get countries by chosen NDC technologies
@app.callback(
    Output("download-getNDCByCountries", "data"),
    [Input("getNDCByCountries", "n_clicks")],
    [State('selectForFig','value')],
    prevent_initial_call=True)
def getNDCByCountries(n_clicks,selected_value):
    if n_clicks is not None:
        if 'All' not in selected_value:
            if type(selected_value)==str:
                sVal = []
                sVal.append(selected_value)
            else:
                sVal = selected_value
            sVal = expandSelection(sVal)
            DFs = []
            for c in sVal:
                x1 = inputDF.loc[inputDF['Country']==c]
                DFs.append(x1)
            countryDF = pd.concat(DFs)
        else:
            countryDF = inputDF
        return dcc.send_data_frame(countryDF.to_csv, "NDCcontributions.csv")
    
# Callback to get climate technology rows where undefined values exist for category or sector.
@app.callback(
    Output("download-getUndefRows", "data"),
    [Input("getUndefRows", "n_clicks")],
    [State('selectForFig','value')],
    prevent_initial_call=True)
def getUndefRows(n_clicks,selected_value):
    if n_clicks is not None:
        if selected_value != [] or selected_value != None:
            if type(selected_value)==str:
                sVal = []
                sVal.append(selected_value)
            else:
                sVal = selected_value
            # This function takes care of 'All' being selected or not
            allTechDF, countries = filterInputDF(inputDF,sVal)
            undefDF,countryDF = handleUndef(allTechDF,countries)
            return dcc.send_data_frame(undefDF.to_csv, "UndefinedContributions.csv")
        
# Callback to get countries by chosen NDC technologies
@app.callback(
    Output("download-getTechDF", "data"),
    [Input("getTechDF", "n_clicks")],
    [State('selectForFig','value')],
    prevent_initial_call=True)
def getTechDF(n_clicks,selected_value):
    if n_clicks is not None:
        if selected_value != [] or selected_value != None:
            # This function takes care of 'All' being selected or not
            if type(selected_value)==str:
                sVal = []
                sVal.append(selected_value)
            else:
                sVal = selected_value
            allTechDF, countries = filterInputDF(inputDF,sVal)
            undefDF,countryDF = handleUndef(allTechDF,countries)
            techDF = determineRelationships(countryDF, countries)
            return dcc.send_data_frame(techDF.to_csv, "TechnologyConnections.csv")
        
# Callback to get NDC tech by country(ies) and regions
@app.callback(
    Output("download-getCountriesByTech", "data"),
    [Input("getCountriesByTech", "n_clicks")],
    [State('selectForTech','value')],
    prevent_initial_call=True)
def downloadCountryByTech(n_clicks,selected_value):
    if n_clicks is not None:
        if 'All' not in selected_value:
            if type(selected_value)==str:
                sVal = []
                sVal.append(selected_value)
            else:
                sVal = selected_value
            DFs = []
            for c in sVal:
                x1 = inputDF.loc[inputDF['INDC technology']==c]
                DFs.append(x1)
            countryDF = pd.concat(DFs)
        else:
            countryDF = inputDF
        return dcc.send_data_frame(countryDF.to_csv, "countriesByTech.csv")

# if __name__ == '__main__':
#     app.run_server(debug=False)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0',port=8080)