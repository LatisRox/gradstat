#######
# This uses a small wheels.csv dataset
# to demonstrate multiple outputs.
######
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.plotly as py
import plotly.graph_objs as go
#import pandas as pd
#import base64
### calculator import
import loans
### FOR TEST
#import numpy as np

app = dash.Dash()
#deploy line
server = app.server
# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501

# APP code 
#general dataframe
#df = pd.read_csv('wheels.csv')
# Creating DATA FOR SIMPLE GRAPHICS
# np.random.seed(42)
# random_x = np.random.randint(1,101,100)
# random_y = np.random.randint(1,101,100)
# # dataframe for map (put in callback function)
# dfMap = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
# for col in dfMap.columns:
#     dfMap[col] = dfMap[col].astype(str)

# scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
#             [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

# dfMap['text'] = dfMap['state'] + '<br>' +\
#     'Beef '+dfMap['beef']+' Dairy '+dfMap['dairy']+'<br>'+\
#     'Fruits '+dfMap['total fruits']+' Veggies ' + dfMap['total veggies']+'<br>'+\
#     'Wheat '+dfMap['wheat']+' Corn '+dfMap['corn']

# dataMap = [ dict(
#         type='choropleth',
#         colorscale = scl,
#         autocolorscale = False,
#         locations = dfMap['code'],
#         z = dfMap['total exports'].astype(float),
#         locationmode = 'USA-states',
#         text = dfMap['text'],
#         marker = dict(
#             line = dict (
#                 color = 'rgb(255,255,255)',
#                 width = 2
#             ) ),
#         colorbar = dict(
#             title = "Millions USD")
#         ) ]

# layoutMap = dict(
#         title = '2011 US Agriculture Exports by State<br>(Hover for breakdown)',
#         geo = dict(
#             scope='usa',
#             projection=dict( type='albers usa' ),
#             showlakes = True,
#             lakecolor = 'rgb(255, 255, 255)'),
#              )
#encoding for images
# def encode_image(image_file):
#     encoded = base64.b64encode(open(image_file, 'rb').read())
#     return 'data:image/png;base64,{}'.format(encoded.decode())
#Global variables for calculations
startingSalary=0
print("starting salary after init", startingSalary)
startingDebt=0
monthlyPayments=0
estimatedNpv=0
attendanceCost=0
#app layout

