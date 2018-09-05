import requests
import json

## Get account details by providing the account name
def requestSummonerData(summonerName, APIKey):
	URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
	response = requests.get(URL)
	return response.json()

## Get an account's ranked match data by account ID
def requestRankedData(ID, APIKey):
	URL = "https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/" + str(ID) + "?api_key=" + APIKey
	response = requests.get(URL)
	return response.json()
	
def main():
  ## Parameters
	summonerName = "<username_here>"
	APIKey = "<riot_games_api_key_here>"
	
	summonerData  = requestSummonerData(summonerName, APIKey)
	
	# Uncomment this line if you want a pretty JSON data dump
	#print(json.dumps(summonerData, sort_keys=True, indent=2))
	
	## Print to the console some basic account information
	print("\n\nSummoner Name:\t" + str(summonerData ['name']))
	print("Level:\t\t" + str(summonerData ['summonerLevel']))
	
	## Pull the ID field from the response data, cast it to an int
	ID = int(summonerData ['id'])
	
	rankedData = requestRankedData(ID, APIKey)
	# Uncomment this line if you want a pretty JSON data dump
	#print(json.dumps(rankedData, sort_keys=True, indent=2))

	# Get some information form the ranked match data, and do some really basic math
	wins = rankedData [1]['wins']
	losses = rankedData [1]['losses']
	ratio = wins / (wins + losses)
	
	# Display some information about the account's rank and stats to the console
	print("Rank:\t\t" + rankedData [1]['tier'] + " " + rankedData [1]['rank'] + " " + str(rankedData [1]['leaguePoints']) + " LP")
	print("W/L:\t\t" + str(wins) + "/" + str(losses))
	print("W/L Ratio:\t" + str(round((ratio) * 100.0, 2)) + "%\n")

	# Some really endearing or supportive messaging, conditionally based on their recent games
	hotStreak = rankedData [1]['hotStreak']
	if hotStreak:
		print("Based on recent games, you must be a smurf because you've been on fire lately!!")
	else:
		print("Based on recent games, you are either boosted or stuck in ELO hell.")
		
	
if __name__ == "__main__":
	main()
