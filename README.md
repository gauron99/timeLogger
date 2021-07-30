# TimeLogger
    App for logging activity
        -- Little app to log time activities manually
        -- input a name of the activity and 'start it' by clicking <Return> or 'start' button
        -- sets up time of start a locks in the name
        -- when activity is ended, calculates time && logs it in
        -- no activity can run over 24h - what u gonna do that long anyways
        -- always run the app from main dir (by makefile)
        -- create log/ dir for your logs

## TODO
-- Ordered by importance/priority
-- currently working on: highest on the list(or one of top 3)


0. add tickbox (with text) for timer (like every 30mins to take a break etc.)
    ~~1. add option when user forgets to start the activity (spontanious etc. to take time from end of last act as start and end as now and add it instantly)
1.  1. make lv4 for all; lv3 == extended activities
    2. keyword for sleep start/end, log in the morning takes in the one from last night and combines them
    3. add time frames
    4. add Meta category of (inside(@PC), outside)
~~2. divide logs to months
3.  1. adding activities manually (if missed or not at PC etc.)
    ~~2. merge _categories _keywords for easier manipulation(adding etc.)
4. rework visual of 'running' state of app
~~5. make word wrap for Last shown activity when its too long it overflows off the window

6. script to make log look prettier

7. think of additions to config -- add eventually
8. make loadConfigFile() & getConfigFile() merged in filework.py
9. Redo the innit func in timeLogger.py -- init everything in class itself and call 
only .config after (aka have only 2 funcs for operating not 3)

Below is both information about specified topics and/or TODO etc.

### Categories
If multiple activities are started ("act1,act2"), the category is chosen by the first
keyword, second act is secondary & is differentiated from being primary when processing
log in processLog.py

### log format
    new day:
        2021-07-12 16:53:29 | Watching twitch       | 0:20:00   | from:2021-07-12 16:33:29  | to:2021-07-12 16:53:29
        --- 2021 07 13 --- #this indicates a new/different day (its without '-' in between so it is colored in log highlights)
        2021-07-13 16:53:29 | Watching twitch       | 0:20:00   | from:2021-07-12 16:33:29  | to:2021-07-12 16:53:29

    categories:
        2021-07-13 16:53:29 | Watching twitch       | 0:20:00   | from:2021-07-12 16:33:29  | to:2021-07-12 16:53:29 | chill #category

### References
    # if needed later
