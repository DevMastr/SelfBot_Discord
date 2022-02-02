import requests
import json


class SelfBot_RAID_Server():
    """
    Author: DevMaster
    This class contains functions to use in Servers
    """

    def __init__(self,token:str):
        self.token = token
        self.headers = {"Authorization": self.token}

    def send_message_server(self,message:str,channel_ID:str): # send messages in a specific channel
        payload = {"content": message}
        r = requests.post(f'https://discord.com/api/v6/channels/{str(channel_ID)}/messages', json=payload,
                        headers=self.headers)
        return json.loads(r.content)

    def join_server(self,invite:str): # join in server with invite
        """
        :1 param str invite: Invitation Code
        """
        invite = invite[-8::]
        r = requests.post(f"https://discordapp.com/api/v6/invites/{invite}",headers=self.headers)
        return r.json()

    def create_invite(self,channel_id):
        return requests.post(f"https://discordapp.com/api/v6/channels/{channel_id}/invites",headers=self.headers)

    def leave_guild(self,guild_ID):
        return requests.delete(f"https://discordapp.com/api/v6/users/@me/guilds/{guild_ID}",headers=self.headers)

    def delete_all_channels(self,guild_ID):
        r_channels = requests.get(f"https://discordapp.com/api/v6/guilds/{guild_ID}/channels",headers=self.headers)
        for x in r_channels.json():
            r_channels_delete = requests.delete(f"https://discordapp.com/api/v6/channels/{x['id']}",headers=self.headers)
        return r_channels_delete

    def edit_name_channels(self,guild_ID,new_Name): # edit name of channels in server
        payload = {"name": new_Name}
        r_channels = requests.get(f"https://discordapp.com/api/v6/guilds/{guild_ID}/channels",headers=self.headers)
        for x in r_channels.json():
            r_channels_edit = requests.patch(f"https://discordapp.com/api/v6/channels/{x['id']}",headers=self.headers,json=payload)

        return r_channels_edit


class SelfBot_RAID_DM(SelfBot_RAID_Server):
    """
    Author: DevMaster
    This class contains functions to use in DM
    """

    def __init__(self, token):
        super().__init__(token)
        self.headers = {"Authorization": self.token}

    def send_DM_message(self, message, userid):
        payload = {'recipient_id': str(userid)}
        src = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=self.headers,json=payload)
        
        dm_json = json.loads(src.content) #get your ID 
        payload = {"content": message}
        r = requests.post(f"https://discordapp.com/api/v6/channels/{dm_json['id']}/messages", headers=self.headers, json=payload)

        return json.loads(r.content)

    def create_new_DM(self,user_ID):
        payload = {"recipient_id": user_ID}
        r = requests.post("https://discordapp.com/api/v6/users/@me/channels", headers=self.headers,json=payload)
        return r.json()

    '''def send_friend_request(self,username: str, discriminator: int):
        """
        :1 param str username: username from someone on discord without '#'
        :2 param int discriminator: discriminator, numbers after "#"
        """
        url = f"https://discord.com/api/v9/users/@me/relationships"
        body = {"username": username, "discriminator": discriminator}
        res = requests.post(url, headers=self.headers,json=body)
        return res'''
        #Essa função tem alto potencial de BANIMENTO, utilize se quiser!


class SelfBot_RAID(SelfBot_RAID_DM):
    """
    Author: DevMaster
    :param str: Token that you will use
    """
    def __init__(self, token:str):
        super().__init__(token)
        self.headers = {"Authorization": self.token}


if __name__ == "__main__":
    SelfBot_RAID()







