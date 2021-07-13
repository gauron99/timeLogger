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


1. add categories so its easier to sort and stuff
2. rework visual of 'running' state of app
3. if its a new day, make a distinction in log file
4. make word wrap for Last shown activity when its too long it overflows off the window
5. think of additions to config -- add eventually
6. make loadConfigFile() & getConfigFile() merged in filework.py
7. TEST timeDifference.py module MORE
8. Redo the innit func in timeLogger.py -- init everything in class itself and call 
only .config after (aka have only 2 funcs for operating not 3)

Below is both information about specified topics and/or TODO etc.

#### Config
* create init view of config ( run with make config)
* user can use fast config option by giving aditional arguments after 'config' on CL
* when mistake is made in some arguments, try to provide correct arguments that can be used !!

#### Time
* what if act runs over 00:00 - needs to be tested
* add pause button, so the activity can be paused and theres no need to create a new one after.
* It will still be logged as two different separate activities? - time calculations/time-spent?
        
### log format
    new day:
        2021-07-12 16:53:29 | Watching twitch       | 0:20:00   | from:2021-07-12 16:33:29  | to:2021-07-12 16:53:29
        ----
        2021-07-13 16:53:29 | Watching twitch       | 0:20:00   | from:2021-07-12 16:33:29  | to:2021-07-12 16:53:29
    categories:
        2021-07-13 16:53:29 | Watching twitch       | 0:20:00   | from:2021-07-12 16:33:29  | to:2021-07-12 16:53:29 | chill #category

### References
    # if needed later
