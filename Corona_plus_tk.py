import os
from tkinter import filedialog
import tkinter as tk
import COVID19Py as cvd
import pandas as pd
import matplotlib.pyplot as plt
###
cvd19 = cvd.COVID19()
latest =cvd19.getLatest()
ratio = latest['deaths']/latest['confirmed']
###
###
root= tk.Tk()
root.title('COVID CONSULTING PLATFORM - by Haller (GLA7)')
canvas1 = tk.Canvas(root, width = 400, height = 500,  relief = 'raised')
canvas1.pack()
label1 = tk.Label(root, text='COVID PLATFORM')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
label2 = tk.Label(root, text='TWO LETTERS CODE: ')
label3 = tk.Label(root, text='CURRENT SITUATION:')
label3.config(font=('helvetica', 12))
#
label4 = tk.Label(root, text='Confirmed: {}\n\nDeaths: {}\n'.format(latest['confirmed'],latest['deaths']))
label4.config(font=('helvetica', 10))
label5 = tk.Label(root, text='Ratio (Deaths/Confirmed): {0:.2f} %\n'.format(ratio*100))
label5.config(font=('helvetica', 10))
#
label2.config(font=('helvetica', 12))
canvas1.create_window(200, 100, window=label2)
canvas1.create_window(200, 300, window=label3)#
canvas1.create_window(200, 350, window=label4)
canvas1.create_window(200, 400, window=label5)
entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

