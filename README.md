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
3. TEST timeDifference.py module MORE
4. test integration of timeDifference.py
5. Stuff below

Low prio -- Redo the innit func in main.py -- init everything in class itself and call 
only .config after (aka have only 2 funcs for operating not 3)

#### File
* open,write etc.
* one file - all info ?
* log text format (below)

#### Time
* what if act runs over 00:00 - needs to be tested
* test new
        
### log format
    possible ideas:
    I.
        day | time-spent | activity | time-start | time-end
        --- //next day
        day | time-spent | activity | time-start | time-end   
        
    II.
        day | time-spent | activity | category | notes | time start->end
