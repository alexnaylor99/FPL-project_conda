'''
FPL Project - API Call
Last Updated: 15:20:00 09/06/2022

Classes that can be used to call the Fantasy Premier League API for player data
'''

import requests
import pandas as pd
import time

class GeneralAPICall:
    """
    Class can be used to make general FPL API call.
    API Documentation: https://www.npmjs.com/package/fpl-api
    """
            
    def __init__(self, general_url):
        """
        Parameters
        
        ----
        general_url : string
            API URL
        """
        self.general_url = general_url
        
    def total_players(self):
        """
        Returns general player information.
        
        Returns
        -----
        total_players : pandas DataFrame
            DataFrame consisting of player information for all players in Premier League
        """
        
        request = requests.get(self.general_url)
     
        json = request.json()
        
        total_players = pd.DataFrame(json["elements"])
        
        return total_players

class DetailedAPICall(GeneralAPICall):
    """
    Inherited class from GeneralAPICall. Used to make detailed API call.
        
    Parameters
    ----
    GeneralAPICall : class
        Class for making general API calls
    """

    def __init__(self, detailed_element_url):
        """
        Parameters
        
        ----
        detailed_element_url : string 
            Detailed element URL
        """
        
        self.detailed_element_url = detailed_element_url

    def player_ids(self, total_players_df):
        """
        Returns Player IDs
        
        Parameters
        ----
        total_players_df : pandas DataFrame
            DataFrame containing basic details on all players
        
        Returns 
        ----
        id_list : list
            List of Player IDs
        """
        
        id_list = list(total_players_df.id)

        return id_list
        
    def detailed_total_players(self, id_list):
        """
        Returns detailed player data as a Pandas DataFrame
        
        Parameters
        ----
        id_list : list
            List of player IDs
            
        Returns 
        ----
        detailed_player_df : pandas DataFrame
            DataFrame consisting of detailed player information
        """
        
        start_time = time.time()
        
        detailed_player_df = pd.DataFrame()
        
        for id in id_list:
            # Need to make individual API call for each Player ID
            
            full_url = self.detailed_element_url + str(id) + '/'
            
            request = requests.get(full_url)
            
            json = request.json()
            
            detailed_df = pd.DataFrame(json['history'])
            
            detailed_player_df = detailed_player_df.append(detailed_df)
            
        print('Runtime: ', time.time() - start_time)
            
        return detailed_player_df



