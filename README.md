# **Introduction**

### CTCN Technology Taxonomy

A document which categorizes climate technologies under Sectors and Technology groups. For example measures intended to enhance CO2 mitigation technologies will fall under Fugitive Technology Control technology group under the Carbon Fixation and Abatement sector.

# **Methods**

1. Data collection steps:
    1. Scope of document analysis was finalized in consultation with client. This included the country categories, and date range from which TNA and NDC documents were to be analyzed.
    2. Rubric to evaluate the documents against (taxonomy and fields to parse out).
        1. CTCN's technology taxonomy was used to categorize climate technologies by their category and sectors
        2. For each technology, the following fields were extracted from documents (see Rajiv's spreadsheet) 
    3. Team gathered all documents and acquired necessary translations to English to begin the process of parsing out the desired information.
    4. Information which was vague and could not be categorized was also parsed out but categorized as undefined.
2. Collating it into a readable form?
    1. Completed information was converted into a single CSV file and used as input to visualization tool. The input file had following columns:
    <br>Parent Category, Category, INDC Sector, INDC technology, Unconditional Target, Technology Needs, More information on INDC technology, TNA / TAP technology prioritised, More information of on TNA / TAP, Technology	Actions / project ideas, Country

3. How python tools were used to create a visualization tool
    1. Tool utilized the following libraries: pandas, dash, dash_core_components, dash_cytoscape, dash_table, dash.dependencies
    1. load data and unique list of countries into python
    2. Create custom filters which would allow a user to select one of the countries from our analysis, or select LDC, SIDS or Africa to pull data for an entire category of countries.
    3. Then we filter out any undefined climate technologies from the raw data
    4. Unique list of countries and all defined climate technologies are then used to determine how the technologies will connect with each other.
    5. For each country, pull their climate technologies and look at techs in pairs in the order they appear in underlying data
        1. Create lists with ordered pairs for all technologies in their order of appearance. We also note the frequency of a pair and countries who mention these technologies.
        2. Create a DF to store this information
    6. Create lists of countries and technologies to be used as dropdown lists in the tool ==> App is ready for user input
    1. Layout: talk about sections created in the app. It has the following componets
        1. Dropdown to select countries included in analysis
        2. A section to show how climate technologies connect with one-another
    7. We use callback functions from Dash core components to bring interactivity to the application. Following user actions are allowed:
        1. Selecting values from the country dropdown updatesthe tech figure and tables
        2. Selecting a specific node highlights all nodes connected to that node
        3. Hovering over a node - shows the node information
        4. Clicking download links -> allows user to export that data as CSV
        5. Get countries by tech

### Questions

1. Define category, sectors in intro
2. Where does the sector and technology group in CTCN taxonomy come from?