app.layout = html.Div([
    # dcc.RadioItems(
    #     id='wheels',
    #     options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
    #     value=1
    # ),
    # html.Div(id='wheels-output'),

    # html.Hr(),  # add a horizontal rule
    # dcc.RadioItems(
    #     id='colors',
    #     options=[{'label': i, 'value': i} for i in df['color'].unique()],
    #     value='blue'
    # ),
    # html.Div(id='colors-output'),
    # html.Img(id='display-image', src='children', height=300),
    #title
    html.Div(
            [
                html.H1(children='GradStat',
                        className='nine columns'),
                html.Img(
                    src="http://i67.tinypic.com/2wq8xhk.png",
                    className='three columns',
                    style={
                        'height': '15%',
                        'width': '15%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                    },
                ),
                html.Div(children='''
                        Going to college most likely will be a good investment and we will tell you for how long you will be paying for it.
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),
    #inputs
    #name
    html.Hr(),  # add a horizontal rule
    #things that change for comparison purposes
    html.Div(
            [
            html.Div(
                [
                    html.Div([
                     dcc.Input(id='my-id', placeholder='Your name?', type='text', value=''),
                     html.Div(id='my-div')
                        ])
                ], className='row'                
                ),
            html.Hr(),  # add a horizontal rule
            html.Div(
                        [
                            html.Div([
                                    html.Div(children='''
                                            In which university do you want to study?
                                            ''',
                                            className='four columns'
                                            ),
                                    html.Div(children='''
                                            Which is your current state of residence?
                                            ''',
                                            className='four columns'
                                            ),
                                    ])
                        ], className='row'
            ), 
            html.Div(
                        [
                            html.Div([
                                            #university
                                            html.Div(
                                                        [
                                                            html.Div([
                                                            dcc.Dropdown(
                                                                id='my-dropdown2',
                                                                #TODO Change for universities lists because this is terrible lol
                                                                options=[
                                                                {'label': 'Stanford University', 'value': 'Stanford University'},
                                                                {'label': 'California Institute of Technology (CIT)', 'value': 'California Institute of Technology (CIT)'},
                                                                {'label': 'University of California, Berkeley', 'value': 'University of California, Berkeley'},
                                                                {'label': 'Pomona College', 'value': 'Pomona College'},
                                                                {'label': 'California State University, Fullerton (CSUF)', 'value': 'California State University, Fullerton (CSUF)'},
                                                                {'label': 'Cal Poly San Luis Obispo', 'value': 'Cal Poly San Luis Obispo'},
                                                                {'label': 'Harvey Mudd College', 'value': 'Harvey Mudd College'},
                                                                {'label': 'San Jose State University (SJSU)', 'value': 'San Jose State University (SJSU)'},
                                                                {'label': 'California State University, Northridge (CSUN)', 'value': 'California State University, Northridge (CSUN)'},
                                                                {'label': 'University of California, Davis', 'value': 'University of California, Davis'},
                                                                {'label': 'San Francisco State University (SFSU)', 'value': 'San Francisco State University (SFSU)'},
                                                                {'label': 'University of California at Los Angeles (UCLA)', 'value': 'University of California at Los Angeles (UCLA)'},
                                                                {'label': 'California State University, Dominguez Hills (CSUDH)', 'value': 'California State University, Dominguez Hills (CSUDH)'},
                                                                {'label': 'San Diego State University (SDSU)', 'value': 'San Diego State University (SDSU)'},
                                                                {'label': 'California State University, Long Beach (CSULB)', 'value': 'California State University, Long Beach (CSULB)'},
                                                                {'label': 'University of California, Santa Barbara (UCSB)', 'value': 'University of California, Santa Barbara (UCSB)'},
                                                                {'label': 'University of California, Irvine (UCI)', 'value': 'University of California, Irvine (UCI)'},
                                                                {'label': 'California State University, Sacramento (CSUS)', 'value': 'California State University, Sacramento (CSUS)'},
                                                                {'label': 'University of Southern California (USC)', 'value': 'University of Southern California (USC)'},
                                                                {'label': 'California State University (CSU), Stanislaus', 'value': 'California State University (CSU), Stanislaus'},
                                                                {'label': 'University of California, Riverside (UCR)', 'value': 'University of California, Riverside (UCR)'},
                                                                {'label': 'University of California, San Diego (UCSD)', 'value': 'University of California, San Diego (UCSD)'},
                                                                {'label': 'University of California, Santa Cruz (UCSC)', 'value': 'University of California, Santa Cruz (UCSC)'},
                                                                {'label': 'Occidental College', 'value': 'Occidental College'},
                                                                {'label': 'Thomas Aquinas College', 'value': 'Thomas Aquinas College'},
                                                                {'label': 'Humboldt State University', 'value': 'Humboldt State University'},
                                                                {'label': 'Colorado School of Mines', 'value': 'Colorado School of Mines'},
                                                                {'label': 'University of Colorado - Boulder (UCB)', 'value': 'University of Colorado - Boulder (UCB)'},
                                                                {'label': 'New Mexico Institute of Mining and Technology (New Mexico Tech)', 'value': 'New Mexico Institute of Mining and Technology (New Mexico Tech)'},
                                                                {'label': 'Brigham Young University (BYU)', 'value': 'Brigham Young University (BYU)'},
                                                                {'label': 'University of Arizona', 'value': 'University of Arizona'},
                                                                {'label': 'University of Washington', 'value': 'University of Washington'},
                                                                {'label': 'Washington State University', 'value': 'Washington State University'},
                                                                {'label': 'University of Colorado - Denver', 'value': 'University of Colorado - Denver'},
                                                                {'label': 'Arizona State University', 'value': 'Arizona State University'},
                                                                {'label': 'Oregon State University', 'value': 'Oregon State University'},
                                                                {'label': 'University of Utah', 'value': 'University of Utah'},
                                                                {'label': 'University of Nevada, Reno (UNR)', 'value': 'University of Nevada, Reno (UNR)'},
                                                                {'label': 'Seattle University', 'value': 'Seattle University'},
                                                                {'label': 'University of Idaho', 'value': 'University of Idaho'},
                                                                {'label': 'University of New Mexico', 'value': 'University of New Mexico'},
                                                                {'label': 'University of Puget Sound', 'value': 'University of Puget Sound'},
                                                                {'label': 'Colorado College', 'value': 'Colorado College'},
                                                                {'label': 'Reed College', 'value': 'Reed College'},
                                                                {'label': 'Whitman College', 'value': 'Whitman College'},
                                                                {'label': 'New Mexico State University', 'value': 'New Mexico State University'},
                                                                {'label': 'Colorado State University', 'value': 'Colorado State University'},
                                                                {'label': 'University of Wyoming', 'value': 'University of Wyoming'},
                                                                {'label': 'Utah State University', 'value': 'Utah State University'},
                                                                {'label': 'University of Oregon', 'value': 'University of Oregon'},
                                                                {'label': 'Montana State University - Bozeman', 'value': 'Montana State University - Bozeman'},
                                                                {'label': 'Gonzaga University', 'value': 'Gonzaga University'},
                                                                {'label': 'University of Hawaii', 'value': 'University of Hawaii'},
                                                                {'label': 'Western Washington University', 'value': 'Western Washington University'},
                                                                {'label': 'Regis University', 'value': 'Regis University'},
                                                                {'label': 'Idaho State University', 'value': 'Idaho State University'},
                                                                {'label': 'University of Alaska, Anchorage', 'value': 'University of Alaska, Anchorage'},
                                                                {'label': 'Lewis & Clark College', 'value': 'Lewis & Clark College'},
                                                                {'label': 'University of Montana', 'value': 'University of Montana'},
                                                                {'label': 'University of Nevada, Las Vegas (UNLV)', 'value': 'University of Nevada, Las Vegas (UNLV)'},
                                                                {'label': 'Portland State University', 'value': 'Portland State University'},
                                                                {'label': 'Eastern Washington University', 'value': 'Eastern Washington University'},
                                                                {'label': 'Fort Lewis College', 'value': 'Fort Lewis College'},
                                                                {'label': 'Boise State University', 'value': 'Boise State University'},
                                                                {'label': 'Utah Valley State College', 'value': 'Utah Valley State College'},
                                                                {'label': 'Evergreen State College', 'value': 'Evergreen State College'},
                                                                {'label': 'Southern Utah University', 'value': 'Southern Utah University'},
                                                                {'label': 'Montana State University - Billings', 'value': 'Montana State University - Billings'},
                                                                {'label': 'University of Notre Dame', 'value': 'University of Notre Dame'},
                                                                {'label': 'University Of Chicago', 'value': 'University Of Chicago'},
                                                                {'label': 'Carleton College', 'value': 'Carleton College'},
                                                                {'label': 'Illinois Institute of Technology', 'value': 'Illinois Institute of Technology'},
                                                                {'label': 'Case Western Reserve University', 'value': 'Case Western Reserve University'},
                                                                {'label': 'University of Illinois at Urbana-Champaign', 'value': 'University of Illinois at Urbana-Champaign'},
                                                                {'label': 'Northwestern University', 'value': 'Northwestern University'},
                                                                {'label': 'University of Missouri - Rolla (UMR)', 'value': 'University of Missouri - Rolla (UMR)'},
                                                                {'label': 'South Dakota School of Mines & Technology', 'value': 'South Dakota School of Mines & Technology'},
                                                                {'label': 'University of Michigan', 'value': 'University of Michigan'},
                                                                {'label': 'Purdue University', 'value': 'Purdue University'},
                                                                {'label': 'Marquette University', 'value': 'Marquette University'},
                                                                {'label': 'DePauw University', 'value': 'DePauw University'},
                                                                {'label': 'University of Wisconsin (UW) - Madison', 'value': 'University of Wisconsin (UW) - Madison'},
                                                                {'label': 'Bradley University', 'value': 'Bradley University'},
                                                                {'label': 'St. Olaf College', 'value': 'St. Olaf College'},
                                                                {'label': 'Michigan State University', 'value': 'Michigan State University'},
                                                                {'label': 'DePaul University', 'value': 'DePaul University'},
                                                                {'label': 'Iowa State University', 'value': 'Iowa State University'},
                                                                {'label': 'University of Minnesota', 'value': 'University of Minnesota'},
                                                                {'label': 'Indiana University (IU), Bloomington', 'value': 'Indiana University (IU), Bloomington'},
                                                                {'label': 'University of Iowa', 'value': 'University of Iowa'},
                                                                {'label': 'Ohio State University', 'value': 'Ohio State University'},
                                                                {'label': 'Denison University', 'value': 'Denison University'},
                                                                {'label': 'University of Illinois at Chicago', 'value': 'University of Illinois at Chicago'},
                                                                {'label': 'Oberlin College', 'value': 'Oberlin College'},
                                                                {'label': 'University of Kansas', 'value': 'University of Kansas'},
                                                                {'label': 'University of Missouri - Columbia', 'value': 'University of Missouri - Columbia'},
                                                                {'label': 'University of Nebraska', 'value': 'University of Nebraska'},
                                                                {'label': 'Northern Illinois University', 'value': 'Northern Illinois University'},
                                                                {'label': 'Gustavus Adolphus College', 'value': 'Gustavus Adolphus College'},
                                                                {'label': 'University of North Dakota', 'value': 'University of North Dakota'},
                                                                {'label': 'Kansas State University', 'value': 'Kansas State University'},
                                                                {'label': 'University of Wisconsin (UW) - Platteville', 'value': 'University of Wisconsin (UW) - Platteville'},
                                                                {'label': 'Wittenberg University', 'value': 'Wittenberg University'},
                                                                {'label': 'North Dakota State University', 'value': 'North Dakota State University'},
                                                                {'label': 'Grinnell College', 'value': 'Grinnell College'},
                                                                {'label': 'Wayne State University', 'value': 'Wayne State University'},
                                                                {'label': 'University of Toledo', 'value': 'University of Toledo'},
                                                                {'label': 'University of Wisconsin (UW) - Whitewater', 'value': 'University of Wisconsin (UW) - Whitewater'},
                                                                {'label': 'Minnesota State University - Mankato', 'value': 'Minnesota State University - Mankato'},
                                                                {'label': 'University of Wisconsin (UW) - Milwaukee', 'value': 'University of Wisconsin (UW) - Milwaukee'},
                                                                {'label': 'Western Michigan University', 'value': 'Western Michigan University'},
                                                                {'label': 'South Dakota State University', 'value': 'South Dakota State University'},
                                                                {'label': 'Ohio University', 'value': 'Ohio University'},
                                                                {'label': 'Illinois State University', 'value': 'Illinois State University'},
                                                                {'label': 'Cleveland State University', 'value': 'Cleveland State University'},
                                                                {'label': 'University of Nebraska at Omaha', 'value': 'University of Nebraska at Omaha'},
                                                                {'label': 'Southern Illinois University Carbondale', 'value': 'Southern Illinois University Carbondale'},
                                                                {'label': 'Eastern Michigan University', 'value': 'Eastern Michigan University'},
                                                                {'label': 'Bowling Green State University', 'value': 'Bowling Green State University'},
                                                                {'label': 'St. Cloud State University', 'value': 'St. Cloud State University'},
                                                                {'label': 'University of Wisconsin (UW) - Parkside', 'value': 'University of Wisconsin (UW) - Parkside'},
                                                                {'label': 'University of Akron', 'value': 'University of Akron'},
                                                                {'label': 'Missouri State University', 'value': 'Missouri State University'},
                                                                {'label': 'University of Wisconsin (UW) - La Crosse', 'value': 'University of Wisconsin (UW) - La Crosse'},
                                                                {'label': 'University of Wisconsin (UW) - Stout', 'value': 'University of Wisconsin (UW) - Stout'},
                                                                {'label': 'University of Missouri - St. Louis (UMSL)', 'value': 'University of Missouri - St. Louis (UMSL)'},
                                                                {'label': 'University of Wisconsin (UW) - Oshkosh', 'value': 'University of Wisconsin (UW) - Oshkosh'},
                                                                {'label': 'University of Missouri - Kansas City (UMKC)', 'value': 'University of Missouri - Kansas City (UMKC)'},
                                                                {'label': 'University of Wisconsin (UW) - Eau Claire', 'value': 'University of Wisconsin (UW) - Eau Claire'},
                                                                {'label': 'Ball State University', 'value': 'Ball State University'},
                                                                {'label': 'Park University', 'value': 'Park University'},
                                                                {'label': 'University of Wisconsin (UW) - Stevens Point', 'value': 'University of Wisconsin (UW) - Stevens Point'},
                                                                {'label': 'Kent State University', 'value': 'Kent State University'},
                                                                {'label': 'University of Wisconsin (UW) - Green Bay', 'value': 'University of Wisconsin (UW) - Green Bay'},
                                                                {'label': 'Indiana Wesleyan University', 'value': 'Indiana Wesleyan University'},
                                                                {'label': 'Pittsburg State University', 'value': 'Pittsburg State University'},
                                                                {'label': 'Davenport University', 'value': 'Davenport University'},
                                                                {'label': 'Black Hills State University', 'value': 'Black Hills State University'},
                                                                {'label': 'Rice University', 'value': 'Rice University'},
                                                                {'label': 'Georgetown University', 'value': 'Georgetown University'},
                                                                {'label': 'Duke University', 'value': 'Duke University'},
                                                                {'label': 'Georgia Institute of Technology', 'value': 'Georgia Institute of Technology'},
                                                                {'label': 'Washington and Lee University', 'value': 'Washington and Lee University'},
                                                                {'label': 'Vanderbilt University', 'value': 'Vanderbilt University'},
                                                                {'label': 'Davidson College', 'value': 'Davidson College'},
                                                                {'label': 'University of Virginia', 'value': 'University of Virginia'},
                                                                {'label': 'George Washington University', 'value': 'George Washington University'},
                                                                {'label': 'Texas A&M University', 'value': 'Texas A&M University'},
                                                                {'label': 'Tulane University', 'value': 'Tulane University'},
                                                                {'label': 'Virginia Polytechnic Institute and State University', 'value': 'Virginia Polytechnic Institute and State University'},
                                                                {'label': 'University of Maryland, College Park', 'value': 'University of Maryland, College Park'},
                                                                {'label': 'University of Richmond', 'value': 'University of Richmond'},
                                                                {'label': 'University of Texas (UT) - Austin', 'value': 'University of Texas (UT) - Austin'},
                                                                {'label': 'Emory University', 'value': 'Emory University'},
                                                                {'label': 'American University, Washington D.C.', 'value': 'American University, Washington D.C.'},
                                                                {'label': 'University of Tulsa', 'value': 'University of Tulsa'},
                                                                {'label': 'Baylor University', 'value': 'Baylor University'},
                                                                {'label': 'University of Florida', 'value': 'University of Florida'},
                                                                {'label': 'Louisiana State University', 'value': 'Louisiana State University'},
                                                                {'label': 'George Mason University', 'value': 'George Mason University'},
                                                                {'label': 'Clemson University', 'value': 'Clemson University'},
                                                                {'label': 'University of Georgia', 'value': 'University of Georgia'},
                                                                {'label': 'Auburn University', 'value': 'Auburn University'},
                                                                {'label': 'University of Delaware', 'value': 'University of Delaware'},
                                                                {'label': 'Randolph-Macon College', 'value': 'Randolph-Macon College'},
                                                                {'label': 'North Carolina State University', 'value': 'North Carolina State University'},
                                                                {'label': 'University of Oklahoma', 'value': 'University of Oklahoma'},
                                                                {'label': 'University of Arkansas', 'value': 'University of Arkansas'},
                                                                {'label': 'University of Alabama at Huntsville', 'value': 'University of Alabama at Huntsville'},
                                                                {'label': 'Howard University', 'value': 'Howard University'},
                                                                {'label': 'University of North Carolina at Chapel Hill', 'value': 'University of North Carolina at Chapel Hill'},
                                                                {'label': 'University of Alabama, Tuscaloosa', 'value': 'University of Alabama, Tuscaloosa'},
                                                                {'label': 'University of Texas at Arlington', 'value': 'University of Texas at Arlington'},
                                                                {'label': 'Oklahoma State University', 'value': 'Oklahoma State University'},
                                                                {'label': 'Tennessee Technological University', 'value': 'Tennessee Technological University'},
                                                                {'label': 'University of Houston', 'value': 'University of Houston'},
                                                                {'label': 'University of Mississippi', 'value': 'University of Mississippi'},
                                                                {'label': 'Lamar University', 'value': 'Lamar University'},
                                                                {'label': 'Mississippi State University', 'value': 'Mississippi State University'},
                                                                {'label': 'University of Kentucky', 'value': 'University of Kentucky'},
                                                                {'label': 'Texas Christian University', 'value': 'Texas Christian University'},
                                                                {'label': 'West Virginia University', 'value': 'West Virginia University'},
                                                                {'label': 'University of Maryland Baltimore County', 'value': 'University of Maryland Baltimore County'},
                                                                {'label': 'University of Louisiana at Lafayette', 'value': 'University of Louisiana at Lafayette'},
                                                                {'label': 'Florida International University', 'value': 'Florida International University'},
                                                                {'label': 'University of Tennessee', 'value': 'University of Tennessee'},
                                                                {'label': 'University of Arkansas - Monticello (UAM)', 'value': 'University of Arkansas - Monticello (UAM)'},
                                                                {'label': 'University of North Carolina at Charlotte', 'value': 'University of North Carolina at Charlotte'},
                                                                {'label': 'Georgia State University', 'value': 'Georgia State University'},
                                                                {'label': 'LeTourneau University', 'value': 'LeTourneau University'},
                                                                {'label': 'Florida State University', 'value': 'Florida State University'},
                                                                {'label': 'University of Texas at El Paso', 'value': 'University of Texas at El Paso'},
                                                                {'label': 'University of Central Florida', 'value': 'University of Central Florida'},
                                                                {'label': 'University of South Carolina', 'value': 'University of South Carolina'},
                                                                {'label': 'Florida Atlantic University', 'value': 'Florida Atlantic University'},
                                                                {'label': 'University of South Florida', 'value': 'University of South Florida'},
                                                                {'label': 'University of Texas at San Antonio', 'value': 'University of Texas at San Antonio'},
                                                                {'label': 'University of Alabama at Birmingham', 'value': 'University of Alabama at Birmingham'},
                                                                {'label': 'University of Memphis', 'value': 'University of Memphis'},
                                                                {'label': 'Appalachian State University', 'value': 'Appalachian State University'},
                                                                {'label': 'Virginia Commonwealth University', 'value': 'Virginia Commonwealth University'},
                                                                {'label': 'East Carolina University', 'value': 'East Carolina University'},
                                                                {'label': 'Western Carolina University', 'value': 'Western Carolina University'},
                                                                {'label': 'Jacksonville University', 'value': 'Jacksonville University'},
                                                                {'label': 'University of North Carolina at Wilmington', 'value': 'University of North Carolina at Wilmington'},
                                                                {'label': 'Oklahoma City University', 'value': 'Oklahoma City University'},
                                                                {'label': 'Arkansas State University', 'value': 'Arkansas State University'},
                                                                {'label': 'Tarleton State University', 'value': 'Tarleton State University'},
                                                                {'label': 'Morehead State University', 'value': 'Morehead State University'},
                                                                {'label': 'Mississippi College', 'value': 'Mississippi College'},
                                                                {'label': 'Dallas Baptist University', 'value': 'Dallas Baptist University'},
                                                                {'label': 'Austin Peay State University', 'value': 'Austin Peay State University'},
                                                                {'label': 'Saint Leo University', 'value': 'Saint Leo University'},
                                                                {'label': 'Tusculum College', 'value': 'Tusculum College'},
                                                                {'label': 'Virginia Wesleyan College', 'value': 'Virginia Wesleyan College'},
                                                                {'label': 'Lee University', 'value': 'Lee University'},
                                                                {'label': 'Florida Metropolitan University', 'value': 'Florida Metropolitan University'},
                                                                {'label': 'Dartmouth College', 'value': 'Dartmouth College'},
                                                                {'label': 'Princeton University', 'value': 'Princeton University'},
                                                                {'label': 'Massachusetts Institute of Technology', 'value': 'Massachusetts Institute of Technology'},
                                                                {'label': 'Yale University', 'value': 'Yale University'},
                                                                {'label': 'Harvard University', 'value': 'Harvard University'},
                                                                {'label': 'University of Pennsylvania', 'value': 'University of Pennsylvania'},
                                                                {'label': 'Polytechnic University of New York, Brooklyn', 'value': 'Polytechnic University of New York, Brooklyn'},
                                                                {'label': 'Cooper Union', 'value': 'Cooper Union'},
                                                                {'label': 'Worcester Polytechnic Institute', 'value': 'Worcester Polytechnic Institute'},
                                                                {'label': 'Carnegie Mellon University', 'value': 'Carnegie Mellon University'},
                                                                {'label': 'Rensselaer Polytechnic Institute', 'value': 'Rensselaer Polytechnic Institute'},
                                                                {'label': 'Cornell University', 'value': 'Cornell University'},
                                                                {'label': 'Bucknell University', 'value': 'Bucknell University'},
                                                                {'label': 'Brown University', 'value': 'Brown University'},
                                                                {'label': 'Colgate University', 'value': 'Colgate University'},
                                                                {'label': 'Columbia University', 'value': 'Columbia University'},
                                                                {'label': 'Amherst College', 'value': 'Amherst College'},
                                                                {'label': 'Lafayette College', 'value': 'Lafayette College'},
                                                                {'label': 'Bowdoin College', 'value': 'Bowdoin College'},
                                                                {'label': 'College of the Holy Cross', 'value': 'College of the Holy Cross'},
                                                                {'label': 'Stevens Institute of Technology', 'value': 'Stevens Institute of Technology'},
                                                                {'label': 'Lehigh University', 'value': 'Lehigh University'},
                                                                {'label': 'Swarthmore College', 'value': 'Swarthmore College'},
                                                                {'label': 'Boston College', 'value': 'Boston College'},
                                                                {'label': 'Williams College', 'value': 'Williams College'},
                                                                {'label': 'Villanova University', 'value': 'Villanova University'},
                                                                {'label': 'Fordham University', 'value': 'Fordham University'},
                                                                {'label': 'Wesleyan University', 'value': 'Wesleyan University'},
                                                                {'label': 'Wentworth Institute of Technology', 'value': 'Wentworth Institute of Technology'},
                                                                {'label': 'Bates College', 'value': 'Bates College'},
                                                                {'label': 'Binghamton University', 'value': 'Binghamton University'},
                                                                {'label': 'Union College', 'value': 'Union College'},
                                                                {'label': 'New York University', 'value': 'New York University'},
                                                                {'label': 'Vassar College', 'value': 'Vassar College'},
                                                                {'label': 'Middlebury College', 'value': 'Middlebury College'},
                                                                {'label': 'Mount Holyoke College', 'value': 'Mount Holyoke College'},
                                                                {'label': 'Boston University', 'value': 'Boston University'},
                                                                {'label': 'Drexel University', 'value': 'Drexel University'},
                                                                {'label': 'St. John\'s University, New York', 'value': 'St. John\'s University, New York'},
                                                                {'label': 'Long Island University', 'value': 'Long Island University'},
                                                                {'label': 'Stony Brook University', 'value': 'Stony Brook University'},
                                                                {'label': 'Franklin and Marshall College', 'value': 'Franklin and Marshall College'},
                                                                {'label': 'Hofstra University', 'value': 'Hofstra University'},
                                                                {'label': 'State University of New York (SUNY) at Albany', 'value': 'State University of New York (SUNY) at Albany'},
                                                                {'label': 'Rutgers University', 'value': 'Rutgers University'},
                                                                {'label': 'Pratt Institute', 'value': 'Pratt Institute'},
                                                                {'label': 'Pace University', 'value': 'Pace University'},
                                                                {'label': 'Seton Hall University', 'value': 'Seton Hall University'},
                                                                {'label': 'Rider University', 'value': 'Rider University'},
                                                                {'label': 'University of Connecticut', 'value': 'University of Connecticut'},
                                                                {'label': 'Providence College', 'value': 'Providence College'},
                                                                {'label': 'University of Massachusetts (UMass) - Amherst', 'value': 'University of Massachusetts (UMass) - Amherst'},
                                                                {'label': 'Ithaca College', 'value': 'Ithaca College'},
                                                                {'label': 'University of Massachusetts (UMass) - Lowell', 'value': 'University of Massachusetts (UMass) - Lowell'},
                                                                {'label': 'Northeastern University', 'value': 'Northeastern University'},
                                                                {'label': 'Syracuse University', 'value': 'Syracuse University'},
                                                                {'label': 'Colby College', 'value': 'Colby College'},
                                                                {'label': 'Gettysburg College', 'value': 'Gettysburg College'},
                                                                {'label': 'Pennsylvania State University', 'value': 'Pennsylvania State University'},
                                                                {'label': 'University of Rhode Island', 'value': 'University of Rhode Island'},
                                                                {'label': 'Siena College', 'value': 'Siena College'},
                                                                {'label': 'La Salle University (Philadelphia)', 'value': 'La Salle University (Philadelphia)'},
                                                                {'label': 'Rochester Institute of Technology', 'value': 'Rochester Institute of Technology'},
                                                                {'label': 'Duquesne University', 'value': 'Duquesne University'},
                                                                {'label': 'State University of New York (SUNY) at Farmingdale', 'value': 'State University of New York (SUNY) at Farmingdale'},
                                                                {'label': 'Smith College', 'value': 'Smith College'},
                                                                {'label': 'Hamilton College', 'value': 'Hamilton College'},
                                                                {'label': 'Wellesley College', 'value': 'Wellesley College'},
                                                                {'label': 'Widener University', 'value': 'Widener University'},
                                                                {'label': 'University of New Haven', 'value': 'University of New Haven'},
                                                                {'label': 'Dowling College', 'value': 'Dowling College'},
                                                                {'label': 'University of Vermont', 'value': 'University of Vermont'},
                                                                {'label': 'State University of New York (SUNY) at Buffalo', 'value': 'State University of New York (SUNY) at Buffalo'},
                                                                {'label': 'State University of New York (SUNY) at Geneseo', 'value': 'State University of New York (SUNY) at Geneseo'},
                                                                {'label': 'Fashion Institute of Technology', 'value': 'Fashion Institute of Technology'},
                                                                {'label': 'Philadelphia University', 'value': 'Philadelphia University'},
                                                                {'label': 'Ursinus College', 'value': 'Ursinus College'},
                                                                {'label': 'Adelphi University', 'value': 'Adelphi University'},
                                                                {'label': 'Juniata College', 'value': 'Juniata College'},
                                                                {'label': 'Fairleigh Dickinson University', 'value': 'Fairleigh Dickinson University'},
                                                                {'label': 'University of New Hampshire', 'value': 'University of New Hampshire'},
                                                                {'label': 'University of Massachusetts (UMass) - Boston', 'value': 'University of Massachusetts (UMass) - Boston'},
                                                                {'label': 'State University of New York at Oswego', 'value': 'State University of New York at Oswego'},
                                                                {'label': 'University of Massachusetts (UMass) - Dartmouth', 'value': 'University of Massachusetts (UMass) - Dartmouth'},
                                                                {'label': 'State University of New York (SUNY) at Oneonta', 'value': 'State University of New York (SUNY) at Oneonta'},
                                                                {'label': 'Quinnipiac University', 'value': 'Quinnipiac University'},
                                                                {'label': 'State University of New York (SUNY) at Plattsburgh', 'value': 'State University of New York (SUNY) at Plattsburgh'},
                                                                {'label': 'Sacred Heart University', 'value': 'Sacred Heart University'},
                                                                {'label': 'Skidmore College', 'value': 'Skidmore College'},
                                                                {'label': 'Moravian College', 'value': 'Moravian College'},
                                                                {'label': 'Penn State - Harrisburg', 'value': 'Penn State - Harrisburg'},
                                                                {'label': 'Suffolk University', 'value': 'Suffolk University'},
                                                                {'label': 'Fitchburg State College', 'value': 'Fitchburg State College'},
                                                                {'label': 'Roger Williams University', 'value': 'Roger Williams University'},
                                                                {'label': 'University Of Maine', 'value': 'University Of Maine'},
                                                                {'label': 'State University of New York (SUNY) at Potsdam', 'value': 'State University of New York (SUNY) at Potsdam'},
                                                                {'label': 'Niagara University', 'value': 'Niagara University'},
                                                                {'label': 'State University of New York (SUNY) at Fredonia', 'value': 'State University of New York (SUNY) at Fredonia'},
                                                                {'label': 'University of Southern Maine', 'value': 'University of Southern Maine'},
                                                                {'label': 'Mercy College', 'value': 'Mercy College'}
                                                                ],
                                                                value='Stanford University',                                
                                                                placeholder="Select a University",
                                                                ),
                                                                html.Div(id='universities1')
                                                                ])
                                                        ], className='four columns'
                                            ),
                                            #state of residency
                                            html.Div(
                                                        [
                                                            html.Div([
                                                            dcc.Dropdown(
                                                                id='my-dropdown3',
                                                                #TODO Change for state lists
                                                                options=[
                                                                {'label': 'Alabama', 'value': 'Alabama'},
                                                                {'label': 'Alaska', 'value': 'Alaska'},
                                                                {'label': 'Arizona', 'value': 'Arizona'},
                                                                {'label': 'Arkansas', 'value': 'Arkansas'},
                                                                {'label': 'California', 'value': 'California'},
                                                                {'label': 'Colorado', 'value': 'Colorado'},
                                                                {'label': 'Connecticut', 'value': 'Connecticut'},
                                                                {'label': 'Delaware', 'value': 'Delaware'},
                                                                {'label': 'District of Columbia', 'value': 'District of Columbia'},
                                                                {'label': 'Florida', 'value': 'Florida'},
                                                                {'label': 'Georgia', 'value': 'Georgia'},
                                                                {'label': 'Hawaii', 'value': 'Hawaii'},
                                                                {'label': 'Idaho', 'value': 'Idaho'},
                                                                {'label': 'Illinois', 'value': 'Illinois'},
                                                                {'label': 'Indiana', 'value': 'Indiana'},
                                                                {'label': 'Iowa', 'value': 'Iowa'},
                                                                {'label': 'Kansas', 'value': 'Kansas'},
                                                                {'label': 'Kentucky', 'value': 'Kentucky'},
                                                                {'label': 'Louisiana', 'value': 'Louisiana'},
                                                                {'label': 'Maine', 'value': 'Maine'},
                                                                {'label': 'Maryland', 'value': 'Maryland'},
                                                                {'label': 'Massachusetts', 'value': 'Massachusetts'},
                                                                {'label': 'Michigan', 'value': 'Michigan'},
                                                                {'label': 'Minnesota', 'value': 'Minnesota'},
                                                                {'label': 'Mississippi', 'value': 'Mississippi'},
                                                                {'label': 'Missouri', 'value': 'Missouri'},
                                                                {'label': 'Montana', 'value': 'Montana'},
                                                                {'label': 'Nebraska', 'value': 'Nebraska'},
                                                                {'label': 'Nevada', 'value': 'Nevada'},
                                                                {'label': 'New Hampshire', 'value': 'New Hampshire'},
                                                                {'label': 'New Jersey', 'value': 'New Jersey'},
                                                                {'label': 'New Mexico', 'value': 'New Mexico'},
                                                                {'label': 'New York', 'value': 'New York'},
                                                                {'label': 'North Carolina', 'value': 'North Carolina'},
                                                                {'label': 'North Dakota', 'value': 'North Dakota'},
                                                                {'label': 'Ohio', 'value': 'Ohio'},
                                                                {'label': 'Oklahoma', 'value': 'Oklahoma'},
                                                                {'label': 'Oregon', 'value': 'Oregon'},
                                                                {'label': 'Pennsylvania', 'value': 'Pennsylvania'},
                                                                {'label': 'Rhode Island', 'value': 'Rhode Island'},
                                                                {'label': 'South Carolina', 'value': 'South Carolina'},
                                                                {'label': 'South Dakota', 'value': 'South Dakota'},
                                                                {'label': 'Tennessee', 'value': 'Tennessee'},
                                                                {'label': 'Texas', 'value': 'Texas'},
                                                                {'label': 'Utah', 'value': 'Utah'},
                                                                {'label': 'Vermont', 'value': 'Vermont'},
                                                                {'label': 'Virginia', 'value': 'Virginia'},
                                                                {'label': 'Washington', 'value': 'Washington'},
                                                                {'label': 'Weste Virginia', 'value': 'Weste Virginia'},
                                                                {'label': 'Wisconsin', 'value': 'Wisconsin'},
                                                                {'label': 'Wyoming', 'value': 'Wyoming'}
                                                                ],
                                                                value='Alabama',
                                                                placeholder="Select your state of residency",
                                                                ),
                                                                html.Div(id='states1')
                                                                ])
                                                        ], className='four columns'
                                            ),
                                    ])
                        ], className='row'
            ),          
            html.Hr(),  # add a horizontal rule
            html.Div(
                        [
                            html.Div([
                                    html.Div(children='''
                                            What do you want to study?
                                            ''',
                                            className='four columns'
                                            ),
                                    html.Div(children='''
                                            Will you be living with your parents while studying?
                                            ''',
                                            className='four columns'
                                            ),
                                    ])
                        ], className='row'
            ), 
            #major
            html.Div(
                        [
                            html.Div([
                             dcc.Dropdown(
                                id='my-dropdown',
                                #majors according to the 8 big groups on the master 
                                options=[
                                {'label': 'Art', 'value': 'Art'},
                                {'label': 'Business', 'value': 'Business'},
                                {'label': 'Communication', 'value': 'Communication'},
                                {'label': 'Computer Science', 'value': 'Computer Science'},
                                {'label': 'Education', 'value': 'Education'},
                                {'label': 'Engineering', 'value': 'Engineering'},
                                {'label': 'Humanities', 'value': 'Humanities'},
                                {'label': 'Physical & Life Science', 'value': 'Physical & Life Science'},
                                {'label': 'Social Sciences', 'value': 'Social Sciences'}
                                ],
                                value='Business',
                                placeholder="Select a Major",
                                ),
                                html.Div(id='majors1')
                                ])
                        ], className='four columns'
            ),            
            #living with parents
            html.Div(
                        [
                            html.Div([                                
                                dcc.Dropdown(
                                id='my-dropdown4',
                                #yes or no values
                                options=[
                                {'label': 'Yes', 'value': 'Yes'},
                                {'label': 'No', 'value': 'No'}
                                ],
                                value='No',
                                placeholder="Will you be living with your parents while studying?",
                                ),
                                html.Div(id='liveparents1')
                                ])
                        ], className='four columns'
            )           
            ], className="row"
        ),
    html.Hr(),  # add a horizontal rule    
    #number of college students in household
    html.Div(
                [
                    html.Div(children='''
                            What is the number of college students in your household? 
                            ''',
                            className='three columns'
                        ),
                    html.Div([
                        dcc.Slider(
                        id='my-slider',
                        min=1,
                        max=10,
                        step=1,
                        value=1,
                    ),
                    html.Div(id='slider-output-container')
                     ],
                     className='nine columns')
                ], className='row'
    ),
    html.Hr(),  # add a horizontal rule
    #number of people living in household
    html.Div(
                [
                    html.Div(children='''
                            What is the number of people living in your household? 
                            ''',
                            className='three columns'
                        ),
                    html.Div([
                        dcc.Slider(
                        id='my-slider2',
                        min=1,
                        max=10,
                        step=1,
                        value=1,
                    ),
                    html.Div(id='slider-output-container2')
                     ],
                     className='nine columns')
                ], className='row'
    ),
    html.Hr(),  # add a horizontal rule
    #what is your parents income 
    html.Div(
                [
                    html.Div(children='''
                            What is your household income? 
                            ''',
                            className='three columns'
                        ),
                    html.Div([
                        dcc.Slider(
                        id='my-slider3',
                        min=0,
                        max=300000,
                        step=500,
                        value=0,
                    ),
                    html.Div(id='slider-output-container3')
                     ],
                     className='nine columns')
                ], className='row'
    ),
    html.Hr(),  # add a horizontal rule
    # #how much money you and/or your parents will countribute for your tuition costs?
    # html.Div(
    #             [
    #                 html.Div(children='''
    #                         how much money you and your parents will countribute for your tuition costs? 
    #                         ''',
    #                         className='three columns'
    #                     ),
    #                 html.Div([
    #                     dcc.Slider(
    #                     id='my-slider4',
    #                     min=0,
    #                     max=500000,
    #                     step=500,
    #                     value=0,
    #                 ),
    #                 html.Div(id='slider-output-container4')
    #                  ],
    #                  className='nine columns')
    #             ], className='row'
    # ),
    #Summary of calculations
    # html.Div(
    #                     [
    #                         html.Div([
    #                          dcc.Textarea(
    #                             id='my-textArea',
    #                             placeholder='Enter a value...',
    #                             value='This is a TextArea component',
    #                             style={'width': '100%'}
    #                             ),
    #                             html.Div(id='textarea')
    #                             ])
    #                     ], className='row'
    #         ),

    html.Div(
                        [
                            html.Div(
                                                [
                                                    html.Div([
                                                        html.H1(id='live-update-AttendanceCost'),
                                                        dcc.Interval(
                                                            id='interval-component-AttendanceCost',
                                                            interval=1000, # 2000 milliseconds = 2 seconds
                                                            n_intervals=0
                                                        )
                                                    ])
                                                ], className='four colums'
                                    ),                            
                            html.Div(
                                                [
                                                    html.Div([
                                                        html.H1(id='live-update-startingSalary'),
                                                        dcc.Interval(
                                                            id='interval-component',
                                                            interval=1000, # 2000 milliseconds = 2 seconds
                                                            n_intervals=0
                                                        )
                                                    ])
                                                ], className='four colums'
                                    ),
                            html.Div(
                                                [
                                                    html.Div([
                                                        html.H1(id='live-update-debt'),
                                                        dcc.Interval(
                                                            id='interval-component2',
                                                            interval=1000, # 2000 milliseconds = 2 seconds
                                                            n_intervals=0
                                                        )
                                                    ])
                                                ], className='four colums'
                                    ),
                            html.Div(
                                                [
                                                    html.Div([
                                                        html.H1(id='live-update-mpayment'),
                                                        dcc.Interval(
                                                            id='interval-component3',
                                                            interval=1000, # 2000 milliseconds = 2 seconds
                                                            n_intervals=0
                                                        )
                                                    ])
                                                ], className='four colums'
                                    ),
                            html.Div(
                                                [
                                                    html.Div([
                                                        html.H1(id='live-update-npv'),
                                                        dcc.Interval(
                                                            id='interval-component4',
                                                            interval=1000, # 2000 milliseconds = 2 seconds
                                                            n_intervals=0
                                                        )
                                                    ])
                                                ], className='four colums'
                                    )                                                               

                        ], className='row'
            ),            
    #graphs
    html.Hr(),  # add a horizontal rule
    html.Div(
                        [
                            html.H1(children='Comparison of yearly amounts of minimum wage, starting career salary and mid career salary'),
                            html.Div([                                
                                dcc.Graph(id='live-update-graph'),                                
                                dcc.Interval(
                                    id='interval-component5',
                                    interval=1000, # 2000 milliseconds = 2 seconds
                                    n_intervals=0
                                )
                            ])
                        ], className='ten columns offset-by-one'
            ) 
                    # dcc.Graph(id='scatterplot2',
                    #                     figure = {'data':[
                    #                             go.Scatter(
                    #                             x=random_x,
                    #                             y=random_y,
                    #                             mode='markers',
                    #                             marker = {
                    #                                 'size':12,
                    #                                 'color': 'rgb(200,204,53)',
                    #                                 'symbol':'pentagon',
                    #                                 'line':{'width':2}
                    #                             }
                    #                             )],
                    #                     'layout':go.Layout(title='Second Plot',
                    #                                         xaxis = {'title':'Some X title'})}
                    #                     )
                    #                    ], className="ten columns offset-by-one")
    # #usa map graph
    # html.Div([dcc.Graph(id='mapusa',    
    #                 figure = dict( data=dataMap, layout=layoutMap )
    #                 #py.iplot( fig, filename='d3-cloropleth-map' )
    #                 )],className='ten columns offset-by-one')
], style={'fontFamily':'helvetica', 'fontSize':18})


#Example callbacks

# @app.callback(
#     Output('wheels-output', 'children'),
#     [Input('wheels', 'value')])
# def callback_a(wheels_value):
#     return 'You\'ve selected "{}"'.format(wheels_value)

# @app.callback(
#     Output('colors-output', 'children'),
#     [Input('colors', 'value')])
# def callback_b(colors_value):
#     return 'You\'ve selected "{}"'.format(colors_value)

# @app.callback(
#     Output('display-image', 'src'),
#     [Input('wheels', 'value'),
#      Input('colors', 'value')])
# def callback_image(wheel, color):
#     path = 'images/'
#     return encode_image(path+df[(df['wheels']==wheel) & \
#     (df['color']==color)]['image'].values[0])

#APP callbacks
#name
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'Hi there "{}"'.format(input_value)
#Major
@app.callback(
    dash.dependencies.Output('majors1', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    loans.major=value
    loans.do_all_calculations()
    global attendanceCost
    attendanceCost=loans.calculatedAttendanceCost
    global startingSalary
    print("starting salary callback before", startingSalary)
    startingSalary=loans.calculatedEarlyCareerPay
    print("starting salary callback after", startingSalary)
    global startingDebt
    startingDebt=loans.calculatedStudentLoan
    global monthlyPayments
    monthlyPayments=loans.calculatedTotalPayment
    global estimatedNpv
    estimatedNpv=loans.calculatedNPV
    return 'You have selected "{}"'.format(value)
#university
@app.callback(
    dash.dependencies.Output('universities1', 'children'),
    [dash.dependencies.Input('my-dropdown2', 'value')])
def update_output(value):
    loans.university=value
    loans.do_all_calculations()
    global attendanceCost
    attendanceCost=loans.calculatedAttendanceCost
    global startingSalary
    print("starting salary callback before", startingSalary)
    startingSalary=loans.calculatedEarlyCareerPay
    print("starting salary callback after", startingSalary)
    global startingDebt
    startingDebt=loans.calculatedStudentLoan
    global monthlyPayments
    monthlyPayments=loans.calculatedTotalPayment
    global estimatedNpv
    estimatedNpv=loans.calculatedNPV
    return 'You have selected "{}"'.format(value)
#state of residence
@app.callback(
    dash.dependencies.Output('states1', 'children'),
    [dash.dependencies.Input('my-dropdown3', 'value')])
def update_output(value):
    loans.state_of_residence=value
    loans.do_all_calculations()
    global attendanceCost
    attendanceCost=loans.calculatedAttendanceCost
    global startingSalary
    print("starting salary callback before", startingSalary)
    startingSalary=loans.calculatedEarlyCareerPay
    print("starting salary callback after", startingSalary)
    global startingDebt
    startingDebt=loans.calculatedStudentLoan
    global monthlyPayments
    monthlyPayments=loans.calculatedTotalPayment
    global estimatedNpv
    estimatedNpv=loans.calculatedNPV
    return 'You have selected "{}"'.format(value)
#living with parents
@app.callback(
    dash.dependencies.Output('liveparents1', 'children'),
    [dash.dependencies.Input('my-dropdown4', 'value')])
def update_output(value):
    if value=='No':
        loans.live_with_parents=False
    loans.do_all_calculations()
    global attendanceCost
    attendanceCost=loans.calculatedAttendanceCost
    global startingSalary
    print("starting salary callback before", startingSalary)
    startingSalary=loans.calculatedEarlyCareerPay
    print("starting salary callback after", startingSalary)
    global startingDebt
    startingDebt=loans.calculatedStudentLoan
    global monthlyPayments
    monthlyPayments=loans.calculatedTotalPayment
    global estimatedNpv
    estimatedNpv=loans.calculatedNPV
    return 'You have selected "{}"'.format(value)
#number of college students in household
@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    loans.number_students=value
    loans.do_all_calculations() 
    global attendanceCost
    attendanceCost=loans.calculatedAttendanceCost   
    global startingSalary
    print("starting salary callback before", startingSalary)
    startingSalary=loans.calculatedEarlyCareerPay
    print("starting salary callback after", startingSalary)
    global startingDebt
    startingDebt=loans.calculatedStudentLoan
    global monthlyPayments
    monthlyPayments=loans.calculatedTotalPayment
    global estimatedNpv
    estimatedNpv=loans.calculatedNPV
    return 'You have selected "{}"'.format(value)
#number of people in parents household
@app.callback(
    dash.dependencies.Output('slider-output-container2', 'children'),
    [dash.dependencies.Input('my-slider2', 'value')])
def update_output(value):
    loans.number_household=value
    loans.do_all_calculations()
    global attendanceCost
    attendanceCost=loans.calculatedAttendanceCost
    global startingSalary
    print("starting salary callback before", startingSalary)
    startingSalary=loans.calculatedEarlyCareerPay
    print("starting salary callback after", startingSalary)
    global startingDebt
    startingDebt=loans.calculatedStudentLoan
    global monthlyPayments
    monthlyPayments=loans.calculatedTotalPayment
    global estimatedNpv
    estimatedNpv=loans.calculatedNPV
    return 'You have selected "{}"'.format(value)
#Parents income 
@app.callback(
    dash.dependencies.Output('slider-output-container3', 'children'),
    [dash.dependencies.Input('my-slider3', 'value')])
def update_output(value):
    loans.parent_income=value
    loans.do_all_calculations()
    global attendanceCost
    attendanceCost=loans.calculatedAttendanceCost
    global startingSalary
    print("starting salary callback before", startingSalary)
    startingSalary=loans.calculatedEarlyCareerPay
    print("starting salary callback after", startingSalary)
    global startingDebt
    startingDebt=loans.calculatedStudentLoan
    global monthlyPayments
    monthlyPayments=loans.calculatedTotalPayment
    global estimatedNpv
    estimatedNpv=loans.calculatedNPV
    print("loans.parent_income should be ", value)
    return 'You have selected $"{}"'.format(value)
# #how much will you or your parents contribute 
# @app.callback(
#     dash.dependencies.Output('slider-output-container4', 'children'),
#     [dash.dependencies.Input('my-slider4', 'value')])
# def update_output(value):
#     return 'You have selected $"{}"'.format(value)
#text area 
# @app.callback(
#     dash.dependencies.Output('textarea', 'children'),
#     [dash.dependencies.Input('my-textArea', 'value')])
# def update_output(value):
#     return 'You have selected $"{}"'.format(value)
#summary of calculations
@app.callback(Output('live-update-AttendanceCost', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    global attendanceCost
    #print("starting salary callback live update", startingSalary)        
    return 'Your estimated attendance cost will be: $ {} '.format(attendanceCost)

@app.callback(Output('live-update-startingSalary', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    global startingSalary
    print("starting salary callback live update", startingSalary)        
    return 'Your estimated starting salary after finishing your major will be: $ {} '.format(startingSalary)

@app.callback(Output('live-update-debt', 'children'),
              [Input('interval-component2', 'n_intervals')])
def update_layout(n):
    global startingDebt
    return 'Your estimated debt if you finish your major in 4 years will be:  $ {} '.format(startingDebt)

@app.callback(Output('live-update-mpayment', 'children'),
              [Input('interval-component3', 'n_intervals')])
def update_layout(n):
    global monthlyPayments
    return 'Your estimated monthly payments of a 15 years loan will be: $ {} '.format(monthlyPayments)

@app.callback(Output('live-update-npv', 'children'),
              [Input('interval-component4', 'n_intervals')])
def update_layout(n):
    global estimatedNpv
    return 'The estimated Net Present Value(NPV) of your education will be: $ {} '.format(estimatedNpv)

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component5', 'n_intervals')])
def update_graph(n):
    fig= go.Figure(
        data=[go.Bar(
            x=['Minimum Wage', 'Starting Salary', 'Mid Career Salary'],
            y=[loans.calculatedMinimumWage, loans.calculatedEarlyCareerPay, loans.calculatedMidCareerPay],
            marker=dict(
                color=['rgba(17,17,17,1)', 'rgba(234,255,0,1)',
               'rgba(255,145,0,1)']),
        )
        ]
    )
    return fig

###MAIN Method
if __name__ == '__main__':
    app.run_server()
