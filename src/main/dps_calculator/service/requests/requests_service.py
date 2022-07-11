from model.player.level_model import Skills, Levels
import requests

class RequestsService:

    @classmethod
    def __fetch_player(cls, player_name: str, load_from_file = False):
        """Do a get request to osrs hiscores with the specified player name.

        Args:
            player_name (str): The player name.
            load_from_file (bool, optional): If set to True, instead of doing a request
            to the OSRS hiscores, it is going to use an default file named
            <hiscore_response.txt>. Defaults to False.

        Returns:
            list[str]: Returns a list containing each line of the response.
            None: If an error occurs whith the request or with loading from the file.
        """

        if load_from_file:
            try:
                f = open("hiscore_response.txt", "r")
            except:
                print("Couldn't find template file <hiscore_response.txt>.")
                return
            else:
                response_list = f.read().split("\n")
                return response_list
        else:
            r = requests.get(f'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={player_name.replace(" ", "%20")}')
            if r.status_code == 200:
                return r.text.split("\n")
            if r.status_code == 404:
                print("Couldn't find player with the specified name.")
                return

            print("The OSRS hiscores might be down. Try again later.")
                  
    @classmethod
    def fetch_player_levels(cls, player_name = ""):
        """Fetch the player levels from OSRS hiscores.

        Args:
            player_name (str, optional): The name of the player. If no name is provided,
            than the levels returned are going to be loaded from a template file.

        Returns:
            Levels: Returns a level object with each level set to the ones from the response.
            None: If an error occurred while fetching the player.
        """

        if player_name == "":
            print("No name specified at fetch_player_levels(). Using default response from <hiscore_response.txt>.")
            response_list = cls.__fetch_player(player_name, load_from_file = True)
        else:
            response_list = cls.__fetch_player(player_name)

        if response_list == None:
            return

        player_levels = Levels()
        i = 0
        player_unprocessed_levels = response_list[1:24]
        for skill in Skills:
            player_skill_info = player_unprocessed_levels[i].split(",")
            # player_skill_info index:  [0] = rank | [1] = level | [2] = experience
            player_levels.set_level(skill, player_skill_info[1])
            i += 1
        
        return player_levels