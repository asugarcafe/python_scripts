# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 11:46:37 2025

@author: sucre
"""
import random
import zipfile, os
from datetime import datetime, timedelta

def generate_target_anonymous_label(length, rando):
    label_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    halfway = int(length/2)
    result = ''
    for x in range(0,halfway):
        result = result + rando.choice(label_chars)
    result = result + '-'
    for x in range(halfway, length):
        result = result + rando.choice(label_chars)
    return result

def get_random_target(pool, existing, rando):
    choice = rando.choice(pool)
    while choice in existing:
        choice = rando.choice(pool)
    return choice

primes_short = [2,3,5,7,11,13] # just some small prime numbers
primes_long = [2029,3023,5393,7591,1171,1319] # just some 4-digit prime numbers
key_length = 8 # number of characters to use in the label

coin = [True, False]
target_objects = ['the S&P 500 index price at market close', 'the Silver Futures price at market close', 'the JP225 index price at market close', 'the SHANGHAI index price at market close', 'the Dow Jones Industrial Average price at market close'] #put the targets here
placebo_objects = ['the CNN Fear & Greed Index daily score', 'the Daily News Sentiment Index daily score', 'the S&P 500 Index Put/Call Ratio for the day', 'the US Cocoa (CCZ5) price at market close'] #put targets here that arent the goal but lower expectations
#metrics = ['Up or down change']
time_intervals = [5,7,10,14] # in days
number_of_rounds = [3,4,5] #number of time periods to create RV targets for, number of RV targets will be this number minus 1
min_start_date = datetime(2025,12,1)
min_end_date = min_start_date + timedelta(days=90)

'''
Idea: by switching this from up/down to true/false I might be able to turn this into an app.
    this would also reduce the possibility of test subjects figuring out what they are RVing
    binary choices to provide the user: 
        plus or minus, red or black, red or green, positive or negative, one or zero,top or bottom, yin or yang
        you might be able to apply a set of binary choices to the types of changes being guessed at
'''

##create RNG
rand = random.Random()

##run the RNG a few times to warm it up
rng_spinner = 0
for x in range(0,rand.choice(primes_short) + rand.choice(primes_short)):
    rng_spinner = rng_spinner + rand.randrange(rand.choice(primes_short), rand.choice(primes_long))
chosen_interval = rand.choice(time_intervals)
chosen_number_of_rounds = rand.choice(number_of_rounds)

##First, choose the targets and placebos
targs = []
##add a desired target
targs.append(get_random_target(target_objects,targs,rand))
##add a placebo target
targs.append(get_random_target(placebo_objects,targs,rand))
##add 2 more desired or placebo targets
for x in range(0,2):
    if rand.choice(coin):
        targs.append(get_random_target(target_objects,targs,rand))
    else:
        targs.append(get_random_target(placebo_objects,targs,rand))

##Next, apply a metric to check by target

##Next, choose the start date and interval dates
new_start_date = min_start_date + timedelta(days=rand.choice(primes_short))
new_end_date = min_end_date + timedelta(days=rand.choice(primes_short) + rand.choice(primes_short))
target_pool_dates = {}
for target in targs:
    targ_dates = []
    interval_date = new_start_date + timedelta(days=chosen_interval)
    targ_dates.append(interval_date)
    for d in range(1,chosen_number_of_rounds):
        interval_date = interval_date + timedelta(days=chosen_interval)
        targ_dates.append(interval_date)
    target_pool_dates[target] = targ_dates


##Next, for each target and dates generate identifier keys
target_pool_keys = {}
for target in targs:
    targ_keys = []
    last_date = None
    curr_date = None
    for date in target_pool_dates[target]:
        curr_date = date
        if last_date is not None:
            dr_str = f'The direction of change of {target} from the day {last_date:%Y-%m-%d} to the day {curr_date:%Y-%m-%d}'
            date_keys = []
            for k in range(0,3): # 3 keys for each date
                key = generate_target_anonymous_label(key_length, rand)
                while key in target_pool_keys.keys():
                    key = generate_target_anonymous_label(key_length, rand)
                target_pool_keys[key] = dr_str
            
        
        last_date = curr_date
            
##Next, put the targets in a zip file
zip_name = ''
target_files = []
label_files = []
output_folder = 'C:/Repos/github_asugarcafe/python_scripts/General Scripts/RV_tools/files/'
ordered_key_list = output_folder + 'ordered_keys.txt'
with open(ordered_key_list, 'w') as k:
    random_list_of_keys = list(target_pool_keys.keys())
    for x in range(0,10):
        rand.shuffle(random_list_of_keys)

    counter = 0
    for x in range(0,len(random_list_of_keys)):        
        key = random_list_of_keys[x]
        k.write(f'{counter:02d} - ' + key + '\n')

        target_file_name = output_folder + key + '.txt'
        label_file_name = output_folder + f'{counter:02d}' + '.txt'

        #create the labeled target file
        with open(target_file_name, 'w') as f:
            f.write(target_pool_keys[key])

        #create the order file for the next target
        with open(label_file_name, 'w') as f:
            f.write(key)

        target_files.append(target_file_name)
        label_files.append(label_file_name)
 
        counter = counter + 1

target_files.append(ordered_key_list)

##zip up the label files        
labels_zipfile_name = output_folder + "target_labels.zip"
labels_zip = zipfile.ZipFile(labels_zipfile_name, "w" )
for label_file in label_files:
    archive_name = os.path.basename(label_file)
    labels_zip.write(label_file, arcname=archive_name, compress_type=zipfile.ZIP_DEFLATED)
labels_zip.close()

##zip up the target fiels
targets_zipfile_name = output_folder + "target_definitions.zip"
target_defs_zip = zipfile.ZipFile(targets_zipfile_name, "w" )
for target_file in target_files:
    archive_name = os.path.basename(target_file)
    target_defs_zip.write(target_file, arcname=archive_name, compress_type=zipfile.ZIP_DEFLATED)
target_defs_zip.close()

##cleanup zipped files
for item in target_files:
    os.remove(os.path.join(item))
for item in label_files:
    os.remove(os.path.join(item))

print(min_start_date)
print(min_end_date)


















#