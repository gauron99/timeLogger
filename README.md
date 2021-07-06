# TimeLogger
    App for logging activity time-wise and activity-wise
        -- Little app to log time activities manually
        -- input a name of the activity and 'start it' by clicking <Return> or 'start' button
        -- sets up time of start a locks in the name
        -- when activity is ended, calculates some stuff with time && log it in
        -- no activity can run over 24h (gonna screw up the times) - actually maybe you can?

## TODO
-- Ordered by importance/priority

1. ~~Create tests.py~~ -- Done
2. ~~TEST timeDifference.py module with tests.py module~~ -- Done
3. Add config option for running the program where it will be possible to
edit almost everything, like: dir of log, name of log(if necessary)
4. TEST timeDifference.py module MORE
5. test integration of timeDifference.py
6. Stuff below

Low prio -- Redo the innit func in main.py -- init everything in class itself and call 
only .config after (aka have only 2 funcs for operating not 3)

Below is both information about specified topics and/or TODO etc.

#### Config
* create init view of config ( run with ./main.py config)
* source code found in config.py
* rename variables, change dirs or something, maybe how to run it
* user can use default config by giving 'config' arg
* user can use fast config option by giving aditional arguments after 'config' on CL
* config file containts --help prints etc. because control is given to it by having arguments on CL(change this? -- not for now) 
* when mistake is made in some arguments, try to provide with actual arguments that can be used !!

#### File
* open,write etc.
* one file - all info ?
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
