import subprocess
import re

# Define variables used for processing
filler_flag = True
filler_list = []
path = '/share/MD0Data/Multimedia/Serien/Anime-Cartoon/OnePiece/'
l = '50-51,54-60,93,98-99,101-102,131-143,196-206,213-216,220-226,279-283,291-292,303,317-319,326-336,382-384,406-407,426-429,457-458,492,497-499,506,542,575-578,590,626-628,653'
l = l.split(',')

# Format l to receive a well sorted list
for i in l:
    if re.search('-', i):
        print(i)
        mini = int(i.split('-')[0])
        maxi = int(i.split('-')[1]) + 1
        for j in range(mini, maxi):
            filler_list.append(j)
    else:
        filler_list.append(i)

# Checks if the current episode is a filler
cmd = 'cat /home/robby/Documents/episode_crawler/episode'
current_episode = int(subprocess.call(cmd))
while filler_flag is True:
    print('Current Episode is: One Piece - Episode ' + current_episode)
    if current_episode in filler_list:
        filler_flag = True
        print('But it is a filler episode. Checking next episode.')
        current_episode = current_episode + 1
    elif current_episode not in filler_list:
        filler_flag = False
        print('Episode is not a filler. Initiate replay...')
    else:
        raise OnePieceException('The Episode is not an integer, otherwise it would have been successfull filtered.')

# Initiates the current episode via VLC
cmd = 'll ' + path + ' | grep ' + current_episode + ' | tr -s " " | cut -d " " -f9'
dir = subprocess.call(cmd)
path = path + dir + '/'
cmd = 'll ' + path + ' | grep '
full_file_path = dir = subprocess.call(cmd) 

subprocess.call('vlc --fullscreen --no-sub-autodetect-file ' + full_file_path)
