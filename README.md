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
0.  can you catch running apps and start activities automatically?  
    
1.  make activities log after midnight to log into the "previous day" because
    if its started before midnight AKA previous day, it "belongs" to the previous day
    AKA its an activity before i go to sleep and in this regard it's part of said day
    --- works already?? needs testing

1.  1. add tickbox (with text) for timer (like every 30mins to take a break etc.)
    3. add 12PM or some devidor for sole purpose of better looking output of readlog
    look in processLog.py -> printDay()

2.  1. add time frames
    2. add Meta category of (inside(@PC), outside)
3. adding activities manually (if missed or not at PC etc.)
4. rework visual of 'running' state of app

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
### Other
1.  Every print has to have a try-except wrap because if terminal is closed and
    print statement is reached by the program, its going to try and execute it
    (aka print the message) & because no terminal window is available, its gonna
    shut down the whole app -- how to see some error messages? - print output to file or something
