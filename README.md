# TimeLogger
    App for logging activity
        -- Little app to log time activities manually
        -- input a name of the activity and 'start it' by clicking <Return> or 'start' button
        -- sets up time of start a locks in the name
        -- when activity is ended, calculates some stuff with time && log it in
        -- no activity can run over 24h (gonna screw up the times) - actually maybe you can?
        -- always run the app from main dir (by makefile)

## TODO
-- Ordered by importance/priority

-- currently working on: highest on the list

1. log file work, create & begin process
2. think of additions to config -- add eventually
3. TEST timeDifference.py module MORE
4. test integration of timeDifference.py

6. when 'Show Log' is clicked(ref 'Filework') 
7. Low prio -- Redo the innit func in timeLogger.py -- init everything in class itself and call 
only .config after (aka have only 2 funcs for operating not 3)

Below is both information about specified topics and/or TODO etc.

#### Config
* create init view of config ( run with make config)
* source code found in config.py
* rename variables, change dirs or something, maybe how to run it
* user can use default config by giving 'config' arg
* user can use fast config option by giving aditional arguments after 'config' on CL
* config file containts --help prints etc. because control is given to it by having arguments on CL(change this? -- not for now) 
* when mistake is made in some arguments, try to provide with actual arguments that can be used !!

#### Filework
* log text format (below)

#### Time
* what if act runs over 00:00 - needs to be tested
* add pause button, so the activity can be paused and theres no need to create a new one after.
* It will still be logged as two different separate activities? - time calculations/time-spent?
        
### log format
    possible ideas:
    I.
        day | time-spent | activity | time-start | time-end
        --- //next day
        day | time-spent | activity | time-start | time-end   
        
    II.
        day | time-spent | activity | category | notes | time start->end
### References
    # if needed later