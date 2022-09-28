print("help me")
print("hi")
type("hi")
type("hello world")
type(3.78899999999)
type(-5)
type(pi)
ballots = (4, 18)
type(ballots)
help("keywords")
listt = [1, 2, 'three']
my_list = list()
counties = ["Arapahoe", "Denver", 'Jefferson']
counties
counties[0]
counties[-2]
len(counties)
counties.append('El Paso')
counties
counties.insert(2,'El Paso')
counties.remove('El Paso')
counties.pop(3)
counties[2] = "El Paso"
counties.append('El Paso')
counties.remove('Arapahoe')
counties[2] = 'Denver'
counties[1] = 'Jefferson'
counties.append('Arapahoe')
counties.remove('Denver')
counties[1] = 'El Paso'
counties
my_tuple = tuple()
counties_tuple = ('Arapahoe', 'Denver', 'Jefferson')
counties_tuple[:-1]
#creating a dictionary 
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
#length of dict
len(counties_dict)
#get all keys and values
counties_dict.items()
#getting all keys 
counties_dict.keys()
#getting all values 
counties_dict.values()
#specific values 
counties_dict.get("Denver")
#dictionary_name[key], strings must be in single or double quotes
counties_dict['Arapahoe']


#create empty list
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#return list of dictionarites
voting_data

#practice
voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})

voting_data.insert(2,{"county":"Denver", "registered_voters": 463353})
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data


