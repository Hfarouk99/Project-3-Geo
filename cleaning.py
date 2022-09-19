def Company_in_cali(c):
    filter_ = {'$and':[{'offices': {'$exists': 1}},{'offices.latitude':{'$type':1}},{'offices.longitude':{'$type': 1}}]}
    projection = {"_id":0,'name':1,'founded_year':1,'offices.country_code':1,"offices.state_code":1,'offices.city':1,'offices.address1':1,'offices.address2':1,'offices.latitude':1,'offices.longitude':1}
    sorting = {'offices.country_code':-1}
    lis = list(companies.find(filter_, projection).sort("offices.country_code", -1))
    df = pd.DataFrame(lis).explode("offices").reset_index(drop=True)
    df = pd.concat([df, df["offices"].apply(pd.Series)], axis=1).reset_index(drop=True)
    df.dropna(subset=["latitude"],inplace=True)
    df.dropna(subset=["founded_year"],inplace=True)
    df.dropna(subset=["address1"],inplace=True)
    df.dropna(subset=["address2"],inplace=True)
    df.dropna(subset=["city"],inplace=True)
    newcols = [element for element in df.columns if element != 'offices']
    df=df[newcols].reset_index(drop=True)
    df=df[df["country_code"]=="USA"]
    df=df[df['state_code'] == 'CA'].reset_index(drop=True)
    df = df.drop(columns="founded_year")
    return df

def Heat_map_cali(df,radius):
    m = folium.Map(location = [34.0218593,-118.498265], zoom_start=10)
    HeatMap(data=df[["latitude","longitude"]],radius=radius).add_to(m)
    return m

def querySM(query, location, radius):

    if " " in query.strip():
           query_ok = query.strip().replace(" ","%20")
    else:
           query_ok = query
    url = f"https://api.foursquare.com/v3/places/search?query={query_ok}&ll={str(location[0]).strip()}%2C{str(location[1]).strip()}&radius={radius}&limit=50"
    headers =  {"Accept": "application/json","Authorization":  f"{client_key}"
    }
    response = requests.get(url, headers=headers)
    
    if response:
        response=response.json()['results']
        places_list = [ {"name" : i["name"],
                      "lat"  : i["geocodes"]["main"]["latitude"],
                      "long" : i["geocodes"]["main"]["longitude"],
                      "type" : {"typepoint":
                                  {"type": "Point",
                                   "coordinates": [lat, lon]}}} for i in response]
    return places_list
def queryAirport(query, location, radius):

    if " " in query.strip():
           query_ok = query.strip().replace(" ","%20")
    else:
           query_ok = query
    url = f"https://api.foursquare.com/v3/places/search?query={query_ok}&ll={str(location[0]).strip()}%2C{str(location[1]).strip()}&radius={radius}&categories=19040&limit=50"
    headers =  {"Accept": "application/json","Authorization":  f"{client_key}"
    }
    response = requests.get(url, headers=headers)
    
    if response:
        response=response.json()['results']
        places_list = [ {"name" : i["name"],
                      "lat"  : i["geocodes"]["main"]["latitude"],
                      "long" : i["geocodes"]["main"]["longitude"],
                      "type" : {"typepoint":
                                  {"type": "Point",
                                   "coordinates": [lat, lon]}}} for i in response]
    return places_list
    
def queryStadium(query, location, radius):

    if " " in query.strip():
           query_ok = query.strip().replace(" ","%20")
    else:
           query_ok = query
    url = f"https://api.foursquare.com/v3/places/search?query={query_ok}&ll={str(location[0]).strip()}%2C{str(location[1]).strip()}&radius={radius}&limit=1"
    headers =  {"Accept": "application/json","Authorization":  f"{client_key}"
    }
    response = requests.get(url, headers=headers)
    
    if response:
        response=response.json()['results']
        places_list = [ {"name" : i["name"],
                      "lat"  : i["geocodes"]["main"]["latitude"],
                      "long" : i["geocodes"]["main"]["longitude"],
                      "type" : {"typepoint":
                                  {"type": "Point",
                                   "coordinates": [lat, lon]}}} for i in response]
    return places_list
def C_C(col,q,r,df):
    lis=[]
    for i in range(len(df)):
        if querySM(q,[df.iloc[i][1], df.iloc[i][2]],r):
            lis.append(querySM(q,[df.iloc[i][1], df.iloc[i][2]],r))
        else:
            lis.append(py.nan)
    dic ={col:lis}
    dff= pd.DataFrame.from_dict(dic)
    return dff
def C_A(col,q,r,df):
    lis=[]
    for i in range(len(df)):
        if queryAirport(q,[df.iloc[i][1], df.iloc[i][2]],r):
            lis.append(queryAirport(q,[df.iloc[i][1], df.iloc[i][2]],r))
        else:
            lis.append(py.nan)
    dic ={col:lis}
    dff= pd.DataFrame.from_dict(dic)
    return dff
def C_S(col,q,r,df):
    lis=[]
    for i in range(len(df)):
        if queryStadium(q,[df.iloc[i][1], df.iloc[i][2]],r):
            lis.append(queryStadium(q,[df.iloc[i][1], df.iloc[i][2]],r))
        else:
            lis.append(py.nan)
    dic ={col:lis}
    dff= pd.DataFrame.from_dict(dic)
    return dff