def cvd_consulting():
    country_code_dict = {'AD' : 'Andorra','AE' : 'United Arab Emirates','AF' : 'Afghanistan','AG' : 'Antigua and Barbuda',
    'AI' : 'Anguilla','AL' : 'Albania','AM' : 'Armenia','AO' : 'Angola','AQ' : 'Antarctica','AR' : 'Argentina','AS' : 'American Samoa',
    'AT' : 'Austria','AU' : 'Australia','AW' : 'Aruba','AX' : 'Åland Islands','AZ' : 'Azerbaijan','BA' : 'Bosnia and Herzegovina',
    'BB' : 'Barbados','BD' : 'Bangladesh','BE' : 'Belgium','BF' : 'Burkina Faso','BG' : 'Bulgaria','BH' : 'Bahrain','BI' : 'Burundi',
    'BJ' : 'Benin','BL' : 'Saint Barthélemy','BM' : 'Bermuda','BN' : 'Brunei Darussalam','BO' : 'Bolivia (Plurinational State of)',
    'BQ' : 'Bonaire','BR' : 'Brazil','BS' : 'Bahamas','BT' : 'Bhutan','BV' : 'Bouvet Island','BW' : 'Botswana','BY' : 'Belarus',
    'BZ' : 'Belize','CA' : 'Canada','CC' : 'Cocos (Keeling) Islands','CD' : 'Congo','CF' : 'Central African Republic','CG' : 'Congo',
    'CH' : 'Switzerland','CI' : "Côte d'Ivoire",'CK' : 'Cook Islands','CL' : 'Chile','CM' : 'Cameroon','CN' : 'China','CO' : 'Colombia',
    'CR' : 'Costa Rica','CU' : 'Cuba','CV' : 'Cabo Verde','CW' : 'Curaçao','CX' : 'Christmas Island','CY' : 'Cyprus','CZ' : 'Czechia',
    'DE' : 'Germany','DJ' : 'Djibouti','DK' : 'Denmark','DM' : 'Dominica','DO' : 'Dominican Republic','DZ' : 'Algeria','EC' : 'Ecuador',
    'EE' : 'Estonia','EG' : 'Egypt','EH' : 'Western Sahara','ER' : 'Eritrea','ES' : 'Spain','ET' : 'Ethiopia','FI' : 'Finland','FJ' : 'Fiji',
    'FK' : 'Falkland Islands (Malvinas)','FM' : 'Micronesia (Federated States of)','FO' : 'Faroe Islands','FR' : 'France',
    'GA' : 'Gabon','GB' : 'United Kingdom of Great Britain and Northern Ireland','(.uk)' : 'ISO 3166-2:GB','GD' : 'Grenada',
    'GE' : 'Georgia','GF' : 'French Guiana','GG' : 'Guernsey','GH' : 'Ghana','GI' : 'Gibraltar','GL' : 'Greenland','GM' : 'Gambia',
    'GN' : 'Guinea','GP' : 'Guadeloupe','GQ' : 'Equatorial Guinea','GR' : 'Greece','GS' : 'South Georgia and the South Sandwich Islands',
    'GT' : 'Guatemala','GU' : 'Guam','GW' : 'Guinea-Bissau','GY' : 'Guyana','HK' : 'Hong Kong','HM' : 'Heard Island and McDonald Islands',
    'HN' : 'Honduras','HR' : 'Croatia','HT' : 'Haiti','HU' : 'Hungary','ID' : 'Indonesia','IE' : 'Ireland','IL' : 'Israel','IM' : 'Isle of Man',
    'IN' : 'India','IO' : 'British Indian Ocean Territory','IQ' : 'Iraq','IR' : 'Iran (Islamic Republic of)','IS' : 'Iceland','IT' : 'Italy',
    'JE' : 'Jersey','JM' : 'Jamaica','JO' : 'Jordan','JP' : 'Japan','KE' : 'Kenya','KG' : 'Kyrgyzstan','KH' : 'Cambodia','KI' : 'Kiribati',
    'KM' : 'Comoros','KN' : 'Saint Kitts and Nevis','KP' : "Korea (Democratic People's Republic of)",'KR' : 'Korea','KW' : 'Kuwait',
    'KY' : 'Cayman Islands','KZ' : 'Kazakhstan','LA' : "Lao People's Democratic Republic",'LB' : 'Lebanon','LC' : 'Saint Lucia','LI' : 'Liechtenstein',
    'LK' : 'Sri Lanka','LR' : 'Liberia','LS' : 'Lesotho','LT' : 'Lithuania','LU' : 'Luxembourg','LV' : 'Latvia','LY' : 'Libya','MA' : 'Morocco',
    'MC' : 'Monaco','MD' : 'Moldova','ME' : 'Montenegro','MF' : 'Saint Martin (French part)','MG' : 'Madagascar','MH' : 'Marshall Islands',
    'MK' : 'North Macedonia','ML' : 'Mali','MM' : 'Myanmar','MN' : 'Mongolia','MO' : 'Macao','MP' : 'Northern Mariana Islands',
    'MQ' : 'Martinique','MR' : 'Mauritania','MS' : 'Montserrat','MT' : 'Malta','MU' : 'Mauritius','MV' : 'Maldives','MW' : 'Malawi',
    'MX' : 'Mexico','MY' : 'Malaysia','MZ' : 'Mozambique','NA' : 'Namibia','NC' : 'New Caledonia','NE' : 'Niger','NF' : 'Norfolk Island',
    'NG' : 'Nigeria','NI' : 'Nicaragua','NL' : 'Netherlands','NO' : 'Norway','NP' : 'Nepal','NR' : 'Nauru','NU' : 'Niue','NZ' : 'New Zealand',
    'OM' : 'Oman','PA' : 'Panama','PE' : 'Peru','PF' : 'French Polynesia','PG' : 'Papua New Guinea','PH' : 'Philippines','PK' : 'Pakistan',
    'PL' : 'Poland','PM' : 'Saint Pierre and Miquelon','PN' : 'Pitcairn','PR' : 'Puerto Rico','PS' : 'Palestine','PT' : 'Portugal',
    'PW' : 'Palau','PY' : 'Paraguay','QA' : 'Qatar','RE' : 'Réunion','RO' : 'Romania','RS' : 'Serbia','RU' : 'Russian Federation',
    'RW' : 'Rwanda','SA' : 'Saudi Arabia','SB' : 'Solomon Islands','SC' : 'Seychelles','SD' : 'Sudan','SE' : 'Sweden','SG' : 'Singapore',
    'SH' : 'Saint Helena','SI' : 'Slovenia','SJ' : 'Svalbard and Jan Mayen','SK' : 'Slovakia','SL' : 'Sierra Leone','SM' : 'San Marino',
    'SN' : 'Senegal','SO' : 'Somalia','SR' : 'Suriname','SS' : 'South Sudan','ST' : 'Sao Tome and Principe','SV' : 'El Salvador',
    'SX' : 'Sint Maarten (Dutch part)','SY' : 'Syrian Arab Republic','SZ' : 'Eswatini','TC' : 'Turks and Caicos Islands','TD' : 'Chad',
    'TF' : 'French Southern Territories','TG' : 'Togo','TH' : 'Thailand','TJ' : 'Tajikistan','TK' : 'Tokelau','TL' : 'Timor-Leste',
    'TM' : 'Turkmenistan','TN' : 'Tunisia','TO' : 'Tonga','TR' : 'Turkey','TT' : 'Trinidad and Tobago','TV' : 'Tuvalu',
    'TW' : 'Taiwan','TZ' : 'Tanzania','UA' : 'Ukraine','UG' : 'Uganda','UM' : 'United States Minor Outlying Islands',
    'US' : 'United States of America','UY' : 'Uruguay','UZ' : 'Uzbekistan','VA' : 'Holy See','VC' : 'Saint Vincent and the Grenadines',
    'VE' : 'Venezuela (Bolivarian Republic of)','VG' : 'Virgin Islands (British)','VI' : 'Virgin Islands (U.S.)','VN' : 'Viet Nam',
    'VU' : 'Vanuatu','WF' : 'Wallis and Futuna','WS' : 'Samoa','YE' : 'Yemen','YT' : 'Mayotte','ZA' : 'South Africa','ZM' : 'Zambia'}
    country_code = entry1.get()
    if country_code == "":
        exit()
    cvd19 = cvd.COVID19()
    country  = cvd19.getLocationByCountryCode(country_code, timelines=True)
    index = country[0]['timelines']['confirmed']
    index = index['timeline'].keys()
    confirm = country[0]['timelines']['confirmed']
    confirm = confirm['timeline'].values()
    deaths = country[0]['timelines']['deaths']
    deaths = deaths['timeline'].values()
    df = pd.DataFrame(data = {'confirmed': list(confirm),
                                'deaths': list(deaths)},
                                index = pd.to_datetime(list(index)))
    df.plot(title='{} coronavirus victims - John Hopkins'.format(country_code_dict[country_code]),rot=30)
    plt.xlabel('Days')
    plt.ylabel('Cases')
    plt.tight_layout()
    plt.show()

button1 = tk.Button(text='CONSULT!', command=cvd_consulting, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.mainloop()