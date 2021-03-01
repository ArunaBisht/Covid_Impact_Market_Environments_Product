from flask import Flask, render_template, request, jsonify
import pandas as pd
from pathlib import Path as p

house_path = p('house_data.csv')
total_df = pd.read_csv(house_path,delimiter=',', header=None, skiprows=1, names=['state','county','city','city_size','less_than_$50000','$50000_to_$99999','$100000_to_$149999','$150000_to_$199999','$200000_to_$299999','$300000_to_$499999','$500000_to_$999999','$1000000_or_more','white','black','native','asian','pacific','hispanic','race_white','race_black','race_native_american','race_asian','race_pacific_islander','race_some_other_race','race_hispanic','diversity','population_total','diversity_score','median_age','median_household_income','median_personal_income','aggreculture','construction','manufacturing','wholesale','retail','warehousing','utilities','information','finance','real_estate','technical_services','corporate_management','administration','education','health_care','arts_entertainment','accomodation','public_administration','aggreculture_f','construction_f','manufacturing_f','wholesale_f','retail_f','warehousing_f','utilities_f','information_f','finance_f','real_estate_f','technical_services_f','corporate_management_f','administration_f','education_f','health_care_f','arts_entertainment_f','accomodation_f','public_administration_f','1-unit_detached','1-unit_attached','2_units','3_or_4_units','5_to_9_units','10_to_19_units','20_or_more_units','unemployment_rate','0_bedroom','1_bedroom','2_bedrooms','3_bedrooms','4_bedrooms','5_or_more_bedrooms','0_vehicles_available','1_vehicle_available','2_vehicles_available','3_or_more_vehicles_available','under_5_years','5_to_9_years','10_to_14_years','15_to_19_years','20_to_24_years','25_to_29_years','30_to_34_years','35_to_39_years','40_to_44_years','45_to_49_years','50_to_54_years','55_to_59_years','60_to_64_years','65_to_69_years','70_to_74_years','75_to_79_years','80_to_84_years','85_years_and_over'])

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/data', methods = ['POST'])
def hello_world():
    data = request.form
    form_culture = data['culture']
    form_city_size = data['city_size']
    form_cultural_identity = data['choice']
    form_diversity = data['diversity']
    form_household_income = float(data['household_income'])
    form_personal_income = float(data['personal_income'])
    form_sex = data['sex']
    form_age = data['age']
    form_mortgage = data['mortgage']
    form_children = data['children'] #change to be column name
    form_industry = data['industry'] #change to be column name
    form_bedrooms = data['bedrooms'] #change to be column name
    form_vehicles = data['vehicles'] #change to be column name
    form_mortgage = data['mortgage']
    form_house_type = data['house_type']

    df_form_city_size = total_df['city_size']
    df_form_mortgage = total_df[form_mortgage]
    df_form_cultural_identity = total_df[form_cultural_identity]
    df_form_industry = total_df[form_industry].astype(float)
    df_form_house_type = total_df[form_house_type]
    df_form_bedrooms = total_df[form_bedrooms]
    df_form_vehicles = total_df[form_vehicles]
    df_state = total_df['state']
    df_county = total_df['county']
    df_city = total_df['city']
    df_race_white = total_df['race_white']*100
    df_race_black = total_df['race_black']*100
    df_race_native_american = total_df['race_native_american']*100
    df_race_asian = total_df['race_asian']*100
    df_race_pacific_islander = total_df['race_pacific_islander']*100
    df_race_hispanic = total_df['race_hispanic']*100
    df_diversity = total_df['diversity']
    df_population_total = total_df['population_total']
    df_diversity_score = total_df['diversity_score'].astype(float)
    df_median_age = total_df['median_age'].astype(float)
    df_unemployment_rate = total_df['unemployment_rate']*100
    df_median_household_income = total_df['median_household_income'].astype(float)
    df_median_personal_income = total_df['median_personal_income'].astype(float)
    personal_income_difference = (form_personal_income - df_median_personal_income)


    results = total_df.loc[(total_df['city_size'] == data['city_size'])&(total_df['city_size'] == data['city_size'])]
    results = results[['city','population_total','median_age', 'median_household_income','median_personal_income', form_industry,form_bedrooms,form_vehicles,form_mortgage,form_cultural_identity,'diversity_score','race_hispanic','race_black','race_white','race_asian','race_pacific_islander' ]]
    html = results.to_html()
    return html

if __name__ == '__main__':
    app.run(debug=True)
